# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo==0.25.2",
# ]
# ///

# Die Rückgaben gehören zum marimo-Format; Typabfrage und Vergleiche sind Lehrbeispiele.
# ruff: noqa: PLR1711, UP003, PLR0133

import marimo

__generated_with = "0.25.2"
app = marimo.App(
    width="medium",
    layout_file="layouts/kurstag_01_folien.slides.json",
    css_file="layouts/folien.css",
)


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
    import pprint as _pprint

    def beispiel(titel, erklaerung, code, ergebnis):
        inhalt = mo.vstack(
            [
                mo.md(f"## {titel}"),
                mo.hstack(
                    [
                        mo.md(erklaerung),
                        mo.vstack(
                            [
                                mo.md(f"```python\n{code}\n```"),
                                mo.md(
                                    f"**Ergebnis:**\n\n```text\n{_pprint.pformat(ergebnis, width=72, compact=True, sort_dicts=False)}\n```"
                                ),
                            ]
                        ),
                    ],
                    widths=[2, 3],
                    gap=2,
                    align="start",
                ),
            ],
            gap=1,
        )

        return mo.Html(
            "<style>"
            ".vhs-beispiel * { min-width: 0; }"
            ".vhs-beispiel pre {"
            " width: 100%; box-sizing: border-box; max-height: none !important;"
            " font-size: 0.78em !important; line-height: 1.35 !important;"
            " padding: 0.65em !important; overflow: visible !important; }"
            ".vhs-beispiel pre, .vhs-beispiel pre * {"
            " white-space: pre-wrap !important; overflow-wrap: anywhere !important; }"
            "</style>"
            f'<div class="vhs-beispiel">{inhalt.text}</div>'
        )

    return (beispiel,)


