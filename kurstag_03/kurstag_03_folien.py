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
app = marimo.App(
    width="medium",
    layout_file="layouts/kurstag_03_folien.slides.json",
    css_file="layouts/folien.css",
)


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    import pprint as _pprint

    def beispiel(titel, erklaerung, code, ergebnis):
        ausgabe = _pprint.pformat(
            ergebnis, width=88, compact=True, sort_dicts=False
        )
        return mo.md(
            f"## {titel}\n\n"
            f"{erklaerung}\n\n"
            f"**Python-Code**\n\n"
            f"```python\n{code}\n```\n\n"
            f"**Ergebnis**\n\n"
            f"```text\n{ausgabe}\n```"
        )

    return (beispiel,)


@app.cell(hide_code=True)
def _(mo):
    from base64 import b64encode as _b64encode
    from pathlib import Path as _Path

    _logo_data = _b64encode(_Path("public/vhs-dresden-logo.png").read_bytes()).decode("ascii")
    _cover_html = """
    <style>
      .vhs-kursstart { box-sizing: border-box; display: block; min-height: 440px; padding: 2.2rem 2.5rem; overflow: hidden; position: relative; border: 1px solid #d7e3ef; border-left: 10px solid #082f5b; border-radius: 24px; background: radial-gradient(circle at 92% 8%, rgba(255, 184, 40, .22) 0 15%, transparent 15.5%), linear-gradient(125deg, #fbfdff 0%, #f0f5fb 58%, #e4eef7 100%); color: #102f51; font-family: system-ui, sans-serif; }
      .vhs-kursstart-copy { position: relative; z-index: 1; max-width: calc(100% - 270px); }
      .vhs-kursstart-logo { display: inline-block; margin-bottom: 1.5rem; padding: .5rem .8rem; border-radius: 12px; background: #fff; box-shadow: 0 6px 20px rgba(7, 40, 74, .08); }
      .vhs-kursstart-logo img { display: block; width: min(290px, 62vw); height: auto; }
      .vhs-kursstart-series { margin: 0 0 .4rem; color: #147e9e; font-size: .86rem; font-weight: 800; letter-spacing: .16em; text-transform: uppercase; }
      .vhs-kursstart-title { margin: 0; color: #082f5b; font-size: clamp(2.1rem, 4.3vw, 3.6rem); font-weight: 800; line-height: 1.05; }
      .vhs-kursstart-title span { display: block; margin-top: .25rem; color: #17668e; font-size: .68em; }
      .vhs-kursstart-summary { max-width: 39rem; margin: 1rem 0 1.25rem; color: #38526d; font-size: 1.08rem; line-height: 1.5; }
      .vhs-kursstart-motto { display: inline-block; padding: .55rem .85rem; border: 1px solid #cfdeeb; border-radius: 999px; background: rgba(255,255,255,.78); color: #173a5d; font-size: .9rem; font-weight: 650; }
      .vhs-kursstart-motto b { padding: 0 .35rem; color: #ed6a32; }
      .vhs-kursstart-art { position: absolute; top: 50%; right: 4%; transform: translateY(-50%); display: grid; place-items: center; width: 220px; height: 220px; border: 1px solid rgba(8,47,91,.12); border-radius: 50%; background: rgba(255,255,255,.48); box-shadow: inset 0 0 0 15px rgba(255,255,255,.28); }
      .vhs-kursstart-core { display: grid; place-items: center; width: 134px; height: 134px; border-radius: 50%; background: #082f5b; box-shadow: 0 16px 30px rgba(8,47,91,.2); color: white; font-size: 3rem; font-weight: 850; letter-spacing: -.08em; }
      .vhs-kursstart-dot { position: absolute; display: block; width: 34px; height: 34px; border-radius: 50%; box-shadow: 0 4px 14px rgba(8,47,91,.12); }
      .vhs-kursstart-dot.one { top: 10px; left: 91px; width: 29px; height: 29px; background: #f6b627; }
      .vhs-kursstart-dot.two { top: 72px; right: 5px; background: #e84b3c; }
      .vhs-kursstart-dot.three { right: 31px; bottom: 17px; width: 27px; height: 27px; background: #39a5d6; }
      .vhs-kursstart-dot.four { bottom: 31px; left: 12px; width: 39px; height: 39px; background: #ef6d32; }
      .vhs-kursstart-dot.five { top: 50px; left: 20px; width: 22px; height: 22px; background: #318fc0; }
      @media (max-width: 680px) { .vhs-kursstart { min-height: 390px; padding: 1.5rem; } .vhs-kursstart-copy { max-width: none; } .vhs-kursstart-art { display: none; } }
    </style>
    <section class="vhs-kursstart">
      <div class="vhs-kursstart-copy">
        <div class="vhs-kursstart-logo"><img src="data:image/png;base64,__VHS_LOGO__" alt="Volkshochschule Dresden e.V."></div>
        <p class="vhs-kursstart-series">Python für Daten und KI</p>
        <h1 class="vhs-kursstart-title">Kurstag 3<span>Funktionen, Klassen und Module</span></h1>
        <p class="vhs-kursstart-summary">Programme mit Funktionen wiederverwendbar machen und mit eigenen Datentypen und Modulen strukturieren.</p>
        <div class="vhs-kursstart-motto">Verstehen <b>·</b> Ausprobieren <b>·</b> Selbst strukturieren</div>
      </div>
      <div class="vhs-kursstart-art" aria-hidden="true"><div class="vhs-kursstart-core">Py</div><i class="vhs-kursstart-dot one"></i><i class="vhs-kursstart-dot two"></i><i class="vhs-kursstart-dot three"></i><i class="vhs-kursstart-dot four"></i><i class="vhs-kursstart-dot five"></i></div>
    </section>
    """
    mo.Html(_cover_html.replace("__VHS_LOGO__", _logo_data))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Unser Weg heute

    **Termin 3:** Funktionen, Parameter, Rückgabewerte, `lambda`, `map` und `filter`.

    **Termin 4:** Klassen, Komposition, Module und Packages. Vererbung und `reduce` sind Zusatzstoff.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Gemeinsam am Rechner

    - Zu zweit: Eine Person tippt, die andere erklärt und prüft.
    - Nach jeder Aufgabe die Rollen wechseln.
    - Erst vermuten, dann ausführen, dann das Ergebnis erklären.
    - Bei einem Fehler die erste rote Zelle lesen und dort beginnen.

    **Schon Erfahrung?** Bearbeite die Zusatzteile und erkläre, wann eine einfachere Lösung besser lesbar wäre.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Das Notebook öffnen

    Im Terminal im Ordner `kurstag_03`:

    ```sh
    uv run --script kurstag_03_folien.py
    ```

    Für Live-Coding und die Folienansicht:

    ```sh
    uvx --from "marimo==0.25.2" marimo edit kurstag_03_folien.py
    ```

    Mit den Pfeiltasten blättern. **C** öffnet den Code der aktuellen Zelle; **Shift+Enter** führt sie aus.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Funktionen

    Eine Funktion bündelt eine Aufgabe unter einem Namen. Sie kann Eingaben annehmen und ein Ergebnis zurückgeben.

    /// note | Grundform
    ```python
    def funktionsname(parameter):
        anweisungen
        return ergebnis
    ```

    **Definieren** legt die Funktion an. **Aufrufen** führt ihren eingerückten Block aus.
    ///
    """)
    return


@app.cell
def _(beispiel):
    def _begruesse(name):
        return f"Hallo, {name}!"

    beispiel(
        "Eine Funktion aufrufen",
        "Der Parameter `name` erhält beim Aufruf den übergebenen Wert.",
        'def begruesse(name):\n    return f"Hallo, {name}!"\n\nbegruesse("Mara")',
        (_begruesse("Mara"), _begruesse("Timo")),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Parameter und Argumente

    **Parameter** stehen in der Funktionsdefinition. **Argumente** sind die konkreten Werte beim Aufruf.

    ```python
    def voller_name(vorname, nachname):  # vorname und nachname sind Parameter
        return f"{vorname} {nachname}"

    voller_name("Ada", "Lovelace")  # Ergebnis: "Ada Lovelace"
    ```
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    def _voller_name(vorname, nachname):
        return f"{vorname} {nachname}"

    beispiel(
        "Mehrere Parameter",
        "Positionsargumente werden von links nach rechts zugeordnet: Vorname, dann Nachname. Vertauschen ändert die Bedeutung.",
        'def voller_name(vorname, nachname):\n    return f"{vorname} {nachname}"\n\nvoller_name("Ada", "Lovelace")\nvoller_name("Lovelace", "Ada")',
        f'"{_voller_name("Ada", "Lovelace")}" · vertauscht: "{_voller_name("Lovelace", "Ada")}"',
    )
    return


@app.cell
def _(beispiel):
    def _beschreibe_kurs(titel, plaetze):
        return f"{titel}: {plaetze} Plätze"

    beispiel(
        "Keyword-Argumente",
        "Die Parameternamen machen die Zuordnung sichtbar. Deshalb dürfen Keyword-Argumente in anderer Reihenfolge stehen.",
        'def beschreibe_kurs(titel, plaetze):\n    return f"{titel}: {plaetze} Plätze"\n\nbeschreibe_kurs("Python", 12)\nbeschreibe_kurs(plaetze=12, titel="Python")',
        (_beschreibe_kurs("Python", 12), _beschreibe_kurs(plaetze=12, titel="Python")),
    )
    return


@app.cell
def _(beispiel):
    def _begruesse(name, text="Guten Tag"):
        return f"{text}, {name}!"

    beispiel(
        "Standardwerte",
        "Ein Standardwert wird verwendet, wenn beim Aufruf kein anderes Argument angegeben ist.",
        'def begruesse(name, text="Guten Tag"):\n    return f"{text}, {name}!"\n\n(begruesse("Mara"), begruesse("Mara", text="Hallo"))',
        (_begruesse("Mara"), _begruesse("Mara", text="Hallo")),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `return` gibt ein Ergebnis zurück

    Eine Funktion kann einen berechneten Wert an die aufrufende Stelle zurückgeben. Ohne `return` ist der Rückgabewert `None`.

    `print(...)` zeigt Text an. `return` macht einen Wert für weitere Berechnungen verfügbar.
    """)
    return


