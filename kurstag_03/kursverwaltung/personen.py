"""
Klassen fuer Personen in der Kursverwaltung.
"""


class Person:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email


class Student(Person):
    def __init__(self, name, student_id, email=None):
        super().__init__(name, email=email)
        self.student_id = student_id


class Dozent(Person):
    def __init__(self, name, fachgebiet, email=None):
        super().__init__(name, email=email)
        self.fachgebiet = fachgebiet