@app.cell(hide_code=True)
def _(mo):
    from base64 import b64encode as _b64encode
    from pathlib import Path as _Path

    _logo_data = _b64encode(_Path("public/vhs-dresden-logo.png").read_bytes()).decode("ascii")
    _cover_html = """
    <style>
      .vhs-kursstart { box-sizing: border-box; display: block; min-height: 440px; padding: 2.2rem 2.5rem; overflow: hidden; position: relative; border: 1px solid #d7e3ef; border-left: 10px solid #082f5b; border-radius: 24px; background: radial-gradient(circle at 92% 8%, rgba(255, 184, 40, .22) 0 15%, transparent 15.5%), linear-gradient(125deg, #fbfdff 0%, #f0f5fb 58%, #e4eef7 100%); color: #102f51; font-family: system-ui, sans-serif; }
      .vhs-kursstart-copy { position: relative; z-index: 1; max-width: calc(100% - 270px); }
      .vhs-kursstart-logo { display: inline-block; margin-bottom: 1.5rem; padding: .5rem .8rem; border-radius: 12px; background: #fff; box-shadow: 0 6px 20px rgba(7, 40, 74, .08); }
      .vhs-kursstart-logo img { display: block; width: min(290px, 62vw); height: auto; }
      .vhs-kursstart-series { margin: 0 0 .4rem; color: #147e9e; font-size: .86rem; font-weight: 800; letter-spacing: .16em; text-transform: uppercase; }
      .vhs-kursstart-title { margin: 0; color: #082f5b; font-size: clamp(2.1rem, 4.3vw, 3.6rem); font-weight: 800; line-height: 1.05; }
      .vhs-kursstart-title span { display: block; margin-top: .25rem; color: #17668e; font-size: .68em; }
      .vhs-kursstart-summary { max-width: 39rem; margin: 1rem 0 1.25rem; color: #38526d; font-size: 1.08rem; line-height: 1.5; }
      .vhs-kursstart-motto { display: inline-block; padding: .55rem .85rem; border: 1px solid #cfdeeb; border-radius: 999px; background: rgba(255,255,255,.78); color: #173a5d; font-size: .9rem; font-weight: 650; }
      .vhs-kursstart-motto b { padding: 0 .35rem; color: #ed6a32; }
      .vhs-kursstart-art { position: absolute; top: 50%; right: 4%; transform: translateY(-50%); display: grid; place-items: center; width: 220px; height: 220px; border: 1px solid rgba(8,47,91,.12); border-radius: 50%; background: rgba(255,255,255,.48); box-shadow: inset 0 0 0 15px rgba(255,255,255,.28); }
      .vhs-kursstart-core { display: grid; place-items: center; width: 134px; height: 134px; border-radius: 50%; background: #082f5b; box-shadow: 0 16px 30px rgba(8,47,91,.2); color: white; font-size: 3rem; font-weight: 850; letter-spacing: -.08em; }
      .vhs-kursstart-dot { position: absolute; display: block; width: 34px; height: 34px; border-radius: 50%; box-shadow: 0 4px 14px rgba(8,47,91,.12); }
      .vhs-kursstart-dot.one { top: 10px; left: 91px; width: 29px; height: 29px; background: #f6b627; }
      .vhs-kursstart-dot.two { top: 72px; right: 5px; background: #e84b3c; }
      .vhs-kursstart-dot.three { right: 31px; bottom: 17px; width: 27px; height: 27px; background: #39a5d6; }
      .vhs-kursstart-dot.four { bottom: 31px; left: 12px; width: 39px; height: 39px; background: #ef6d32; }
      .vhs-kursstart-dot.five { top: 50px; left: 20px; width: 22px; height: 22px; background: #318fc0; }
      @media (max-width: 680px) { .vhs-kursstart { min-height: 390px; padding: 1.5rem; } .vhs-kursstart-copy { max-width: none; } .vhs-kursstart-art { display: none; } }
    </style>
    <section class="vhs-kursstart">
      <div class="vhs-kursstart-copy">
        <div class="vhs-kursstart-logo"><img src="data:image/png;base64,__VHS_LOGO__" alt="Volkshochschule Dresden e.V."></div>
        <p class="vhs-kursstart-series">Python für Daten und KI</p>
        <h1 class="vhs-kursstart-title">Kurstag 1<span>Erste Schritte</span></h1>
        <p class="vhs-kursstart-summary">Python starten, Werte benennen und mit Daten experimentieren.</p>
        <div class="vhs-kursstart-motto">Verstehen <b>·</b> Ausprobieren <b>·</b> Gemeinsam lernen</div>
      </div>
      <div class="vhs-kursstart-art" aria-hidden="true"><div class="vhs-kursstart-core">Py</div><i class="vhs-kursstart-dot one"></i><i class="vhs-kursstart-dot two"></i><i class="vhs-kursstart-dot three"></i><i class="vhs-kursstart-dot four"></i><i class="vhs-kursstart-dot five"></i></div>
    </section>
    """
    mo.Html(_cover_html.replace("__VHS_LOGO__", _logo_data))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Unser Weg heute

    1. **Starten:** Python, uv und marimo kennenlernen.
    2. **Benennen:** Werte in Variablen speichern.
    3. **Unterscheiden:** Text, Zahlen und Wahrheitswerte.
    4. **Anwenden:** Ein kleines Kursprofil erstellen.

    **Zusatzteil nach Lerntempo:** Listen, Ausschnitte und Mengen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Gemeinsam am Rechner

    - Zu zweit: Eine Person tippt, die andere erklärt und prüft.
    - Nach jeder Aufgabe die Rollen wechseln.
    - Erst vermuten, dann ausführen, dann das Ergebnis erklären.

    **Codeübungen:** Auf der nächsten Folie `C` drücken, Code ergänzen und
    mit `Shift+Enter` ausführen. `None` bedeutet hier: noch offen.
    Nutze dafür `marimo edit`, siehe Startanleitung.

    **Falls die Software fehlt:** An einem funktionierenden Rechner mitarbeiten.

    **Schon Erfahrung?** Die Vertiefung bearbeiten und Fragen stellen, die anderen beim Verstehen helfen.
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
    ## Das Notebook öffnen

    Im Terminal im Ordner `kurstag_01`:

    ```sh
    marimo run kurstag_01_folien.py
    ```

    Zum Bearbeiten und Live-Coding:

    ```sh
    marimo edit kurstag_01_folien.py
    ```

    **marimo führt abhängige Zellen erneut aus**, wenn sich ein verwendeter Wert ändert.
    Jeden Namen deshalb nur in einer Zelle definieren.
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


