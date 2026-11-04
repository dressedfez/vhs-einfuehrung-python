# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo==0.25.2",
# ]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    def pruefhinweis(status, aufgabe, hinweis):
        if status is None:
            return mo.callout(
                mo.md(f"**Noch offen · {aufgabe}**\n\n{hinweis}"),
                kind="neutral",
            )
        if status:
            return mo.callout(
                mo.md(f"**✓ Richtig · {aufgabe}**\n\n{hinweis}"),
                kind="success",
            )
        return mo.callout(
            mo.md(f"**Noch nicht ganz · {aufgabe}**\n\n{hinweis}"), kind="warn"
        )

    return (pruefhinweis,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Kurstag 2 · Mein Python-Arbeitsheft

    **Rechnen · entscheiden · wiederholen**

    Dieses Arbeitsheft begleitet die Folien. Lies die kurzen Erklärungen, verändere die Beispiele und bearbeite die vier Übungen. Zu den Basisaufgaben erhältst du direkt darunter eine Rückmeldung. Musterlösungen werden im Unterricht besprochen.

    ## So arbeitest du mit dem Notebook

    - Im Ordner `kurstag_02` starten: `uvx --from "marimo==0.25.2" marimo edit kurstag_02_teilnehmende.py`.
    - Eine Codezelle mit **Shift+Enter** ausführen.
    - Erst vorhersagen, dann ausführen, dann das Ergebnis erklären.
    - **Neutral:** Aufgabe noch offen · **Orange:** Hinweis beachten · **Grün:** Prüfung bestanden.
    - Die vorgegebenen Antwortvariablen in den Übungszellen beibehalten, damit die Rückmeldung sie findet.

    Zu zweit: Eine Person tippt, die andere erklärt. Regelmäßig wechseln. Die Änderungen werden in dieser Datei gespeichert; für einen frischen Start eine Kopie anlegen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Unser Weg heute

    1. Rechenoperatoren und ihre Reihenfolge
    2. Vergleiche und bedingte Ausführung
    3. `while`- und `for`-Schleifen
    4. Interaktive Eingaben mit marimo

    Die Abschnitte **Zusatzteil** sind freiwillig und können nach dem Grundteil bearbeitet werden.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mathematische Operatoren

    | Bedeutung | Operator | Beispiel |
    | --- | --- | --- |
    | Addition | `+` | `7 + 3` |
    | Subtraktion | `-` | `7 - 3` |
    | Multiplikation | `*` | `7 * 3` |
    | Division | `/` | `7 / 3` |
    | Ganzzahldivision | `//` | `7 // 3` |
    | Rest | `%` | `7 % 3` |
    | Potenz | `**` | `7 ** 2` |

    `/` ergibt einen `float`. `//` und `%` helfen bei vollständigen Portionen und Resten.
    """)
    return


@app.cell
def _():
    _ergebnis = (8 + 3, 8 - 3, 8 * 3, 7 / 2, 17 // 5, 17 % 5, 3**2)
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Reihenfolge von Rechenoperationen

    Potenzieren kommt vor Multiplikation und Division. Diese kommen vor Addition und Subtraktion. Klammern machen die Reihenfolge deutlich.

    **Ausprobieren:** Vergleiche `2 + 3 * 4` mit `(2 + 3) * 4`.
    """)
    return


@app.cell
def _():
    _ergebnis = (2 + 3 * 4, (2 + 3) * 4)
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Gleitkommazahlen

    Viele Dezimalzahlen kann ein Computer binär nur annähernd speichern. Zum Beispiel ist `0.1 + 0.2` intern nicht exakt `0.3`.

    /// attention | Genauigkeit
    Verwende bei `float` keinen direkten Gleichheitsvergleich, wenn Rundungsabweichungen möglich sind. Für die Anzeige kann `round(wert, 2)` helfen.
    ///
    """)
    return


@app.cell
def _():
    _ergebnis = (0.1 + 0.2, round(0.1 + 0.2, 2))
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mitmachen · Portionen aufteilen

    17 Kekse werden gleichmäßig auf 5 Personen verteilt. Ergänze die beiden Platzhalter:

    - `_pro_person`: ganze Kekse pro Person
    - `_uebrig`: übrige Kekse

    Nutze `//` und `%`. Prüfe anschließend: `5 * _pro_person + _uebrig` soll wieder 17 ergeben.
    """)
    return


