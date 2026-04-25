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
    import csv
    import io

    import marimo as mo

    return csv, io, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Kurstag 6: Rückblick und Ausblick

    Unser Aufgabenplaner ist fertig genug, um als echtes Lernprojekt zu dienen.
    Heute geht es um zwei Fragen:

    1. Welche Python-Ideen haben wir wirklich benutzt?
    2. Wie führen dieselben Denkweisen später zu Datenanalyse oder KI?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ziele des Kurstags

    Am Ende dieses Kurstags kannst du:

    - die wichtigsten Python-Bausteine des Projekts benennen
    - erklären, wie aus Listen und Wörterbüchern tabellarische Daten werden
    - die Begriffe Zeile, Spalte und Tabelle verwenden
    - einfache CSV-Daten einlesen und filtern
    - Textwerte aus CSV-Daten bei Bedarf in Zahlen umwandeln
    - kleine Auswertungen aus CSV-Zeilen berechnen
    - realistisch einschätzen, was ein Folgekurs zu Datenanalyse oder KI leisten würde
    """)
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
    mo.md(f"""
    ## Rückblick auf das Projekt

    Diese Bausteine stecken bereits im Aufgabenplaner:

    {chr(10).join(f"- {eintrag}" for eintrag in projekt_bausteine)}

    /// note | Transfer
    Datenanalyse ist kein völlig anderes Denken.
    Wir verwenden weiterhin Variablen, Bedingungen, Schleifen, Listen, Dictionaries und Funktionen,
    nur auf größeren oder stärker strukturierten Daten.
    ///
    """)
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

    for _zeile in zeilen:
        if _zeile["erledigt"] == "False":
            offene_titel.append(_zeile["titel"].strip())

    offene_titel
    return (offene_titel,)


@app.cell
def _(zeilen):
    csv_anzahl_pro_kategorie = {}

    for _zeile in zeilen:
        _kategorie = _zeile["kategorie"].strip()
        if _kategorie not in csv_anzahl_pro_kategorie:
            csv_anzahl_pro_kategorie[_kategorie] = 0
        csv_anzahl_pro_kategorie[_kategorie] += 1

    csv_anzahl_pro_kategorie
    return (csv_anzahl_pro_kategorie,)


@app.cell
def _(zeilen):
    csv_hohe_prioritaet = []

    for _zeile in zeilen:
        if int(_zeile["prioritaet"]) >= 2:
            csv_hohe_prioritaet.append(_zeile["titel"].strip())

    csv_hohe_prioritaet
    return (csv_hohe_prioritaet,)


@app.cell(hide_code=True)
def _(csv_anzahl_pro_kategorie, csv_hohe_prioritaet, mo, offene_titel):
    mo.md(f"""
    ## Kleiner Ausblick auf Datenanalyse

    Auch in tabellarischen Daten machen wir im Kern ähnliche Dinge:

    - Daten einlesen
    - Zeilen prüfen
    - Werte filtern
    - Ergebnisse zusammenfassen

    /// note | Begriff: Tabelle
    Eine Tabelle besteht aus Zeilen und Spalten.
    Eine Zeile beschreibt einen Datensatz, eine Spalte beschreibt eine Eigenschaft.
    ///

    /// note | Begriff: CSV
    CSV steht für "comma-separated values".
    Es ist ein einfaches Textformat für tabellarische Daten.
    ///

    /// note | Begriff: Typumwandlung
    Beim Einlesen aus CSV-Dateien kommen Werte zuerst als Text an.
    Wenn wir damit rechnen oder vergleichen wollen, wandeln wir `"3"` mit `int("3")` in eine Zahl um.
    ///

    Offene Titel aus einem Mini-CSV:

    {chr(10).join(f"- {titel}" for titel in offene_titel)}

    Aufgaben pro Kategorie:

    {chr(10).join(f"- {kategorie}: {anzahl}" for kategorie, anzahl in csv_anzahl_pro_kategorie.items())}

    Aufgaben mit Priorität ab 2:

    {chr(10).join(f"- {titel}" for titel in csv_hohe_prioritaet)}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Was wäre der nächste sinnvolle Schritt?

    Nach diesem Kurs wäre ein Folgekurs zu Datenanalyse sinnvoll, wenn wir:

    - größere Dateien einlesen wollen
    - Daten nach mehreren Kriterien filtern wollen
    - Ergebnisse als Diagramm darstellen wollen
    - einfache Vorhersagen oder Klassifikationen verstehen wollen

    Die Grundlage dafür ist aber dieselbe:
    Werte verstehen, Daten strukturieren, Wiederholungen nutzen und Programme in klare Schritte zerlegen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Erweiterungsaufgaben

    1. Ergänze ein Fälligkeitsdatum im Aufgabenplaner.
    2. Schreibe eine Funktion, die nur Aufgaben einer Kategorie zurückgibt.
    3. Überlege, welche Teile des Projekts sich später mit `pandas` bequemer lösen ließen.

    Wichtig:
    Datenanalyse und KI sind nicht das Ziel dieses Einstiegskurses.
    Sie sind der nächste mögliche Schritt auf einer jetzt tragfähigen Grundlage.
    """)
    return


if __name__ == "__main__":
    app.run()
