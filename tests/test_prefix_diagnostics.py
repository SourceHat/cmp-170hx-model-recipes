"""Exercise prefix attribution and numerical streaming logs without CUDA."""
import ast
from collections import OrderedDict, deque
from contextvars import ContextVar
import heapq
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest

REPO = Path(__file__).resolve().parents[1]


def patched_source(name):
    base = REPO / ".local/scheduler-base" / name
    if not base.is_file():
        raise RuntimeError("Prepare the pinned source checkout; source regressions must run")
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / name
        path.parent.mkdir(parents=True)
        path.write_bytes(base.read_bytes())
        blocks = (REPO / "runtimes/tabby/exllamav3.patch").read_text().split("diff --git ")[1:]
        subset = "".join("diff --git " + b for b in blocks if b.startswith("a/" + name + " "))
        if subset:
            subprocess.run(["git", "apply", "-"], input=subset, text=True, cwd=folder, check=True, capture_output=True)
        return path.read_text()


def source_class(name, cls, namespace):
    tree = ast.parse(patched_source(name))
    node = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == cls)
    imports = ast.parse("from __future__ import annotations").body
    exec(compile(ast.Module(body=imports + [node], type_ignores=[]), name, "exec"), namespace)
    return namespace[cls]


def pure_history():
    patch = (REPO / "runtimes/tabby/exllamav3.patch").read_text()
    block = next(b for b in patch.split("diff --git ") if b.startswith("a/exllamav3/generator/prefix_diagnostics.py "))
    text = "\n".join(line[1:] for line in block.splitlines() if line.startswith("+") and not line.startswith("+++"))
    ns = {}
    exec(text, ns)
    return ns["PrefixHistory"]


def table(hashes, broken_at=None):
    pages = [SimpleNamespace(phash=h, prev_hash=hashes[i-1] if i else None,
                             kv_position=256, page_index=i, access_serial=i,
                             ref_count=0, children=[]) for i, h in enumerate(hashes)]
    if broken_at is not None:
        pages[broken_at].prev_hash = "missing"
    index = {p.phash: p for p in pages}
    return SimpleNamespace(get_live_page=index.get, all_pages=pages,
                           referenced_pages={}, unreferenced_pages=index,
                           generator=SimpleNamespace(active_jobs=[]))


class DiagnosticsTests(unittest.TestCase):
    def setUp(self):
        self.history = pure_history()(max_histories=4, max_pages=32)

    def test_unknown_history_is_not_claimed_to_be_an_input_edit(self):
        pt = table(["a", "b", "c"])
        row = self.history.allocation(1, ["a", "b", "c"], 800, pt, {})
        self.history.restored(row, 0, None)
        self.assertFalse(row["history_known"])
        self.assertIn("unknown_history", row["replay_reasons"])
        self.assertNotIn("incoming_prefix_change", row["replay_reasons"])

    def test_page_loss_and_state_loss_are_distinct(self):
        hashes = ["a", "b", "c", "d"]
        pt = table(hashes)
        self.history.completed_sequence(1, pt.all_pages)
        self.history.allocation(1, hashes, 1100, pt, {})
        rc = OrderedDict(a={"position": 256})
        rc.loss_reasons = {"c": "budget"}
        row = self.history.allocation(2, hashes, 1100, pt, rc)
        self.history.restored(row, 256, rc["a"])
        self.assertEqual(row["previous_completed_kv_missing_tokens"], 0)
        self.assertEqual(row["resident_kv_without_state_tokens"], 768)
        self.assertEqual(row["checkpoint_loss_tokens"]["budget"], 768)
        self.assertIn("checkpoint_budget", row["replay_reasons"])
        pt = table(hashes[:2])
        row = self.history.allocation(3, hashes, 1100, pt, rc)
        self.assertEqual(row["previous_completed_kv_missing_tokens"], 512)
        self.assertEqual(row["resident_kv_without_state_tokens"], 256)

    def test_interleaved_long_histories_keep_separate_positions(self):
        a = ["root"] + [f"a{i}" for i in range(12)]
        b = ["root"] + [f"b{i}" for i in range(12)]
        for serial, hashes in ((1, a), (2, b)):
            pt = table(hashes)
            self.history.completed_sequence(serial, pt.all_pages)
            self.history.allocation(serial, hashes, 3400, pt, {hashes[-1]: {"position": 3328}})
        for serial, hashes in ((3, a), (4, b)):
            row = self.history.allocation(serial, hashes, 3400, table(hashes), {hashes[-1]: {"position": 3328}})
            self.assertEqual(row["previous_completed_prefix_tokens"], 3328)
            self.assertEqual(row["valid_checkpoint_tokens"], 3328)

    def test_only_demonstrated_shared_prefix_gaps_request_a_checkpoint(self):
        row = {"resident_prefix_tokens": 13312, "previous_completed_prefix_tokens": 13312,
               "valid_checkpoint_tokens": 0}
        self.assertEqual(self.history.checkpoint_target(row), 13312)
        row["previous_completed_prefix_tokens"] = 0
        self.assertIsNone(self.history.checkpoint_target(row))
        row.update(previous_completed_prefix_tokens=13312, valid_checkpoint_tokens=13312)
        self.assertIsNone(self.history.checkpoint_target(row))
        row.update(resident_prefix_tokens=13568, previous_completed_prefix_tokens=13568)
        self.assertIsNone(self.history.checkpoint_target(row))

    def test_intentional_middle_edit_stops_at_its_first_changed_page(self):
        before, after = ["a", "b", "c"], ["a", "edited", "edited-tail"]
        meta = {"session_key": "session", "message_hashes": ["same", "old"]}
        self.history.allocation(1, before, 800, table(before), {}, meta)
        row = self.history.allocation(2, after, 800, table(before), {},
                                     {"session_key": "session", "message_hashes": ["same", "new"]})
        self.assertEqual(row["session_shared_prefix_tokens"], 256)
        self.assertEqual(row["session_first_changed_message"], 1)
        self.assertTrue(row["session_prefix_changed"])
        self.assertEqual(row["resident_prefix_tokens"], 256)

    def test_broken_ancestry_and_wrong_position_have_separate_fields(self):
        hashes = ["a", "b", "c"]
        row = self.history.allocation(1, hashes, 800, table(hashes, broken_at=1), {"c": {"position": 512}})
        self.assertEqual(row["broken_ancestry_at_tokens"], 256)
        self.assertEqual(row["invalid_checkpoint_positions"], 1)
        self.assertEqual(row["valid_checkpoint_tokens"], 0)

    def test_history_and_index_stay_bounded_under_churn(self):
        for i in range(200):
            hashes = [f"{i}-{j}" for j in range(8)]
            self.history.allocation(i, hashes, 2200, table(hashes), {}, {"session_key": str(i)})
            self.history.completed_sequence(i, table(hashes).all_pages)
        for histories, counts in ((self.history.observed, self.history.observed_pages),
                                  (self.history.completed, self.history.completed_pages)):
            self.assertLessEqual(len(histories), 4)
            self.assertLessEqual(len(counts), 32)
            self.assertTrue(all(n > 0 for n in counts.values()))
        self.assertLessEqual(len(self.history.sessions), 4)


