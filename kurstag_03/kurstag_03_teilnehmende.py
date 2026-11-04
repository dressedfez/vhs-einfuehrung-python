# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo==0.25.2",
# ]
# ///

# Zellenausdrücke und Rückgaben gehören zum marimo-Notebook-Format.
# ruff: noqa: B018, PLR1711, UP003, PLR0133

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    def pruefhinweis(status, aufgabe, hinweis):
        if status is None:
            return mo.callout(
                mo.md(f"**Noch offen · {aufgabe}**\n\n{hinweis}"),
                kind="neutral",
            )
        if status:
            return mo.callout(
                mo.md(f"**✓ Richtig · {aufgabe}**\n\n{hinweis}"),
                kind="success",
            )
        return mo.callout(
            mo.md(f"**Noch nicht ganz · {aufgabe}**\n\n{hinweis}"),
            kind="warn",
        )

    return (pruefhinweis,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Kurstag 3 · Mein Python-Arbeitsheft

    **Funktionen · Klassen · Module**

    Dieses Arbeitsheft begleitet die Folien. Lies die kurzen Erklärungen, führe die Beispiele aus und bearbeite die vier Basisübungen. Die Musterlösungen werden im Unterricht besprochen und stehen in der Folienpräsentation.

    ## So arbeitest du mit dem Notebook

    - Im Ordner `kurstag_03` starten: `uvx --from "marimo==0.25.2" marimo edit kurstag_03_teilnehmende.py`.
    - Eine Codezelle mit **Shift+Enter** ausführen.
    - Erst vermuten, dann ausführen, dann das Ergebnis erklären.
    - **Neutral:** Aufgabe noch offen · **Orange:** Hinweis beachten · **Grün:** Prüfung bestanden.
    - Die vorgegebenen Antwortvariablen in den Übungszellen beibehalten, damit die Rückmeldung sie findet.

    Zu zweit: Eine Person tippt, die andere erklärt. Regelmäßig wechseln. Deine Änderungen werden in dieser Datei gespeichert; für einen frischen Start vorher eine Kopie anlegen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Unser Weg heute

    1. Funktionen definieren, aufrufen und Ergebnisse zurückgeben.
    2. Funktionen als Werte verwenden: `lambda`, `map`, `filter`, `reduce`.
    3. Daten und Verhalten mit Klassen und Objekten verbinden.
    4. Vererbung, Komposition und gemeinsames Verhalten unterscheiden.
    5. Code mit Modulen und Packages organisieren.

    Die Abschnitte **Zusatzteil** sind freiwillig und können nach dem Grundteil bearbeitet werden.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Funktionen

    Eine Funktion bündelt Anweisungen unter einem Namen. Mit Parametern erhält sie Eingaben; `return` gibt ein Ergebnis zurück.

    ```python
    def verdopple(zahl):
        return zahl * 2

    verdopple(5)
    ```

    `def` definiert die Funktion. Der eingerückte Block gehört zur Funktion. Der Aufruf `verdopple(5)` führt sie aus.
    """)
    return


@app.cell
def _(mo):
    def begruesse(name):
        return f"Hallo, {name}!"

    begruesse("Mara")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Parameter, Argumente und Rückgabewerte

    **Parameter** sind die Namen in der Definition. **Argumente** sind die Werte beim Aufruf.

    ```python
    def voller_name(vorname, nachname):  # vorname und nachname sind Parameter
        return f"{vorname} {nachname}"

    voller_name("Ada", "Lovelace")  # Ergebnis: "Ada Lovelace"
    voller_name("Lovelace", "Ada")  # vertauscht: "Lovelace Ada"
    ```

    `print(...)` zeigt etwas an. `return` übergibt einen Wert, mit dem der aufrufende Code weiterarbeiten kann. Ohne `return` ist der Rückgabewert `None`.
    """)
    return


