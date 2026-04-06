"""
Klassen fuer Kurse in der Kursverwaltung.
"""


class Kurs:
    def __init__(self, titel, dozent=None, max_teilnehmende=20):
        self.titel = titel
        self.dozent = dozent
        self.max_teilnehmende = max_teilnehmende
        self.teilnehmende = []

    def hat_freie_plaetze(self):
        return len(self.teilnehmende) < self.max_teilnehmende

    def student_einschreiben(self, student):
        if student in self.teilnehmende:
            return False
        if not self.hat_freie_plaetze():
            return False
        self.teilnehmende.append(student)
        return True

    def teilnehmende_namen(self):
        return [student.name for student in self.teilnehmende]
