import datetime
import random
import sys


class Climber:

    def __init__(self, email, username, first_name, last_name) -> None:
        self.id = str(datetime.datetime.utcnow()) + 'T' + \
            str(random.randint(0, sys.maxsize))
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
