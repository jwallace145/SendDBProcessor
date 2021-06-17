import datetime
import random
import sys


class Route:

    def __init__(self, climber_id: str = '', name: str = '', grade: str = '', type: str = '', crag: str = '', style: str = '', ascent: str = '', height: int = '', pitches: int = '') -> None:
        self.id = str(datetime.datetime.utcnow()) + 'T' + \
            str(random.randint(0, sys.maxsize))
        self.climber_id = climber_id
        self.name = name
        self.grade = grade
        self.type = type
        self.crag = crag
        self.style = style
        self.ascent = ascent
        self.height = height
        self.pitches = pitches
        self.timestamp = str(datetime.datetime.utcnow())

    def initialize_from_db_item(self, item: dict):
        self.id = item['id']['S']
        self.climber_id = item['climber_id']['S']
        self.name = item['name']['S']
        self.grade = item['grade']['S']
        self.type = item['type']['S']
        self.crag = item['crag']['S']
        self.style = item['style']['S']
        self.ascent = item['ascent']['S']
        self.height = item['height']['S']
        self.pitches = item['pitches']['S']
        self.timestamp = item['timestamp']['S']
