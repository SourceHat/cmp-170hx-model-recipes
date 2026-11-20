"""Exercise the exported scheduler and generator methods without a CUDA runtime."""
import ast
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import time
from types import SimpleNamespace
import unittest


REPO = Path(__file__).resolve().parents[1]


class Tokens:
    def __init__(self, length):
        self.length = length
        self.shape = (1, length)

    def __len__(self):
        return self.length

    def torch_slice(self, start, end):
        return Tokens(end - start)

    def __getitem__(self, key):
        return self

    def copy_(self, other):
        return self


def method(path, class_name, method_name, namespace):
    tree = ast.parse(path.read_text())
    cls = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == class_name)
    fn = next(node for node in cls.body if isinstance(node, ast.FunctionDef) and node.name == method_name)
    fn.decorator_list = []
    exec(compile(ast.fix_missing_locations(ast.Module(body=[fn], type_ignores=[])), str(path), "exec"), namespace)
    return namespace[method_name]


class PrefillSchedulerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)
        # Fetching weights or importing CUDA is unnecessary: reconstruct precisely
        # the three changed source files from the pinned base and public patch.
        patch = (REPO / "runtimes/tabby/exllamav3.patch").read_text()
        blocks = patch.split("diff --git ")[1:]
        scheduler_block = next(block for block in blocks if block.startswith("a/exllamav3/generator/prefill_scheduler.py "))
        scheduler_path = cls.root / "prefill_scheduler.py"
        scheduler_path.write_text("\n".join(line[1:] for line in scheduler_block.splitlines()
                                          if line.startswith("+") and not line.startswith("+++")) + "\n")
        spec = importlib.util.spec_from_file_location("prefill_scheduler", scheduler_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.scheduler_type = module.PrefillScheduler
        cls.source_available = (REPO / ".local/scheduler-base/exllamav3/generator/job.py").is_file()
        if not cls.source_available:
            return
        for relative in ["generator/generator.py", "generator/job.py"]:
            target = "exllamav3/" + relative
            output = cls.root / target
            output.parent.mkdir(parents=True, exist_ok=True)
            # The upstream copies used by verification are kept out of the public repo.
            source = REPO / ".local" / "scheduler-base" / target
            output.write_bytes(source.read_bytes())
        subset = "".join("diff --git " + block for block in blocks
                         if block.startswith("a/exllamav3/generator/generator.py ")
                         or block.startswith("a/exllamav3/generator/job.py ")
                         or block.startswith("a/exllamav3/generator/prefill_scheduler.py "))
        subprocess.run(["git", "apply", "-"], input=subset, text=True, cwd=cls.root, check=True)
        ns = {"PAGE_SIZE": 256, "time": time,
              "torch": SimpleNamespace(tensor=lambda value, **kwargs: value, int32=int)}
        cls.prefill = staticmethod(method(cls.root / "exllamav3/generator/job.py", "Job", "prefill", ns))
        cls.boundary = staticmethod(method(cls.root / "exllamav3/generator/job.py", "Job", "is_checkpoint_boundary", {"PAGE_SIZE": 256}))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def jobs(self, *serials):
        return [SimpleNamespace(serial_number=serial) for serial in serials]

    def job(self, position=0, cached=False, checkpoint=0):
        if not self.source_available:
            self.skipTest("Source tests require the pinned checkout in .local/scheduler-base (prepared by CI)")
        pages = [SimpleNamespace(kv_position=256 if cached else 0, can_revert=True,
                                 page_index=index, phash=index, prev_hash=None, sequence=Tokens(256))
                 for index in range(4)]
        seq = SimpleNamespace(prefill_complete=False, kv_position=position, sequence_ids=Tokens(1025),
                              allocated_pages=pages, block_index_tensor=None)
        state = SimpleNamespace(position=checkpoint)
        forwards = []
        def forward(**kwargs):
            forwards.append(kwargs["input_ids"].shape[-1])
            state.position = seq.kv_position + kwargs["input_ids"].shape[-1]
        generator = SimpleNamespace(max_chunk_size=512, model=SimpleNamespace(caps={}, prefill=forward),
                                    recurrent_cache=object(), draft_model=None, dflash_draft=False,
                                    mtp_draft=False, cache=None, recurrent_checkpoint_interval=256,
                                    recurrent_checkpoint_interval_pp=512)
        return SimpleNamespace(sequences=[seq], generator=generator, recurrent_state=state,
                               time_first_prefill=None, embeddings=None, cached_pages=0, cached_tokens=0,
                               alt_rope_freqs=None, identifier=None, serial_number=1,
                               maybe_stash_recurrent=lambda *args: None), forwards

    def test_mixed_load_gets_decode_time_and_new_prompts_progress(self):
        scheduler = self.scheduler_type(0.25)
        jobs = self.jobs(1, 2)
        self.assertEqual(scheduler.select(jobs, True), [jobs[0]])
        scheduler.account(True, True, 0.2)
        for _ in range(10):
            self.assertEqual(scheduler.select(jobs, True), [])
            scheduler.account(True, False, 0.05)
        scheduler.account(True, False, 0.2)
        self.assertEqual(scheduler.select(jobs, True), [jobs[1]])

    def test_prefills_rotate_across_completion_and_cancellation(self):
        scheduler = self.scheduler_type(1.0)
        first, second, third = self.jobs(1, 2, 3)
        self.assertEqual(scheduler.select([first, second, third], True), [first])
        self.assertEqual(scheduler.select([second, third], True), [second])
        self.assertEqual(scheduler.select([third], True), [third])
        self.assertEqual(scheduler.select([first, third], True), [first])

    def test_solo_prefill_is_unthrottled_and_stale_debt_clears(self):
        scheduler = self.scheduler_type()
        jobs = self.jobs(1, 2)
        scheduler.account(True, True, 5)
        self.assertEqual(scheduler.select(jobs, False), jobs)
        self.assertEqual(scheduler.decode_debt, 0)
        scheduler.account(True, True, 5)
        self.assertEqual(scheduler.select([], True), [])
        self.assertEqual(scheduler.select(jobs, True), [jobs[0]])

    def test_invalid_time_fractions_are_rejected(self):
        for fraction in [0, -1, 1.1, float("nan"), float("inf")]:
            with self.subTest(fraction=fraction), self.assertRaises(ValueError):
                self.scheduler_type(fraction)

    def test_smaller_chunk_does_not_mutate_checkpoint_geometry(self):
        job, forwards = self.job()
        self.prefill(job, [], max_chunk_size=256)
        self.assertEqual(forwards, [256])
        self.assertEqual(job.sequences[0].kv_position, 256)
        self.assertEqual(job.generator.max_chunk_size, 512)
        self.assertTrue(self.boundary(job))

    def test_solo_chunk_preserves_configured_prefill_size(self):
        job, forwards = self.job()
        self.prefill(job, [])
        self.assertEqual(forwards, [512])
        self.assertEqual(job.sequences[0].kv_position, 512)

    def test_shared_prefix_checkpoint_uses_its_actual_state_position(self):
        job, forwards = self.job()
        seq = job.sequences[0]
        seq.shared_checkpoint_position = 256
        saved = []
        job.maybe_stash_recurrent = lambda *args: saved.append((job.recurrent_state.position, seq.kv_position))
        self.prefill(job, [])
        self.assertEqual(forwards, [256])
        self.assertEqual(saved, [(256, 256)])
        self.assertEqual(seq.allocated_pages[0].kv_position, 256)
        self.prefill(job, [])
        self.assertEqual(forwards, [256, 512])
        self.assertEqual(saved, [(256, 256)])

    def test_existing_state_and_multimodal_chunks_do_not_add_fork_splits(self):
        job, forwards = self.job(position=512, checkpoint=512)
        job.sequences[0].shared_checkpoint_position = 256
        self.prefill(job, [])
        self.assertEqual(forwards, [512])
        job, forwards = self.job()
        job.sequences[0].shared_checkpoint_position = 256
        job.embeddings = [object()]
        job.sequences[0].multimodal_mask = [False] * 1025
        self.prefill(job, [])
        self.assertEqual(forwards, [512])

    def test_cache_only_never_launches_target_or_draft(self):
        job, forwards = self.job(cached=True, checkpoint=512)
        self.prefill(job, [], cache_only=True)
        self.assertEqual(forwards, [])
        self.assertEqual(job.sequences[0].kv_position, 512)
        self.assertEqual(job.cached_pages, 2)
        self.prefill(job, [], cache_only=True)
        self.assertEqual(job.sequences[0].kv_position, 512)
        self.assertEqual(forwards, [])

    def test_recurrent_replay_keeps_untouched_shared_suffix_complete(self):
        job, forwards = self.job(cached=True, checkpoint=0)
        self.prefill(job, [])
        self.assertEqual(forwards, [512])
        self.assertEqual(job.sequences[0].kv_position, 512)
        self.assertEqual([p.kv_position for p in job.sequences[0].allocated_pages], [256]*4)
        # A different job can trigger pruning before this one replays its next
        # chunk; the original branch's later checkpoint must stay resumable.
        from test_prefix_diagnostics import source_class
        from collections import OrderedDict
        cls = source_class('exllamav3/cache/recurrent.py', 'RecurrentCache',
                           {'OrderedDict': OrderedDict, 'PAGE_SIZE': 256, 'note_freed': lambda n: None})
        cache = cls(SimpleNamespace(loaded_tp=False), 100)
        cache['original-tail'] = {'checkpoint_size': 4}
        pages = job.sequences[0].allocated_pages
        cache.pagetable = SimpleNamespace(checkpoint_retention_hashes=lambda:
                                         {'original-tail'} if all(p.kv_position == 256 for p in pages) else set())
        self.assertEqual(cache.prune_stranded(), 0)
        self.assertIn('original-tail', cache)

    def test_cache_only_with_no_usable_prefix_leaves_position_unchanged(self):
        job, forwards = self.job()
        self.prefill(job, [], cache_only=True)
        self.assertEqual(job.sequences[0].kv_position, 0)
        self.assertEqual(forwards, [])

    def test_final_partial_page_is_not_skipped(self):
        job, forwards = self.job(position=768, checkpoint=768)
        job.sequences[0].sequence_ids = Tokens(1001)
        self.prefill(job, [], max_chunk_size=256)
        self.assertEqual(forwards, [232])
        self.assertEqual(job.sequences[0].kv_position, 1000)
        self.assertTrue(job.sequences[0].prefill_complete)

    def test_generator_really_interleaves_decode_and_round_robin_prefill(self):
        if not self.source_available:
            self.skipTest("Source tests require the pinned checkout prepared by CI")
        clock = SimpleNamespace(value=0.0)
        iterate = method(self.root / "exllamav3/generator/generator.py", "Generator", "iterate",
                         {"time": SimpleNamespace(perf_counter=lambda: clock.value)})
        events = []
        def job(serial, ready):
            def prefill(results, max_chunk_size=None, cache_only=False):
                if not cache_only:
                    events.append((serial, max_chunk_size))
                    clock.value += 0.2
            return SimpleNamespace(serial_number=serial, is_prefill_done=lambda: ready, prefill=prefill)
        first, second = job(1, False), job(2, False)
        def decode(results):
            clock.value += 0.05
            events.append("decode")
        generator = SimpleNamespace(cache=SimpleNamespace(initialized=True), draft_cache=None,
                                    active_jobs=[job(0, True), first, second], pending_jobs=[],
                                    fair_queue=SimpleNamespace(prefill_due=lambda job, pending: False),
                                    iterate_start_jobs=lambda results: None, recurrent_cache=None,
                                    draft_model=None, ngram_match_min=0, visualizer=None,
                                    iterate_gen=decode, mixed_prefill_chunk_size=256,
                                    prefill_scheduler=self.scheduler_type(0.25))
        iterate(generator)
        self.assertEqual(events, [(1, 256), "decode"])
        for _ in range(20):
            iterate(generator)
        self.assertEqual([event for event in events if isinstance(event, tuple)][:2], [(1, 256), (2, 256)])
        self.assertEqual(events.count("decode"), 21)


if __name__ == "__main__":
    unittest.main()