@app.cell
def _(mo):
    # Ändere die Zahl und führe die Zelle erneut aus.
    anzahl_teilnehmende = 11
    anzahl_nach_anmeldung = anzahl_teilnehmende + 1

    mo.md(
        "## Was passiert bei einer Anmeldung?\n\n"
        "Die erste Zeile speichert die aktuelle Zahl. Die zweite Zeile "
        "berechnet den Wert nach einer weiteren Anmeldung.\n\n"
        f"**Nach einer Anmeldung:** {anzahl_nach_anmeldung} Teilnehmende"
    )
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// tip | Gemeinsam besprechen
    - Verrät der erste Name, dass der Wert ein Vorname ist?
    - Verrät der zweite Name, dass der Wert eine Kursanzahl ist?
    - Sind die Namen gültig und in `snake_case` geschrieben?
    - Ist die Ausgabe weiterhin `("Frank", 3)`?

    Verschiedene verständliche Namen sind möglich.
    ///
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


@app.cell
def _():
    # Übung 1: a enthält einen Vornamen, b die Anzahl gebuchter Kurse.
    # Benenne a und b verständlich um – auch in der Ausgabezeile.
    # Die Werte "Frank" und 3 sollen unverändert bleiben.
    a = "Frank"
    b = 3
    (a, b)  # noqa: B018
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Auflösung · Variablennamen

    <strong>Gültig:</strong> A, C und F.

    <strong>Ungültig:</strong>
    - B beginnt mit einer Ziffer.
    - D enthält ein Minuszeichen; Python liest es als Subtraktion.
    - E ist ein Schlüsselwort.

    `name` und `Name` sind zwei unterschiedliche Namen.

    **Jetzt selbst:** Wähle einen verständlichen Namen für die Anzahl freier Kursplätze.
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
def _(beispiel):
    _ergebnis = (2 + 3, "2" + "3")
    beispiel(
        "Text oder Zahl?",
        "Erst vorhersagen: Was unterscheidet die beiden Ergebnisse?\n\nAnführungszeichen machen aus einer Ziffernfolge einen Text.",
        '_ergebnis = (2 + 3, "2" + "3")',
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(beispiel):
    _vorname = "Ada"
    _begruessung = "Hallo, " + _vorname
    _ergebnis = _begruessung
    beispiel(
        "Strings verbinden",
        "`+` verbindet Zeichenketten. Leerzeichen gehören ebenfalls zum Text.\n\n**Ausprobieren:** Entferne das Leerzeichen.",
        '_vorname = "Ada"\n_begruessung = "Hallo, " + _vorname\n_ergebnis = _begruessung',
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(beispiel):
    _karten = 2
    _preis = 3.5
    _ergebnis = f"{_karten} Karten zu je {_preis:.2f} Euro"
    beispiel(
        "Werte in Text einsetzen",
        "Ein **f-String** setzt Werte an den Stellen mit `{…}` ein.\n\n`:.2f` zeigt zwei Nachkommastellen.",
        '_karten = 2\n_preis = 3.5\n_ergebnis = f"{_karten} Karten zu je {_preis:.2f} Euro"',
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(beispiel):
    _text = """Hallo!
    Willkommen im Python-Kurs."""
    _ergebnis = _text
    beispiel(
        "Text über mehrere Zeilen",
        "Drei Anführungszeichen begrenzen einen mehrzeiligen String.\n\nIn der Ergebnisdarstellung steht `\\n` für einen Zeilenumbruch.",
        '_text = """Hallo!\nWillkommen im Python-Kurs."""\n_ergebnis = _text',
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(beispiel):
    _ergebnis = (type(3).__name__, 10**100)
    beispiel(
        "Ganze Zahlen · int",
        "Ganze Zahlen gehören zu ℤ: …, −2, −1, 0, 1, 2, …\n\nPython hat für `int` keine feste Bitbreite. Die Größe ist praktisch durch die verfügbaren Ressourcen begrenzt.\n\n`10**100` heißt **Googol**.",
        "_ergebnis = (type(3).__name__, 10**100)",
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(beispiel):
    _ergebnis = (2.5, 1 / 127, 0.1 + 0.2)
    beispiel(
        "Gleitkommazahlen · float",
        "Im Python-Code steht ein **Punkt** als Dezimaltrennzeichen.\n\nViele Dezimalbrüche lassen sich binär nur näherungsweise darstellen.",
        "_ergebnis = (2.5, 1 / 127, 0.1 + 0.2)",
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(beispiel):
    import math as _math

    _ergebnis = (_math.pi, _math.e)
    beispiel(
        "Mathematische Konstanten",
        "`math` ist ein Modul der Python-Standardbibliothek.\n\nNach `import math` kannst du zum Beispiel π und e verwenden.",
        "import math as _math\n_ergebnis = (_math.pi, _math.e)",
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(beispiel):
    _ergebnis = (int("12"), float("3.14"), str(12), int(3.9))
    beispiel(
        "Datentypen umwandeln",
        '`int`, `float` und `str` wandeln passende Werte um.\n\n/// attention | Typumwandlung\n`int(3.9)` schneidet den Nachkommaanteil ab; es rundet nicht.\n`int("Hallo")` würde einen Fehler auslösen.\n///',
        '_ergebnis = (int("12"), float("3.14"), str(12), int(3.9))',
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(beispiel):
    _ergebnis = (3 == 3, 3 == "3", 5 > 2)
    beispiel(
        "Wahr oder falsch · bool",
        "`==` vergleicht zwei Werte. Das Ergebnis ist `True` oder `False`.\n\n/// attention | Zuweisen oder vergleichen?\n`=` weist zu. `==` vergleicht zwei Werte.\n///",
        '_ergebnis = (3 == 3, 3 == "3", 5 > 2)',
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mitmachen · Mein Kursprofil

    **Basis:** Ergänze die vorbereitete Codezelle auf der nächsten Folie:

    ```python
    profil_name = "Ada"
    profil_kurse = 2
    profil_preis = 3.5
    ```

    Erzeuge einen f-String mit Name, Kursanzahl und Preis.

    **Vertiefung:** Berechne den Gesamtpreis und zeige ihn mit zwei Nachkommastellen.

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
    (_profil_text, _profil_gesamtpreis)  # noqa: B018
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
def _(beispiel):
    _name = "Ada"
    _kurse = 2
    _preis = 3.5
    _ergebnis = (
        f"{_name}: {_kurse} Kurse, insgesamt {_kurse * _preis:.2f} Euro"
    )
    beispiel(
        "Eine mögliche Lösung",
        "Vergleiche mit deiner Lösung. Andere verständliche Namen und Formulierungen sind ebenfalls möglich.",
        '_name = "Ada"\n_kurse = 2\n_preis = 3.5\n_ergebnis = f"{_name}: {_kurse} Kurse, insgesamt {_kurse * _preis:.2f} Euro"',
        _ergebnis,
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
def _(beispiel):
    _kurse = ["Python", "Julia", "Python"]
    _kurse.append("Datenanalyse")
    _kurse.remove("Python")
    _entfernt = _kurse.pop()
    _ergebnis = (_kurse, _entfernt)
    beispiel(
        "Listen verändern",
        "/// tip | Listen verändern\n`append` hängt ein Element an.\n`remove` entfernt den ersten passenden Wert.\n`pop()` entfernt das letzte Element und gibt es zurück.\n///\n\nAlle Änderungen stehen hier zusammen, damit das Beispiel wiederholbar bleibt.",
        '_kurse = ["Python", "Julia", "Python"]\n_kurse.append("Datenanalyse")\n_kurse.remove("Python")\n_entfernt = _kurse.pop()\n_ergebnis = (_kurse, _entfernt)',
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(beispiel):
    _sprachen = ["Python", "Julia", "TypeScript"]
    _ergebnis = (_sprachen[0], _sprachen[-1], len(_sprachen))
    beispiel(
        "Positionen beginnen bei null",
        "Bei drei Elementen sind die Indizes `0`, `1` und `2`.\n\n`-1` bezeichnet das letzte Element; `len` liefert die Länge.",
        '_sprachen = ["Python", "Julia", "TypeScript"]\n_ergebnis = (_sprachen[0], _sprachen[-1], len(_sprachen))',
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(beispiel):
    _zahlen = [1, 2, 3, 4, 5, 6]
    _ergebnis = (_zahlen[0:3], _zahlen[::2], _zahlen[::-1])
    beispiel(
        "Ausschnitte · Slicing",
        "/// note | Definition · Slicing\n`folge[start:stop:step]` wählt einen Ausschnitt einer Sequenz.\n///\n\n/// attention | Grenzen eines Ausschnitts\nDer Start ist enthalten, der **stop-Wert ist ausgeschlossen**.\n///\n`[::2]` nimmt jedes zweite Element; `[::-1]` kehrt die Reihenfolge um.",
        "_zahlen = [1, 2, 3, 4, 5, 6]\n_ergebnis = (_zahlen[0:3], _zahlen[::2], _zahlen[::-1])",
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mitmachen · Listen und Strings

    **Basis:** Ergänze die Liste in der Codezelle auf der nächsten Folie mit drei Lieblingsgerichten.
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
    (_gerichte, _erstes, _letztes)  # noqa: B018
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
def _(beispiel):
    _wort = "ANNA"
    _zahlen = list(range(1, 101))
    _ungerade = _zahlen[::2]
    _gerade = _zahlen[1::2]
    _ergebnis = (_wort == _wort[::-1], _ungerade[:5], _gerade[:5])
    beispiel(
        "Lösungen · Palindrom und Zahlen",
        "`range(1, 101)` erzeugt Zahlen von 1 bis einschließlich 100.\n\nDie ungeraden Zahlen beginnen bei Index 0, die geraden bei Index 1.\nHier zeigen wir jeweils nur die ersten fünf.",
        '_wort = "ANNA"\n_zahlen = list(range(1, 101))\n_ungerade = _zahlen[::2]\n_gerade = _zahlen[1::2]\n_ergebnis = (_wort == _wort[::-1], _ungerade[:5], _gerade[:5])',
        _ergebnis,
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
def _(beispiel):
    _sprachen = set()
    _sprachen.add("Python")
    _sprachen.add("Python")
    _sprachen.add("Julia")
    _ergebnis = sorted(_sprachen)
    beispiel(
        "Mengen ergänzen",
        "`add` fügt einen Wert hinzu. Erneutes Hinzufügen desselben Werts ändert die Menge nicht.\n\nFür eine übersichtliche Ausgabe sortieren wir die Werte mit `sorted`.",
        '_sprachen = set()\n_sprachen.add("Python")\n_sprachen.add("Python")\n_sprachen.add("Julia")\n_ergebnis = sorted(_sprachen)',
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(beispiel):
    _volleyball = {"Frank", "Egon", "Markus", "Georg"}
    _fussball = {"Egon", "Franz", "Steffi", "Markus"}
    _ergebnis = (
        sorted(_volleyball & _fussball),
        sorted(_volleyball | _fussball),
    )
    beispiel(
        "Wer hat einen Terminkonflikt?",
        "Volleyball und Fußball finden gleichzeitig statt.\n\n`&` / `intersection`: in beiden Gruppen.\n`|` / `union`: in mindestens einer Gruppe.",
        '_volleyball = {"Frank", "Egon", "Markus", "Georg"}\n_fussball = {"Egon", "Franz", "Steffi", "Markus"}\n_ergebnis = (sorted(_volleyball & _fussball), sorted(_volleyball | _fussball))',
        _ergebnis,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mitmachen · Mengen erkunden

    **Basis:** Ergänze die vorbereitete Codezelle auf der nächsten Folie.
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
    (_nur_volleyball, _genau_eine_gruppe)  # noqa: B018
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
def _(beispiel):
    _a = {"Frank", "Egon", "Markus", "Georg"}
    _b = {"Egon", "Franz", "Steffi", "Markus"}
    _gemeinsam = set("Hallo Welt") & set("Weltraum")
    _ergebnis = (sorted(_a - _b), sorted(_a ^ _b), sorted(_gemeinsam))
    beispiel(
        "Lösungen · Mengen vergleichen",
        "`A - B`: nur in A.\n`A ^ B`: in genau einer der beiden Mengen.\n\nDie Buchstaben vergleichen wir hier einschließlich Groß- und Kleinschreibung.",
        '_a = {"Frank", "Egon", "Markus", "Georg"}\n_b = {"Egon", "Franz", "Steffi", "Markus"}\n_gemeinsam = set("Hallo Welt") & set("Weltraum")\n_ergebnis = (sorted(_a - _b), sorted(_a ^ _b), sorted(_gemeinsam))',
        _ergebnis,
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
    ## Was bleibt von heute?

    **Variablen benennen Werte. Datentypen bestimmen die Möglichkeiten.**

    - Text zusammensetzen: `"Hallo " + "Welt"`
    - Werte einsetzen: `f"Hallo {name}"`
    - Typen prüfen und umwandeln: `type`, `int`, `float`, `str`
    - Zusatz: Listen ordnen Werte; Mengen sammeln unterschiedliche Werte.

    **Abschlussrunde:** Ein Aha-Erlebnis und eine offene Frage.

    **Nächstes Mal:** Mit Daten und Operationen weiterarbeiten.
    """)
    return


if __name__ == "__main__":
    app.run()
