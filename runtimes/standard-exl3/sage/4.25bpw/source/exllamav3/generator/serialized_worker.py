"""One inference owner thread without blocking the HTTP event loop."""
import asyncio
from concurrent.futures import ThreadPoolExecutor


class SerializedWorker:
    def __init__(self, initializer=None):
        self.executor = ThreadPoolExecutor(max_workers=1, initializer=initializer,
                                           thread_name_prefix="inference")
        self.closed = False
        self._cleanup = None

    def submit(self, function, *args, **kwargs):
        if self.closed:
            raise RuntimeError("Inference worker is closed")
        return self.executor.submit(function, *args, **kwargs)

    async def call(self, function, *args, **kwargs):
        future = asyncio.wrap_future(self.submit(function, *args, **kwargs))
        # A disconnected caller must not cancel a queued mutation or leave a
        # still-running CUDA step mistaken for completed work.
        future.add_done_callback(lambda done: None if done.cancelled() else done.exception())
        return await asyncio.shield(future)

    async def close(self, cleanup=None):
        if self._cleanup is None:
            self._cleanup = asyncio.wrap_future(self.submit(cleanup or (lambda: None)))
            self.closed = True
        try:
            await asyncio.shield(self._cleanup)
        except asyncio.CancelledError:
            await asyncio.shield(self._cleanup)
            raise
        finally:
            if self._cleanup.done():
                self.executor.shutdown(wait=False, cancel_futures=False)
