class Contestant:

    def __init__(self, first_name, last_name, email, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email
        self.registration_number = registration_number

    def notify(self, winner):
        print(f'{winner} has won the sweepstakes')