@app.cell
def _(mo):
    def _voller_name(vorname, nachname):
        return f"{vorname} {nachname}"

    (_voller_name("Ada", "Lovelace"), _voller_name("Lovelace", "Ada"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Standardwerte

    Ein Standardwert wird verwendet, wenn beim Aufruf kein anderes Argument angegeben ist.

    ```python
    def begruesse(name, text="Guten Tag"):
        return f"{text}, {name}!"

    begruesse("Mara")
    begruesse("Mara", text="Hallo")
    begruesse(text="Hallo", name="Mara")  # Reihenfolge bei Keyword-Argumenten ist frei
    ```

    **Keyword-Argumente** nennen den Parameter beim Aufruf. So ist die Zuordnung klar und die Reihenfolge frei: `text="Hallo", name="Mara"` ergibt ebenfalls `Hallo, Mara!`.
    """)
    return


@app.cell
def _(mo):
    def min_max(werte):
        return min(werte), max(werte)

    kleinster, groesster = min_max([7, 2, 9, 4])
    (kleinster, groesster)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Lokale Namen und innere Funktionen · Zusatzteil

    Namen, die innerhalb einer Funktion entstehen, sind dort lokal. Sie halten Zwischenschritte von anderen Programmteilen getrennt.

    Eine Funktion kann eine Hilfsfunktion enthalten. Das passt, wenn die Hilfsfunktion nur an dieser Stelle gebraucht wird.
    """)
    return


@app.cell
def _(mo):
    def mittelwert(werte):
        def total(zahlen):
            return sum(zahlen)

        return total(werte) / len(werte)

    mittelwert([2, 4, 6])
    return


@app.cell
def _(mo):
    def transformiere(texte, funktion):
        return [funktion(text) for text in texte]

    (transformiere(["anna", "ben"], str.title), transformiere(["anna", "ben"], str.upper))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Lambda-Funktionen

    `lambda` erzeugt eine kurze Funktion aus einem einzelnen Ausdruck:

    ```python
    lambda parameter: ausdruck
    ```

    Lambda ist praktisch, wenn eine kurze Funktion direkt übergeben wird. Bei mehreren Schritten ist eine mit `def` benannte Funktion leichter zu lesen.
    """)
    return


@app.cell
def _(mo):
    quadriere = lambda zahl: zahl**2
    quadriere(5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `map` und `filter`

    - `map(funktion, folge)` wendet die Funktion auf jedes Element an.
    - `filter(pruefung, folge)` behält die Elemente, für die die Prüfung `True` ergibt.

    Beide geben einen Iterator zurück. Mit `list(...)` kannst du alle Ergebnisse anzeigen.
    """)
    return


@app.cell
def _(mo):
    _namen = ["anna", "ben", "carla"]
    list(map(str.title, _namen))
    return


@app.cell
def _(mo):
    _punkte = [12, 5, 18, 9, 20]
    list(filter(lambda punkt: punkt >= 10, _punkte))
    return


@app.cell
def _(mo):
    _punkte = [12, 5, 18, 9, 20]
    [punkt for punkt in _punkte if punkt >= 10]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Eine Listen-Abstraktion kann Filtern und Umwandeln verbinden:

    ```python
    namen = ["frank", "egon", "karl"]
    [name.title() for name in namen if "a" in name]
    ```

    Wähle die Schreibweise, die die Absicht der Aufgabe am klarsten zeigt.
    """)
    return


@app.cell
def _(mo):
    _namen = ["frank", "egon", "karl"]
    list(map(str.title, filter(lambda name: "a" in name, _namen)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `reduce` · Zusatzteil

    `functools.reduce` fasst eine Folge schrittweise zu einem Wert zusammen. Eine Funktion verbindet jeweils das Zwischenergebnis mit dem nächsten Element.

    ```python
    from functools import reduce

    reduce(lambda bisher, zahl: bisher + zahl, [1, 2, 3], 0)
    ```

    Für Summen ist `sum(...)` in Python meist die klarere Wahl. Für Produkte gibt es `math.prod(...)`.
    """)
    return


