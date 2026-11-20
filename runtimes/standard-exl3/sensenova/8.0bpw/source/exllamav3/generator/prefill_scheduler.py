"""Share mixed prefill/decode time without changing cache ownership or kernels."""
import math


class PrefillScheduler:
    def __init__(self, time_fraction=0.25):
        if not math.isfinite(time_fraction) or not 0 < time_fraction <= 1:
            raise ValueError("prefill_time_fraction must be in (0, 1]")
        self.time_fraction = time_fraction
        self.decode_debt = 0.0
        self.last_serial = -1
        self.mixed_prefill_steps = 0
        self.decode_only_steps = 0
        self.mixed_step_seconds = 0.0
        self.decode_only_seconds = 0.0

    def select(self, jobs, decoding):
        if not jobs or not decoding:
            self.decode_debt = 0.0
            return list(jobs)
        if self.decode_debt > 0:
            return []
        ordered = sorted(jobs, key=lambda job: job.serial_number)
        job = next((job for job in ordered if job.serial_number > self.last_serial), ordered[0])
        self.last_serial = job.serial_number
        return [job]

    def account(self, decoding, prefilling, elapsed):
        if not decoding:
            self.decode_debt = 0.0
        elif prefilling:
            # Charge the whole mixed step: decode's readback also waits for any
            # asynchronous prefill kernels, so host enqueue time would undercount.
            self.decode_debt += elapsed * (1 - self.time_fraction) / self.time_fraction
            self.mixed_prefill_steps += 1
            self.mixed_step_seconds += elapsed
        else:
            self.decode_debt = max(0.0, self.decode_debt - elapsed)
            self.decode_only_steps += 1
            self.decode_only_seconds += elapsed

    def stats(self):
        return {
            "prefill_time_fraction": self.time_fraction,
            "decode_debt_seconds": self.decode_debt,
            "mixed_prefill_steps": self.mixed_prefill_steps,
            "decode_only_steps": self.decode_only_steps,
            "mixed_step_seconds": self.mixed_step_seconds,
            "decode_only_seconds": self.decode_only_seconds,
        }
