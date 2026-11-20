"""Test inference ownership and HTTP responsiveness without a CUDA runtime."""
import ast
import asyncio
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import threading
from types import SimpleNamespace
import unittest


REPO = Path(__file__).resolve().parents[1]


class Tensor:
    def __init__(self, value):
        self.value = value
        self.device = SimpleNamespace(type="cpu")

    def detach(self):
        return self

    def clone(self):
        return Tensor(self.value)


class Job:
    def __init__(self, fail_enqueue=False):
        self.fail_enqueue = fail_enqueue
        self.serial_number = None
        self.new_tokens = 0
        self.rq_new_tokens = 0
        self.owner = None

    def constrain_output_now(self, output):
        self.owner.record("constrain")


class Generator:
    def __init__(self):
        self.operations = []
        self.threads = []
        self.pending_jobs = []
        self.active_jobs = []
        self.started = threading.Event()
        self.release = threading.Event()
        self.release.set()
        self.failure = None
        self.finish = False
        self.staging = Tensor(0)
        self.cpu_page_cache = SimpleNamespace(close=lambda: self.record("cleanup"))

    def record(self, operation):
        self.operations.append(operation)
        self.threads.append(threading.get_ident())

    def enqueue(self, job):
        self.record("enqueue")
        if job.fail_enqueue:
            raise ValueError("invalid request")
        job.serial_number = len(self.operations)
        job.owner = self
        self.pending_jobs.append(job)

    def cancel(self, job):
        self.record("cancel")
        for queue in (self.pending_jobs, self.active_jobs):
            if job in queue:
                queue.remove(job)

    def iterate(self):
        self.record("iterate")
        self.started.set()
        if not self.release.wait(3):
            raise TimeoutError("test did not release inference")
        if self.failure is not None:
            raise self.failure
        self.active_jobs.extend(self.pending_jobs)
        self.pending_jobs.clear()
        results = []
        for job in list(self.active_jobs):
            job.new_tokens += 1
            self.staging.value = job.new_tokens
            results.append({"job": job, "stage": "streaming", "eos": self.finish,
                            "serial": job.serial_number, "token_ids": self.staging})
            if self.finish:
                self.active_jobs.remove(job)
        return results

    def get_cache_stats(self):
        return {"active_jobs": len(self.active_jobs), "pending_jobs": len(self.pending_jobs)}


