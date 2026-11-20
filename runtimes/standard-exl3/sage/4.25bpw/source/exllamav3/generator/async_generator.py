from __future__ import annotations
from .generator import Generator
from .job import Job
from .serialized_worker import SerializedWorker
from .prefix_diagnostics import PREFIX_REQUEST
import asyncio
import torch

# Sentinel pushed to an AsyncJob's queue on cancellation so a consumer parked in queue.get() wakes up and
# exits, rather than waiting forever for results that will no longer be produced
_CANCELLED_SENTINEL = object()

class AsyncGenerator:
    """
    Async wrapper for dynamic generator. See definition of Generator.
    """
    def __init__(self, *args, **kwargs):
        self.generator = Generator(*args, **kwargs)
        device = torch.cuda.current_device() if torch.cuda.is_initialized() else None
        self.worker = SerializedWorker(
            initializer=(lambda: torch.cuda.set_device(device)) if device is not None else None
        )
        self.jobs = {}
        self.error = None
        self.cache_stats = self.generator.get_cache_stats()
        self._closing = False
        self._close_task = None
        self._mutations = set()
        self.condition = asyncio.Condition()
        self.iteration_task = asyncio.create_task(self._run_iteration())

    async def _run_iteration(self):
        try:
            while True:
                # Sleep while there is no async work registered. The condition releases its lock while waiting and
                # is notified by enqueue() or close(), so this background task does not spin between requests.
                async with self.condition:
                    # Wake when the first job arrives or when close() has cancelled the iteration task.
                    await self.condition.wait_for(lambda: len(self.jobs) > 0 or self.iteration_task.cancelled())

                # Drive exactly one synchronous generator step and fan out any returned events to the owning
                # AsyncJob queues. Missing jobs can happen if a job was cancelled after iterate() started.
                # Delivery must never block: this single task serves every job, so waiting on one stalled
                # consumer (e.g. a disconnected client that stopped draining its queue) would wedge the whole
                # generator (issue #227).
                results, self.cache_stats = await self.worker.call(self._iterate)
                self.deliver_results(results)

                # The worker await already lets network I/O run during inference.
                # Give ready consumers a chance to queue controls before the next step.
                await asyncio.sleep(0)

        except asyncio.CancelledError:
            # Silently return on cancel
            return

        except Exception as e:
            # If the generator throws an exception it won't pertain to any one ongoing job, so push it to all of
            # them. The iteration task ends here and the generator is unusable, so record the error and deliver
            # it to any job enqueued later as well, instead of letting those jobs wait forever on a dead loop.
            self.error = e
            for async_job in self.jobs.values():
                async_job.put_result(e)
            self.jobs.clear()

    def _iterate(self):
        try:
            return self._step()
        except Exception as error:
            # Queued control operations must see a fatal inference failure
            # before the event loop receives and broadcasts it.
            self.error = error
            raise

    def _step(self):
        results = self.generator.iterate()
        cuda_devices = set()

        def freeze(value):
            if isinstance(value, torch.Tensor):
                result = value.detach().clone()
                if result.device.type == "cuda":
                    cuda_devices.add(result.device)
                return result
            if isinstance(value, dict):
                return {key: freeze(child) for key, child in value.items()}
            if isinstance(value, list):
                return [freeze(child) for child in value]
            if isinstance(value, tuple):
                return tuple(freeze(child) for child in value)
            return value

        frozen = []
        for result in results:
            # Tensor staging and Job counters belong to the worker. Consumers
            # can keep an event after the next inference step has begun.
            event = {key: value if key == "job" else freeze(value)
                     for key, value in result.items()}
            job = event["job"]
            event["cumulative_tokens"] = max(0, job.rq_new_tokens + job.new_tokens)
            frozen.append(event)
        for device in cuda_devices:
            torch.cuda.synchronize(device)
        return frozen, self.generator.get_cache_stats()

    async def call(self, operation, *args, **kwargs):
        """Serialize cache inspection and control with inference."""
        return await self.worker.call(operation, *args, **kwargs)

    def _submit_mutation(self, job, operation, *args):
        future = asyncio.wrap_future(self.worker.submit(operation, *args))
        self._mutations.add(future)

        def completed(done):
            self._mutations.discard(done)
            if done.cancelled():
                return
            error = done.exception()
            if error is not None and self.jobs.pop(job.job, None) is not None:
                job.put_result(error)
                if not self._closing and self.error is None:
                    self._submit_mutation(job, self.generator.cancel, job.job)

        future.add_done_callback(completed)

    def deliver_results(self, results):
        """
        Fan generator results out to the owning AsyncJob queues. Missing jobs can happen if a job
        was cancelled after iterate() started. Delivery must never block: this single task serves
        every job, so waiting on one stalled consumer would wedge the whole generator (issue #227).
        """
        for result in results:
            job = result["job"]
            async_job = self.jobs.get(job)
            if not async_job:
                continue
            if result.get("stage") == "error":
                # Per-job failure contained by Generator.reap_failed_job. The raw exception
                # must go into the queue as an exception object, not as a result dict:
                # __aiter__ re-raises queued exceptions, which the server surfaces as an
                # error for this request. A dict here would instead stream as a clean
                # (empty) completion.
                async_job.put_result(result["error"])
                del self.jobs[job]
                continue
            async_job.put_result(result)
            if result["eos"]:
                del self.jobs[job]

    def enqueue(self, job: AsyncJob):
        # The iteration task died on a generator exception; surface it to the new job's consumer immediately
        if self.error is not None or self._closing:
            job.put_result(self.error or RuntimeError("Generator is closed"))
            return

        # Track the AsyncJob before enqueueing the underlying Job so any immediate generator result has a queue to
        # land in. The sync generator still owns scheduling and serial assignment.
        assert job.job not in self.jobs
        self.jobs[job.job] = job
        self._submit_mutation(job, self._enqueue_job, job.job)

        # Condition.notify_all() must run while holding the condition lock, so schedule a tiny coroutine instead of
        # trying to notify directly from this synchronous method.
        asyncio.create_task(self._notify_condition())

    async def _notify_condition(self):
        async with self.condition:
            self.condition.notify_all()

    def _enqueue_job(self, job):
        if self.error is not None:
            raise self.error
        return self.generator.enqueue(job)

    async def close(self):
        if self._close_task is None:
            self._closing = True
            self._close_task = asyncio.create_task(self._close())
        try:
            await asyncio.shield(self._close_task)
        except asyncio.CancelledError:
            await asyncio.shield(self._close_task)
            raise

    async def _close(self):
        self.iteration_task.cancel()

        # Force a re-check of the condition to unlock the loop
        await self._notify_condition()
        try:
            await self.iteration_task
        except asyncio.CancelledError:
            pass

        # Wake any consumers still parked on job queues; no more results will be produced
        for async_job in self.jobs.values():
            async_job.put_result(_CANCELLED_SENTINEL)
        self.jobs.clear()

        await self.worker.close(self._cleanup)

    def _cleanup(self):
        if self.error is None:
            for job in list(self.generator.pending_jobs) + list(self.generator.active_jobs):
                self.generator.cancel(job)
        if torch.cuda.is_initialized():
            for device in range(torch.cuda.device_count()):
                torch.cuda.synchronize(device)
        cpu_cache = getattr(self.generator, "cpu_page_cache", None)
        if cpu_cache is not None:
            cpu_cache.close()

    async def cancel(self, job: AsyncJob):
        # Wake the HTTP consumer immediately; cache release follows any running
        # step on the owner thread, and late results have no async recipient.
        if self.jobs.pop(job.job, None) is not None:
            job.put_result(_CANCELLED_SENTINEL)
        if self.error is None and not self._closing:
            await self.worker.call(self._cancel_job, job.job)

    def _cancel_job(self, job):
        if self.error is None:
            self.generator.cancel(job)

    def constrain_output(self, job, output):
        if self.jobs.get(job.job) is job and not self._closing and self.error is None:
            if isinstance(output, torch.Tensor):
                output = output.clone()
            self._submit_mutation(job, self._constrain_job, job.job, output)

    def _constrain_job(self, job, output):
        if self.error is None and (
            job in self.generator.active_jobs or job in self.generator.pending_jobs
        ):
            job.constrain_output_now(output)


