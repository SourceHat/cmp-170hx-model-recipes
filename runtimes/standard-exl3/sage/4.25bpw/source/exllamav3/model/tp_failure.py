"""Surface TP worker faults even when the local rank is inside a collective."""
from __future__ import annotations

import json
from multiprocessing import Pipe
from multiprocessing.connection import wait
import os
from pathlib import Path
import re
import threading
import time


EXIT_CODE = 70


def failure_record(device, error=None, exit_code=None):
    record = {"at": time.time(), "pid": os.getpid(), "device": device,
              "error_code": "tp_worker_failed" if error is not None else "tp_worker_exited",
              "error_type": type(error).__name__ if error is not None else "TPWorkerExited"}
    if error is not None:
        frame = error.__traceback__
        while frame is not None and frame.tb_next is not None:
            frame = frame.tb_next
        if frame is not None:
            name = Path(frame.tb_frame.f_code.co_filename).name
            if re.fullmatch(r"[A-Za-z0-9_.-]+\.py", name):
                record["failure_site"] = f"{name}:{frame.tb_lineno}"
    if exit_code is not None:
        record["worker_exit_code"] = exit_code
    return record


def record_failure(record):
    """Write the first fault atomically, without exception text or tensor data."""
    job = os.environ.get("MESHIFY_JOB_ID", "")
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,256}", job):
        return
    root = os.environ.get("EXLLAMA_TP_FAILURE_LOG_DIR")
    if not root:
        return
    directory = Path(root) / job
    temporary = directory / ('.tp-failure-' + str(os.getpid()) + '.tmp')
    try:
        directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        temporary.write_text(json.dumps(record, allow_nan=False) + '\n')
        temporary.chmod(0o600)
        try:
            os.link(temporary, directory / 'tp-failure.json')
        except FileExistsError:
            return
        os.replace(temporary, directory / 'generation-failure.json')
    except OSError:
        pass
    finally:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass


def tp_worker_entry(function, device, *args):
    try:
        function(*args)
    except BaseException as error:
        record_failure(failure_record(device, error=error))
        # A failed rank cannot rejoin an in-flight collective. Its sentinel
        # wakes the parent independently of the ordinary response pipe.
        os._exit(EXIT_CODE)


class TPFailureMonitor:
    def __init__(self):
        self._reader, self._writer = Pipe(duplex=False)
        self._children = {}
        self._lock = threading.Lock()
        self._stopped = False
        self._thread = threading.Thread(target=self._watch, name='tp-worker-fault', daemon=True)
        self._thread.start()

    def add(self, process, device):
        with self._lock:
            if self._stopped:
                raise RuntimeError('TP failure monitor is closed')
            self._children[process.sentinel] = (process, device)
            self._writer.send_bytes(b'w')

    def _watch(self):
        while True:
            with self._lock:
                if self._stopped:
                    return
                children = dict(self._children)
            ready = wait([self._reader, *children])
            if self._reader in ready:
                self._reader.recv_bytes(1)
                continue
            with self._lock:
                if self._stopped:
                    return
                for sentinel in ready:
                    process, device = children[sentinel]
                    record_failure(failure_record(device, exit_code=process.exitcode))
                    # The supervisor owns the cgroup, normal teardown and
                    # serving recovery. Do not try to reuse poisoned ranks.
                    os._exit(EXIT_CODE)

    def local(self, device, function, *args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as error:
            record_failure(failure_record(device, error=error))
            os._exit(EXIT_CODE)

    def close(self):
        with self._lock:
            if self._stopped:
                return
            self._stopped = True
            self._writer.send_bytes(b'x')
        self._thread.join()
        self._reader.close()
        self._writer.close()