@app.cell
def _(beispiel):
    def preis_mit_rabatt(preis, rabatt):
        return preis * (1 - rabatt)

    grundpreis = 50
    endpreis = preis_mit_rabatt(grundpreis, 0.1)
    beispiel(
        "Mit dem Rückgabewert weiterrechnen",
        "Die Funktion liefert den Preis zurück. Der Aufrufer speichert und verwendet ihn weiter.",
        "def preis_mit_rabatt(preis, rabatt):\n    return preis * (1 - rabatt)\n\nendpreis = preis_mit_rabatt(50, 0.1)",
        endpreis,
    )
    return


@app.cell
def _(beispiel):
    def min_max(werte):
        return min(werte), max(werte)

    beispiel(
        "Mehrere Werte zurückgeben",
        "Mehrere Rückgabewerte werden zu einem Tupel zusammengefasst und können beim Aufruf entpackt werden.",
        "kleinster, groesster = min_max([7, 2, 9, 4])",
        min_max([7, 2, 9, 4]),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Lokale Variablen

    Namen, die in einer Funktion entstehen, sind dort lokal. So bleiben die Schritte einer Funktion von anderen Programmteilen getrennt.

    Verwende sprechende Namen und gib Ergebnisse mit `return` ausdrücklich zurück.
    """)
    return


@app.cell
def _(beispiel):
    def mittelwert(werte):
        anzahl = len(werte)
        summe = sum(werte)
        return summe / anzahl

    beispiel(
        "Eine Funktion in Schritte gliedern",
        "Die lokalen Namen `anzahl` und `summe` helfen, den Rechenweg zu lesen.",
        "def mittelwert(werte):\n    anzahl = len(werte)\n    summe = sum(werte)\n    return summe / anzahl\n\nmittelwert([2, 4, 6])",
        mittelwert([2, 4, 6]),
    )
    return


@app.cell
def _(beispiel):
    def mittelwert_mit_hilfsfunktion(werte):
        def total(zahlen):
            return sum(zahlen)

        return total(werte) / len(werte)

    beispiel(
        "Innere Funktionen · Zusatzteil",
        "Eine innere Funktion ist nur innerhalb der äußeren Funktion verfügbar. Sie passt für einen Hilfsschritt, der dort gebraucht wird.",
        "def mittelwert(werte):\n    def total(zahlen):\n        return sum(zahlen)\n    return total(werte) / len(werte)",
        mittelwert_mit_hilfsfunktion([2, 4, 6]),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Funktionen als Argumente

    In Python sind Funktionen Werte. Eine Funktion kann eine andere Funktion als Argument erhalten.

    Das ist nützlich, wenn dieselbe Ablauflogik mit unterschiedlichen Aktionen arbeiten soll.
    """)
    return


