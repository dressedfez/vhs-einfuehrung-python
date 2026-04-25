# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.20.0",
# ]
# ///

import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import csv
    import io

    import marimo as mo

    return csv, io, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Kurstag 6: Rückblick und Ausblick

        Unser Aufgabenplaner ist fertig genug, um als echtes Lernprojekt zu dienen.
        Heute geht es um zwei Fragen:

        1. Welche Python-Ideen haben wir wirklich benutzt?
        2. Wie führen dieselben Denkweisen später zu Datenanalyse oder KI?
        """
    )
    return


@app.cell
def _():
    projekt_bausteine = [
        "Variablen für einzelne Werte",
        "Bedingungen für Entscheidungen",
        "Schleifen für mehrere Einträge",
        "Listen für viele Aufgaben",
        "Wörterbücher für zusammengehörige Informationen",
        "Funktionen für klare Programmstruktur",
        "Dateien für dauerhaftes Speichern",
    ]
    projekt_bausteine
    return (projekt_bausteine,)


@app.cell(hide_code=True)
def _(mo, projekt_bausteine):
    mo.md(
        f"""
        ## Rückblick auf das Projekt

        Diese Bausteine stecken bereits im Aufgabenplaner:

        {chr(10).join(f"- {eintrag}" for eintrag in projekt_bausteine)}
        """
    )
    return


@app.cell
def _():
    csv_text = """titel,kategorie,prioritaet,erledigt
Einkauf erledigen,Alltag,2,False
Python-Hausaufgabe bearbeiten,Lernen,3,False
Geburtstagskarte schreiben,Privat,1,True
"""
    return (csv_text,)


@app.cell
def _(csv, csv_text, io):
    zeilen = list(csv.DictReader(io.StringIO(csv_text)))
    zeilen
    return (zeilen,)


@app.cell
def _(zeilen):
    offene_titel = []

    for zeile in zeilen:
        if zeile["erledigt"] == "False":
            offene_titel.append(zeile["titel"])

    offene_titel
    return (offene_titel,)


@app.cell(hide_code=True)
def _(mo, offene_titel):
    mo.md(
        f"""
        ## Kleiner Ausblick auf Datenanalyse

        Auch in tabellarischen Daten machen wir im Kern aehnliche Dinge:

        - Daten einlesen
        - Zeilen prüfen
        - Werte filtern
        - Ergebnisse zusammenfassen

        Offene Titel aus einem Mini-CSV:

        {chr(10).join(f"- {titel}" for titel in offene_titel)}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Erweiterungsaufgaben

        1. Ergänze ein Fälligkeitsdatum im Aufgabenplaner.
        2. Schreibe eine Funktion, die nur Aufgaben einer Kategorie zurückgibt.
        3. Überlege, welche Teile des Projekts sich später mit `pandas` bequemer lösen ließen.

        Wichtig:
        Datenanalyse und KI sind nicht das Ziel dieses Einstiegskurses.
        Sie sind der naechste moegliche Schritt auf einer jetzt tragfaehigen Grundlage.
        """
    )
    return


if __name__ == "__main__":
    app.run()
