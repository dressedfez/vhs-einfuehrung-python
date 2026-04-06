"""
Oeffentliche API des Pakets fuer eine einfache Kursverwaltung.
"""

from .kurse import Kurs
from .personen import Dozent, Student
from .verwaltung import Kursverwaltung

__all__ = ["Student", "Dozent", "Kurs", "Kursverwaltung"]
