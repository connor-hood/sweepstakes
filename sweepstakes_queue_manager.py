from data_queue import Queue
from sweepstake import Sweepstake


class SweepstakesQueueManager:
    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstakes):
        self.queue.enqueue(sweepstakes)
        pass

    def get_sweepstakes(self):
        contest = Sweepstake()
        print("Let's get a contest going!")
        entry = input("what's your name?")
        contest.register_contestant(entry)
        print(contest)
