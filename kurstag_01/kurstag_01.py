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
    # Kurstag 1: Das Problem verstehen

    Unser Leitprojekt ist ein kleiner **Aufgabenplaner**.
    Wir starten heute nicht mit vielen Begriffen, sondern mit einer einfachen Frage:

    **Wie kann ein Programm eine Aufgabe beschreiben, damit wir sie später weiterverarbeiten können?**

    Heute brauchen wir dafür nur wenige Bausteine:

    - Werte
    - Variablen
    - Datentypen
    - Strings und Zahlen
    - erste formatierte Ausgaben
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ziele des Kurstags

    Am Ende dieses Kurstags kannst du:

    - erklären, welches Problem unser Aufgabenplaner lösen soll
    - eine einzelne Aufgabe mit Variablen beschreiben
    - die Begriffe Wert, Variable und Datentyp unterscheiden
    - gute und schlechte Variablennamen unterscheiden
    - einfache Werte als String, Zahl oder Wahrheitswert erkennen
    - mit einem `f`-String eine lesbare Textausgabe erzeugen
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hauptziel des Projekts

    Am Ende des Kurses soll unser Aufgabenplaner Folgendes können:

    - neue Aufgaben speichern
    - Aufgaben mit Titel, Kategorie, Priorität und Status beschreiben
    - offene und dringende Aufgaben anzeigen
    - Aufgaben als erledigt markieren
    - Aufgaben in einer Datei speichern und später wieder laden

    Das bauen wir nicht alles heute.
    Kurstag 1 legt nur den ersten Baustein:
    **Wir beschreiben eine einzelne Aufgabe mit passenden Werten und Variablen.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Arbeitsstart mit `uv` und `marimo`

    `uv` und `marimo` sind heute nur Mittel zum Zweck.
    Sobald der Kurs arbeitsfähig ist, konzentrieren wir uns auf Python.

    ```bash
    uv run marimo edit kurstag_01.py
    ```

    In einem `marimo`-Notebook besteht das Material aus Textzellen und Codezellen.
    Jede Codezelle kann einzeln ausprobiert und verändert werden.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Welche Informationen braucht eine Aufgabe?

    Bevor wir programmieren, klären wir das Problem fachlich.
    Eine Aufgabe ist nicht nur ein Satz. Für unseren Aufgabenplaner sind diese Informationen nützlich:

    - ein Titel, damit wir wissen, worum es geht
    - eine Priorität, damit Wichtiges auffällt
    - eine geschätzte Dauer, damit wir planen können
    - später zusätzlich: Kategorie, Status und Speicherung

    Heute verwenden wir nur Titel, Priorität und Dauer.
    Das reicht, um die ersten Python-Bausteine sinnvoll zu benutzen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    titel = mo.ui.text(label="Aufgabentitel", value="Python-Notizen schreiben")
    prioritaet = mo.ui.dropdown(
        options=["niedrig", "mittel", "hoch"], value="mittel", label="Priorität"
    )
    minuten = mo.ui.number(start=5, stop=180, step=5, value=30, label="Dauer in Minuten")
    mo.vstack([titel, prioritaet, minuten])
    return minuten, prioritaet, titel


@app.cell(hide_code=True)
def _(minuten, mo, prioritaet, titel):
    mo.md(f"""
    ## Erste Variablen

    In einem Programm geben wir Werten Namen, damit wir später wieder auf sie zugreifen können.

    Aktuell arbeiten wir mit diesen Werten:

    - Titel: `{titel.value}`
    - Priorität: `{prioritaet.value}`
    - Dauer: `{minuten.value}` Minuten

    /// note | Begriff: Variable
    Eine Variable ist ein Name für einen Wert.
    Wir nutzen Variablen, damit ein Programm später wieder auf diesen Wert zugreifen kann.
    ///

    /// note | Begriff: Wert
    Ein Wert ist eine konkrete Information im Programm, zum Beispiel `"Python-Notizen schreiben"` oder `30`.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Regeln für Variablennamen

    Variablennamen müssen in Python bestimmten Regeln folgen:

    - Sie dürfen Buchstaben, Zahlen und Unterstriche enthalten.
    - Sie dürfen nicht mit einer Zahl beginnen.
    - Sie dürfen keine Leerzeichen oder Sonderzeichen enthalten.
    - Groß- und Kleinschreibung sind verschieden: `titel` und `Titel` sind zwei unterschiedliche Namen.
    - Python-Schlüsselwörter wie `if`, `for` oder `while` dürfen nicht als Variablennamen verwendet werden.

    Nach PEP 8 schreibt man normale Variablen in Python meistens klein und trennt Wörter mit Unterstrichen.
    Diese Schreibweise heißt `snake_case`.

    /// tip | PEP 8 im Kurs
    Wir schreiben Code-Bezeichner ohne Umlaute, zum Beispiel `geschaetzte_minuten`.
    In Erklärungstexten verwenden wir normale deutsche Umlaute.
    ///
    """)
    return


@app.cell
def _():
    # Gute Variablennamen fuer unseren Aufgabenplaner
    beispiel_titel = "Python-Notizen schreiben"
    beispiel_prioritaet = "mittel"
    beispiel_minuten = 30
    beispiel_ist_erledigt = False
    return (
        beispiel_ist_erledigt,
        beispiel_minuten,
        beispiel_prioritaet,
        beispiel_titel,
    )


