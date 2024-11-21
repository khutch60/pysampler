import time


class Clock:
    def __init__(self):
        self.start_time = None
        self.reset = time.time()
        self.step_length = None

    def step(self):
        if time.time() - self.reset >= self.step_length - .002:
            self.reset = time.time()
            return True
        else:
            pass