@app.cell
def _(beispiel):
    def transformiere(texte, funktion):
        return [funktion(text) for text in texte]

    beispiel(
        "Verhalten übergeben",
        "Die Funktion `transformiere` bestimmt nicht selbst, wie ein Text verändert wird. Diese Aufgabe übernimmt das Argument `funktion`.",
        'transformiere(["anna", "ben"], str.title)',
        transformiere(["anna", "ben"], str.title),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Lambda-Funktionen

    `lambda` erzeugt eine kurze Funktion aus einem einzelnen Ausdruck.

    ```python
    lambda parameter: ausdruck
    ```

    Lambda eignet sich vor allem dort, wo eine kurze Funktion direkt gebraucht wird. Für mehrere Schritte ist `def` lesbarer.
    """)
    return


@app.cell
def _(beispiel):
    quadriere = lambda zahl: zahl**2
    beispiel(
        "Eine kurze Funktion",
        "Die Lambda-Funktion nimmt `zahl` entgegen und gibt den Wert des Ausdrucks `zahl**2` zurück.",
        "quadriere = lambda zahl: zahl**2\nquadriere(5)",
        quadriere(5),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `map` · jedes Element umwandeln

    `map(funktion, folge)` wendet eine Funktion auf jedes Element an. Das Ergebnis ist ein Iterator; `list(...)` macht die Werte sichtbar.

    Für eine reine Umwandlung ist eine Listen-Abstraktion oft genauso klar oder klarer.
    """)
    return


