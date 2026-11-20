'Local text API for the tested HY4 Flash EXL3 runtime.'

from dataclasses import dataclass

from dataclasses import field

from http.server import BaseHTTPRequestHandler

import json

import os

from queue import Empty

from queue import Full

from queue import Queue

import time

import uuid

DEFAULT_CONTEXT = 524288

NATIVE_CONTEXT = 1048576

LANES = 4

POOL = 1400064

@dataclass
class Pending:
    ids: list
    limit: int
    dfly: bool
    stream: bool
    chat: bool
    ident: str = field(default_factory=lambda: "hy4-" + uuid.uuid4().hex)
    created: int = field(default_factory=lambda: int(time.time()))
    updates: Queue = field(default_factory=Queue)
    output: list = field(default_factory=list)
    decoder: object | None = None
    stream_chars: int = 0
    reason: str | None = None

    @property
    def slots(self):
        # Every lane stays in its batch until the longest generation finishes.
        return (len(self.ids) + (6 if self.dfly else 1) * self.limit + 255) // 256

class Engine:

    def request(self, body, chat):
        if not isinstance(body, dict) or body.get("temperature", 0) != 0 or body.get("tools"):
            raise ValueError("This local profile supports greedy text generation")
        cap = body.get("max_tokens", body.get("max_completion_tokens", 128))
        ctx = body.get("max_context_tokens", DEFAULT_CONTEXT)
        dfly, stream = body.get("dfly2", False), body.get("stream", False)
        if (type(cap) is not int or not 1 <= cap <= 32768 or type(ctx) is not int
                or not 1 <= ctx <= NATIVE_CONTEXT or type(dfly) is not bool or type(stream) is not bool):
            raise ValueError("Invalid generation budget")
        if chat:
            messages = body.get("messages")
            if not isinstance(messages, list) or not messages or any(
                    not isinstance(x, dict) or x.get("role") not in ("system", "user", "assistant")
                    or not isinstance(x.get("content"), str) for x in messages):
                raise ValueError("Use text-only chat messages")
            ids = self.tokenizer.apply_chat_template(messages, tokenize=True, return_dict=False,
                add_generation_prompt=True, reasoning_effort=body.get("reasoning_effort", "no_think"))
        else:
            prompt = body.get("prompt")
            if not isinstance(prompt, str) or not prompt:
                raise ValueError("Use one text prompt")
            ids = self.tokenizer.encode(prompt, add_special_tokens=False)
        if not ids or len(ids) + cap * (6 if dfly else 1) > ctx:
            raise ValueError("Prompt plus generation exceeds this request's context")
        req = Pending(ids, cap, dfly, stream, chat)
        if req.slots + 3 * ((cap * (6 if dfly else 1) + 256) // 256) > POOL // 256:
            raise ValueError("This request exceeds the shared Q8 pool")
        self.queue.put_nowait(req)
        return req

    def sample(self):
        batch = [self.backlog.popleft() if self.backlog else self.queue.get(timeout=.2)]
        end = time.monotonic() + (.03 if self.fast_target and not batch[0].dfly else .30)
        while len(batch) < LANES and time.monotonic() < end:
            try:
                row = (self.backlog.popleft() if self.fast_target and self.backlog
                       else self.queue.get(timeout=max(0, end - time.monotonic())))
            except Empty:
                break
            if self.fast_target and not batch[0].dfly:
                from hy4_serving_batch import fits
                admit = not row.dfly and fits([*batch, row], POOL // 256)
            else:
                same = (row.limit, row.dfly) == (batch[0].limit, batch[0].dfly)
                padding = (row.limit * (6 if row.dfly else 1) + 256) // 256 * (3 - len(batch))
                admit = same and sum(x.slots for x in batch) + row.slots + padding <= POOL // 256
            if admit:
                batch.append(row)
            else:
                if self.fast_target:
                    self.backlog.appendleft(row)
                else:
                    self.backlog.append(row)
                break
        return batch

    def emit(self, row, tokens, final):
        start = len(row.output)
        for token in tokens:
            if row.reason:
                break
            if token == self.eos:
                row.reason = "stop"
                break
            row.output.append(token)
            if len(row.output) == row.limit:
                row.reason = "length"
        if row.stream and not final and len(row.output) > start:
            if row.decoder is None:
                from tokenizers.decoders import DecodeStream

                row.decoder = DecodeStream(skip_special_tokens=True)
            delta = row.decoder.step(self.tokenizer.backend_tokenizer, row.output[start:])
            if delta:
                row.updates.put(("delta", delta))
                row.stream_chars += len(delta)
        if not final:
            return ""
        decoded = self.tokenizer.decode(row.output, skip_special_tokens=True, clean_up_tokenization_spaces=False)
        if row.stream and row.stream_chars < len(decoded):
            row.updates.put(("delta", decoded[row.stream_chars:]))
            row.stream_chars = len(decoded)
        return decoded

    def generate(self, batch):
        if self.fast_target and not batch[0].dfly:
            from hy4_serving_batch import generate
            return generate(self, batch)
        runner, torch = self.runner, self.torch
        target = runner.target
        ids = [torch.tensor(row.ids, dtype=torch.long, device=target.entry) for row in batch]
        ids.extend([ids[0][:1]] * (LANES - len(ids)))
        with torch.inference_mode():
            # Reuse the query/key geometry already measured during HY4 bring-up.
            with self.use_recall({"method": "measured_causal_topk", "query_tile": 32,
                                  "key_tile": 8192, "split_ragged": True}):
                anchor = runner.prefill_ragged(tuple(ids))
            next_ids = anchor.next_tokens
            while not all(row.reason for row in batch):
                if self.stopped.is_set():
                    raise InterruptedError("Model is draining")
                if batch[0].dfly:
                    mode = getattr(self, "draft_verify", None)
                    if mode is None:
                        wave = runner.verify(anchor)
                    else:
                        from hy4_draft_verify import verify

                        wave = verify(runner, anchor, mode, live_lanes=len(batch))
                    tokens = [seq[:n + 1] for seq, n in zip(wave.proposed.tolist(), wave.accepted_counts, strict=True)]
                    anchor = wave.anchor
                else:
                    tokens = next_ids[:, None].tolist()
                    if not all(row.reason or len(row.output) + 1 == row.limit for row in batch):
                        target.begin(1)
                        _, logits, _ = target.step(next_ids[:, None])
                        target.commit((1,) * LANES)
                        next_ids = logits[:, 0].argmax(-1)
                for row, out in zip(batch, tokens, strict=False):
                    self.emit(row, out, final=False)
            self.reset(target)
        for row in batch:
            row.updates.put(("done", self.emit(row, (), final=True)))

    def stats(self):
        return {"ready": not self.stopped.is_set(), "job_id": self.job, "model": self.name,
                "context": DEFAULT_CONTEXT, "native_context": NATIVE_CONTEXT, "max_batch_size": LANES,
                "peer_directions": self.peers, "last_batch": self.last_batch,
                "target_decode": ("fused_mla" if self.fused_mla else "device_step") if self.fast_target else "reference",
                "target_expert_dispatch": self.expert_mode,
                "rank_graph_widths": self.rank_graph_widths, "long_decode": self.long_decode,
                "partial_replay_widths": self.partial_replay_widths,
                "grouped_replay_history_limit": self.grouped_replay_limit,
                "exact_fallback_buckets": self.exact_fallback_buckets,
                "blocking_token_readback_widths": sorted(self.cpu_readback.widths) if self.cpu_readback else [],
                "cpu_nice": os.getpriority(os.PRIO_PROCESS, 0),
                "native_dfly2_requests": self.draft_requests, "cache": {
                    "max_tokens": POOL, "mode": "Q8", "active_jobs": self.active,
                    "pending_jobs": self.queue.qsize() + len(self.backlog),
                }}

def handler(engine):
    class API(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def json(self, body, status=200):
            data = json.dumps(body).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            if self.path in ("/meshify/stats", "/health"):
                self.json(engine.stats())
            elif self.path == "/v1/models":
                self.json({"object": "list", "data": [{"id": engine.name, "object": "model"}]})
            else:
                self.json({"error": "Not found"}, 404)

        def do_POST(self):
            chat = self.path == "/v1/chat/completions"
            if not (chat or self.path == "/v1/completions"):
                return self.json({"error": "Not found"}, 404)
            if engine.stopped.is_set():
                return self.json({"error": "Model is draining"}, 503)
            try:
                size = int(self.headers["Content-Length"])
                if not 0 < size <= 16 * 1024 * 1024:
                    raise ValueError("Invalid request size")
                row = engine.request(json.loads(self.rfile.read(size)), chat)
            except Full:
                return self.json({"error": "Queue is full"}, 429)
            except (ValueError, KeyError, TypeError) as error:
                return self.json({"error": str(error)}, 400)

            obj = "chat.completion" if chat else "text_completion"
            base = {"id": row.ident, "created": row.created, "model": engine.name}
            if row.stream:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.end_headers()
            while True:
                event, text = row.updates.get()
                if event == "error":
                    return None if row.stream else self.json({"error": "Generation failed"}, 503)
                if event == "done":
                    use = {"prompt_tokens": len(row.ids), "completion_tokens": len(row.output),
                           "total_tokens": len(row.ids) + len(row.output)}
                    if not row.stream:
                        result = {"message": {"role": "assistant", "content": text}} if chat else {"text": text}
                        return self.json({**base, "object": obj, "usage": use,
                            "choices": [{"index": 0, "finish_reason": row.reason, **result}]})
                if row.stream:
                    delta = text if event == "delta" else ""
                    result = {"delta": {"content": delta}} if chat else {"text": delta}
                    chunk = {**base, "object": obj + ".chunk",
                             "choices": [{"index": 0, "finish_reason": row.reason if event == "done" else None,
                                          **result}]}
                    if event == "done":
                        chunk["usage"] = use
                    try:
                        self.wfile.write(("data: " + json.dumps(chunk) + "\n\n").encode())
                        self.wfile.flush()
                        if event == "done":
                            self.wfile.write(b"data: [DONE]\n\n")
                            return
                    except (BrokenPipeError, ConnectionResetError):
                        return
    return API
