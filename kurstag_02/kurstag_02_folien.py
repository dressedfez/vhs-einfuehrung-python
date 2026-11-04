# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo==0.25.2",
# ]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App(
    width="medium",
    layout_file="layouts/kurstag_02_folien.slides.json",
)


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    def pruefhinweis(status, aufgabe, hinweis):
        if status is None:
            return mo.callout(mo.md(f"**Noch offen · {aufgabe}**\n\n{hinweis}"), kind="neutral")
        if status:
            return mo.callout(mo.md(f"**✓ Richtig · {aufgabe}**\n\n{hinweis}"), kind="success")
        return mo.callout(mo.md(f"**Noch nicht ganz · {aufgabe}**\n\n{hinweis}"), kind="warn")

    return


@app.cell(hide_code=True)
def _(mo):
    import pprint as _pprint

    def beispiel(titel, erklaerung, code, ergebnis):
        ausgabe = _pprint.pformat(
            ergebnis, width=88, compact=True, sort_dicts=False
        )
        return mo.md(
            f"## {titel}\n\n"
            f"{erklaerung}\n\n"
            f"**Python-Code**\n\n"
            f"```python\n{code}\n```\n\n"
            f"**Ergebnis**\n\n"
            f"```text\n{ausgabe}\n```"
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
        <h1 class="vhs-kursstart-title">Kurstag 2<span>Rechnen, entscheiden, wiederholen</span></h1>
        <p class="vhs-kursstart-summary">Programme berechnen Werte, unterscheiden Fälle und wiederholen Arbeitsschritte.</p>
        <div class="vhs-kursstart-motto">Verstehen <b>·</b> Ausprobieren <b>·</b> Gemeinsam lernen</div>
      </div>
      <div class="vhs-kursstart-art" aria-hidden="true"><div class="vhs-kursstart-core">Py</div><i class="vhs-kursstart-dot one"></i><i class="vhs-kursstart-dot two"></i><i class="vhs-kursstart-dot three"></i><i class="vhs-kursstart-dot four"></i><i class="vhs-kursstart-dot five"></i></div>
    </section>
    """
    mo.Html(_cover_html.replace("__VHS_LOGO__", _logo_data))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Unser Weg heute

    1. **Rechnen:** Operatoren und Reihenfolge verstehen.
    2. **Entscheiden:** Bedingungen mit `if`, `elif` und `else` schreiben.
    3. **Wiederholen:** `while` und `for` passend einsetzen.
    4. **Interaktiv werden:** Eingaben mit marimo-Elementen verknüpfen.

    **Zusatzteil:** Schleifensteuerung, List Comprehensions und komplexe Zahlen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Gemeinsam am Rechner

    - Zu zweit: Eine Person tippt, die andere erklärt und prüft.
    - Nach jeder Aufgabe die Rollen wechseln.
    - Erst vermuten, dann ausführen, dann das Ergebnis erklären.
    - Bei einem Fehler: die erste rote Zelle lesen und dort beginnen.

    **Schon Erfahrung?** Bearbeite den Zusatzteil und unterstütze andere beim Begründen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Das Notebook öffnen

    Im Terminal im Ordner `kurstag_02`:

    ```sh
    uv run --script kurstag_02_folien.py
    ```

    Für die Folienansicht mit editierbarem Python-Code:

    ```sh
    uvx --from "marimo==0.25.2" marimo edit kurstag_02_folien.py
    ```

    Mit den Pfeiltasten blättern. **C** öffnet den Code der aktuellen Zelle; **Shift+Enter** führt sie aus.
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

    Python wertet Zahlen-Ausdrücke nach festen Regeln aus.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Ganze Zahlen und Gleitkommazahlen', 'Ganze Zahlen haben den Typ `int`. Zahlen mit Dezimalpunkt haben den Typ `float`.\n\nBei einer Rechnung mit `int` und `float` ist das Ergebnis in der Regel ein `float`.', 'anzahl = 4\npreis = 2.5\nergebnis = (anzahl * preis, type(anzahl * preis).__name__)', (10.0, 'float'))
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Addition, Subtraktion und Multiplikation', 'Die Operatoren `+`, `-` und `*` rechnen mit Zahlen.\n\n`+` und `*` funktionieren außerdem mit Text: Sie verbinden oder wiederholen Zeichenketten.', 'ergebnis = (8 + 3, 8 - 3, 8 * 3, "ha" * 3)', (11, 5, 24, 'hahaha'))
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Division mit `/`', 'Der Operator `/` liefert in Python immer einen Wert vom Typ `float`, auch wenn die Division ohne Rest aufgeht.', 'ergebnis = (6 / 2, 7 / 2, type(6 / 2).__name__)', (3.0, 3.5, 'float'))
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Ganzzahldivision und Rest', '`//` liefert den ganzzahligen Quotienten. `%` liefert den Rest.\n\nZusammen beantworten sie zum Beispiel: Wie viele ganze Portionen passen, und wie viel bleibt übrig?', 'ergebnis = (17 // 5, 17 % 5)', (3, 2))
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Klammern machen die Reihenfolge sichtbar', 'Potenzieren kommt vor Multiplikation und Division; diese kommen vor Addition und Subtraktion.\n\nKlammern zeigen die gewünschte Reihenfolge ausdrücklich.', 'ergebnis = (2 + 3 * 4, (2 + 3) * 4, 2 ** 3 ** 2)', (14, 20, 512))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Gleitkommazahlen sind Näherungen

    Viele Dezimalzahlen lassen sich im Binärsystem nur annähernd darstellen.

    /// attention | Bei Geldbeträgen aufpassen
    `0.1 + 0.2` ergibt intern nicht exakt `0.3`. Für erste Beispiele reicht `float`; bei Geldberechnungen muss man die Darstellung bewusst wählen.
    ///

    Zum Einstieg: Ergebnis ansehen und nicht auf exakte Gleichheit mit einem Dezimalwert vertrauen.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Rundungsabweichung beobachten', 'Der sichtbare Dezimalwert ist eine Näherung. `round` kann die Ausgabe für eine Anzeige runden, ändert aber nicht die grundsätzliche Arbeitsweise von `float`.', 'ergebnis = (0.1 + 0.2, round(0.1 + 0.2, 2))', (0.30000000000000004, 0.3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mitmachen · Portionen aufteilen

    17 Kekse werden gleichmäßig auf 5 Personen verteilt.

    - Wie viele Kekse erhält jede Person?
    - Wie viele bleiben übrig?
    - Welche Operatoren passen zu den beiden Fragen?

    **Danach:** Ändere die Werte und prüfe, ob Quotient und Rest zusammen wieder 17 ergeben.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Eine mögliche Lösung', '`//` zählt ganze Portionen. `%` berechnet den Rest.\n\nDie Probe lautet: `5 * 3 + 2 == 17`.', 'kekse = 17\npersonen = 5\npro_person = kekse // personen\nuebrig = kekse % personen\n(pro_person, uebrig, personen * pro_person + uebrig)', (3, 2, 17))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Vergleiche ergeben Wahrheitswerte

    Ein Vergleich hat das Ergebnis `True` oder `False`.

    | Operator | Bedeutung |
    | --- | --- |
    | `==` | gleich |
    | `!=` | ungleich |
    | `<`, `<=` | kleiner, kleiner oder gleich |
    | `>`, `>=` | größer, größer oder gleich |

    `=` weist einen Wert zu. `==` vergleicht zwei Werte.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Vergleiche lesen', 'Vergleiche können Zahlen, Text oder Variablen prüfen. Unterschiedliche Datentypen sind nicht automatisch gleich.', 'ergebnis = (5 == 5, 5 != 3, 18 <= 18, 5 == "5")', (True, True, True, False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Bedingungen verbinden

    - `and`: Beide Teilbedingungen müssen wahr sein.
    - `or`: Mindestens eine Teilbedingung muss wahr sein.
    - `not`: Kehrt einen Wahrheitswert um.

    /// tip | Lesbare Bedingungen
    Setze bei Bedarf Klammern und schreibe Bedingungen so, dass man die Fälle direkt erkennen kann.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Bedingungen kombinieren', 'Eine Person ist volljährig, wenn sie mindestens 18 Jahre alt ist. Ein Rabatt gilt für Kinder oder Seniorinnen und Senioren.', 'alter = 67\nvolljaehrig = alter >= 18\nrabatt = alter < 18 or alter >= 65\n(volljaehrig, rabatt, not volljaehrig)', (True, True, False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Verzweigungen mit `if`, `elif` und `else`

    ```python
    if bedingung_1:
        # erster Fall
    elif bedingung_2:
        # weiterer Fall
    else:
        # übrige Fälle
    ```

    `elif` und `else` sind optional. Die Einrückung legt fest, welcher Code zu einem Zweig gehört.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Ein Eintrittspreis', 'Die Zweige werden von oben nach unten geprüft. Der erste passende Zweig wird ausgeführt.', 'alter = 17\nif alter < 6:\n    preis = "Eintritt frei"\nelif alter < 18:\n    preis = "Kinderpreis: 5 €"\nelif alter < 65:\n    preis = "Normalpreis: 10 €"\nelse:\n    preis = "Seniorenpreis: 6 €"\npreis', 'Kinderpreis: 5 €')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Bedingungen in der richtigen Reihenfolge

    Prüfe Grenzwerte bewusst:

    - genau 6 Jahre
    - genau 18 Jahre
    - genau 65 Jahre

    Wenn breite Fälle zuerst geprüft werden, können spätere Zweige unerreichbar werden. Formuliere jeden Zweig als klar abgegrenzten Fall.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel(
        'Vergleichsketten vereinfachen',
        'Eine verkettete Bedingung prüft beide Grenzen. `18 <= alter < 65` bedeutet: mindestens 18 und kleiner als 65. Die vier Bedingungen decken alle Altersgruppen ab.',
        'alter = 30\nergebnis = {\n    "unter 6": alter < 6,\n    "6 bis 17": 6 <= alter < 18,\n    "18 bis 64": 18 <= alter < 65,\n    "ab 65": alter >= 65,\n}\nergebnis',
        {'unter 6': False, '6 bis 17': False, '18 bis 64': True, 'ab 65': False},
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Kurzform für zwei Werte

    Für eine einfache Auswahl zwischen zwei Werten gibt es den bedingten Ausdruck:

    ```python
    wert_wenn_wahr if bedingung else wert_wenn_falsch
    ```

    Verwende ihn für kurze Zuweisungen. Mehrere Fälle bleiben mit `if` und `elif` meist leichter zu lesen.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Eine kurze Auswahl', 'Der Ausdruck liefert einen Wert. Er ersetzt keine längere Verzweigung mit mehreren Anweisungen.', 'alter = 16\nstatus = "Jugendpreis" if alter < 18 else "Normalpreis"\nstatus', 'Jugendpreis')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Interaktive Zahleneingabe

    Ein marimo-Element stellt einen Wert bereit. Zellen, die das Element verwenden, aktualisieren sich bei einer Änderung.

    **So läuft es ab:** Du änderst das Alter, eine andere Zelle liest den Wert mit `.value` aus und prüft anschließend die Bedingung `alter < 18`.

    Probiere zuerst **16**, dann **18**. So siehst du, dass die Grenze selbst schon zum Vollpreis führt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    alter_eingabe = mo.ui.number(start=1, stop=99, step=1, value=16, label="Alter in Jahren")
    return (alter_eingabe,)


@app.cell
def _(alter_eingabe, mo):
    alter = alter_eingabe.value
    if alter < 18:
        meldung = "Jugendpreis"
    else:
        meldung = "Vollpreis"
    mo.vstack([
        mo.md("""
        ## Alter eingeben

        Stelle eine Zahl zwischen **1 und 99** ein. Ändere den Wert über die Pfeile oder tippe ihn direkt ein.
        """),
        alter_eingabe,
        mo.md(f"""
        ### Ergebnis: {meldung}

        Eingegebenes Alter: **{alter} Jahre**

        Die Regel lautet: `alter < 18`. Bei **18** ist sie bereits falsch, deshalb gilt dann der Vollpreis.
        """),
    ]).style({"max-width": "900px", "margin": "0 auto"})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mitmachen · Temperatur prüfen

    Ordne eine Temperatur einer Nachricht zu:

    - über 30 °C: `Es ist heiß!`
    - 20 bis 30 °C einschließlich: `Angenehmes Wetter.`
    - unter 20 °C: `Ziemlich kühl heute.`

    Teste danach auch die Grenzwerte 20 °C und 30 °C.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Eine mögliche Lösung', 'Die mittlere Bedingung schließt beide Grenzen ein. Weil die erste Bedingung bereits `> 30` abdeckt, reicht danach `>= 20`.', 'temperatur = 25\nif temperatur > 30:\n    nachricht = "Es ist heiß!"\nelif temperatur >= 20:\n    nachricht = "Angenehmes Wetter."\nelse:\n    nachricht = "Ziemlich kühl heute."\nnachricht', 'Angenehmes Wetter.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Schleifen wiederholen Schritte

    Eine Schleife führt einen eingerückten Block mehrfach aus.

    - `while`: wiederholen, solange eine Bedingung wahr ist.
    - `for`: nacheinander Elemente einer Folge verarbeiten.

    Wähle die Schleifenart nach der Frage: **Wie lange?** oder **Für jedes Element?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `while`-Schleife

    ```python
    while bedingung:
        # wiederholter Code
    ```

    Bei jedem Durchlauf muss sich etwas ändern, das die Bedingung beeinflusst. Sonst endet die Schleife möglicherweise nie.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Einen Zähler erhöhen', 'Der Zähler wird in jedem Durchlauf erhöht. Sobald `zaehler < 4` falsch wird, endet die Schleife.', 'zaehler = 1\nfolge = []\nwhile zaehler < 4:\n    folge.append(zaehler)\n    zaehler += 1\nfolge', [1, 2, 3])
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel(
        'Lösung · Countdown',
        'Hänge vor dem Verringern des Zählers seinen aktuellen Wert an die Liste an.',
        'zahl = 5\nfolge = []\nwhile zahl > 0:\n    folge.append(zahl)\n    zahl -= 1\nfolge',
        [5, 4, 3, 2, 1],
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Endlosschleifen vermeiden

    Vor dem Start einer `while`-Schleife fragen:

    1. Ist die Bedingung anfangs wahr?
    2. Ändert der Schleifenblock einen relevanten Wert?
    3. Wird die Bedingung dadurch irgendwann falsch?

    **Sicherer Einstieg:** mit kleinem Startwert und kurzer Schleife ausprobieren.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('`break` und `continue`', '`break` beendet die Schleife sofort. `continue` überspringt den Rest des aktuellen Durchlaufs und beginnt den nächsten.', 'ausgabe = []\nfor zahl in range(1, 7):\n    if zahl == 4:\n        continue\n    if zahl == 6:\n        break\n    ausgabe.append(zahl)\nausgabe', [1, 2, 3, 5])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · `while-else`

    Der `else`-Zweig einer `while`-Schleife läuft, wenn die Bedingung falsch wird.

    Wird die Schleife mit `break` beendet, läuft der `else`-Zweig nicht.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Schleife normal beenden', 'Hier wird der `else`-Zweig ausgeführt, weil `zahl < 3` schließlich falsch wird.', 'zahl = 0\nwhile zahl < 3:\n    zahl += 1\nelse:\n    status = "Bedingung wurde falsch"\n(zahl, status)', (3, 'Bedingung wurde falsch'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `for`-Schleife und `range`

    ```python
    for element in folge:
        # mit element arbeiten
    ```

    `range(start, stop, schritt)` erzeugt Zahlen. Der `stop`-Wert ist ausgeschlossen.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Zahlen mit `range`', '`range(1, 6)` enthält 1 bis 5. Mit einem dritten Wert kannst du Schritte überspringen.', 'ergebnis = (list(range(1, 6)), list(range(0, 10, 2)))', ([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]))
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Über eine Liste laufen', 'Die Schleifenvariable nimmt der Reihe nach jeden Wert an. Der Block läuft einmal pro Element.', 'gerichte = ["Suppe", "Salat", "Pasta"]\ntexte = []\nfor gericht in gerichte:\n    texte.append(f"Heute gibt es {gericht}.")\ntexte', ['Heute gibt es Suppe.', 'Heute gibt es Salat.', 'Heute gibt es Pasta.'])
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Mit einer Schleife summieren', 'Ein **Akkumulator** sammelt ein Zwischenergebnis. Er wird vor der Schleife auf den Startwert gesetzt und in jedem Durchlauf aktualisiert.', 'punkte = [12, 8, 15, 5]\nsumme = 0\nfor punkt in punkte:\n    summe += punkt\nsumme', 40)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · `for-else` bei einer Suche

    Der `else`-Zweig läuft, wenn die Schleife vollständig durchläuft. Nach einem `break` wird er übersprungen.

    So lässt sich eine erfolglose Suche behandeln.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('42 in einer Liste suchen', 'Wenn die Zahl gefunden wird, beendet `break` die Schleife. Nur wenn kein `break` stattfindet, erscheint die Meldung im `else`-Zweig.', 'zahlen = [10, 24, 42, 57]\nfor zahl in zahlen:\n    if zahl == 42:\n        ergebnis = "Zahl gefunden"\n        break\nelse:\n    ergebnis = "Zahl nicht gefunden"\nergebnis', 'Zahl gefunden')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Eine Sammlung nicht während der Schleife ändern

    Entfernst du Elemente aus einer Liste, über die du gerade läufst, können Elemente übersprungen werden.

    Baue stattdessen eine neue Liste oder filtere die Werte in einem separaten Schritt.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Eine neue Liste erzeugen', 'Die ursprüngliche Liste bleibt unverändert. Die neue Liste enthält nur Namen, die nicht ausgeschlossen werden sollen.', 'teilnehmende = ["George", "Frank", "Ralf", "Udo"]\naktive = []\nfor name in teilnehmende:\n    if name != "Frank":\n        aktive.append(name)\naktive', ['George', 'Ralf', 'Udo'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · List Comprehension

    Eine List Comprehension erzeugt eine neue Liste aus einer Folge:

    ```python
    [ausdruck for element in folge if bedingung]
    ```

    Für den Einstieg ist die ausgeschriebene `for`-Schleife oft leichter zu lesen. Verwende die Kurzform, wenn sie übersichtlich bleibt.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Quadratzahlen bilden', 'Der Ausdruck vor `for` wird für jedes Element berechnet.', 'quadrate = [zahl**2 for zahl in range(1, 6)]\nquadrate', [1, 4, 9, 16, 25])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mitmachen · Punkte summieren

    Nutze eine `for`-Schleife und einen Akkumulator, um die Punkte zu addieren:

    ```python
    punkte = [12, 8, 15, 5]
    ```

    Ändere danach einen Listenwert und führe die Zelle erneut aus.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Lösung · Punkte summieren', 'Starte mit `0` und addiere in jedem Durchlauf den aktuellen Wert.', 'punkte = [12, 8, 15, 5]\nsumme = 0\nfor punkt in punkte:\n    summe += punkt\nsumme', 40)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## marimo-Elemente verbinden Eingabe und Ergebnis

    1. Ein Element wie Slider oder Dropdown bekommt einen Variablennamen.
    2. Die Zelle zeigt das Element an.
    3. Eine weitere Zelle liest `.value`.
    4. marimo führt abhängige Zellen nach einer Änderung erneut aus.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    anzahl_slider = mo.ui.slider(start=1, stop=10, step=1, value=3, label="Anzahl")
    return (anzahl_slider,)


@app.cell
def _(anzahl_slider, mo):
    anzahl = anzahl_slider.value
    preis_pro_person = 4.5
    gesamtpreis = anzahl * preis_pro_person
    gesamtpreis_formatiert = f"{gesamtpreis:.2f}".replace(".", ",")
    mo.vstack([
        mo.md("""
        ## Personenzahl einstellen

        Der Eintritt kostet **4,50 Euro pro Person**. Stelle mit dem Regler eine Anzahl von 1 bis 10 ein.
        """),
        anzahl_slider,
        mo.md(f"""
        ```python
        anzahl = anzahl_slider.value
        gesamtpreis = anzahl * 4.5
        ```

        **Aktuelle Rechnung:** {anzahl} Personen × 4,50 Euro = **{gesamtpreis_formatiert} Euro**

        Schätze zuerst den Preis für 5 Personen. Bewege dann den Regler und beobachte, wie sich die Rechnung sofort aktualisiert.
        """),
    ]).style({"max-width": "900px", "margin": "0 auto"})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Dropdown für eine Auswahl

    Ein Dropdown zeigt mögliche Werte an. Die ausgewählte Option steht in `.value`.

    Das Dictionary verbindet einen sichtbaren Namen mit einem Wert, den der Code weiterverarbeitet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    kurswahl = mo.ui.dropdown(
        options={"Python": 49, "Datenanalyse": 59, "KI": 69},
        value="Python",
        label="Kurs auswählen",
    )
    return (kurswahl,)


@app.cell
def _(kurswahl, mo):
    kursname = kurswahl.selected_key
    preis = kurswahl.value
    mo.vstack([
        mo.md("""
        ## Kurs auswählen

        Wähle einen Kurs aus der Liste. Jeder Name ist mit einem anderen Teilnahmebeitrag verknüpft.
        """),
        kurswahl,
        mo.md(f"""
        ### Deine Auswahl

        **{kursname}** kostet **{preis} Euro**.

        Der sichtbare Kursname und der zugehörige Preis kommen aus demselben Dictionary. Probiere auch **Datenanalyse** und **KI** aus.
        """),
    ]).style({"max-width": "900px", "margin": "0 auto"})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Weitere marimo-Elemente

    marimo bietet unter anderem:

    - `mo.ui.number` für Zahlen
    - `mo.ui.slider` für Werte in einem Bereich
    - `mo.ui.dropdown` und `mo.ui.radio` für Auswahlen
    - `mo.ui.text` für kurze Texte

    Wähle das Element, das zur Art der Eingabe passt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    antwort = mo.ui.radio(
        options=["Ja", "Nein"],
        value="Ja",
        label="Möchtest du eine Vertiefung?",
    )
    return (antwort,)


@app.cell
def _(antwort, mo):
    mo.vstack([
        mo.md("""
        ## Eine Antwort auswählen

        Klicke auf **Ja** oder **Nein**. Eine Radio-Auswahl eignet sich, wenn genau eine Option gewählt werden soll.
        """),
        antwort,
        mo.md(f"""
        ### Deine Antwort

        Du hast **{antwort.value}** gewählt.

        In einer echten Anwendung kann das Programm abhängig von dieser Antwort unterschiedliche Inhalte anzeigen.
        """),
    ]).style({"max-width": "900px", "margin": "0 auto"})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · Komplexe Zahlen

    Python schreibt den imaginären Anteil mit `j`, zum Beispiel `2 + 3j`.

    Komplexe Zahlen unterstützen Addition, Subtraktion und Multiplikation. `abs` liefert ihren Betrag.

    Dieser Abschnitt ist ein Ausblick und keine Voraussetzung für die folgenden Kurstage.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Komplexe Zahlen in Python', '`complex(real, imaginär)` erzeugt einen Wert vom Typ `complex`. `abs` berechnet den Abstand zum Ursprung.', 'a = complex(3, 4)\nb = 1 + 2j\n(a, a + b, abs(a), type(a).__name__)', ((3+4j), (4+6j), 5.0, 'complex'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · Eingaben in Zahlen umwandeln

    `mo.ui.text` liefert Text. Für eine ganze Zahl kann `int(...)` verwendet werden.

    Ungültige Eingaben lösen `ValueError` aus. `try` und `except` ermöglichen eine verständliche Rückmeldung.
    """)
    return