@app.cell
def _(beispiel):
    laengen = list(map(lambda wort: len(wort), ["Code", "Daten", "KI"]))
    beispiel(
        "Lambda direkt verwenden",
        "Die Lambda-Funktion braucht keinen eigenen Namen. `map` wendet sie auf jedes Wort an.",
        'list(map(lambda wort: len(wort), ["Code", "Daten", "KI"]))',
        laengen,
    )
    return


@app.cell
def _(beispiel):
    _namen = ["anna", "ben", "carla"]
    _gross = list(map(str.title, _namen))
    beispiel(
        "Namen vereinheitlichen",
        "`str.title` ist die Funktion, die `map` auf jeden Namen anwendet.",
        "namen = ['anna', 'ben', 'carla']\nlist(map(str.title, namen))",
        _gross,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `filter` · passende Elemente auswählen

    `filter(funktion, folge)` behält die Elemente, für die die Funktion `True` liefert.

    Die Prüf-Funktion heißt **Prädikat**. Sie sollte eine klare Wahr/Falsch-Frage beantworten.
    """)
    return


@app.cell
def _(beispiel):
    _punkte = [12, 5, 18, 9, 20]
    _bestanden = list(filter(lambda punkt: punkt >= 10, _punkte))
    beispiel(
        "Punkte filtern",
        "Das Prädikat prüft, ob ein Punktestand mindestens 10 beträgt.",
        "punkte = [12, 5, 18, 9, 20]\nlist(filter(lambda punkt: punkt >= 10, punkte))",
        _bestanden,
    )
    return


@app.cell
def _(beispiel):
    namen_mit_a = list(
        map(
            str.title,
            filter(lambda name: "a" in name, ["frank", "egon", "karl"]),
        )
    )
    beispiel(
        "Filtern und umwandeln",
        "Zuerst wählt `filter` Namen mit `a` aus. Danach schreibt `map` sie einheitlich.",
        'list(map(str.title, filter(lambda name: "a" in name, namen)))',
        namen_mit_a,
    )
    return


@app.cell
def _(beispiel):
    _punkte = [12, 5, 18, 9, 20]
    _bestanden = [punkt for punkt in _punkte if punkt >= 10]
    beispiel(
        "Dieselbe Auswahl als Listen-Abstraktion",
        "Eine Listen-Abstraktion drückt Umwandeln und Filtern kompakt aus. Wähle die Form, die für die Aufgabe am besten lesbar ist.",
        "[punkt for punkt in punkte if punkt >= 10]",
        _bestanden,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `reduce` · viele Werte zu einem verbinden

    `functools.reduce` führt eine Funktion wiederholt auf zwei Werte an. Ein **Startwert** legt das erste Zwischenergebnis fest.

    Für Summe und Produkt sind `sum` und `math.prod` meist einfacher. `reduce` ist sinnvoll, wenn genau dieses schrittweise Zusammenführen gebraucht wird.
    """)
    return


