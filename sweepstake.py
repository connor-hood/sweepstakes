from contestant import Contestant


class Sweepstake:

    def __init__(self):
        self.contestants = []
        self.name = " "

    def register_contestant(self, contestant):
        self.contestants.append(contestant)
        pass

    def pick_winner(self):
        # should return the winner
        pass

    def print_contestant_info(self, winner):
        pass
