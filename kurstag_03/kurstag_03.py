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
    # Kurstag 3: Daten sinnvoll strukturieren

    Bisher hatten wir mehrere getrennte Listen.
    Das wird schnell unübersichtlich.

    Heute bauen wir ein einfaches Datenmodell für unseren Aufgabenplaner:

    - eine Aufgabe besteht aus mehreren Informationen
    - mehrere Aufgaben stehen in einer Liste
    - zusammengehörige Informationen speichern wir in einem Wörterbuch
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ziele des Kurstags

    Am Ende dieses Kurstags kannst du:

    - eine Aufgabe als Wörterbuch modellieren
    - mehrere Aufgaben in einer Liste sammeln
    - Dictionaries, Schlüssel und Werte benennen
    - Werte über Schlüssel wie `"titel"` oder `"erledigt"` lesen und ändern
    - offene Aufgaben aus einer Liste herausfiltern
    - Bool-Werte für Statusinformationen nutzen
    - einfache Zusammenfassungen nach Kategorie und Priorität erstellen
    """)
    return


@app.cell
def _():
    aufgabe_1 = {
        "titel": "Einkauf erledigen",
        "kategorie": "Alltag",
        "prioritaet": 2,
        "erledigt": False,
    }

    aufgabe_2 = {
        "titel": "Python-Hausaufgabe bearbeiten",
        "kategorie": "Lernen",
        "prioritaet": 3,
        "erledigt": False,
    }

    aufgabe_3 = {
        "titel": "Geburtstagskarte schreiben",
        "kategorie": "Privat",
        "prioritaet": 1,
        "erledigt": True,
    }
    return aufgabe_1, aufgabe_2, aufgabe_3


@app.cell
def _(aufgabe_1, aufgabe_2, aufgabe_3):
    aufgaben = [aufgabe_1, aufgabe_2, aufgabe_3]
    aufgaben
    return (aufgaben,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Listen und Wörterbücher

    Eine Liste ist nützlich für viele Einträge.
    Ein Wörterbuch ist nützlich, wenn ein Eintrag mehrere benannte Teile hat.

    /// note | Begriff: Liste
    Eine Liste (`list`) ist eine geordnete Sammlung von Werten.
    Wir verwenden eine Liste, weil unser Aufgabenplaner mehrere Aufgaben verwalten soll.
    ///

    /// note | Begriff: Dictionary
    Ein Dictionary (`dict`) speichert Werte unter Namen.
    Diese Namen nennt man Schlüssel.
    Eine Aufgabe kann dadurch Titel, Kategorie, Priorität und Status in einem einzigen Objekt bündeln.
    ///

    /// note | Begriff: Schlüssel und Wert
    In `aufgabe["titel"]` ist `"titel"` der Schlüssel.
    Der dazugehörige Wert ist zum Beispiel `"Einkauf erledigen"`.
    ///

    /// note | Begriff: Bool-Wert
    Der Schlüssel `"erledigt"` enthält einen Bool-Wert.
    `False` bedeutet: Die Aufgabe ist noch offen.
    `True` bedeutet: Die Aufgabe ist erledigt.
    ///
    """)
    return


@app.cell
def _(aufgaben):
    aufgaben[0]["titel"]
    return


@app.cell
def _(aufgaben):
    offene_aufgaben = []

    for _aufgabe in aufgaben:
        if not _aufgabe["erledigt"]:
            offene_aufgaben.append(_aufgabe)

    offene_aufgaben
    return (offene_aufgaben,)


@app.cell
def _(offene_aufgaben):
    uebersicht = []

    for _aufgabe in offene_aufgaben:
        text = (
            f'{_aufgabe["titel"]} '
            f'[{_aufgabe["kategorie"]}] '
            f'- Priorität {_aufgabe["prioritaet"]}'
        )
        uebersicht.append(text)

    uebersicht
    return (uebersicht,)


@app.cell(hide_code=True)
def _(mo, uebersicht):
    mo.md(f"""
    ## Zwischenstand im Projekt

    Unser Datenmodell ist jetzt deutlich stärker:

    {chr(10).join(f"- {zeile}" for zeile in uebersicht)}
    """)
    return


@app.cell
def _(offene_aufgaben):
    kategorien = []

    for _aufgabe in offene_aufgaben:
        kategorien.append(_aufgabe["kategorie"].lower())

    kategorien
    return


@app.cell
def _(aufgaben):
    anzahl_pro_kategorie = {}

    for _aufgabe in aufgaben:
        _kategorie = _aufgabe["kategorie"]
        if _kategorie not in anzahl_pro_kategorie:
            anzahl_pro_kategorie[_kategorie] = 0
        anzahl_pro_kategorie[_kategorie] += 1

    anzahl_pro_kategorie
    return (anzahl_pro_kategorie,)


@app.cell
def _(aufgaben):
    wichtigste_offene_titel = []

    for _aufgabe in aufgaben:
        if not _aufgabe["erledigt"] and _aufgabe["prioritaet"] >= 3:
            wichtigste_offene_titel.append(_aufgabe["titel"])

    wichtigste_offene_titel
    return (wichtigste_offene_titel,)


@app.cell(hide_code=True)
def _(anzahl_pro_kategorie, mo, wichtigste_offene_titel):
    mo.md(f"""
    ## Kleine Zusammenfassung

    Aufgaben pro Kategorie:

    {chr(10).join(f"- {kategorie}: {anzahl}" for kategorie, anzahl in anzahl_pro_kategorie.items())}

    Wichtigste offene Aufgaben:

    {chr(10).join(f"- {titel}" for titel in wichtigste_offene_titel)}

    /// note | Begriff: Aggregation
    Aggregation bedeutet, mehrere Einzelwerte zu einer Zusammenfassung zu verdichten.
    Hier zählen wir Aufgaben pro Kategorie.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mini-Übungen

    1. Füge eine neue Aufgabe als weiteres Wörterbuch hinzu.
    2. Ergänze einen neuen Schlüssel, zum Beispiel `dauer_minuten`.
    3. Erzeuge eine Liste, die nur Titel aus der Kategorie `Lernen` enthält.
    4. Zähle, wie viele Aufgaben erledigt und wie viele offen sind.
    """)
    return


if __name__ == "__main__":
    app.run()
