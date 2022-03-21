from enum import Enum
from uuid import uuid4


class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1


class Person:
    def __init__(self, first_name, last_name, dob, alive):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive

    def update_first_name(self,new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name

    def update_dob(self, new_dob):
        self.dob = new_dob

    def update_status(self, new_status):
        self.alive = new_status


class Instructor(Person):
    def __init__(self, first_name, last_name, dob, alive):
        super.__init__(first_name,last_name, dob, alive)
        self.instructor_id = f'instructor_{uuid4()}'


class Student(Person):
    def __init__(self, first_name, last_name, dob, alive):
        super.__init__(first_name,last_name, dob, alive)
        self.student_id = f'student_{uuid4()}'


class ZipCodeStudent(Student):
    def __init__(self, first_name, last_name, dob, alive):
        super.__init__(first_name,last_name, dob, alive)


class PreKStudent(Student):
    def __init__(self, first_name, last_name, dob, alive):
        super.__init__(first_name, last_name, dob, alive)


class Classroom:
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor):
        self.instructors[instructor.instructor_id] = instructor
        return self.instructors