class SourceRetentionTests(unittest.TestCase):
    def retained_table(self):
        page_type = source_class("exllamav3/generator/pagetable.py", "CachePage",
                                 {"dataclass": lambda cls: cls, "_randomhash": lambda: "temporary"})
        pt_type = source_class("exllamav3/generator/pagetable.py", "PageTable", {"PAGE_SIZE": 256})
        pt = pt_type.__new__(pt_type)
        page = page_type()
        for name, value in {"pagetable": pt, "page_index": 0, "phash": "original", "prev_hash": None,
                            "kv_position": 256, "access_serial": 1, "ref_count": 0, "can_revert": False}.items():
            setattr(page, name, value)
        pt.all_pages = [page]
        pt.referenced_pages = {}
        pt.unreferenced_pages = {"original": page}
        pt.cpu_tier = None
        pt.max_pages = 1
        return pt, page

    def test_unused_generation_allocation_retains_state_until_revert(self):
        pt, page = self.retained_table()
        cls = source_class("exllamav3/cache/recurrent.py", "RecurrentCache",
                           {"OrderedDict": OrderedDict, "PAGE_SIZE": 256, "note_freed": lambda n: None})
        cache = cls(SimpleNamespace(loaded_tp=False), 100)
        cache.pagetable = pt
        cache["original"] = {"checkpoint_size": 4}
        page.add_ref_unique(2)
        self.assertFalse(pt.is_resumable("original"))
        self.assertIn("original", pt.checkpoint_retention_hashes())
        self.assertEqual(cache.prune_stranded(), 0)
        page.sub_ref()
        self.assertTrue(pt.is_resumable("original"))
        self.assertIn("original", cache)

    def test_written_generation_page_drops_the_destroyed_checkpoint(self):
        pt, page = self.retained_table()
        cls = source_class("exllamav3/cache/recurrent.py", "RecurrentCache",
                           {"OrderedDict": OrderedDict, "PAGE_SIZE": 256, "note_freed": lambda n: None})
        cache = cls(SimpleNamespace(loaded_tp=False), 100)
        cache.pagetable = pt
        cache["original"] = {"checkpoint_size": 4}
        page.add_ref_unique(2)
        page.can_revert = False
        page.kv_position = 1
        self.assertEqual(cache.prune_stranded(), 1)
        self.assertNotIn("original", cache)
        self.assertEqual(cache.loss_reasons["original"], "stranded")

    def test_tree_eviction_keeps_referenced_and_incoming_prefixes(self):
        cls = source_class("exllamav3/generator/pagetable.py", "PageTable",
                           {"PAGE_SIZE": 256, "deque": deque, "heapq": heapq})
        pt = table(["a", "b", "c", "d"])
        pt.eviction_policy = "tree"
        pt.all_pages[1].ref_count = 1
        del pt.unreferenced_pages["b"]
        pt.referenced_pages["b"] = pt.all_pages[1]
        order = list(cls.build_eviction_order(pt, {"c"}))
        self.assertEqual(order[0].phash, "d")
        self.assertNotIn("b", [p.phash for p in order])
        self.assertEqual(order[-1].phash, "c")

    def test_budget_loss_and_tp_deletion_are_recorded(self):
        deletions = []
        model = SimpleNamespace(loaded_tp=True, tp_dispatch_all=lambda fn, args: deletions.append(args))
        cls = source_class("exllamav3/cache/recurrent.py", "RecurrentCache",
                           {"OrderedDict": OrderedDict, "PAGE_SIZE": 256, "note_freed": lambda n: None,
                            "mp_cache_recurrent_del": object()})
        cache = cls(model, 8)
        count = iter(range(20))
        state = SimpleNamespace(stash=lambda: {"checkpoint_size": 4, "tp_handle": next(count), "position": 256})
        cache.put("a", state)
        cache.put("b", state)
        cache.put("c", state)
        self.assertEqual(cache.loss_reasons["a"], "budget")
        self.assertEqual(cache.current_size, 8)
        self.assertEqual(deletions, [(id(cache), 0)])
        cache.put("a", state)
        self.assertNotIn("a", cache.loss_reasons)


