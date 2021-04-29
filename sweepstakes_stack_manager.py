from data_stack import Stack
from sweepstake import Sweepstake


class SweepstakesStackManager:
    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self, sweepstakes):
        self.stack.push(sweepstakes)
        pass

    def get_sweepstakes(self):
        contest = Sweepstake()
        print("Let's get a contest going!")
        entry = input("what's your name?")
        contest.register_contestant(entry)