@app.cell
def _(beispiel):
    from functools import reduce as _reduce_produkt

    _produkt = _reduce_produkt(lambda bisher, zahl: bisher * zahl, [2, 3, 4], 1
                              )
    beispiel(
        "Werte schrittweise zusammenführen",
        "`bisher` startet bei 1. In jedem Schritt wird mit der nächsten Zahl multipliziert.",
        "from functools import reduce\nreduce(lambda bisher, zahl: bisher * zahl, [2, 3, 4], 1)",
        _produkt,
    )
    return


@app.cell
def _(beispiel):
    from functools import reduce as _reduce_fakultaet

    _fakultaet = _reduce_fakultaet(lambda bisher, zahl: bisher * zahl, range(1, 6), 1)
    beispiel(
        "Fakultät als Zusatzübung",
        "Der Startwert 1 ist wichtig: Er ist das neutrale Element der Multiplikation und funktioniert auch bei einer leeren Folge.",
        "from functools import reduce\nreduce(lambda bisher, zahl: bisher * zahl, range(1, 6), 1)",
        _fakultaet,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Termin 4 · Klassen und Objekte

    Eine **Klasse** beschreibt, welche Daten und welches Verhalten ihre Objekte haben. Ein erzeugtes Objekt heißt **Instanz**.

    /// note | Vergleich
    Die Klasse ist der Bauplan; eine Instanz ist ein konkretes Ding nach diesem Bauplan.
    ///

    Für viele zusammengehörige Werte ist ein Tupel eine einfache, feste Struktur. Wenn Werte Namen und Verhalten brauchen, passt eine Klasse besser.
    """)
    return


@app.cell
def _(beispiel):
    person = ("Mara", "mara@example.org", "Python")
    beispiel(
        "Tupel oder Klasse?",
        "Im Tupel muss die Bedeutung von Position 0, 1 und 2 bekannt sein. Eine Klasse kann Felder beim Namen zugänglich machen.",
        'person = ("Mara", "mara@example.org", "Python")\nperson[0]',
        person[0],
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack([
        mo.md("""
    ## Eine Klasse definieren

    Das UML-Diagramm zeigt eine Klasse mit ihrem Namen, ihren Eigenschaften und ihren Methoden. In Python bündeln `class`, `__init__` und `self` diese Teile.

    ```python
    class Kurs:
        def __init__(self, titel):
            self.titel = titel
    ```

    `__init__` richtet eine neue Instanz ein. `self` bezeichnet genau diese Instanz.
    """),
        mo.center(mo.image(
            src="public/Klassendiagramm.png",
            alt="UML-Diagramm einer Klasse Buchstabe mit Eigenschaften und Methoden",
        )),
    ], gap=1)
    return


@app.cell
def _(beispiel):
    class _Kurs:
        def __init__(self, titel, plaetze):
            self.titel = titel
            self.plaetze = plaetze

        def beschreibung(self):
            return f"{self.titel}: {self.plaetze} Plätze"

    _python_kurs = _Kurs("Python", 12)
    beispiel(
        "Eine Instanz erzeugen",
        "`python_kurs` ist eine Instanz der Klasse `Kurs`. Die Methode verwendet die Attribute dieses Objekts.",
        'python_kurs = Kurs("Python", 12)\npython_kurs.beschreibung()',
        _python_kurs.beschreibung(),
    )
    return


@app.cell
def _(beispiel):
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

    _python_kurs = _Kurs("Python", max_plaetze=2)
    _ergebnis = (
        _python_kurs.anmelden("Mara"),
        _python_kurs.anmelden("Timo"),
        _python_kurs.anmelden("Noah"),
        _python_kurs.teilnehmende,
    )
    beispiel(
        "Methoden ändern den Zustand",
        "Die Methode `anmelden` verändert die Liste der Teilnehmenden und gibt zurück, ob die Anmeldung gelungen ist.",
        'kurs = Kurs("Python", max_plaetze=2)\nkurs.anmelden("Mara")\nkurs.anmelden("Timo")\nkurs.anmelden("Noah")',
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Daten kapseln

    Python erzwingt keine privaten Attribute wie manche andere Sprachen.

    - `name`: öffentlich verwendbar
    - `_name`: Konvention für ein internes Detail
    - `__name`: Namensumformung; kein verlässlicher Schutz vor Zugriff

    Ein Unterstrich ist ein Hinweis an andere Programmierende. Verwende ein internes Attribut nur, wenn es für die Aufgabe nötig ist.
    """)
    return


