# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo==0.25.2",
# ]
# ///

# Zellenausdrücke und Rückgaben sind Teil des marimo-Notebook-Formats.
# ruff: noqa: B018, PLR1711, UP003, PLR0133

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
    mo.md(r"""
    # Kurstag 1 · Mein Python-Arbeitsheft

    **Python für Daten und KI – Verstehen, ausprobieren, selbst programmieren**

    Dieses Notebook gehört dir: Lies die kurzen Erklärungen, ändere die Beispiele
    und bearbeite die vier Codeübungen. Bei drei Übungen stehen automatische Rückmeldungen direkt darunter; die Namensübung besprechen wir gemeinsam.
    Die Musterlösungen werden im Unterricht besprochen und stehen in der Präsentation.

    ## So arbeitest du mit dem Notebook

    - Starte es mit `uvx --from "marimo==0.25.2" marimo edit kurstag_01_teilnehmende.py`.
    - Bearbeite die sichtbaren Python-Zellen und führe sie mit **Shift+Enter** aus.
    - **Neutral:** noch offen · **Orange:** Hinweis beachten · **Grün:** Prüfung bestanden.
    - `None` ist ein Platzhalter für eine noch offene Antwort. Ersetze ihn durch deinen Code.
    - In Übungszellen die vorgegebenen Antwortzuweisungen beibehalten: Die Prüfung benötigt sie.
    - Bei einem Python-Fehler zuerst die markierte Zelle korrigieren; danach läuft die Prüfung weiter.

    **Zusammenarbeit:** Eine Person tippt, die andere erklärt. Regelmäßig wechseln.
    Erst vorhersagen, dann ausführen, dann das Ergebnis begründen.

    Die Änderungen werden in dieser Datei gespeichert. Lege für einen frischen Start
    eine Kopie an. Zusätzliche Zellen kannst du zwischen den Beispielen einfügen.
    Namen mit führendem Unterstrich sind in unseren Beispielen lokal; andere Namen
    dürfen in marimo jeweils nur in einer Zelle definiert werden.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Drei Werkzeuge, drei Aufgaben

    | Werkzeug | Aufgabe |
    | --- | --- |
    | Python | Führt unseren Programmcode aus. |
    | uv | Verwaltet Python, Pakete und Projekte. |
    | marimo | Verbindet Erklärungen, Code und Ergebnisse. |

    **Heute zählt zuerst:** ein funktionierendes Beispiel selbst verändern.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Python starten

    Im Terminal im Ordner `kurstag_01`:

    ```sh
    uv python install 3.13
    uv run --python 3.13 python
    ```

    Bei `>>>` eingeben: `2 + 3` und mit Enter ausführen.

    Mit `exit()` die Python-Konsole verlassen.

    **Ohne uv?** Gemeinsam an einem eingerichteten Rechner starten.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Variablen geben Werten einen Namen

    ```python
    anzahl_teilnehmende = 10
    ```

    - Links steht der **Name**.
    - Rechts steht der **Wert**.
    - `=` weist dem Namen ein Objekt zu.

    /// note | Definition · Variable
    Eine Variable ist ein Name, der auf ein Objekt verweist.
    Eine Zuweisung kann diesen Namen an ein anderes Objekt binden.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Einen Wert verwenden

    Ändere die Teilnehmerzahl und beobachte das Ergebnis.

    **Frage:** Was passiert bei einer zusätzlichen Anmeldung?

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _anzahl = 10
    _ergebnis = _anzahl + 1
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Welche Namen sind erlaubt?

    /// tip | Regeln für Variablennamen
    - Buchstaben, Ziffern und `_`; die erste Stelle darf keine Ziffer sein.
    - Keine Leerzeichen oder Zeichen wie `-` und `&`.
    - Schlüsselwörter wie `class` sind reserviert.
    - Groß- und Kleinschreibung zählen: `name` und `Name` sind verschieden.
    ///

    Python erlaubt auch viele Unicode-Buchstaben, beispielsweise Umlaute.
    Für unsere Beispiele verwenden wir einfache Namen wie `anzahl_karten`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Gute Namen erklären den Code

    | Wenig aussagekräftig | Verständlich |
    | --- | --- |
    | `x = 10` | `anzahl_teilnehmende = 10` |
    | `b = 2.5` | `preis_pro_karte = 2.5` |

    /// tip | Namenskonventionen
    Verständliche Namen in Kleinbuchstaben mit Unterstrichen (`snake_case`).
    Konstanten schreibt man üblicherweise groß: `MAX_TEILNEHMER = 12`.
    Python verhindert eine spätere Änderung dadurch nicht.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mitmachen · Variablennamen

    Welche Namen sind gültig? Begründe deine Wahl.

    ```python
    vorname       # A
    2_karten      # B
    anzahl_karten # C
    mein-name     # D
    class         # E
    Name          # F
    ```

    **Danach:** Benenne in der folgenden Codezelle die Variablen `a` und `b` verständlich um.

    **Vertiefung:** Sind `name` und `Name` derselbe Name?
    """)
    return