@app.cell
def _():
    _kekse = 17
    _personen = 5
    _pro_person = None  # Ersetze None durch eine passende Rechnung.
    _uebrig = None  # Ersetze None durch eine passende Rechnung.
    teilung_antwort = (_pro_person, _uebrig)
    teilung_antwort
    return (teilung_antwort,)


@app.cell(hide_code=True)
def _(pruefhinweis, teilung_antwort):
    _pro_person, _uebrig = teilung_antwort
    _offen = _pro_person is None and _uebrig is None
    _richtig = _pro_person == 3 and _uebrig == 2
    pruefhinweis(
        None if _offen else _richtig,
        "Portionen aufteilen",
        "Jede Person erhält 3 Kekse; 2 bleiben übrig."
        if _richtig
        else "Nutze Ganzzahldivision für ganze Portionen und Modulo für den Rest.",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Vergleiche und Wahrheitswerte

    Vergleiche ergeben `True` oder `False`.

    | Operator | Bedeutung |
    | --- | --- |
    | `==` | gleich |
    | `!=` | ungleich |
    | `<`, `<=` | kleiner, kleiner oder gleich |
    | `>`, `>=` | größer, größer oder gleich |

    `=` weist einen Wert zu. `==` vergleicht zwei Werte. Bedingungen lassen sich mit `and`, `or` und `not` verbinden.
    """)
    return


@app.cell
def _():
    _ergebnis = (5 == 5, 5 != 3, 18 <= 18, 18 <= 30 < 65, 5 == "5")
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Bedingte Ausführung mit `if`

    ```python
    if bedingung:
        # erster Fall
    elif weitere_bedingung:
        # weiterer Fall
    else:
        # übrige Fälle
    ```

    Nur der erste passende Zweig läuft. Die Einrückung gehört zur Syntax.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Beispiel · Eintrittspreis

    Ändere `_alter` und beobachte, welcher Zweig ausgeführt wird. Prüfe besonders die Werte 5, 6, 17, 18 und 65.
    """)
    return


@app.cell
def _():
    _alter = 17
    if _alter < 6:
        _preis = "Eintritt frei"
    elif _alter < 18:
        _preis = "Kinderpreis: 5 €"
    elif _alter < 65:
        _preis = "Normalpreis: 10 €"
    else:
        _preis = "Seniorenpreis: 6 €"
    _preis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mitmachen · Temperatur prüfen

    Ordne die Temperatur einer Nachricht zu:

    - über 30 °C: `Es ist heiß!`
    - 20 bis 30 °C einschließlich: `Angenehmes Wetter.`
    - unter 20 °C: `Ziemlich kühl heute.`

    Ergänze die drei Nachrichtentexte in der Codezelle. Teste danach die Grenzwerte 20 und 30.
    """)
    return


@app.cell
def _():
    _temperatur = 25
    _nachricht = ""
    # Ergänze die drei Nachrichtentexte.
    if _temperatur > 30:
        _nachricht = ""
    elif _temperatur >= 20:
        _nachricht = ""
    else:
        _nachricht = ""
    wetter_antwort = (_temperatur, _nachricht)
    wetter_antwort
    return (wetter_antwort,)


@app.cell(hide_code=True)
def _(pruefhinweis, wetter_antwort):
    _temperatur, _nachricht = wetter_antwort
    _offen = _nachricht == ""
    _richtig = _temperatur == 25 and _nachricht == "Angenehmes Wetter."
    pruefhinweis(
        None if _offen else _richtig,
        "Temperatur prüfen",
        "25 °C ist angenehmes Wetter. Prüfe auch, dass 20 und 30 °C eingeschlossen sind."
        if _richtig
        else "Prüfe die Fälle der Reihe nach: über 30, mindestens 20, sonst unter 20.",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Schleifen

    - `while bedingung:` wiederholt, solange die Bedingung wahr ist.
    - `for element in folge:` verarbeitet nacheinander jedes Element.

    Bei `while` muss sich ein Wert ändern, der die Bedingung beeinflusst. Sonst kann eine Endlosschleife entstehen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### `while`-Schleife

    ```python
    while bedingung:
        # wiederholter Code
    ```

    Der eingerückte Block wird so lange ausgeführt, wie die Bedingung wahr ist.
    """)
    return


@app.cell
def _():
    _zaehler = 1
    _folge = []
    while _zaehler < 4:
        _folge.append(_zaehler)
        _zaehler += 1
    _folge
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### `for`-Schleife und `range`

    `for` verarbeitet jedes Element einer Folge.

    `range(start, stop, schritt)` erzeugt Zahlen. Der `stop`-Wert ist ausgeschlossen.
    """)
    return


@app.cell
def _():
    _zahlen = list(range(1, 6))
    _summe = 0
    for _zahl in _zahlen:
        _summe += _zahl
    (_zahlen, _summe)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mitmachen · Punkte summieren

    Nutze einen Akkumulator und eine `for`-Schleife, um die Punkte zu addieren:

    ```python
    punkte = [12, 8, 15, 5]
    ```

    Ersetze in der Codezelle die `0` in `_summe += 0` durch die aktuelle Schleifenvariable.
    """)
    return


@app.cell
def _():
    _punkte = [12, 8, 15, 5]
    _summe = 0
    for _punkt in _punkte:
        _summe += 0  # Ersetze 0 durch _punkt.
    punkte_antwort = _summe
    punkte_antwort
    return (punkte_antwort,)


@app.cell(hide_code=True)
def _(pruefhinweis, punkte_antwort):
    _offen = punkte_antwort == 0
    _richtig = punkte_antwort == 40
    pruefhinweis(
        None if _offen else _richtig,
        "Punkte summieren",
        "Die vier Werte ergeben zusammen 40 Punkte."
        if _richtig
        else "Starte die Summe bei 0 und addiere in jedem Durchlauf den aktuellen Punkt.",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mitmachen · Countdown

    Zähle mit einer `while`-Schleife von 5 bis 1 herunter.

    Ergänze in der Codezelle den Wert, der an die Liste angehängt wird. Vergiss nicht, den Zähler pro Durchlauf zu verkleinern.
    """)
    return


@app.cell
def _():
    _zahl = 5
    _folge = []
    while _zahl > 0:
        _folge.append(0)
        _zahl -= 1
    countdown_antwort = _folge
    countdown_antwort
    return (countdown_antwort,)


@app.cell(hide_code=True)
def _(countdown_antwort, pruefhinweis):
    _offen = countdown_antwort == [0, 0, 0, 0, 0]
    _richtig = countdown_antwort == [5, 4, 3, 2, 1]
    pruefhinweis(
        None if _offen else _richtig,
        "Countdown",
        "Die Liste enthält 5, 4, 3, 2, 1."
        if _richtig
        else "Hänge den aktuellen Zähler an und verringere ihn in jedem Durchlauf um 1.",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · `break` und `continue`

    - `break` beendet eine Schleife sofort.
    - `continue` überspringt den Rest dieses Durchlaufs.

    Vor dem Ausführen: Welche Zahlen landen in der Liste?
    """)
    return


@app.cell
def _():
    _ausgabe = []
    for _zahl in range(1, 7):
        if _zahl == 4:
            continue
        if _zahl == 6:
            break
        _ausgabe.append(_zahl)
    _ausgabe
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · Schleifen mit `else`

    Bei `for` und `while` läuft der `else`-Zweig, wenn die Schleife normal endet. Nach einem `break` wird er übersprungen.

    Ein häufiger Einsatz ist eine Suche: `break` bei einem Treffer, `else` bei keinem Treffer.
    """)
    return


@app.cell
def _():
    _zahlen = [10, 24, 42, 57]
    for _zahl in _zahlen:
        if _zahl == 99:
            _meldung = "Zahl gefunden"
            break
    else:
        _meldung = "Zahl nicht gefunden"
    _meldung
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · List Comprehension

    Mit einer List Comprehension lässt sich eine neue Liste aus einer Folge erzeugen:

    ```python
    [ausdruck for element in folge if bedingung]
    ```

    Wenn die Kurzform schwer zu lesen ist, verwende eine normale `for`-Schleife.
    """)
    return