@app.cell
def _(mo):
    from functools import reduce

    reduce(lambda bisher, zahl: bisher * zahl, [2, 3, 4], 1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mitmachen · Preis mit Rabatt berechnen

    Schreibe `berechne_preis(preis, rabatt=0)`. Die Funktion soll den Preis nach Abzug des Rabattanteils zurückgeben.

    - Ohne Rabatt: `berechne_preis(100)` ergibt `100`.
    - Mit 20 Prozent: `berechne_preis(100, rabatt=0.2)` ergibt `80`.

    Ergänze den Rückgabewert und führe die Zelle aus.
    """)
    return


@app.cell
def _(mo):
    def berechne_preis(preis, rabatt=0):
        return None  # Ersetze None durch die passende Berechnung.

    preis_antwort = (
        berechne_preis(100),
        berechne_preis(100, rabatt=0.2),
    )
    preis_antwort
    return (preis_antwort,)


@app.cell(hide_code=True)
def _(preis_antwort, pruefhinweis):
    _offen = preis_antwort == (None, None)
    _richtig = preis_antwort == (100, 80)
    pruefhinweis(
        None if _offen else _richtig,
        "Preis mit Rabatt",
        "Ziehe den Rabattanteil vom Grundpreis ab: `preis * (1 - rabatt)`.",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mitmachen · Namen filtern und umwandeln

    Wähle mit `filter` Namen mit mehr als drei Buchstaben aus und schreibe diese mit `map` in Titel-Schreibweise.

    Ergänze `lang` und `ausgabe` in der Codezelle. Erwartet werden:

    - `lang`: `['anna', 'carla', 'david']`
    - `ausgabe`: `['Anna', 'Carla', 'David']`
    """)
    return


@app.cell
def _(mo):
    _namen = ["anna", "ben", "carla", "david"]
    lang = None  # Wähle hier Namen mit mehr als drei Buchstaben aus.
    ausgabe = None  # Wende hier str.title auf die ausgewählten Namen an.
    namen_antwort = (lang, ausgabe)
    namen_antwort
    return (namen_antwort,)


@app.cell(hide_code=True)
def _(namen_antwort, pruefhinweis):
    _offen = namen_antwort == (None, None)
    _richtig = namen_antwort == (
        ["anna", "carla", "david"],
        ["Anna", "Carla", "David"],
    )
    pruefhinweis(
        None if _offen else _richtig,
        "Namen filtern und umwandeln",
        "Filtere zuerst nach Länge. Wandle danach die übrig gebliebenen Namen um.",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Klassen und Objekte

    Eine **Klasse** beschreibt Daten und Verhalten. Ein erzeugtes Objekt ist eine **Instanz** dieser Klasse.

    ```python
    class Kurs:
        def __init__(self, titel):
            self.titel = titel
    ```

    `__init__` richtet eine neue Instanz ein. `self` bezeichnet die Instanz, mit der gerade gearbeitet wird.
    """)
    return


@app.cell
def _(mo):
    class _Kurs:
        def __init__(self, titel, plaetze=12):
            self.titel = titel
            self.plaetze = plaetze

        def beschreibung(self):
            return f"{self.titel}: {self.plaetze} Plätze"

    _python_kurs = _Kurs("Python")
    (_python_kurs.titel, _python_kurs.beschreibung())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Attribute und Methoden

    - **Attribute** speichern den Zustand eines Objekts, zum Beispiel `titel` und `plaetze`.
    - **Methoden** sind Funktionen, die zu einer Klasse gehören. Der erste Parameter `self` verweist auf die aktuelle Instanz.

    Ein Aufruf wie `kurs.anmelden("Mara")` entspricht intern einem Aufruf der Methode mit genau diesem Kursobjekt.
    """)
    return


@app.cell
def _(mo):
    class _Kurs:
        def __init__(self, titel, max_plaetze=2):
            self.titel = titel
            self.max_plaetze = max_plaetze
            self.teilnehmende = []

        def anmelden(self, name):
            if len(self.teilnehmende) >= self.max_plaetze:
                return False
            self.teilnehmende.append(name)
            return True

    _kurs = _Kurs("Python")
    (_kurs.anmelden("Mara"), _kurs.teilnehmende)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Eine Klasse mit `__str__` lesbar machen

    `__str__` legt fest, welcher Text beim Anzeigen mit `print(...)` entsteht. Ohne diese Methode verwendet Python eine allgemeine Objektbeschreibung.

    Attribute mit einem einzelnen Unterstrich sind nach Konvention interne Details. Python verhindert den Zugriff darauf nicht.
    """)
    return


@app.cell
def _(mo):
    class Person:
        def __init__(self, name):
            self._name = name

        def __str__(self):
            return f"Person: {self._name}"

    print(Person("Mara"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Vererbung und Polymorphismus

    Vererbung beschreibt eine **Ist-ein**-Beziehung: Ein Student ist eine Person. Die Unterklasse übernimmt Attribute und Methoden und kann sie erweitern.

    ```python
    class Student(Person):
        def __init__(self, name, nummer):
            super().__init__(name)
            self.nummer = nummer
    ```

    `super()` ruft Verhalten der Oberklasse auf.
    """)
    return


