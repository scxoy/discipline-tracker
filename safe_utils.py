import time
class Safety:
    def __init__(self, timeout_seconde=10, max_steps=10000):
        self.start_time = time.time()
        self.timeout_seconds = timeout_seconde
        self.max_steps = max_steps
        self.steps = 0
        def step(self):
            self.steps += 1
            if self.steps > self.max_steps:
                raise RuntimeError("SAFETY STOP/ trop de tours")
            if time.time() - self.start > self.timeout_seconds:
                raise TimeoutError("SAFETY STOP: timeout")
        