@app.cell
def _(
    beispiel_ist_erledigt,
    beispiel_minuten,
    beispiel_prioritaet,
    beispiel_titel,
):
    (
        beispiel_titel,
        beispiel_prioritaet,
        beispiel_minuten,
        beispiel_ist_erledigt,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Diese Namen sind erlaubt, aber für unseren Kurs weniger gut lesbar:

    ```python
    x = "Python-Notizen schreiben"
    p = "mittel"
    dauer = 30
    ```

    Diese Namen wären in Python nicht erlaubt:

    ```python
    1_aufgabe = "Startet mit einer Zahl"
    aufgaben titel = "Enthält ein Leerzeichen"
    for = "Ist ein Python-Schlüsselwort"
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Namen bewerten

    Welche Namen helfen beim Lesen des Programms?

    | Name | Bewertung |
    | --- | --- |
    | `x` | erlaubt, aber zu unklar |
    | `titel` | gut, wenn es nur einen Titel gibt |
    | `aufgaben_titel` | besser, wenn klar sein soll, wozu der Titel gehört |
    | `geschätzte_minuten` | fachlich gut, aber im Code verwenden wir besser `geschaetzte_minuten` |
    | `geschaetzte_minuten` | gut lesbar und ohne Umlaut im Code |

    Grundregel:
    Ein Name sollte so kurz wie möglich und so deutlich wie nötig sein.
    """)
    return


@app.cell
def _(minuten, prioritaet, titel):
    aufgaben_titel = titel.value
    aufgaben_prioritaet = prioritaet.value
    geschaetzte_minuten = minuten.value
    return aufgaben_prioritaet, aufgaben_titel, geschaetzte_minuten


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zahlen und Strings

    Mit Zahlen können wir rechnen, mit Strings können wir Text speichern.
    Beides brauchen wir schon im ersten kleinen Programmfragment.

    Mit einem `f`-String können wir Werte aus Variablen in einen Text einsetzen.

    /// note | Begriff: Datentyp
    Ein Datentyp beschreibt, welche Art von Wert vorliegt und was Python damit tun kann.
    `"Text"` ist ein `str`, `30` ist ein `int`, `30.0` ist ein `float` und `False` ist ein `bool`.
    ///

    /// note | Begriff: String
    Ein String (`str`) ist Text in Anführungszeichen.
    Strings brauchen wir zum Beispiel für Titel, Kategorien oder Ausgabetexte.
    ///

    /// note | Begriff: Integer
    Ein Integer (`int`) ist eine ganze Zahl.
    Ganze Zahlen brauchen wir zum Beispiel für Minuten oder Prioritäten.
    ///
    """)
    return


@app.cell
def _(aufgaben_prioritaet, aufgaben_titel, geschaetzte_minuten):
    (
        type(aufgaben_titel),
        type(aufgaben_prioritaet),
        type(geschaetzte_minuten),
    )
    return


@app.cell
def _(aufgaben_prioritaet, aufgaben_titel, geschaetzte_minuten):
    f"Offene Aufgabe: {aufgaben_titel} ({aufgaben_prioritaet}, {geschaetzte_minuten} Minuten)"
    return


@app.cell
def _(geschaetzte_minuten):
    stunden = geschaetzte_minuten / 60
    stunden
    return (stunden,)


@app.cell
def _(stunden):
    type(stunden)
    return


@app.cell
def _(aufgaben_titel, stunden):
    f"Für '{aufgaben_titel}' planen wir rund {stunden:.1f} Stunden ein."
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Kleine Fehler bewusst lesen

    Fehler gehören zum Programmieren dazu.
    Heute reicht es, typische Meldungen grob einzuordnen.

    Beispiel 1: Die Variable wurde anders geschrieben.

    ```python
    aufgaben_titel = "Python-Notizen schreiben"
    aufgabe_titel
    ```

    Erwartbare Meldung: `NameError`, weil `aufgabe_titel` ohne `n` nicht definiert wurde.

    Beispiel 2: Der Variablenname ist nicht erlaubt.

    ```python
    1_aufgabe = "Python-Notizen schreiben"
    ```

    Erwartbare Meldung: `SyntaxError`, weil ein Variablenname nicht mit einer Zahl beginnen darf.

    /// tip | Fehlermeldungen lesen
    Lies Fehlermeldungen zuerst von unten nach oben.
    Meist stehen dort der Fehlertyp und ein Hinweis auf die betroffene Zeile.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Abschlussübung

    Beschreibe eine eigene Aufgabe mit vier Variablen:

    ```python
    eigener_titel = "..."
    eigene_prioritaet = "..."
    eigene_minuten = ...
    eigener_ort = "..."
    ```

    Gib danach einen Satz mit einem `f`-String aus.

    Zusatzfragen:

    1. Welcher Variablenname ist besonders gut lesbar?
    2. Welche Werte sind Strings?
    3. Welcher Wert ist eine Zahl?

    Ziel des Tages:
    Am Ende kann jede Person ein kleines Python-Programm lesen und eigene Werte darin austauschen.
    """)
    return


if __name__ == "__main__":
    app.run()
