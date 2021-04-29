from sweepstakes_queue_manager import SweepstakesQueueManager
from sweepstakes_stack_manager import SweepstakesStackManager


class MarketingFirmCreator:

    def choose_manager_type(self):
        answer = input("Enter 'queue' or 'stack' for sweepstake management")
        while answer == "queue":
            contest = SweepstakesQueueManager()
            contest.get_sweepstakes()
            return contest
        while answer == "stack":
            contest = SweepstakesStackManager()
            contest.get_sweepstakes()
            return contest
        while answer != "queue":
            print("This is not a valid choice")
            self.choose_manager_type()
        while answer != "stack":
            print("This is not a valid choice")
            self.choose_manager_type()