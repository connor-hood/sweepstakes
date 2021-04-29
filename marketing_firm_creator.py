import sweepstakes_queue_manager
import sweepstakes_stack_manager
from sweepstakes_queue_manager import SweepstakesQueueManager
from sweepstakes_stack_manager import SweepstakesStackManager


class MarketingFirmCreator:

    def choose_manager_type(self):
        answer = input("Enter queue or stack for sweepstake management")
        if answer == "queue":
            contest = sweepstakes_queue_manager.SweepstakesQueueManager
            return contest
        elif answer == "stack":
            contest = sweepstakes_stack_manager.SweepstakesStackManager
            return contest
        else:
            print("This is not a valid choice")
        pass
