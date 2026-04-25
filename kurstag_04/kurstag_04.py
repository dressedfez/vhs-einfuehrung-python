# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.20.0",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Kurstag 4: Funktionen und Programmstruktur

        Unser Aufgabenplaner ist jetzt groß genug, dass doppelter Code stört.
        Heute schreiben wir kleine Funktionen mit klarer Aufgabe.

        Leitfrage:
        **Welche Teile unseres Programms sollten einen eigenen Namen bekommen?**
        """
    )
    return


@app.cell
def _():
    aufgaben = [
        {
            "titel": "Einkauf erledigen",
            "kategorie": "Alltag",
            "prioritaet": 2,
            "erledigt": False,
        },
        {
            "titel": "Python-Hausaufgabe bearbeiten",
            "kategorie": "Lernen",
            "prioritaet": 3,
            "erledigt": False,
        },
    ]
    return (aufgaben,)


@app.function
def neue_aufgabe(titel, kategorie, prioritaet):
    return {
        "titel": titel,
        "kategorie": kategorie,
        "prioritaet": prioritaet,
        "erledigt": False,
    }


@app.function
def aufgabe_hinzufuegen(aufgaben, titel, kategorie, prioritaet):
    aufgaben.append(neue_aufgabe(titel, kategorie, prioritaet))
    return aufgaben


@app.function
def offene_aufgaben_finden(aufgaben):
    offene_aufgaben = []

    for aufgabe in aufgaben:
        if not aufgabe["erledigt"]:
            offene_aufgaben.append(aufgabe)

    return offene_aufgaben


@app.function
def als_text(aufgabe):
    return (
        f'{aufgabe["titel"]} '
        f'[{aufgabe["kategorie"]}] '
        f'- Priorität {aufgabe["prioritaet"]}'
    )


@app.cell
def _(aufgaben, aufgabe_hinzufuegen):
    aufgaben_mit_neuem_eintrag = aufgabe_hinzufuegen(
        aufgaben, "Geburtstagskarte schreiben", "Privat", 1
    )
    aufgaben_mit_neuem_eintrag
    return (aufgaben_mit_neuem_eintrag,)


@app.cell
def _(aufgaben_mit_neuem_eintrag, offene_aufgaben_finden):
    offene_aufgaben = offene_aufgaben_finden(aufgaben_mit_neuem_eintrag)
    offene_aufgaben
    return (offene_aufgaben,)


@app.cell
def _(als_text, offene_aufgaben):
    text_ausgabe = []

    for aufgabe in offene_aufgaben:
        text_ausgabe.append(als_text(aufgabe))

    text_ausgabe
    return (text_ausgabe,)


@app.cell(hide_code=True)
def _(mo, text_ausgabe):
    mo.md(
        f"""
        ## Warum Funktionen helfen

        Unser Programm liest sich jetzt in Schritten:

        1. Aufgabe erzeugen
        2. Aufgabe hinzufügen
        3. offene Aufgaben finden
        4. Ausgabe vorbereiten

        Aktueller Stand:

        {chr(10).join(f"- {zeile}" for zeile in text_ausgabe)}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Fehlersuche

        Typische Fragen beim Debuggen:

        - Hat eine Variable wirklich den Wert, den ich erwarte?
        - Gibt meine Funktion etwas zurück?
        - Stimmt der Schlüssel im Wörterbuch wirklich?

        Ein guter erster Schritt ist oft:
        kleine Zwischenwerte ausgeben und den Code in kleine Funktionen zerlegen.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Mini-Übungen

        1. Schreibe eine Funktion `als_kurztext`, die nur Titel und Status ausgibt.
        2. Ergänze eine Funktion, die alle Aufgaben mit Priorität `>= 2` findet.
        3. Baue absichtlich einen falschen Schlüssel ein und lies die Fehlermeldung.
        """
    )
    return


if __name__ == "__main__":
    app.run()
