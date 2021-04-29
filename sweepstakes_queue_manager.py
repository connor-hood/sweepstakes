from data_queue import Queue
from sweepstake import Sweepstake


class SweepstakesQueueManager:
    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstakes):
        self.queue.enqueue(sweepstakes)
        pass

    def get_sweepstakes(self):
        print("Let's get a contest going!")
        contestants = Sweepstake()
        contestants.register_contestant("Bill")
        contestants.register_contestant("Ted")
        pass
