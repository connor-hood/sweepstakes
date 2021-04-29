from data_stack import Stack
from sweepstake import Sweepstake


class SweepstakesStackManager:
    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self, sweepstakes):
        self.stack.push(sweepstakes)
        contest = Sweepstake()
        winner = contest.pick_winner()
        print(f"The winner of the contest is:{winner}")
        pass

    def get_sweepstakes(self):
        contest = Sweepstake()
        print("Let's get a contest going!")
        entry = input("what's your name?")
        contest.register_contestant(entry)
        