@app.cell
def _(beispiel):
    class Person:
        def __init__(self, name):
            self.name = name

        def beschreibung(self):
            return f"Person: {self.name}"

    class _Student(Person):
        def __init__(self, name, matrikelnummer):
            super().__init__(name)
            self.matrikelnummer = matrikelnummer

        def beschreibung(self):
            return f"Student: {self.name} (Nr. {self.matrikelnummer})"

    _student = _Student("Mara", 47)
    beispiel(
        "Vererbung und `super()`",
        "`Student` erbt von `Person`. `super().__init__` übernimmt das Einrichten des gemeinsamen Attributs `name`.",
        'class Student(Person):\n    def __init__(self, name, matrikelnummer):\n        super().__init__(name)\n        self.matrikelnummer = matrikelnummer',
        _student.beschreibung(),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Methoden überschreiben

    Eine Unterklasse kann eine geerbte Methode mit demselben Namen neu definieren. Dann gilt für diese Instanz die speziellere Variante.

    Nutze Vererbung für eine klare **Ist-ein**-Beziehung, zum Beispiel: Ein Student ist eine Person.
    """)
    return


@app.cell
def _(beispiel):
    class Form:
        def flaeche(self):
            return 0

    class Rechteck(Form):
        def __init__(self, breite, hoehe):
            self.breite = breite
            self.hoehe = hoehe

        def flaeche(self):
            return self.breite * self.hoehe

    rechteck = Rechteck(4, 3)
    beispiel(
        "Eine Methode anpassen",
        "`Rechteck` liefert seine eigene Berechnung für `flaeche`.",
        "class Rechteck(Form):\n    def flaeche(self):\n        return self.breite * self.hoehe",
        rechteck.flaeche(),
    )
    return


@app.cell
def _(beispiel):
    class _Student:
        def __init__(self, name):
            self.name = name

        def beschreibung(self):
            return f"Student: {self.name}"

    class _Dozent:
        def __init__(self, name, fach):
            self.name = name
            self.fach = fach

        def beschreibung(self):
            return f"Dozent: {self.name} · {self.fach}"

    _personen = [_Student("Mara"), _Dozent("Sam", "Python")]
    beispiel(
        "Polymorphismus · gleicher Aufruf",
        "Beide Objekte verstehen `beschreibung()`. Der Aufruf bleibt gleich; das Ergebnis hängt vom konkreten Objekt ab.",
        "for person in personen:\n    person.beschreibung()",
        [person.beschreibung() for person in _personen],
    )
    return


@app.cell
def _(beispiel):
    class Gast:
        def __init__(self, name):
            self.name = name

        def beschreibung(self):
            return f"Gast: {self.name}"

    def drucke_beschreibungen(objekte):
        return [objekt.beschreibung() for objekt in objekte]

    _ergebnis = drucke_beschreibungen([Gast("Noah")])
    beispiel(
        "Duck Typing · passendes Verhalten",
        "`Gast` muss nicht von `Student` erben. Es reicht, dass das Objekt die aufgerufene Methode `beschreibung()` anbietet.",
        "def drucke_beschreibungen(objekte):\n    return [objekt.beschreibung() for objekt in objekte]",
        _ergebnis,
    )
    return


@app.cell
def _(beispiel):
    class _Dozent:
        def __init__(self, name):
            self.name = name

        def beschreibung(self):
            return f"Kursleitung: {self.name}"

    class _Kurs:
        def __init__(self, titel, dozent):
            self.titel = titel
            self.dozent = dozent

        def kursleitung(self):
            return self.dozent.beschreibung()

    _kurs = _Kurs("Python", _Dozent("Sam"))
    beispiel(
        "Komposition · ein Kurs hat eine Kursleitung",
        "`Kurs` speichert ein `Dozent`-Objekt. Die Methode `kursleitung` delegiert die Beschreibung an diese Komponente.",
        'kurs = Kurs("Python", Dozent("Sam"))\nkurs.kursleitung()',
        _kurs.kursleitung(),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack([
        mo.md("""
    ## Vererbung oder Komposition?

    | Beziehung | Frage | Beispiel |
    | --- | --- | --- |
    | Vererbung | Ist ein …? | Student ist eine Person |
    | Komposition | Hat ein …? | Kurs hat eine Kursleitung |

    Vererbung teilt gemeinsames Verhalten. Komposition verbindet eigenständige Objekte und kann Aufgaben an sie weitergeben.
    """),
        mo.center(mo.image(
            src="public/KlassendiagrammVererbung.png",
            alt="UML-Diagramm mit Vererbung von Student und Professor zu Person sowie einer Adresse als Bestandteil",
            width=640,
        )),
        mo.md("*Links: Student und Professor sind Personen. Rechts: Eine Person lebt in einer Adresse — eine Hat-ein-Beziehung.*"),
    ], gap=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Module und Packages

    Ein **Modul** ist eine Python-Datei. Es kann Funktionen, Klassen und Werte enthalten.

    Ein **Package** fasst zusammengehörige Module in einem Verzeichnis zusammen. Eine Datei `__init__.py` macht die öffentliche Struktur sichtbar.
    """)
    return


