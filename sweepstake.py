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
        group = self.contestants
        winner = random.choice(group)
        return winner
        # should return the winner

    def print_contestant_info(self, contestant):
        print(f"Contestant's first name:{contestant.first_name}")
        print(f"Contestant's last name:{contestant.last_name}")
        print(f"Contestant's email address:{contestant.email_address}")
        print(f"Contestant's registration #:{contestant.registration_number}")
        pass
