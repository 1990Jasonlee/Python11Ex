from enum import Enum


class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 0


class Person:
    def __init__(self, first_name, last_name, dob, alive):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive