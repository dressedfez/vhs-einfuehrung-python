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
    # Kurstag 4: Funktionen und Programmstruktur

    Unser Aufgabenplaner ist jetzt groß genug, dass doppelter Code stört.
    Heute schreiben wir kleine Funktionen mit klarer Aufgabe.

    Leitfrage:
    **Welche Teile unseres Programms sollten einen eigenen Namen bekommen?**

    /// note | Begriff: Funktion
    Eine Funktion ist ein benannter Programmteil, den wir wiederverwenden können.
    Funktionen helfen, ein größeres Programm in verständliche Schritte zu zerlegen.
    ///

    /// note | Begriff: Parameter
    Parameter sind Platzhalter für Werte, die beim Aufruf an eine Funktion übergeben werden.
    In `neue_aufgabe(titel, kategorie, prioritaet)` sind `titel`, `kategorie` und `prioritaet` Parameter.
    ///

    /// note | Begriff: Rückgabewert
    Mit `return` gibt eine Funktion ein Ergebnis zurück.
    Dieses Ergebnis kann danach in einer Variable gespeichert oder direkt weiterverarbeitet werden.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ziele des Kurstags

    Am Ende dieses Kurstags kannst du:

    - wiederholte Programmlogik als Funktion ausdrücken
    - Parameter und Rückgabewerte in eigenen Funktionen nutzen
    - den Unterschied zwischen Rückgabewert und Seiteneffekt erkennen
    - Aufgaben über Funktionen hinzufügen und abschließen
    - eine kurze Projektübersicht aus mehreren Funktionen zusammensetzen
    - einfache Fehler in Funktionsaufrufen systematisch untersuchen
    """)
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
def aufgabe_abschliessen(aufgaben, titel):
    for aufgabe in aufgaben:
        if aufgabe["titel"] == titel:
            aufgabe["erledigt"] = True
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


@app.function
def projekt_zusammenfassung(aufgaben):
    offene_anzahl = len(offene_aufgaben_finden(aufgaben))
    erledigte_anzahl = len(aufgaben) - offene_anzahl
    return f"{offene_anzahl} offen, {erledigte_anzahl} erledigt"


@app.cell
def _(aufgaben):
    aufgaben_mit_neuem_eintrag = aufgabe_hinzufuegen(
        aufgaben, "Geburtstagskarte schreiben", "Privat", 1
    )
    aufgaben_mit_neuem_eintrag
    return (aufgaben_mit_neuem_eintrag,)


@app.cell
def _(aufgaben_mit_neuem_eintrag):
    aufgaben_nach_abschluss = aufgabe_abschliessen(
        aufgaben_mit_neuem_eintrag, "Einkauf erledigen"
    )
    aufgaben_nach_abschluss
    return (aufgaben_nach_abschluss,)


@app.cell
def _(aufgaben_nach_abschluss):
    offene_aufgaben = offene_aufgaben_finden(aufgaben_nach_abschluss)
    offene_aufgaben
    return (offene_aufgaben,)


@app.cell
def _(offene_aufgaben):
    text_ausgabe = []

    for aufgabe in offene_aufgaben:
        text_ausgabe.append(als_text(aufgabe))

    text_ausgabe
    return (text_ausgabe,)


@app.cell
def _(aufgaben_nach_abschluss):
    zusammenfassung_text = projekt_zusammenfassung(aufgaben_nach_abschluss)
    zusammenfassung_text
    return (zusammenfassung_text,)


@app.cell(hide_code=True)
def _(mo, text_ausgabe, zusammenfassung_text):
    mo.md(f"""
    ## Warum Funktionen helfen

    Unser Programm liest sich jetzt in Schritten:

    1. Aufgabe erzeugen
    2. Aufgabe hinzufügen
    3. offene Aufgaben finden
    4. Ausgabe vorbereiten

    Zusammenfassung:
    `{zusammenfassung_text}`

    Aktueller Stand:

    {chr(10).join(f"- {zeile}" for zeile in text_ausgabe)}

    /// note | Begriff: Seiteneffekt
    Ein Seiteneffekt bedeutet, dass eine Funktion nicht nur ein Ergebnis zurückgibt,
    sondern auch etwas an vorhandenen Daten verändert.
    `aufgabe_abschliessen(...)` verändert den Wert `"erledigt"` in einer bestehenden Aufgabe.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fehlersuche

    Typische Fragen beim Debuggen:

    - Hat eine Variable wirklich den Wert, den ich erwarte?
    - Gibt meine Funktion etwas zurück?
    - Stimmt der Schlüssel im Wörterbuch wirklich?

    Ein guter erster Schritt ist oft:
    kleine Zwischenwerte ausgeben und den Code in kleine Funktionen zerlegen.

    /// tip | Debugging
    Prüfe bei Funktionen zuerst drei Dinge:
    Welche Werte gehen hinein?
    Welche Werte kommen zurück?
    Welche vorhandenen Daten werden verändert?
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mini-Übungen

    1. Schreibe eine Funktion `als_kurztext`, die nur Titel und Status ausgibt.
    2. Ergänze eine Funktion, die alle Aufgaben mit Priorität `>= 2` findet.
    3. Baue absichtlich einen falschen Schlüssel ein und lies die Fehlermeldung.
    4. Schreibe eine Funktion, die eine Aufgabe wieder auf `erledigt = False` setzt.
    """)
    return


if __name__ == "__main__":
    app.run()