class AsyncJob:
    """
    Async wrapper for dynamic generator job. See definition of Job.
    """
    def __init__(self, generator: AsyncGenerator, *args: object, **kwargs: object):
        self.generator = generator
        self.job = Job(*args, **kwargs)
        self.job.prefix_metadata = dict(PREFIX_REQUEST.get() or {})
        # The queue is unbounded and written with put_nowait: the shared iteration task must never block on a
        # consumer that stopped draining (see _run_iteration). Growth is paced by the sync generator's own token
        # rate and ends when the job completes or is cancelled, which is the frontend's responsibility on client
        # disconnect.
        self.queue = asyncio.Queue()
        self.generator.enqueue(self)
        self.cancelled = False

    def put_result(self, result):
        self.queue.put_nowait(result)

    async def __aiter__(self):
        while True:
            # cancel() sets this flag after removing the job from the generator; the iterator exits cleanly instead
            # of waiting forever for an EOS event that will no longer be produced.
            if self.cancelled:
                break

            # Results are pushed by AsyncGenerator._run_iteration(). Exceptions are broadcast to all queues if the
            # shared generator loop fails, so consuming code sees the error at the await point. The sentinel wakes
            # this iterator when the job is cancelled from another task while parked here.
            result = await self.queue.get()
            if result is _CANCELLED_SENTINEL:
                break
            if isinstance(result, Exception):
                raise result
            yield result
            if result["eos"]:
                break

    def constrain_output_now(self, output: str | torch.Tensor):
        """
        Inject a fixed token string into the job's output stream; see Job.constrain_output_now. Safe to
        call from any coroutine on the generator's event loop. Note that tokens already sampled by the
        shared iteration task but still queued for this consumer precede the injection in the stream.
        """
        self.generator.constrain_output(self, output)

    async def cancel(self):
        # Delegate cancellation to the wrapper so it can update both the sync generator queue and the async job map,
        # then mark this iterator as closed for any current or future consumers.
        await self.generator.cancel(self)
        self.cancelled = True