@app.cell(hide_code=True)
def _(beispiel):
    beispiel('Eingabe absichern', 'Die Umwandlung steht im `try`-Block. `except ValueError` behandelt Text, der keine ganze Zahl ist.', 'eingabe = "18"\ntry:\n    alter = int(eingabe)\nexcept ValueError:\n    alter = None\nalter', 18)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · Ein Bild mit Pillow zuschneiden

    Pillow kann Bilder öffnen, zuschneiden, drehen und speichern. Dieses Beispiel nutzt das Bild `pictures/wasserfarben.png`.

    Für diesen optionalen Abschnitt marimo mit Pillow starten:

    ```sh
    uvx --with "pillow==12.1.1" --from "marimo==0.25.2" marimo edit kurstag_02_teilnehmende.py
    ```

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
    ## Was bleibt von heute?

    - `/`, `//` und `%` beantworten unterschiedliche Rechenfragen.
    - Vergleiche ergeben `True` oder `False`.
    - `if` wählt einen Zweig, `while` wiederholt bis zu einer Bedingung, `for` verarbeitet eine Folge.
    - marimo-Elemente stellen Werte bereit; abhängige Zellen reagieren darauf.

    **Abschlussrunde:** Welche Aufgabe wurde klarer, nachdem du das Ergebnis ausgeführt hast?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zum Nachschlagen · Operatoren

    | Ausdruck | Bedeutung |
    | --- | --- |
    | `a + b`, `a - b` | addieren, subtrahieren |
    | `a * b`, `a / b` | multiplizieren, dividieren |
    | `a // b`, `a % b` | Quotient ohne Rest, Rest |
    | `a ** b` | Potenz |
    | `a == b`, `a != b` | gleich, ungleich |
    | `a < b`, `a >= b` | kleiner, größer oder gleich |
    | `and`, `or`, `not` | Wahrheitswerte verbinden oder umkehren |
    """)
    return


if __name__ == "__main__":
    app.run()