class StreamDiagnosticsTests(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        path = REPO / "runtimes/tabby/helpers/meshify_prefix_diagnostics.py"
        spec = importlib.util.spec_from_file_location("prefix_helper", path)
        cls.helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.helper)

    async def test_progress_ignores_headers_and_logs_no_prompt_or_generated_text(self):
        clock = [10.0]
        context = ContextVar("request", default=None)
        async def app(scope, receive, send):
            await receive()
            await send({"type": "http.response.start", "status": 200})
            clock[0] = 11.0
            await send({"type": "http.response.body", "body": b'data: {"choices":[{"delta":{"role":"assistant"}}]}\n\n'})
            clock[0] = 12.0
            await send({"type": "http.response.body", "body": b'data: {"choices":[{"delta":{"reasoning_content":"PRIVATE OUTPUT"}}]}\n\n'})
            clock[0] = 15.0
            await send({"type": "http.response.body", "body": b'data: {"choices":[{"delta":{"content":"PRIVATE ANSWER"}}]}\n\n'})
        async def receive():
            return {"type": "http.request", "body": b'PRIVATE PROMPT'}
        sent = []
        async def send(event):
            sent.append(event)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "requests.jsonl"
            middleware = self.helper.PrefixMiddleware(app, context, path, clock=lambda: clock[0])
            await middleware({"type": "http", "method": "POST", "path": "/v1/chat/completions",
                              "headers": [(b"x-meshify-session", b"PRIVATE SESSION")]}, receive, send)
            raw = path.read_text()
        row = json.loads(raw)
        self.assertEqual(row["first_progress_s"], 2)
        self.assertEqual(row["max_progress_gap_s"], 3)
        self.assertNotIn("PRIVATE", raw)
        self.assertIsNone(context.get())
        self.assertEqual(len(sent), 4)

    async def test_identical_normalized_inputs_get_stable_fingerprints(self):
        context = ContextVar("request", default=None)
        async def render(messages, existing_template_vars=None):
            return "SYNTHETIC RENDER", None, {"messages": [{"role": "user", "content": "synthetic"}], "enable_thinking": True}
        api = SimpleNamespace(format_messages_with_template=render)
        backend = SimpleNamespace(log_metrics=lambda *args, **kwargs: None)
        app = SimpleNamespace(add_middleware=lambda *args, **kwargs: None)
        self.helper.install(app, api, backend, context=context)
        rows = []
        for _ in range(2):
            meta = {}
            token = context.set(meta)
            await api.format_messages_with_template([SimpleNamespace(model_dump=lambda **kwargs: {"content": "synthetic"})])
            context.reset(token)
            rows.append(meta)
        self.assertEqual(rows[0], rows[1])
        self.assertNotIn("SYNTHETIC RENDER", json.dumps(rows))

    async def test_split_crlf_frames_and_native_completion_progress(self):
        clock = [0.0]
        context = ContextVar("request", default=None)
        async def app(scope, receive, send):
            clock[0] = 1
            await send({"type": "http.response.start", "status": 200})
            await send({"type": "http.response.body", "body": b'data: {"choices":[{"text":"synthetic"}]}\r\n'})
            clock[0] = 2
            await send({"type": "http.response.body", "body": b'\r\n'})
        async def unused():
            return {}
        async def send(event):
            pass
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "requests.jsonl"
            middleware = self.helper.PrefixMiddleware(app, context, path, clock=lambda: clock[0])
            await middleware({"type": "http", "method": "POST", "path": "/v1/completions"}, unused, send)
            row = json.loads(path.read_text())
        self.assertEqual(row["first_progress_s"], 2)
        self.assertFalse(row["stream_diagnostic_truncated"])


if __name__ == "__main__":
    unittest.main()
