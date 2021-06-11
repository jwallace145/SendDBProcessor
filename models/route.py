import datetime
import random
import sys


class Route:

    def __init__(self, climber_email: str, name: str, grade: str, type: str, crag: str, style: str, ascent: str, height: int, pitches: int) -> None:
        self.id = str(datetime.datetime.utcnow()) + 'T' + \
            str(random.randint(0, sys.maxsize))
        self.climber_email = climber_email
        self.name = name
        self.grade = grade
        self.type = type
        self.crag = crag
        self.style = style
        self.ascent = ascent
        self.height = height
        self.pitches = pitches
        self.timestamp = str(datetime.datetime.utcnow())
