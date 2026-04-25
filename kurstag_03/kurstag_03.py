# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.20.0",
# ]
# ///

import marimo

__generated_with = "0.23.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Kurstag 3: Daten sinnvoll strukturieren

        Bisher hatten wir mehrere getrennte Listen.
        Das wird schnell unübersichtlich.

        Heute bauen wir ein einfaches Datenmodell für unseren Aufgabenplaner:

        - eine Aufgabe besteht aus mehreren Informationen
        - mehrere Aufgaben stehen in einer Liste
        - zusammengehörige Informationen speichern wir in einem Wörterbuch
        """
    )
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
    mo.md(
        r"""
        ## Listen und Wörterbücher

        Eine Liste ist nützlich für viele Einträge.
        Ein Wörterbuch ist nützlich, wenn ein Eintrag mehrere benannte Teile hat.
        """
    )
    return


@app.cell
def _(aufgaben):
    aufgaben[0]["titel"]
    return


@app.cell
def _(aufgaben):
    offene_aufgaben = []

    for aufgabe in aufgaben:
        if not aufgabe["erledigt"]:
            offene_aufgaben.append(aufgabe)

    offene_aufgaben
    return (offene_aufgaben,)


@app.cell
def _(offene_aufgaben):
    uebersicht = []

    for aufgabe in offene_aufgaben:
        text = (
            f'{aufgabe["titel"]} '
            f'[{aufgabe["kategorie"]}] '
            f'- Priorität {aufgabe["prioritaet"]}'
        )
        uebersicht.append(text)

    uebersicht
    return (uebersicht,)


@app.cell(hide_code=True)
def _(mo, uebersicht):
    mo.md(
        f"""
        ## Zwischenstand im Projekt

        Unser Datenmodell ist jetzt deutlich staerker:

        {chr(10).join(f"- {zeile}" for zeile in uebersicht)}
        """
    )
    return


@app.cell
def _(offene_aufgaben):
    kategorien = []

    for aufgabe in offene_aufgaben:
        kategorien.append(aufgabe["kategorie"].lower())

    kategorien
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Mini-Übungen

        1. Füge eine neue Aufgabe als weiteres Wörterbuch hinzu.
        2. Ergänze einen neuen Schlüssel, zum Beispiel `dauer_minuten`.
        3. Erzeuge eine Liste, die nur Titel aus der Kategorie `Lernen` enthält.
        """
    )
    return


if __name__ == "__main__":
    app.run()