@app.cell
def _(beispiel):
    import math

    beispiel(
        "Ein Standardbibliotheks-Modul importieren",
        "Mit `import math` wird die Funktion über ihren Modulnamen verwendet. Das macht ihre Herkunft sichtbar.",
        "import math\nmath.sqrt(81), math.pi",
        (math.sqrt(81), round(math.pi, 3)),
    )
    return


@app.cell
def _(beispiel):
    from math import sqrt as wurzel

    beispiel(
        "Gezielt importieren und umbenennen",
        "`from ... import ...` bindet ausgewählte Namen direkt ein. Ein Alias kann einen langen oder fremdsprachigen Namen ersetzen.",
        "from math import sqrt as wurzel\nwurzel(144)",
        wurzel(144),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Aufbau eines eigenen Packages

    ```text
    simple_math_package/
    ├── __init__.py
    └── math_operations/
        ├── __init__.py
        ├── math.py
        └── simple_operations.py
    ```

    `__init__.py` bündelt die Namen, die ein Package nach außen anbieten möchte. `from ... import *` vermeiden: Es verschleiert, woher Namen stammen.
    """)
    return


@app.cell
def _(beispiel):
    from simple_math_package import add, subtract

    beispiel(
        "Funktionen aus dem Kurs-Package",
        "Die Funktionen liegen in Modulen unter `simple_math_package` und werden über dessen öffentliche Schnittstelle importiert.",
        "from simple_math_package import add, subtract\nadd(2, 3), subtract(10, 4)",
        (add(2, 3), subtract(10, 4)),
    )
    return


@app.cell
def _(beispiel):
    from simple_math_package import Matrix

    links = Matrix([[1, 2], [3, 4]])
    rechts = Matrix([[2, 1], [0, 3]])
    beispiel(
        "Eine Klasse aus dem Package importieren",
        "Neben Funktionen kann ein Package auch Klassen bereitstellen. `Matrix` bündelt die Daten und die passenden Methoden zum Addieren und Subtrahieren.",
        "from simple_math_package import Matrix\nlinks.add(rechts).data",
        links.add(rechts).data,
    )
    return


@app.cell
def _(beispiel):
    from kursverwaltung import Kurs as _Kurs
    from kursverwaltung import Kursverwaltung as _Kursverwaltung
    from kursverwaltung import Student as _Student

    _kurs = _Kurs("Python für Einsteiger", max_teilnehmende=2)
    _mara = _Student("Mara", student_id=1)
    _timo = _Student("Timo", student_id=2)
    _verwaltung = _Kursverwaltung()
    _verwaltung.kurs_hinzufuegen(_kurs)
    _angemeldet = (
        _verwaltung.student_einschreiben(_mara, _kurs.titel),
        _verwaltung.student_einschreiben(_timo, _kurs.titel),
    )
    beispiel(
        "Ein Package zusammenspielen lassen",
        "Die Kursverwaltung verteilt Klassen auf Module. Hier werden Kurs und Student verbunden und beide Anmeldungen über die Verwaltung verarbeitet.",
        'from kursverwaltung import Kurs, Kursverwaltung, Student\n...\nverwaltung.student_einschreiben(mara, kurs.titel)',
        (_angemeldet, _kurs.teilnehmende_namen()),
    )
    return


@app.cell
def _(beispiel):
    def berechne_preis(preis, rabatt=0):
        return preis * (1 - rabatt)

    _ergebnis = (
        berechne_preis(100),
        berechne_preis(100, rabatt=0.2),
    )
    beispiel(
        "Übungslösung · Preis mit Rabatt",
        "Der Rabatt ist ein Anteil am Grundpreis. Der Standardwert `0` bedeutet: ohne Rabatt.",
        "def berechne_preis(preis, rabatt=0):\n    return preis * (1 - rabatt)",
        _ergebnis,
    )
    return


@app.cell
def _(beispiel):
    _namen = ["anna", "ben", "carla", "david"]
    _ausgewaehlt = list(filter(lambda name: len(name) > 3, _namen))
    _ergebnis = (_ausgewaehlt, list(map(str.title, _ausgewaehlt)))
    beispiel(
        "Übungslösung · Namen verarbeiten",
        "Erst filtert `filter` nach der Länge. Danach wandelt `map` die übrig gebliebenen Namen um.",
        "ausgewaehlt = list(filter(lambda name: len(name) > 3, namen))\nlist(map(str.title, ausgewaehlt))",
        _ergebnis,
    )
    return


@app.cell
def _(beispiel):
    class Kleingruppe:
        def __init__(self, max_plaetze):
            self.max_plaetze = max_plaetze
            self.teilnehmende = []

        def anmelden(self, name):
            if len(self.teilnehmende) >= self.max_plaetze:
                return False
            self.teilnehmende.append(name)
            return True

        def freie_plaetze(self):
            return self.max_plaetze - len(self.teilnehmende)

    _gruppe = Kleingruppe(2)
    _ergebnis = (
        _gruppe.anmelden("Mara"),
        _gruppe.anmelden("Timo"),
        _gruppe.anmelden("Noah"),
        _gruppe.freie_plaetze(),
        _gruppe.teilnehmende,
    )
    beispiel(
        "Übungslösung · Kleingruppe verwalten",
        "Die Methode prüft die Kapazität, bevor sie die Liste verändert. Die freie Platzzahl ergibt sich aus Kapazität minus Anmeldungen.",
        "def anmelden(self, name):\n    if len(self.teilnehmende) >= self.max_plaetze:\n        return False\n    self.teilnehmende.append(name)\n    return True",
        _ergebnis,
    )
    return


@app.cell
def _(beispiel):
    class _Tier:
        def __init__(self, name):
            self.name = name

        def laut_geben(self):
            return "Geräusch"

    class _Hund(_Tier):
        def laut_geben(self):
            return "Wuff!"

    class _Katze(_Tier):
        def laut_geben(self):
            return "Miau!"

    class _Signal:
        def laut_geben(self):
            return "Pieps!"

    _tiere = [_Hund("Bello"), _Katze("Minka"), _Signal()]
    _ergebnis = [tier.laut_geben() for tier in _tiere]
    beispiel(
        "Übungslösung · Verhalten austauschen",
        "Die Funktion ruft dieselbe Methode auf jedem Objekt auf. `Signal` passt trotz anderer Klasse, weil es `laut_geben()` bereitstellt.",
        "[objekt.laut_geben() for objekt in tiere]",
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Das nehmen wir mit

    - Funktionen geben wiederverwendbare Aufgaben einen Namen.
    - `return` übergibt Werte an den aufrufenden Code.
    - `map`, `filter` und `reduce` wenden Funktionen auf Folgen an.
    - Klassen verbinden benannte Daten mit Verhalten.
    - Vererbung beschreibt „ist ein“, Komposition beschreibt „hat ein“.
    - Module und Packages halten zusammengehörigen Code in übersichtlichen Dateien.

    **Rückblick:** Welche Struktur hilft dir, den nächsten Python-Code verständlicher zu machen?
    """)
    return


if __name__ == "__main__":
    app.run()