@app.cell
def _(mo):
    class _Tier:
        def __init__(self, name):
            self.name = name

        def laut_geben(self):
            return "Ein Tier macht ein Geräusch."

    class _Hund(_Tier):
        def laut_geben(self):
            return "Wuff!"

    class _Katze(_Tier):
        def laut_geben(self):
            return "Miau!"

    _tiere = [_Hund("Bello"), _Katze("Minka")]
    [tier.laut_geben() for tier in _tiere]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Polymorphismus und Duck Typing

    **Polymorphismus** heißt: Derselbe Methodenaufruf kann je nach Objekt ein anderes Verhalten haben.

    Bei **Duck Typing** zählt, welche Methoden ein Objekt bereitstellt. Es muss nicht von einer bestimmten Klasse erben.

    ```python
    def gib_alle_toene_aus(objekte):
        return [objekt.laut_geben() for objekt in objekte]
    ```
    """)
    return


@app.cell
def _(mo):
    class _Hund:
        def laut_geben(self):
            return "Wuff!"

    class _Katze:
        def laut_geben(self):
            return "Miau!"

    class _Signal:
        def laut_geben(self):
            return "Pieps!"

    _tiere_und_signal = [_Hund(), _Katze(), _Signal()]
    [objekt.laut_geben() for objekt in _tiere_und_signal]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Komposition · ein Objekt enthält ein anderes

    Komposition beschreibt eine **Hat-ein**-Beziehung: Ein Kurs hat eine Kursleitung. Die Objekte bleiben eigenständig; der Kurs kann eine Aufgabe an die Kursleitung delegieren.

    Vererbung passt zu „ist ein“. Komposition passt zu „hat ein“.
    """)
    return


@app.cell
def _(mo):
    class Dozent:
        def __init__(self, name):
            self.name = name

        def vorstellen(self):
            return f"Kursleitung: {self.name}"

    class _Kurs:
        def __init__(self, titel, dozent):
            self.titel = titel
            self.dozent = dozent

        def kursleitung_anzeigen(self):
            return self.dozent.vorstellen()

    _kurs = _Kurs("Python", Dozent("Sam"))
    _kurs.kursleitung_anzeigen()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mitmachen · Eine Kleingruppe verwalten

    Ergänze die Klasse `Kleingruppe`:

    - `anmelden(name)` nimmt eine Person auf, solange ein Platz frei ist, und gibt `True` oder `False` zurück.
    - `freie_plaetze()` gibt die Zahl der noch freien Plätze zurück.

    Die Gruppe hat zwei Plätze. Die ersten beiden Anmeldungen sollen gelingen; die dritte nicht.
    """)
    return


@app.cell
def _(mo):
    class Kleingruppe:
        def __init__(self, max_plaetze):
            self.max_plaetze = max_plaetze
            self.teilnehmende = []

        def anmelden(self, name):
            return None  # Ergänze Aufnahme und Rückgabewert.

        def freie_plaetze(self):
            return None  # Berechne die Zahl der freien Plätze.

    gruppe = Kleingruppe(2)
    gruppen_antwort = (
        gruppe.anmelden("Mara"),
        gruppe.anmelden("Timo"),
        gruppe.anmelden("Noah"),
        gruppe.freie_plaetze(),
        gruppe.teilnehmende,
    )
    gruppen_antwort
    return (gruppen_antwort,)


@app.cell(hide_code=True)
def _(gruppen_antwort, pruefhinweis):
    _offen = gruppen_antwort == (None, None, None, None, [])
    _richtig = gruppen_antwort == (
        True,
        True,
        False,
        0,
        ["Mara", "Timo"],
    )
    pruefhinweis(
        None if _offen else _richtig,
        "Kleingruppe verwalten",
        "Prüfe vor dem Anhängen, ob noch ein Platz frei ist. `len(...)` zählt die Anmeldungen.",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mitmachen · Verhalten austauschen

    Ergänze bei `Hund` und `Katze` die Methode `laut_geben()`. Danach soll `tier_konzert` alle Töne in einer Liste zurückgeben.

    `Signal` erbt nicht von `Tier`. Es bietet trotzdem dieselbe Methode an und kann deshalb ebenfalls in der Liste stehen.
    """)
    return


