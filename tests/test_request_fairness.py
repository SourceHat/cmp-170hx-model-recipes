"""Exercise slot rotation, continuation accounting and RAM cleanup without CUDA."""
import ast
from collections import OrderedDict
from pathlib import Path
from types import SimpleNamespace
import unittest


REPO = Path(__file__).resolve().parents[1]


def addition(path):
    blocks = (REPO / 'runtimes/tabby/exllamav3.patch').read_text().split('diff --git ')
    block = next(b for b in blocks if b.startswith('a/' + path + ' '))
    return '\n'.join(line[1:] for line in block.splitlines()
                     if line.startswith('+') and not line.startswith('+++')) + '\n'


def method(path, cls, name, namespace):
    tree = ast.parse(path.read_text())
    owner = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == cls)
    node = next(n for n in owner.body if isinstance(n, ast.FunctionDef) and n.name == name)
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), 'exec'), namespace)
    return namespace[name]


class FairnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        namespace = {}
        exec(addition('exllamav3/generator/fair_queue.py'), namespace)
        cls.policy_type = namespace['FairQueue']

    def job(self, position=2048, start=0, outputs=512, complete=False):
        return SimpleNamespace(sequences=[SimpleNamespace(kv_position=position)],
                               embeddings=None, prefix_token=None, new_tokens=outputs,
                               prefill_turn_start=start, is_prefill_done=lambda: complete)

    def test_uncontended_jobs_keep_their_normal_execution(self):
        policy = self.policy_type()
        job = self.job()
        self.assertFalse(policy.prefill_due(job, []))
        self.assertFalse(policy.generation_due(job, []))

    def test_cached_prefix_does_not_spend_the_prefill_turn(self):
        policy = self.policy_type()
        job = self.job(position=65536 + 512, start=65536)
        self.assertFalse(policy.prefill_due(job, [object()]))
        job.sequences[0].kv_position += 1536
        self.assertTrue(policy.prefill_due(job, [object()]))

    def test_partial_pages_never_yield_state(self):
        policy = self.policy_type()
        job = self.job(position=2049)
        self.assertFalse(policy.prefill_due(job, [object()]))
        self.assertFalse(policy.generation_due(job, [object()]))

    def test_token_healing_and_multimodal_prefill_keep_their_state(self):
        policy = self.policy_type()
        job = self.job()
        job.prefix_token = object()
        self.assertFalse(policy.prefill_due(job, [object()]))
        job.prefix_token = None
        job.embeddings = [object()]
        self.assertFalse(policy.prefill_due(job, [object()]))

    def test_completed_prefill_is_not_rotated_before_decode(self):
        policy = self.policy_type()
        self.assertFalse(policy.prefill_due(self.job(complete=True), [object()]))

    def test_generation_releases_only_a_completed_page_after_its_turn(self):
        policy = self.policy_type()
        job = self.job(outputs=511)
        self.assertFalse(policy.generation_due(job, [object()]))
        job.new_tokens = 512
        self.assertTrue(policy.generation_due(job, [object()]))

    def test_multisequence_jobs_are_not_reinitialized_as_single_sequences(self):
        policy = self.policy_type()
        job = self.job()
        job.sequences.append(SimpleNamespace(kv_position=2048))
        self.assertFalse(policy.prefill_due(job, [object()]))
        self.assertFalse(policy.generation_due(job, [object()]))

    def test_banned_string_rewind_buffers_keep_their_existing_execution(self):
        policy = self.policy_type()
        job = self.job()
        job.banned_strings = ['restricted sequence']
        self.assertFalse(policy.prefill_due(job, [object()]))
        self.assertFalse(policy.generation_due(job, [object()]))


class SourceFairnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        namespace = {}
        exec(addition('exllamav3/generator/fair_queue.py'), namespace)
        cls.policy_type = namespace['FairQueue']
        cls.root = REPO / '.local/scheduler-base'
        cls.available = (cls.root / 'exllamav3/generator/generator.py').is_file()

    def source(self, name):
        if not self.available:
            self.skipTest('Requires pinned source checkout prepared by CI')
        import subprocess
        import tempfile
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        path = Path(self.tmp.name) / name
        base = self.root / name
        path.parent.mkdir(parents=True)
        if base.is_file():
            path.write_bytes(base.read_bytes())
        blocks = (REPO / 'runtimes/tabby/exllamav3.patch').read_text().split('diff --git ')[1:]
        subset = ''.join('diff --git ' + b for b in blocks if b.startswith('a/' + name + ' '))
        subprocess.run(['git', 'apply', '-'], input=subset, text=True,
                       cwd=self.tmp.name, check=True, capture_output=True)
        return path

    def test_prefill_rotation_preserves_state_before_releasing_the_slot(self):
        source = self.source('exllamav3/generator/generator.py')
        run = method(source, 'Generator', 'yield_prefill',
                     {'time': SimpleNamespace(time=lambda: 120), 'PAGE_SIZE': 256})
        actions = []
        job = SimpleNamespace(time_enqueue=100, time_first_prefill=110,
                              time_enqueued=3, time_prefill=5)
        job.maybe_stash_recurrent = lambda *args: actions.append('stash')
        job.deallocate_pages = lambda: actions.append('release')
        def requeue():
            actions.append('requeue')
            return job
        job.prepare_for_requeue = requeue
        waiting = object()
        gen = SimpleNamespace(recurrent_cache=object(), active_jobs=[job],
                              pending_jobs=[waiting], fair_queue=self.policy_type())
        run(gen, job)
        self.assertEqual(actions, ['stash', 'release', 'requeue'])
        self.assertEqual(gen.pending_jobs, [waiting, job])
        self.assertEqual(gen.active_jobs, [])
        self.assertEqual((job.time_enqueued, job.time_prefill), (13, 15))

    def test_generation_continuations_do_not_jump_a_waiting_request(self):
        source = self.source('exllamav3/generator/generator.py')
        tree = ast.parse(source.read_text())
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'Generator')
        fn = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == 'iterate_gen')
        loop = next(n for n in fn.body if isinstance(n, ast.For)
                    and isinstance(n.iter, ast.Name) and n.iter.id == 'requeuing_jobs')
        waiting = object()
        continuation = SimpleNamespace()
        continuation.prepare_for_requeue = lambda: continuation
        gen = SimpleNamespace(pending_jobs=[waiting])
        exec(compile(ast.Module(body=[loop], type_ignores=[]), str(source), 'exec'),
             {'self': gen, 'requeuing_jobs': [continuation]})
        self.assertEqual(gen.pending_jobs, [waiting, continuation])

    def test_repeated_requeues_keep_all_previous_output_tokens(self):
        source = self.source('exllamav3/generator/job.py')
        run = method(source, 'Job', 'prepare_for_requeue', {})
        class Tokens(list):
            def torch(self):
                return self
        class Replay:
            def __init__(self, **args):
                state = args['rq_state']
                self.rq_new_tokens = state['rq_new_tokens']
                self.max_new_tokens = args['max_new_tokens']
                self.min_new_tokens = args['min_new_tokens']
                self.new_tokens = 0
                ids = args['input_ids']
                self.sequences = [SimpleNamespace(input_ids=list(ids), sequence_ids=Tokens(ids))]
            def prepare_for_queue(self, generator, serial_number, rq=False):
                self.generator, self.serial_number = generator, serial_number
        job = Replay.__new__(Replay)
        fields = ['rng', 'stop_strings', 'stop_tokens', 'stop_strings_utf32_buffer',
                  'stop_strings_utf32_offsets', 'held_text', 'held_tokens', 'held_probs',
                  'held_k_tokens', 'held_k_probs', 'held_logits', 'full_completion',
                  'sam', 'forced_ids', 'sampler', 'filters', 'identifier',
                  'banned_strings', 'embeddings', 'orig_max_rq_tokens', 'stop_on_loop']
        for field in fields:
            setattr(job, field, None)
        for field in ('time_enqueued', 'time_prefill', 'time_generate',
                      'accepted_draft_tokens', 'rejected_draft_tokens'):
            setattr(job, field, 0)
        job.filters_suspended = False
        job.rq_prompt_tokens = 10
        job.rq_cached = (0, 0)
        job.decode_special_tokens = False
        job.return_top_tokens = 0
        job.return_logits = job.return_probs = job.rq_new_tokens = False
        job.max_new_tokens = job.min_new_tokens = 20
        job.generator = object()
        job.serial_number = 1
        job.sequences = [SimpleNamespace(input_ids=list(range(10)), sequence_ids=Tokens(range(10)))]
        for size in (3, 5, 2):
            job.new_tokens = size
            job.sequences[0].sequence_ids.extend([0] * size)
            run(job)
        self.assertEqual(job.rq_new_tokens, 10)
        self.assertEqual(job.max_new_tokens, 10)
        self.assertEqual(job.min_new_tokens, 10)

    def test_recurrent_cleanup_keeps_resumable_checkpoints(self):
        source = self.source('exllamav3/cache/recurrent.py')
        tree = ast.parse(source.read_text())
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'RecurrentCache')
        freed = []
        namespace = {'OrderedDict': OrderedDict, 'PAGE_SIZE': 256,
                     'note_freed': freed.append}
        exec(compile(ast.Module(body=[cls], type_ignores=[]), str(source), 'exec'), namespace)
        cache = namespace['RecurrentCache'](SimpleNamespace(loaded_tp=False), 100)
        cache.pagetable = SimpleNamespace(checkpoint_retention_hashes=lambda: {'live'})
        state = SimpleNamespace(stash=lambda: {'checkpoint_size': 4})
        cache.put('live', state)
        cache.put('orphan', state)
        for _ in range(14):
            cache.put('live', state)
        self.assertIn('live', cache)
        self.assertNotIn('orphan', cache)
        self.assertEqual(cache.current_size, 4)
        self.assertEqual(freed, [4])

    def test_ordinary_host_backing_does_not_scan_memory_maps(self):
        source = self.source('exllamav3/util/host_backing.py')
        tree = ast.parse(source.read_text())
        fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'backing_statistics')
        def forbidden(*args):
            raise AssertionError('ordinary backing should not read smaps')
        namespace = {'_mappings': {}, 'os': SimpleNamespace(environ={}), 'Path': forbidden}
        exec(compile(ast.Module(body=[fn], type_ignores=[]), str(source), 'exec'), namespace)
        result = namespace['backing_statistics']()
        self.assertEqual(result['live_custom_mappings'], 0)
        self.assertEqual(result['actual_hugetlb_bytes'], 0)

    def test_fully_cached_resume_moves_mtp_carry_before_a_mixed_decode_batch(self):
        source = self.source('exllamav3/generator/job.py')
        run = method(source, 'Job', 'allocate_pages', {'PAGE_SIZE': 256})
        moved = []
        class Hidden:
            def to(self, device):
                moved.append(device)
                return 'gpu carry'
        stash = {'mtp_hidden': Hidden()}
        seq = SimpleNamespace(allocate_pages=lambda *args: (2, 1, 0, stash))
        gen = SimpleNamespace(recurrent_cache=object(), mtp_draft=True,
                              model=SimpleNamespace(output_device='cuda:0'),
                              cache=SimpleNamespace(new_from_stashed=lambda *args, **kwargs:
                                                    SimpleNamespace(position=256)))
        job = SimpleNamespace(sequences=[seq], generator=gen, all_unique_hashes=[],
                              pagetable=object(), cached_pages=0, total_pages=0,
                              non_sequential_pages=0, free_recurrent_state=lambda: None)
        run(job)
        self.assertEqual(moved, ['cuda:0'])
        self.assertEqual(job.mtp_last_hidden, 'gpu carry')
        self.assertEqual(seq.mtp_carry_hidden, 'gpu carry')

    def test_mtp_carry_is_frozen_with_the_checkpoint_and_counted_in_its_budget(self):
        source = self.source('exllamav3/cache/recurrent.py')
        tree = ast.parse(source.read_text())
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'RecurrentCache')
        namespace = {'OrderedDict': OrderedDict, 'PAGE_SIZE': 256, 'note_freed': lambda size: None}
        exec(compile(ast.Module(body=[cls], type_ignores=[]), str(source), 'exec'), namespace)
        class Hidden:
            def __init__(self, value):
                self.value = value
            def detach(self):
                return self
            def cpu(self):
                return self
            def clone(self):
                return Hidden(self.value)
            def numel(self):
                return 4
            def element_size(self):
                return 2
        cache = namespace['RecurrentCache'](SimpleNamespace(loaded_tp=False), 100)
        carry = Hidden(7)
        cache.put('prefix', SimpleNamespace(stash=lambda: {'checkpoint_size': 20}), mtp_hidden=carry)
        carry.value = 99
        self.assertEqual(cache['prefix']['mtp_hidden'].value, 7)
        self.assertEqual(cache.current_size, 28)


if __name__ == '__main__':
    unittest.main()
