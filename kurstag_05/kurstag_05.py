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
    import json
    import tempfile
    from pathlib import Path

    import marimo as mo

    return Path, json, mo, tempfile


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Kurstag 5: Speichern und Laden

        Ein Aufgabenplaner ist erst dann wirklich nützlich, wenn Aufgaben nach dem Schließen des Programms
        nicht verloren gehen. Heute speichern wir Daten in einer Datei.

        Wir verwenden dafür **JSON**:

        - leicht lesbar
        - gut geeignet für Listen und Wörterbücher
        - ohne Zusatzpakete nutzbar
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
        {
            "titel": "Geburtstagskarte schreiben",
            "kategorie": "Privat",
            "prioritaet": 1,
            "erledigt": True,
        },
    ]
    return (aufgaben,)


@app.cell
def _(Path, tempfile):
    speicherort = Path(tempfile.gettempdir()) / "aufgabenplaner_demo.json"
    speicherort
    return (speicherort,)


@app.cell
def _(aufgaben, json):
    json_text = json.dumps(aufgaben, indent=2, ensure_ascii=False)
    json_text
    return (json_text,)


@app.cell
def _(json_text, speicherort):
    speicherort.write_text(json_text, encoding="utf-8")
    speicherort
    return


@app.cell
def _(json, speicherort):
    geladene_aufgaben = json.loads(speicherort.read_text(encoding="utf-8"))
    geladene_aufgaben
    return (geladene_aufgaben,)


@app.cell(hide_code=True)
def _(geladene_aufgaben, mo, speicherort):
    mo.md(
        f"""
        ## Zwischenstand im Projekt

        Unsere Aufgaben wurden erfolgreich gespeichert und wieder geladen.

        Speicherort für die Demo:
        `{speicherort}`

        Anzahl geladener Aufgaben:
        `{len(geladene_aufgaben)}`
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Übungen in Stufen

        **Stufe 1**
        Füge einen weiteren Eintrag hinzu und speichere erneut.

        **Stufe 2**
        Markiere eine Aufgabe als erledigt und prüfe, ob die Änderung nach dem Laden noch vorhanden ist.

        **Stufe 3**
        Schreibe eine kleine Funktion, die nur offene Aufgaben aus der geladenen Datei zurückgibt.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Ziel des Tages:
        Der Aufgabenplaner ist jetzt ein kleines, vollstaendiges Programm mit Eingaben, Verarbeitung und einfacher Speicherung.
        """
    )
    return


if __name__ == "__main__":
    app.run()