@app.cell
def _(mo):
    class _Tier:
        def __init__(self, name):
            self.name = name

        def laut_geben(self):
            return "Geräusch"

    class _Hund(_Tier):
        def laut_geben(self):
            return None  # Ersetze None durch den Ton des Hundes.

    class _Katze(_Tier):
        def laut_geben(self):
            return None  # Ersetze None durch den Ton der Katze.

    class _Signal:
        def laut_geben(self):
            return "Pieps!"

    def tier_konzert(objekte):
        return [objekt.laut_geben() for objekt in objekte]

    _tiere = [_Hund("Bello"), _Katze("Minka"), _Signal()]
    tier_antwort = tier_konzert(_tiere)
    tier_antwort
    return (tier_antwort,)


@app.cell(hide_code=True)
def _(pruefhinweis, tier_antwort):
    _offen = tier_antwort == [None, None, "Pieps!"]
    _richtig = tier_antwort == ["Wuff!", "Miau!", "Pieps!"]
    pruefhinweis(
        None if _offen else _richtig,
        "Verhalten austauschen",
        "Überschreibe `laut_geben()` in den Unterklassen. Die Funktion muss nicht prüfen, zu welcher Klasse ein Objekt gehört.",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Module und Packages

    Ein **Modul** ist eine Python-Datei. Ein **Package** ist ein Verzeichnis mit zusammengehörigen Modulen und einer `__init__.py`.

    ```text
    kursverwaltung/
    ├── __init__.py
    ├── personen.py
    ├── kurse.py
    └── verwaltung.py
    ```

    `__init__.py` legt mit fest, welche Namen über das Package importiert werden können.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Importieren

    ```python
    import math
    math.sqrt(81)

    from math import sqrt
    sqrt(81)

    import math as mathe
    mathe.pi
    ```

    Benenne genau, woher ein importierter Name kommt. `from modul import *` vermeiden, weil es unklar macht, welche Namen verwendet werden.
    """)
    return


@app.cell
def _(mo):
    from simple_math_package import add, subtract

    (add(2, 3), subtract(10, 4))
    return


@app.cell
def _(mo):
    from kursverwaltung import Kurs as _Kurs
    from kursverwaltung import Kursverwaltung as _Kursverwaltung
    from kursverwaltung import Student as _Student

    _kurs = _Kurs("Python für Einsteiger", max_teilnehmende=2)
    _mara = _Student("Mara", student_id=1)
    _verwaltung = _Kursverwaltung()
    _verwaltung.kurs_hinzufuegen(_kurs)
    _verwaltung.student_einschreiben(_mara, _kurs.titel)
    (_verwaltung.kurs_anzeigen(), _kurs.teilnehmende_namen())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Das nehme ich mit

    - Funktionen benennen Aufgaben und geben Ergebnisse mit `return` weiter.
    - `lambda`, `map` und `filter` helfen beim Weitergeben und Anwenden kurzer Funktionen.
    - Klassen verbinden benannte Daten mit passendem Verhalten.
    - Vererbung bedeutet „ist ein“, Komposition bedeutet „hat ein“.
    - Duck Typing nutzt gemeinsames Verhalten, auch wenn Objekte nicht dieselbe Klasse haben.
    - Module und Packages halten Python-Code übersichtlich.

    **Rückblick:** Welches Beispiel möchtest du noch einmal selbst verändern?
    """)
    return


if __name__ == "__main__":
    app.run()