@app.cell
def _():
    # Übung 1: a enthält einen Vornamen, b die Anzahl gebuchter Kurse.
    # Benenne a und b verständlich um – auch in der Ausgabezeile.
    # Die Werte "Frank" und 3 sollen unverändert bleiben.
    a = "Frank"
    b = 3
    (a, b)
    return a, b


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// tip | Gemeinsam besprechen
    - Verrät der erste Name, dass der Wert ein Vorname ist?
    - Verrät der zweite Name, dass der Wert eine Kursanzahl ist?
    - Sind die Namen gültig und in `snake_case` geschrieben?
    - Ist die Ausgabe weiterhin `("Frank", 3)`?

    Verschiedene verständliche Namen sind möglich. Diese Aufgabe wird gemeinsam
    besprochen und nicht automatisch bewertet.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Vier Datentypen für den Einstieg

    /// note | Definition · Datentyp
    Ein Datentyp bestimmt, welche Werte und Operationen ein Objekt unterstützt.
    ///

    | Typ | Bedeutung | Beispiel |
    | --- | --- | --- |
    | `str` | Text | `"Hallo"` |
    | `int` | Ganze Zahl | `10` |
    | `float` | Gleitkommazahl | `2.5` |
    | `bool` | Wahrheitswert | `True` |

    Mit `type(wert)` kannst du den Typ nachschlagen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Text oder Zahl?

    Erst vorhersagen: Was unterscheidet die beiden Ergebnisse?

    Anführungszeichen machen aus einer Ziffernfolge einen Text.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _ergebnis = (2 + 3, "2" + "3")
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Strings verbinden

    `+` verbindet Zeichenketten. Leerzeichen gehören ebenfalls zum Text.

    **Ausprobieren:** Entferne das Leerzeichen.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _vorname = "Ada"
    _begruessung = "Hallo, " + _vorname
    _ergebnis = _begruessung
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Werte in Text einsetzen

    Ein **f-String** setzt Werte an den Stellen mit `{…}` ein.

    `:.2f` zeigt zwei Nachkommastellen.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _karten = 2
    _preis = 3.5
    _ergebnis = f"{_karten} Karten zu je {_preis:.2f} Euro"
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Text über mehrere Zeilen

    Drei Anführungszeichen begrenzen einen mehrzeiligen String.

    In der Ergebnisdarstellung steht `\n` für einen Zeilenumbruch.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _text = "Hallo!\n    Willkommen im Python-Kurs."
    _ergebnis = _text
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ganze Zahlen · int

    Ganze Zahlen gehören zu ℤ: …, −2, −1, 0, 1, 2, …

    Python hat für `int` keine feste Bitbreite. Die Größe ist praktisch durch die verfügbaren Ressourcen begrenzt.

    `10**100` heißt **Googol**.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _ergebnis = (type(3).__name__, 10**100)
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Gleitkommazahlen · float

    Im Python-Code steht ein **Punkt** als Dezimaltrennzeichen.

    Viele Dezimalbrüche lassen sich binär nur näherungsweise darstellen.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _ergebnis = (2.5, 1 / 127, 0.1 + 0.2)
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Mathematische Konstanten

    `math` ist ein Modul der Python-Standardbibliothek.

    Nach `import math` kannst du zum Beispiel π und e verwenden.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    import math as _math

    _ergebnis = (_math.pi, _math.e)
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Datentypen umwandeln

    `int`, `float` und `str` wandeln passende Werte um.

    /// attention | Typumwandlung
    `int(3.9)` schneidet den Nachkommaanteil ab; es rundet nicht.
    `int("Hallo")` würde einen Fehler auslösen.
    ///

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _ergebnis = (int("12"), float("3.14"), str(12), int(3.9))
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Wahr oder falsch · bool

    `==` vergleicht zwei Werte. Das Ergebnis ist `True` oder `False`.

    /// attention | Zuweisen oder vergleichen?
    `=` weist zu. `==` vergleicht zwei Werte.
    ///

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _ergebnis = (3 == 3, 3 == "3", 5 > 2)
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mitmachen · Mein Kursprofil

    **Basis:** Ergänze die vorbereitete Codezelle direkt darunter:

    ```python
    profil_name = "Ada"
    profil_kurse = 2
    profil_preis = 3.5
    ```

    Erzeuge einen f-String mit Name, Kursanzahl und Preis.

    **Vertiefung:** Berechne den Gesamtpreis als Text mit genau zwei Nachkommastellen, ohne Währungsangabe.

    **Zu zweit:** Vor dem Ausführen gegenseitig das Ergebnis erklären.
    """)
    return


@app.cell
def _():
    # Übung 2: Ersetze None durch einen f-String mit den drei Werten.
    _profil_name = "Ada"
    _profil_kurse = 2
    _profil_preis = 3.5
    _profil_text = None
    # Bonus: Gesamtpreis als Text mit genau zwei Nachkommastellen (ohne Euro).
    _profil_gesamtpreis = None
    profil_antwort = (
        _profil_name,
        _profil_kurse,
        _profil_preis,
        _profil_text,
        _profil_gesamtpreis,
    )
    (_profil_text, _profil_gesamtpreis)
    return (profil_antwort,)


@app.cell(hide_code=True)
def _(mo, profil_antwort, pruefhinweis):
    _name, _anzahl, _preis, _text, _gesamt = profil_antwort
    _eingaben_ok = (
        isinstance(_name, str)
        and type(_anzahl) is int
        and type(_preis) in (int, float)
    )
    _text_ok = (
        _eingaben_ok
        and isinstance(_text, str)
        and all(
            _teil in _text
            for _teil in (str(_name), str(_anzahl), f"{_preis:.2f}")
        )
    )
    _gesamt_ok = (
        _eingaben_ok
        and isinstance(_gesamt, str)
        and _gesamt == f"{_anzahl * _preis:.2f}"
    )
    mo.vstack(
        [
            pruefhinweis(
                None if _text is None else _text_ok,
                "Kursprofil",
                "Name, Kursanzahl und Einzelpreis mit zwei Nachkommastellen sind enthalten."
                if _text_ok
                else "Setze Name, Kursanzahl und Einzelpreis in einen Text ein; formatiere den Preis mit :.2f.",
            ),
            pruefhinweis(
                None if _gesamt is None else _gesamt_ok,
                "Bonus · Gesamtpreis",
                "Der Gesamtpreis stimmt und hat zwei Nachkommastellen."
                if _gesamt_ok
                else "Multipliziere Kursanzahl und Einzelpreis. Formatiere das Ergebnis als Text mit :.2f, ohne Währungsangabe.",
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zwischenstopp

    Kannst du …

    - einen Wert mit einem verständlichen Namen versehen?
    - `"3"`, `3` und `3.0` unterscheiden?
    - einen f-String schreiben?
    - `=` und `==` erklären?

    **Als Nächstes:** Mehrere Werte gemeinsam speichern.
    Der folgende Zusatzteil kann auch beim Nacharbeiten bearbeitet werden.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zusatzteil · Listen sammeln Werte

    ```python
    kursnamen = ["Python", "Julia", "Python"]
    ```

    /// tip | Eigenschaften von Listen
    - Die Reihenfolge zählt.
    - Doppelte Werte sind erlaubt.
    - Listen sind veränderbar und können wachsen oder schrumpfen.
    - Elemente dürfen unterschiedliche Typen haben.
    ///

    Eine leere Liste: `[]` oder `list()`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Listen verändern

    /// tip | Listen verändern
    `append` hängt ein Element an.
    `remove` entfernt den ersten passenden Wert.
    `pop()` entfernt das letzte Element und gibt es zurück.
    ///

    Alle Änderungen stehen hier zusammen, damit das Beispiel wiederholbar bleibt.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _kurse = ["Python", "Julia", "Python"]
    _kurse.append("Datenanalyse")
    _kurse.remove("Python")
    _entfernt = _kurse.pop()
    _ergebnis = (_kurse, _entfernt)
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Positionen beginnen bei null

    Bei drei Elementen sind die Indizes `0`, `1` und `2`.

    `-1` bezeichnet das letzte Element; `len` liefert die Länge.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _sprachen = ["Python", "Julia", "TypeScript"]
    _ergebnis = (_sprachen[0], _sprachen[-1], len(_sprachen))
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ausschnitte · Slicing

    /// note | Definition · Slicing
    `folge[start:stop:step]` wählt einen Ausschnitt einer Sequenz.
    ///

    /// attention | Grenzen eines Ausschnitts
    Der Start ist enthalten, der **stop-Wert ist ausgeschlossen**.
    ///
    `[::2]` nimmt jedes zweite Element; `[::-1]` kehrt die Reihenfolge um.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _zahlen = [1, 2, 3, 4, 5, 6]
    _ergebnis = (_zahlen[0:3], _zahlen[::2], _zahlen[::-1])
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mitmachen · Listen und Strings

    **Basis:** Ergänze die Liste in der Codezelle direkt darunter mit drei Lieblingsgerichten.
    Lies das erste und das letzte Gericht aus und ergänze ein viertes.

    **Vertiefung A:** Ist `ANNA` ein Palindrom? Vergleiche das Wort mit seiner Umkehrung.

    **Vertiefung B:** Erzeuge `list(range(1, 101))`.
    Wähle mit Slicing die geraden und die ungeraden Zahlen aus.

    **Tipp:** Slicing funktioniert auch direkt mit Strings.
    """)
    return


