"""
Verwaltungslogik fuer Kurse.
"""


class Kursverwaltung:
    def __init__(self):
        self.kurse = {}

    def kurs_hinzufuegen(self, kurs):
        self.kurse[kurs.titel] = kurs

    def kurs_anzeigen(self):
        return list(self.kurse.keys())

    def student_einschreiben(self, student, kurstitel):
        kurs = self.kurse.get(kurstitel)
        if kurs is None:
            raise ValueError(f"Unbekannter Kurs: {kurstitel}")
        return kurs.student_einschreiben(student)
