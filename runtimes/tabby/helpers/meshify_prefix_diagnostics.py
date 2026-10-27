"""Numerical prefix/stream diagnostics for managed and portable Tabby serving."""
from contextvars import ContextVar
import functools
import hashlib
import json
import os
from pathlib import Path
import secrets
import time


_KEY = secrets.token_bytes(32)
_METRICS = ("prompt_tokens", "cached_tokens", "gen_tokens", "prompt_time", "gen_time",
            "queue_time", "total_time", "gen_tokens_per_sec", "draft_accept", "draft_reject")
_OPTIONS = ("enable_thinking", "preserve_thinking", "clear_thinking", "reasoning_effort",
            "add_generation_prompt", "continue_final_message")


def fingerprint(value):
    data = json.dumps(value, ensure_ascii=True, separators=(",", ":"), default=str).encode()
    return hashlib.blake2b(data, key=_KEY, digest_size=16).hexdigest()


def _meaningful(value):
    if not isinstance(value, dict):
        return False
    if value.get("type") in ("response.output_text.delta", "response.reasoning_text.delta",
                              "response.function_call_arguments.delta", "response.custom_tool_call_input.delta"):
        return bool(value.get("delta"))
    for choice in value.get("choices", []):
        if choice.get("text"):
            return True
        delta = choice.get("delta", {})
        if delta.get("content") or delta.get("reasoning_content") or delta.get("tool_calls"):
            return True
    return False


class PrefixMiddleware:
    def __init__(self, app, context, path=None, clock=time.monotonic):
        self.app = app
        self.context = context
        self.path = Path(path) if path else None
        self.clock = clock
        self.errors = 0

    async def __call__(self, scope, receive, send):
        endpoint = scope.get("path", "").rstrip("/")
        if scope.get("type") != "http" or scope.get("method") != "POST" or endpoint not in (
            "/v1/chat/completions", "/chat/completions", "/v1/responses", "/responses",
            "/v1/completions", "/completions"):
            return await self.app(scope, receive, send)
        start = self.clock()
        headers = dict(scope.get("headers", []))
        session = next((headers.get(name) for name in (b"x-meshify-prefix-session", b"x-meshify-session",
                                                      b"x-litellm-session-id") if headers.get(name)), None)
        meta = {"request_key": secrets.token_hex(12), "endpoint": endpoint,
                "session_key": fingerprint(session.hex()) if session else None}
        token = self.context.set(meta)
        body_hash = hashlib.blake2b(key=_KEY, digest_size=16)
        stream_buffer = b""
        first_body = first_progress = last_progress = None
        max_gap = 0.0
        chunks = body_bytes = 0
        status = None
        truncated = False

        async def observed_receive():
            event = await receive()
            if event.get("type") == "http.request":
                body_hash.update(event.get("body", b""))
            return event

        async def observed_send(event):
            nonlocal stream_buffer, first_body, first_progress, last_progress, max_gap, chunks, body_bytes, status, truncated
            if event["type"] == "http.response.start":
                status = event["status"]
            if event["type"] == "http.response.body" and event.get("body"):
                now = self.clock()
                if first_body is None:
                    first_body = now - start
                body = event["body"]
                chunks += 1
                body_bytes += len(body)
                stream_buffer += body
                while True:
                    boundaries = [(stream_buffer.find(mark), mark) for mark in (b"\n\n", b"\r\n\r\n")]
                    boundaries = [(offset, mark) for offset, mark in boundaries if offset >= 0]
                    if not boundaries:
                        break
                    offset, mark = min(boundaries)
                    frame, stream_buffer = stream_buffer[:offset], stream_buffer[offset + len(mark):]
                    if len(frame) > 65536:
                        truncated = True
                        continue
                    for line in frame.splitlines():
                        if line.startswith(b"data:"):
                            try:
                                value = json.loads(line[5:])
                            except (ValueError, UnicodeDecodeError):
                                continue
                            if _meaningful(value):
                                if first_progress is None:
                                    first_progress = now - start
                                if last_progress is not None:
                                    max_gap = max(max_gap, now - last_progress)
                                last_progress = now
                if len(stream_buffer) > 65536:
                    stream_buffer = b""
                    truncated = True
            await send(event)

        try:
            await self.app(scope, observed_receive, observed_send)
        finally:
            self.context.reset(token)
            if self.path is not None:
                row = {"version": 1, "at": time.time(), "request_key": meta["request_key"],
                       "endpoint": endpoint, "session_key": meta["session_key"], "http_status": status,
                       "raw_body_hash": body_hash.hexdigest(),
                       "first_body_s": first_body, "first_progress_s": first_progress,
                       "max_progress_gap_s": max_gap, "response_chunks": chunks,
                       "response_bytes": body_bytes, "http_duration_s": self.clock() - start,
                       "stream_diagnostic_truncated": truncated}
                for name in ("message_hashes", "normalized_message_hashes", "rendered_hash",
                             "template_options_hash", "template_flags", "metrics", "prefix_diagnostic"):
                    if name in meta:
                        row[name] = meta[name]
                try:
                    with self.path.open("a") as output:
                        output.write(json.dumps(row, separators=(",", ":"), allow_nan=False) + "\n")
                except (OSError, ValueError):
                    self.errors += 1


def install(app, chat_completion, backend, path=None, responses=None, context=None):
    if context is None:
        from exllamav3.generator.prefix_diagnostics import PREFIX_REQUEST
        context = PREFIX_REQUEST
    original_format = chat_completion.format_messages_with_template

    @functools.wraps(original_format)
    async def format_observed(messages, existing_template_vars=None):
        meta = context.get()
        if meta is not None:
            meta.setdefault("message_hashes", [fingerprint(m.model_dump(exclude_none=True)) for m in messages])
        result = await original_format(messages, existing_template_vars)
        if meta is not None:
            prompt, _, variables = result
            meta["normalized_message_hashes"] = [fingerprint(m) for m in variables.get("messages", [])]
            meta["rendered_hash"] = fingerprint(prompt)
            meta["template_options_hash"] = fingerprint({k: v for k, v in variables.items() if k != "messages"})
            meta["template_flags"] = {k: v for k, v in variables.items()
                                      if k in _OPTIONS and (isinstance(v, bool) or v in ("low", "medium", "high", "none"))}
        return result

    chat_completion.format_messages_with_template = format_observed
    original_metrics = backend.log_metrics

    @functools.wraps(original_metrics)
    def metrics_observed(*args, **kwargs):
        values = next((a for a in args if isinstance(a, dict) and "gen_tokens" in a), {})
        meta = context.get()
        if values and meta is not None:
            meta["metrics"] = {k: v if isinstance(v := values.get(k), (int, float)) else None for k in _METRICS}
            meta["prefix_diagnostic"] = values.get("prefix_diagnostic")
        return original_metrics(*args, **kwargs)

    backend.log_metrics = metrics_observed
    if responses is not None:
        original_conversion = responses.responses_to_chat_payload

        @functools.wraps(original_conversion)
        def convert_observed(body):
            meta = context.get()
            if meta is not None and isinstance(body.get("input"), list):
                meta["message_hashes"] = [fingerprint(item) for item in body["input"]]
            return original_conversion(body)

        responses.responses_to_chat_payload = convert_observed
    app.add_middleware(PrefixMiddleware, context=context,
                       path=path or os.environ.get("MESHIFY_PREFIX_DIAGNOSTICS_PATH"))