@app.cell
def _():
    # Übung 3: Trage drei Lieblingsgerichte in die Liste ein.
    _gerichte = []
    # Lies das erste und letzte der ursprünglichen drei Gerichte aus.
    _erstes = None
    _letztes = None
    # Ergänze erst danach einen append-Aufruf für ein viertes Gericht.
    gerichte_antwort = (_gerichte.copy(), _erstes, _letztes)
    (_gerichte, _erstes, _letztes)
    return (gerichte_antwort,)


@app.cell(hide_code=True)
def _(gerichte_antwort, pruefhinweis):
    _gerichte, _erstes, _letztes = gerichte_antwort
    _offen = _gerichte == [] and _erstes is None and _letztes is None
    _liste_ok = (
        isinstance(_gerichte, list)
        and len(_gerichte) == 4
        and all(
            isinstance(_gericht, str) and bool(_gericht.strip())
            for _gericht in _gerichte
        )
    )
    _richtig = (
        _liste_ok and _erstes == _gerichte[0] and _letztes == _gerichte[-2]
    )
    pruefhinweis(
        None if _offen else _richtig,
        "Lieblingsgerichte",
        "Vier Gerichte und beide Zugriffe auf die ursprüngliche Liste stimmen."
        if _richtig
        else "Beginne mit drei Gerichten, lies das erste und letzte aus und hänge anschließend ein viertes Gericht an.",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zusatzteil · Mengen vermeiden Duplikate

    ```python
    sprachen = {"Python", "Julia", "Python"}
    ```

    /// tip | Eigenschaften von Mengen
    - Jeder unterschiedliche Wert kommt nur einmal vor.
    - Mengen haben keine festgelegte Elementreihenfolge und keine Positionsindizes.
    - Elemente müssen hashbar sein, z. B. Strings und Zahlen; Listen sind es nicht.
    ///

    /// attention | Leere Menge
    `set()` erzeugt eine leere Menge. `{}` erzeugt ein Dictionary.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Mengen ergänzen

    `add` fügt einen Wert hinzu. Erneutes Hinzufügen desselben Werts ändert die Menge nicht.

    Für eine übersichtliche Ausgabe sortieren wir die Werte mit `sorted`.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _sprachen = set()
    _sprachen.add("Python")
    _sprachen.add("Python")
    _sprachen.add("Julia")
    _ergebnis = sorted(_sprachen)
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Wer hat einen Terminkonflikt?

    Volleyball und Fußball finden gleichzeitig statt.

    `&` / `intersection`: in beiden Gruppen.
    `|` / `union`: in mindestens einer Gruppe.

    **Ausprobieren:** Verändere einen Wert und beobachte die Ausgabe.
    """)
    return


@app.cell
def _():
    _volleyball = {"Frank", "Egon", "Markus", "Georg"}
    _fussball = {"Egon", "Franz", "Steffi", "Markus"}
    _ergebnis = (
        sorted(_volleyball & _fussball),
        sorted(_volleyball | _fussball),
    )
    _ergebnis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mitmachen · Mengen erkunden

    **Basis:** Ergänze die vorbereitete Codezelle direkt darunter.
    Finde mit `difference` heraus, wer nur Volleyball spielt.

    **Vertiefung A:** Was liefert `symmetric_difference`?

    **Vertiefung B:** Welche Buchstaben teilen sich `"Hallo Welt"` und `"Weltraum"`?

    **Tipp:** `set("Hallo")` erzeugt eine Menge aus den einzelnen Zeichen.
    Groß- und Kleinschreibung bleiben verschieden; Leerzeichen zählen mit.
    """)
    return


