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
    import json
    import tempfile
    from pathlib import Path

    import marimo as mo

    return Path, json, mo, tempfile


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Kurstag 5: Speichern und Laden

    Ein Aufgabenplaner ist erst dann wirklich nützlich, wenn Aufgaben nach dem Schließen des Programms
    nicht verloren gehen. Heute speichern wir Daten in einer Datei.

    Wir verwenden dafür **JSON**:

    - leicht lesbar
    - gut geeignet für Listen und Wörterbücher
    - ohne Zusatzpakete nutzbar

    /// note | Begriff: Datei
    Eine Datei speichert Daten außerhalb des laufenden Programms.
    Dadurch sind Aufgaben nach dem Schließen des Notebooks nicht sofort verloren.
    ///

    /// note | Begriff: JSON
    JSON ist ein textbasiertes Datenformat.
    Es passt gut zu Python-Listen und Dictionaries und ist deshalb für unseren Aufgabenplaner geeignet.
    ///

    /// note | Begriff: Serialisierung
    Serialisierung bedeutet: Python-Daten werden in Text umgewandelt, damit man sie speichern kann.
    `json.dumps(...)` macht aus unseren Aufgaben JSON-Text.
    ///

    /// note | Begriff: Deserialisierung
    Deserialisierung bedeutet: gespeicherter Text wird wieder zu Python-Daten.
    `json.loads(...)` macht aus JSON-Text wieder Listen und Dictionaries.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ziele des Kurstags

    Am Ende dieses Kurstags kannst du:

    - Python-Daten als JSON-Text darstellen
    - JSON in eine Datei schreiben und wieder laden
    - Pfade mit `Path` verwenden
    - einfache Speicher- und Ladefunktionen formulieren
    - Serialisierung und Deserialisierung benennen
    - prüfen, ob geladene Daten noch dieselbe Struktur haben
    - das Projekt als kleines vollständiges Programm beschreiben
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Speicherort und Pfade

    Bevor wir speichern können, brauchen wir einen Ort für die Datei.

    /// note | Begriff: Pfad
    Ein Pfad beschreibt, wo eine Datei liegt.
    `Path(...)` hilft uns, solche Pfade in Python zu bauen und zu verwenden.
    ///

    Für die Kursdemo speichern wir in einem temporären Ordner.
    In einem echten Projekt könnte die Datei zum Beispiel direkt neben dem Notebook liegen.
    """)
    return


@app.function
def aufgaben_speichern(aufgaben, speicherort, json):
    json_text = json.dumps(aufgaben, indent=2, ensure_ascii=False)
    speicherort.write_text(json_text, encoding="utf-8")
    return json_text


@app.function
def aufgaben_laden(speicherort, json):
    return json.loads(speicherort.read_text(encoding="utf-8"))


@app.cell
def _(aufgaben, json):
    json_text = json.dumps(aufgaben, indent=2, ensure_ascii=False)
    json_text
    return


@app.cell
def _(aufgaben, json, speicherort):
    gespeicherter_json_text = aufgaben_speichern(aufgaben, speicherort, json)
    gespeicherter_json_text
    return


@app.cell
def _(speicherort):
    speicherort
    return


@app.cell
def _(json, speicherort):
    geladene_aufgaben = aufgaben_laden(speicherort, json)
    geladene_aufgaben
    return (geladene_aufgaben,)


@app.cell
def _(geladene_aufgaben):
    geladene_titel = []

    for _aufgabe in geladene_aufgaben:
        geladene_titel.append(_aufgabe["titel"])

    geladene_titel
    return (geladene_titel,)


@app.cell
def _(geladene_aufgaben):
    geladene_offene_anzahl = 0

    for _aufgabe in geladene_aufgaben:
        if not _aufgabe["erledigt"]:
            geladene_offene_anzahl += 1

    geladene_offene_anzahl
    return (geladene_offene_anzahl,)


@app.cell(hide_code=True)
def _(
    geladene_aufgaben,
    geladene_offene_anzahl,
    geladene_titel,
    mo,
    speicherort,
):
    mo.md(f"""
    ## Zwischenstand im Projekt

    Unsere Aufgaben wurden erfolgreich gespeichert und wieder geladen.

    Speicherort für die Demo:
    `{speicherort}`

    Anzahl geladener Aufgaben:
    `{len(geladene_aufgaben)}`

    Offene Aufgaben:
    `{geladene_offene_anzahl}`

    Geladene Titel:

    {chr(10).join(f"- {titel}" for titel in geladene_titel)}

    /// tip | Kontrolle nach dem Laden
    Nach dem Laden prüfen wir nicht nur, ob kein Fehler aufgetreten ist.
    Wir prüfen auch, ob Anzahl, Titel und Status der Aufgaben noch sinnvoll aussehen.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Übungen in Stufen

    **Stufe 1**
    Füge einen weiteren Eintrag hinzu und speichere erneut.

    **Stufe 2**
    Markiere eine Aufgabe als erledigt und prüfe, ob die Änderung nach dem Laden noch vorhanden ist.

    **Stufe 3**
    Schreibe eine kleine Funktion, die nur offene Aufgaben aus der geladenen Datei zurückgibt.

    **Stufe 4**
    Ändere einen Titel, speichere erneut und prüfe danach die geladene Liste.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ziel des Tages:
    Der Aufgabenplaner ist jetzt ein kleines, vollständiges Programm mit Eingaben, Verarbeitung und einfacher Speicherung.
    """)
    return


if __name__ == "__main__":
    app.run()