@app.cell
def _():
    _quadrate = [zahl**2 for zahl in range(1, 6)]
    _quadrate
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## marimo-Elemente

    Ein marimo-Element bekommt einen Variablennamen und wird in einer Zelle angezeigt. In einer anderen Zelle liest du seinen aktuellen Wert mit `.value`.

    Wenn du ein Element änderst, aktualisiert marimo Zellen, die auf dieses Element zugreifen.
    """)
    return


@app.cell
def _(mo):
    teilnehmer_slider = mo.ui.slider(
        start=1, stop=10, step=1, value=3, label="Anzahl Teilnehmende"
    )
    teilnehmer_slider
    return (teilnehmer_slider,)


@app.cell
def _(teilnehmer_slider):
    _anzahl = teilnehmer_slider.value
    _preis_pro_person = 4.5
    _gesamtpreis = _anzahl * _preis_pro_person
    f"{_anzahl} Personen: {_gesamtpreis:.2f} Euro"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Dropdown-Auswahl

    Wähle eine Option und lies den ausgewählten Wert in der nächsten Codezelle aus.

    **Ausprobieren:** Ergänze eine weitere Obstsorte in der Optionsliste.
    """)
    return


@app.cell
def _(mo):
    obstwahl = mo.ui.dropdown(
        options=["Apfel", "Banane", "Birne"],
        value="Apfel",
        label="Lieblingsobst",
    )
    obstwahl
    return (obstwahl,)


@app.cell
def _(obstwahl):
    f"Ausgewählt: {obstwahl.value}"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · Eingaben in Zahlen umwandeln

    Ein Texteingabefeld liefert Text. `int(...)` wandelt passende Ziffernfolgen in eine ganze Zahl um. Ungültige Eingaben lösen `ValueError` aus; `try` und `except` fangen diesen Fall ab.

    **Ausprobieren:** Gib eine Zahl und danach Buchstaben in das Feld ein.
    """)
    return


@app.cell
def _(mo):
    textfeld = mo.ui.text(value="18", label="Ganze Zahl eingeben")
    textfeld
    return (textfeld,)


@app.cell
def _(textfeld):
    try:
        _alter = int(textfeld.value)
    except ValueError:
        _meldung = "Bitte eine ganze Zahl eingeben."
    else:
        _meldung = f"Eingabe erkannt: {_alter}"
    _meldung
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · Komplexe Zahlen

    Python verwendet `j` für den imaginären Anteil: `2 + 3j`.

    ```python
    a = complex(3, 4)
    abs(a)  # Betrag der Zahl
    ```

    Dieser Ausblick ist keine Voraussetzung für die nächsten Kurstage.
    """)
    return


@app.cell
def _():
    _a = complex(3, 4)
    (_a, abs(_a), type(_a).__name__)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · Ein Bild mit Pillow zuschneiden

    Pillow kann Bilder öffnen, zuschneiden, drehen und speichern. Das Beispielbild `pictures/wasserfarben.png` liegt im Kursordner.

    Diesen optionalen Abschnitt mit Pillow starten:

    ```sh
    uvx --with "pillow==12.1.1" --from "marimo==0.25.2" marimo edit kurstag_02_teilnehmende.py
    ```

    Füge den folgenden Code in eine neue Codezelle ein:

    ```python
    from PIL import Image

    bild = Image.open("pictures/wasserfarben.png")
    ausschnitt = bild.crop((0, 0, bild.width // 2, bild.height // 2))
    ausschnitt
    ```

    **Vertiefung:** Probiere `bild.resize((200, 200))`, `bild.rotate(90)` und speichere ein Ergebnis unter einem neuen Namen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mein Rückblick

    - Wann verwendest du `//` und wann `%`?
    - Worin unterscheiden sich `if`, `while` und `for`?
    - Was verändert sich, wenn du einen Slider oder ein Dropdown auswählst?
    - Welche Übung möchtest du noch einmal bearbeiten?

    ### Meine Notizen

    **Das habe ich verstanden:** …

    **Das möchte ich noch üben:** …

    **Meine Frage:** …
    """)
    return


if __name__ == "__main__":
    app.run()