@app.cell
def _():
    # Übung 4: Ersetze None durch passende Mengenoperationen.
    _volleyball = {"Frank", "Egon", "Markus", "Georg"}
    _fussball = {"Egon", "Franz", "Steffi", "Markus"}
    _nur_volleyball = None
    # Bonus: Wer ist in genau einer Gruppe?
    _genau_eine_gruppe = None
    mengen_antwort = (
        _volleyball,
        _fussball,
        _nur_volleyball,
        _genau_eine_gruppe,
    )
    (_nur_volleyball, _genau_eine_gruppe)
    return (mengen_antwort,)


@app.cell(hide_code=True)
def _(mengen_antwort, mo, pruefhinweis):
    _a, _b, _nur, _genau = mengen_antwort
    _nur_ok = isinstance(_nur, set) and _nur == _a - _b
    _genau_ok = isinstance(_genau, set) and _genau == _a ^ _b
    mo.vstack(
        [
            pruefhinweis(
                None if _nur is None else _nur_ok,
                "Nur Volleyball",
                "Die Menge enthält genau die Personen, die nur Volleyball spielen."
                if _nur_ok
                else "Gesucht ist eine Menge: Personen aus Volleyball ohne die Personen aus Fußball. Prüfe difference und die Reihenfolge.",
            ),
            pruefhinweis(
                None if _genau is None else _genau_ok,
                "Bonus · Genau eine Gruppe",
                "Die Menge enthält genau die Personen aus nur einer der beiden Gruppen."
                if _genau_ok
                else "Personen aus beiden Gruppen gehören nicht dazu. Untersuche symmetric_difference.",
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zum Nachschlagen · Weitere Datentypen

    | Kategorie | Python-Typen |
    | --- | --- |
    | Zahlen | `int`, `float`, `complex` |
    | Text und Wahrheitswerte | `str`, `bool` |
    | Sequenzen | `list`, `tuple`, `range` |
    | Schlüssel-Wert-Zuordnung | `dict` |
    | Mengen | `set`, `frozenset` |
    | Binärdaten | `bytes`, `bytearray`, `memoryview` |
    | Fehlender Wert | `None` (Typ: `NoneType`) |

    Heute musst du diese Typen noch nicht alle kennen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mein Rückblick

    - Was unterscheidet `"3"`, `3` und `3.0`?
    - Was ist der Unterschied zwischen `=` und `==`?
    - Welche Übung konnte ich selbstständig lösen?
    - Welche Frage möchte ich beim nächsten Kurstag stellen?

    Trage deine Notizen in der folgenden Markdown-Zelle ein.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Meine Notizen

    **Das habe ich verstanden:** …

    **Das möchte ich noch üben:** …

    **Meine Frage:** …
    """)
    return


if __name__ == "__main__":
    app.run()