class AsyncGeneratorTests(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = Path(cls.tmp.name)
        blocks = (REPO / "runtimes/tabby/exllamav3.patch").read_text().split("diff --git ")[1:]
        worker = next(b for b in blocks if b.startswith("a/exllamav3/generator/serialized_worker.py "))
        path = root / "serialized_worker.py"
        path.write_text("\n".join(line[1:] for line in worker.splitlines()
                                  if line.startswith("+") and not line.startswith("+++")) + "\n")
        spec = importlib.util.spec_from_file_location("serialized_worker", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.worker_type = module.SerializedWorker
        source = REPO / ".local/scheduler-base/exllamav3/generator/async_generator.py"
        cls.source_available = source.is_file()
        if not cls.source_available:
            return
        target = root / "exllamav3/generator/async_generator.py"
        target.parent.mkdir(parents=True)
        target.write_bytes(source.read_bytes())
        subset = "".join("diff --git " + b for b in blocks
                         if b.startswith("a/exllamav3/generator/async_generator.py "))
        subprocess.run(["git", "apply", "-"], input=subset, text=True, cwd=root, check=True)
        tree = ast.parse(target.read_text())
        tree.body = [node for node in tree.body
                     if not (isinstance(node, ast.ImportFrom) and node.level)
                     and not (isinstance(node, ast.Import) and any(n.name == "torch" for n in node.names))]
        cuda = SimpleNamespace(is_initialized=lambda: False)
        namespace = {"Generator": Generator, "Job": Job, "SerializedWorker": cls.worker_type,
                     "torch": SimpleNamespace(Tensor=Tensor, cuda=cuda)}
        from contextvars import ContextVar
        namespace["PREFIX_REQUEST"] = ContextVar("test_prefix_request", default=None)
        exec(compile(tree, str(target), "exec"), namespace)
        cls.generator_type = namespace["AsyncGenerator"]
        cls.job_type = namespace["AsyncJob"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    async def wait_for(self, predicate):
        async with asyncio.timeout(2):
            while not predicate():
                await asyncio.sleep(0.001)

    async def setup_generator(self, blocked=False):
        if not self.source_available:
            self.skipTest("Requires the pinned checkout in .local/scheduler-base (prepared by CI)")
        generator = self.generator_type()
        self.addAsyncCleanup(generator.close)
        if blocked:
            generator.generator.release.clear()
            self.addCleanup(generator.generator.release.set)
        return generator

    async def test_http_loop_stays_responsive_during_inference(self):
        generator = await self.setup_generator(blocked=True)
        job = self.job_type(generator)
        await self.wait_for(generator.generator.started.is_set)
        marker = []
        asyncio.get_running_loop().call_soon(marker.append, "http")
        await asyncio.sleep(0.005)
        self.assertEqual(marker, ["http"])
        self.assertTrue(job.queue.empty())
        generator.generator.release.set()
        await self.wait_for(lambda: not job.queue.empty())

    async def test_two_requests_advance_in_the_same_delivery(self):
        generator = await self.setup_generator()
        first, second = self.job_type(generator), self.job_type(generator)
        one, two = await asyncio.gather(first.queue.get(), second.queue.get())
        self.assertEqual((one["cumulative_tokens"], two["cumulative_tokens"]), (1, 1))
        self.assertNotEqual(one["serial"], two["serial"])
        self.assertEqual(len(set(generator.generator.threads)), 1)
        self.assertNotEqual(generator.generator.threads[0], threading.get_ident())

    async def test_cancellation_wakes_stream_before_worker_releases_cache(self):
        generator = await self.setup_generator(blocked=True)
        job = self.job_type(generator)
        await self.wait_for(generator.generator.started.is_set)
        stream = asyncio.create_task(anext(job.__aiter__()))
        cancel = asyncio.create_task(job.cancel())
        await self.wait_for(stream.done)
        with self.assertRaises(StopAsyncIteration):
            await stream
        self.assertFalse(cancel.done())
        self.assertNotIn("cancel", generator.generator.operations)
        generator.generator.release.set()
        await cancel
        self.assertNotIn(job.job, generator.generator.active_jobs)

    async def test_constraints_and_snapshots_queue_behind_inference(self):
        generator = await self.setup_generator(blocked=True)
        job = self.job_type(generator)
        await self.wait_for(generator.generator.started.is_set)
        job.constrain_output_now("end reasoning")
        snapshot = asyncio.create_task(generator.call(generator.generator.record, "snapshot"))
        await asyncio.sleep(0.005)
        self.assertFalse(snapshot.done())
        generator.generator.release.set()
        await snapshot
        operations = generator.generator.operations
        self.assertLess(operations.index("iterate"), operations.index("constrain"))
        self.assertLess(operations.index("constrain"), operations.index("snapshot"))
        self.assertEqual(len(set(generator.generator.threads)), 1)

    async def test_delayed_consumers_keep_independent_tensor_payloads(self):
        generator = await self.setup_generator()
        job = self.job_type(generator)
        first = await job.queue.get()
        await self.wait_for(lambda: job.job.new_tokens > 3)
        self.assertEqual(first["token_ids"].value, 1)
        self.assertEqual(first["cumulative_tokens"], 1)

    async def test_failed_enqueue_does_not_latch_or_strand_other_request(self):
        generator = await self.setup_generator()
        invalid, valid = self.job_type(generator, fail_enqueue=True), self.job_type(generator)
        failed, passed = await asyncio.gather(invalid.queue.get(), valid.queue.get())
        self.assertIsInstance(failed, ValueError)
        self.assertEqual(passed["cumulative_tokens"], 1)
        self.assertIsNone(generator.error)

    async def test_fatal_inference_error_reaches_current_and_future_requests(self):
        generator = await self.setup_generator()
        generator.generator.failure = ValueError("inference failed")
        first, second = self.job_type(generator), self.job_type(generator)
        for job in (first, second):
            self.assertIsInstance(await job.queue.get(), ValueError)
        later = self.job_type(generator)
        self.assertIsInstance(await later.queue.get(), ValueError)
        await later.cancel()
        self.assertNotIn("cancel", generator.generator.operations)

    async def test_close_waits_for_inflight_step_before_cleanup(self):
        generator = await self.setup_generator(blocked=True)
        self.job_type(generator)
        await self.wait_for(generator.generator.started.is_set)
        closing = asyncio.create_task(generator.close())
        await asyncio.sleep(0.005)
        self.assertFalse(closing.done())
        self.assertNotIn("cleanup", generator.generator.operations)
        generator.generator.release.set()
        await closing
        self.assertEqual(generator.generator.operations[-1], "cleanup")
        self.assertEqual(len(set(generator.generator.threads)), 1)
        await generator.close()
        self.assertEqual(generator.generator.operations.count("cleanup"), 1)

    async def test_cancelled_close_still_drains_before_returning(self):
        generator = await self.setup_generator(blocked=True)
        self.job_type(generator)
        await self.wait_for(generator.generator.started.is_set)
        closing = asyncio.create_task(generator.close())
        await asyncio.sleep(0.005)
        closing.cancel()
        await asyncio.sleep(0.005)
        self.assertFalse(closing.done())
        generator.generator.release.set()
        with self.assertRaises(asyncio.CancelledError):
            await closing
        self.assertEqual(generator.generator.operations[-1], "cleanup")

    async def test_closed_generator_fails_new_requests_immediately(self):
        generator = await self.setup_generator()
        await generator.close()
        job = self.job_type(generator)
        self.assertIsInstance(await job.queue.get(), RuntimeError)

    async def test_worker_caller_cancellation_does_not_cancel_mutation(self):
        worker = self.worker_type()
        started, release = threading.Event(), threading.Event()
        events = []
        def step():
            started.set()
            release.wait(2)
            events.append("step")
        task = asyncio.create_task(worker.call(step))
        await self.wait_for(started.is_set)
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task
        release.set()
        await worker.close(lambda: events.append("cleanup"))
        self.assertEqual(events, ["step", "cleanup"])
        with self.assertRaises(RuntimeError):
            worker.submit(lambda: 1)


if __name__ == "__main__":
    unittest.main()
