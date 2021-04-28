from contestant import Contestant
import random


class Sweepstake:

    def __init__(self):
        self.contestants = []
        self.name = " "

    def register_contestant(self, contestant):
        self.contestants.append(contestant)
        pass

    def pick_winner(self):
        pot_of_entries = self.contestants
        winner = random.choice(pot_of_entries)
        return winner
        # should return the winner
        pass

    def print_contestant_info(self, winner):
        pass
