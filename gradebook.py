from enum import Enum
from uuid import uuid4


class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1


class Person:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = AliveStatus

    def update_first_name(self,new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name

    def update_dob(self, new_dob):
        self.dob = new_dob

    def update_status(self, new_status):
        self.alive = new_status


class Instructor(Person):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name,last_name, dob)
        self.instructor_id = f'instructor_{uuid4()}'


class Student(Person):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name,last_name, dob)
        self.student_id = f'student_{uuid4()}'


class ZipCodeStudent(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name,last_name, dob)


class PreKStudent(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)


class Classroom:
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor):
        self.instructors[instructor.instructor_id] = instructor
        return self.instructors

    def remove_instructor(self, instructor_id):
        del self.instructors[instructor_id]
        return self.instructors

    def add_student(self, student):
        self.students[student.student_id] = student
        return self.students

    def remove_student(self, student_id):
        self.students[student_id]
        return self.students

    def print_instructors(self):
        for instructor in self.instructors.value():
            print(f'{instructor.instructor_id} {instructor.first_name} {instructor.last_name} {instructor.dob} {instructor.alive}')

    def print_students(self):
        for student in self.students.value():
            print(f'{student.students_id} {student.first_name} {student.last_name} {student.dob} {student.alive}')
