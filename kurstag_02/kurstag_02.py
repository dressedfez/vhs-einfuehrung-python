# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.20.0",
# ]
# ///

import marimo

__generated_with = "0.23.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Kurstag 2: Entscheidungen und Wiederholungen

    Unser Aufgabenplaner soll heute mehr können als nur eine Aufgabe anzeigen.
    Er soll prüfen:

    - ist ein Eintrag leer?
    - ist eine Aufgabe dringend?
    - welche Aufgaben liegen in einer Liste?

    Dafür brauchen wir **Bedingungen** und **Schleifen**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ziele des Kurstags

    Am Ende dieses Kurstags kannst du:

    - Bedingungen mit `if`, `elif` und `else` lesen
    - Wahrheitswerte (`True`/`False`) und Vergleiche verstehen
    - einfache Vergleiche für Prioritäten formulieren
    - mit einer `for`-Schleife mehrere Aufgaben verarbeiten
    - Listen als Sammlung mehrerer Werte nutzen
    - leere Einträge überspringen
    - aus mehreren Aufgaben eine gefilterte Übersicht erzeugen
    """)
    return


@app.cell
def _():
    aufgaben = [
        "Einkauf erledigen",
        "",
        "Arzttermin vorbereiten",
        "Python-Hausaufgabe bearbeiten",
    ]
    prioritaeten = [1, 0, 2, 3]
    return aufgaben, prioritaeten


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Bedingungen

    Mit `if`, `elif` und `else` kann ein Programm auf unterschiedliche Situationen reagieren.

    /// note | Begriff: Wahrheitswert
    Ein Wahrheitswert (`bool`) ist entweder `True` oder `False`.
    Bedingungen arbeiten immer mit solchen Wahrheitswerten.
    ///

    /// note | Begriff: Vergleich
    Ein Vergleich wie `prioritaet >= 3` erzeugt einen Wahrheitswert.
    Python prüft also, ob eine Aussage stimmt oder nicht.
    ///

    /// note | Begriff: Bedingung
    Eine Bedingung entscheidet, welcher Code ausgeführt wird.
    Mit `if` beginnt die Prüfung, `elif` ergänzt weitere Fälle und `else` beschreibt den Restfall.
    ///
    """)
    return


@app.cell
def _(aufgaben):
    erste_aufgabe = aufgaben[0]

    if erste_aufgabe == "":
        meldung = "Die erste Aufgabe ist leer."
    else:
        meldung = f"Die erste Aufgabe lautet: {erste_aufgabe}"

    meldung
    return


@app.cell
def _(aufgaben):
    zweite_aufgabe = aufgaben[1]

    if zweite_aufgabe == "":
        zweite_meldung = "Die zweite Aufgabe ist leer und wird übersprungen."
    else:
        zweite_meldung = f"Die zweite Aufgabe lautet: {zweite_aufgabe}"

    zweite_meldung
    return


@app.cell
def _(prioritaeten):
    letzte_prioritaet = prioritaeten[-1]

    if letzte_prioritaet >= 3:
        status = "dringend"
    elif letzte_prioritaet == 2:
        status = "bald erledigen"
    else:
        status = "kann warten"

    status
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Schleifen

    Eine `for`-Schleife arbeitet mehrere Werte nacheinander ab.
    Das brauchen wir, sobald unser Aufgabenplaner mehr als einen Eintrag kennt.

    /// note | Begriff: Liste
    Eine Liste speichert mehrere Werte in einer festen Reihenfolge.
    Unsere Liste `aufgaben` enthält mehrere Aufgabentitel.
    ///

    /// note | Begriff: Schleife
    Eine Schleife wiederholt denselben Code für mehrere Werte.
    Bei `for _aufgabe in aufgaben` bekommt `_aufgabe` nacheinander jeden Wert aus der Liste.
    ///

    /// note | Begriff: `append`
    Mit `append(...)` hängen wir einen neuen Wert an eine Liste an.
    Das nutzen wir, um gefilterte Aufgaben in einer neuen Liste zu sammeln.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zwei Listen gemeinsam verarbeiten

    Unsere Titel stehen in `aufgaben`, die passenden Prioritäten in `prioritaeten`.
    Damit wir beide Listen gemeinsam durchlaufen können, verwenden wir `zip(...)`.

    /// note | Begriff: `zip`
    `zip(liste_a, liste_b)` verbindet die Werte zweier Listen paarweise.
    Aus `["A", "B"]` und `[1, 2]` werden beim Durchlaufen die Paare `("A", 1)` und `("B", 2)`.
    ///

    Diese Technik ist praktisch, aber auch fehleranfällig:
    Die Listen müssen dieselbe Reihenfolge haben.
    Am nächsten Kurstag ersetzen wir diese parallelen Listen durch ein besseres Datenmodell.
    """)
    return


@app.cell
def _(aufgaben):
    saubere_aufgaben = []

    for _aufgabe in aufgaben:
        if _aufgabe != "":
            saubere_aufgaben.append(_aufgabe)

    saubere_aufgaben
    return (saubere_aufgaben,)


@app.cell
def _(aufgaben, prioritaeten):
    dringende_aufgaben = []

    for _aufgabe, _prioritaet in zip(aufgaben, prioritaeten):
        if _aufgabe != "" and _prioritaet >= 2:
            dringende_aufgaben.append(_aufgabe)

    dringende_aufgaben
    return (dringende_aufgaben,)


@app.cell
def _(aufgaben, prioritaeten):
    aufgaben_bericht = []

    for _aufgabe, _prioritaet in zip(aufgaben, prioritaeten):
        if _aufgabe == "":
            aufgaben_bericht.append("Leerer Eintrag übersprungen")
        elif _prioritaet >= 3:
            aufgaben_bericht.append(f"{_aufgabe}: dringend")
        elif _prioritaet == 2:
            aufgaben_bericht.append(f"{_aufgabe}: bald erledigen")
        else:
            aufgaben_bericht.append(f"{_aufgabe}: kann warten")

    aufgaben_bericht
    return


@app.cell
def _(dringende_aufgaben, saubere_aufgaben):
    anzahl_aufgaben = len(saubere_aufgaben)
    anzahl_dringend = len(dringende_aufgaben)
    f"{anzahl_dringend} von {anzahl_aufgaben} Aufgaben sind dringend oder bald wichtig."
    return


@app.cell(hide_code=True)
def _(dringende_aufgaben, mo):
    mo.md(f"""
    ## Zwischenstand im Projekt

    Der Aufgabenplaner kann jetzt schon Aufgaben prüfen, filtern und kurz bewerten.

    Dringende Aufgaben:

    {chr(10).join(f"- {aufgabe}" for aufgabe in dringende_aufgaben)}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mini-Übungen

    1. Ergänze eine weitere Aufgabe mit hoher Priorität.
    2. Ändere die Regel für `dringend`, zum Beispiel erst ab Priorität `3`.
    3. Erzeuge eine neue Liste, die nur Aufgaben mit mindestens 15 Zeichen enthält.
    4. Gib für jede Aufgabe einen Satz mit Titel und Bewertung aus.
    """)
    return


if __name__ == "__main__":
    app.run()
