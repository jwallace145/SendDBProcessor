import datetime
import random
import sys


class Climber:

    def __init__(self, email: str = '', username: str = '', first_name: str = '', last_name: str = '') -> None:
        self.id = str(datetime.datetime.utcnow()) + 'T' + \
            str(random.randint(0, sys.maxsize))
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def initialize_from_db_item(self, item: dict):
        self.id = item['Item']['id']['S']
        self.email = item['Item']['email']['S']
        self.username = item['Item']['username']['S']
        self.first_name = item['Item']['first_name']['S']
        self.last_name = item['Item']['last_name']['S']
