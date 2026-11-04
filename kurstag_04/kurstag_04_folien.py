# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo==0.25.2",
#     "pandas==2.3.3",
#     "openpyxl==3.1.5",
# ]
# ///

# Zellenausdrücke und Rückgaben gehören zum marimo-Notebook-Format.
# ruff: noqa: B018, PLR1711, UP003

import marimo

__generated_with = "0.25.2"
app = marimo.App(
    width="medium",
    layout_file="layouts/kurstag_04_folien.slides.json",
)


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    import pandas as pd
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

    return beispiel, pd


@app.cell(hide_code=True)
def _(mo):
    from base64 import b64encode as _b64encode
    from pathlib import Path as _Path

    _logo_data = _b64encode(
        _Path("public/vhs-dresden-logo.png").read_bytes()
    ).decode("ascii")
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
        <h1 class="vhs-kursstart-title">Kurstag 4<span>Datenanalyse mit Pandas</span></h1>
        <p class="vhs-kursstart-summary">Tabellen verstehen, gezielt auswählen und aus Daten Antworten gewinnen.</p>
        <div class="vhs-kursstart-motto">Daten <b>·</b> Fragen <b>·</b> Erkenntnisse</div>
      </div>
      <div class="vhs-kursstart-art" aria-hidden="true"><div class="vhs-kursstart-core">df</div><i class="vhs-kursstart-dot one"></i><i class="vhs-kursstart-dot two"></i><i class="vhs-kursstart-dot three"></i><i class="vhs-kursstart-dot four"></i><i class="vhs-kursstart-dot five"></i></div>
    </section>
    """
    mo.Html(_cover_html.replace("__VHS_LOGO__", _logo_data))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Unser Weg heute

    1. **Tabellen verstehen:** Series, DataFrames und erste Prüfmethoden.
    2. **Daten finden:** Spalten auswählen, Zeilen filtern, `loc` und `iloc` nutzen.
    3. **Fragen beantworten:** Spalten berechnen, gruppieren und zusammenfassen.
    4. **Ergebnisse ordnen:** Pivot und Pivot-Tabellen sinnvoll einsetzen.

    **Arbeitsweise:** Eine Frage stellen, passende Daten auswählen, Ergebnis prüfen und verständlich beschreiben.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Von der Tabelle zur Erkenntnis

    Eine Datenanalyse beginnt mit einer konkreten Frage. Dann prüfen wir, welche Daten und Spalten dafür passen, filtern die benötigten Zeilen und fassen die Ergebnisse zusammen.

    **Beispiel:** In welcher Region wurde welcher Umsatz erzielt?

    Wir arbeiten heute mit einem kleinen Ausschnitt aus einer Online-Shop-Tabelle. Die Methoden lassen sich später auf größere Datensätze übertragen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.image(
            "public/01_table_dataframe.svg",
            alt="Ein DataFrame mit Zeilen, Spalten und Index",
        )
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zwei wichtige Datenstrukturen

    - **Series:** eine einzelne Spalte mit Index und Werten.
    - **DataFrame:** eine Tabelle aus mehreren benannten Series.

    Den Index verwendet Pandas, um Zeilen zu finden. Spaltennamen beschreiben, welche Information in jeder Spalte steht.
    """)
    return


@app.cell
def _(beispiel, pd):
    _besuche = pd.Series(
        [12, 18, 15], index=["Montag", "Dienstag", "Mittwoch"], name="Besuche"
    )
    beispiel(
        "Eine Series erstellen",
        "Werte, Index und Name machen aus einer Liste eine beschriftete Spalte.",
        'pd.Series([12, 18, 15], index=["Montag", "Dienstag", "Mittwoch"], name="Besuche")',
        _besuche,
    )
    return


@app.cell
def _(beispiel, pd):
    _kurse = pd.DataFrame(
        {
            "Kurs": ["Python", "Excel", "Daten"],
            "Teilnehmende": [12, 16, 9],
            "Gebühr": [48.0, 36.0, 52.0],
        }
    )
    beispiel(
        "Ein DataFrame aus einem Dictionary",
        "Jeder Schlüssel wird zu einem Spaltennamen. Die Listen liefern die Werte jeder Spalte.",
        'pd.DataFrame({"Kurs": ["Python", "Excel"], "Teilnehmende": [12, 16]})',
        _kurse,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Erst die Daten prüfen

    Bei einer neuen Tabelle schauen wir zuerst auf die Form und einige Zeilen. Danach prüfen wir die Spalten und Datentypen. So fällt auf, wenn Werte fehlen oder als falscher Typ eingelesen wurden.

    - `head()` zeigt die ersten Zeilen.
    - `tail()` zeigt die letzten Zeilen.
    - `info()` nennt Spalten, Datentypen und fehlende Werte.
    - `describe()` fasst numerische Spalten zusammen.
    """)
    return


@app.cell
def _(beispiel, pd):
    verkauf = pd.read_excel(
        "online_shop_verkaufsdaten.xlsx", sheet_name="Verkaufsdaten"
    )
    beispiel(
        "Die Beispieldaten ansehen",
        "Wir lesen die lokale Excel-Datei ein und sehen zunächst nur fünf Zeilen.",
        'verkauf = pd.read_excel("online_shop_verkaufsdaten.xlsx", sheet_name="Verkaufsdaten")\nverkauf.head()',
        verkauf.head(),
    )
    return (verkauf,)


@app.cell
def _(beispiel, verkauf):
    _pruefung = {
        "Form (Zeilen, Spalten)": verkauf.shape,
        "Spalten": list(verkauf.columns),
        "Erste Zeilen": verkauf.head(3),
        "Statistik für Preis und Menge": verkauf[["Preis", "Menge"]]
        .describe()
        .round(2),
    }
    beispiel(
        "Form, Spalten und Kennzahlen",
        "`shape` zählt Zeilen und Spalten. `describe()` zeigt zum Beispiel Mittelwert und Spannweite.",
        'verkauf.shape\nverkauf.columns\nverkauf[["Preis", "Menge"]].describe()',
        _pruefung,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Daten aus Dateien lesen und speichern

    Pandas kann unter anderem CSV- und Excel-Dateien lesen:

    ```python
    pd.read_csv("verkauf.csv")
    pd.read_excel("verkauf.xlsx", sheet_name="Tabelle1")
    ```

    Der Dateiname ist relativ zum Arbeitsordner. Beim Speichern geben wir mit `index=False` an, dass der technische Zeilenindex nicht als eigene Spalte exportiert werden soll.

    ```python
    df.to_csv("auswertung.csv", index=False)
    df.to_excel("auswertung.xlsx", index=False)
    ```
    """)
    return


@app.cell
def _(beispiel, verkauf):
    _csv_text = verkauf.head(3).to_csv(index=False)
    beispiel(
        "CSV-Ausgabe vorbereiten",
        "Ohne Dateinamen gibt `to_csv()` den CSV-Text zurück. Mit einem Dateinamen wird er gespeichert.",
        "verkauf.head(3).to_csv(index=False)",
        _csv_text,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Spalten auswählen

    Mit einem Spaltennamen in eckigen Klammern erhalten wir eine Series. Mit einer Liste von Spaltennamen erhalten wir einen DataFrame.

    ```python
    df["Produkt"]
    df[["Produkt", "Umsatz"]]
    ```

    Die zweite Schreibweise ist für mehrere Spalten wichtig: Die innere Liste nennt die gewünschten Spalten.
    """)
    return


@app.cell
def _(beispiel, verkauf):
    _auswahl = verkauf[["Produkt", "Umsatz"]].head(5)
    beispiel(
        "Zwei Spalten auswählen",
        "Wir behalten den Produktnamen und den Umsatz jeder Zeile.",
        'verkauf[["Produkt", "Umsatz"]].head()',
        _auswahl,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `loc` und `iloc`

    - `loc` wählt Zeilen und Spalten über **Labels** aus, zum Beispiel über einen Namen.
    - `iloc` wählt über **Positionen** aus, also über Zahlen von 0 an.

    Bei `loc` ist das Ende eines Bereichs eingeschlossen. Bei `iloc` ist das Ende ausgeschlossen – wie bei normalen Python-Slices.
    """)
    return


@app.cell
def _(beispiel, verkauf):
    _labels = verkauf.loc[0:4, ["Produkt", "Umsatz"]]
    beispiel(
        "Mit `loc` nach Labels auswählen",
        "Der Bereich `0:4` enthält beim Label-Zugriff beide Endpunkte.",
        'verkauf.loc[0:4, ["Produkt", "Umsatz"]]',
        _labels,
    )
    return


@app.cell
def _(beispiel, verkauf):
    _positionen = verkauf.iloc[0:5, [1, 5]]
    beispiel(
        "Mit `iloc` nach Positionen auswählen",
        "Die Zeilen 0 bis 4 und die Spalten an Position 1 und 5 werden ausgewählt. Die Endposition 5 ist ausgeschlossen.",
        "verkauf.iloc[0:5, [1, 5]]",
        _positionen,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zeilen mit einer Bedingung filtern

    Ein Vergleich wie `verkauf["Umsatz"] > 500` erzeugt für jede Zeile `True` oder `False`. Diese Wahrheitswerte können wir als Filter verwenden.

    ```python
    maske = verkauf["Umsatz"] > 500
    verkauf.loc[maske]
    ```

    Lies den Vergleich als Frage: „Ist der Umsatz dieser Zeile größer als 500?“
    """)
    return


@app.cell
def _(beispiel, verkauf):
    _maske = verkauf["Umsatz"] > 500
    _teure_bestellungen = verkauf.loc[
        _maske, ["Produkt", "Region", "Umsatz"]
    ].head(6)
    beispiel(
        "Bestellungen über 500 Euro",
        "Die Maske wählt nur Zeilen aus, die die Bedingung erfüllen.",
        'maske = verkauf["Umsatz"] > 500\nverkauf.loc[maske, ["Produkt", "Region", "Umsatz"]].head()',
        _teure_bestellungen,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mehrere Bedingungen verbinden

    Setze jede Bedingung in Klammern und verbinde sie mit:

    - `&` für **und**
    - `|` für **oder**
    - `~` für **nicht**

    ```python
    (verkauf["Region"] == "Hamburg") & (verkauf["Umsatz"] > 500)
    ```

    Für Pandas-Series verwenden wir `&` und `|`, nicht die Python-Wörter `and` und `or`.
    """)
    return


@app.cell
def _(beispiel, verkauf):
    _hamburg_und_hoch = verkauf.loc[
        (verkauf["Region"] == "Hamburg") & (verkauf["Umsatz"] > 500),
        ["Produkt", "Kategorie", "Umsatz"],
    ].head(5)
    beispiel(
        "Zwei Bedingungen",
        "Hier bleiben Bestellungen aus Hamburg, deren Umsatz über 500 Euro liegt.",
        'verkauf.loc[(verkauf["Region"] == "Hamburg") & (verkauf["Umsatz"] > 500)]',
        _hamburg_und_hoch,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Interaktiv filtern

    Wähle eine Stadt und eine oder mehrere Kategorien aus. Die Tabelle unter den Auswahlfeldern aktualisiert sich direkt.

    **Beobachte:** Welche Zeilen bleiben übrig, wenn du die Auswahl änderst?
    """)
    return


@app.cell(hide_code=True)
def _(mo, verkauf):
    _regionen = ["Alle"] + sorted(verkauf["Region"].dropna().unique().tolist())
    _kategorien = sorted(verkauf["Kategorie"].dropna().unique().tolist())
    auswahl_region = mo.ui.dropdown(
        options=_regionen, value="Alle", label="Region"
    )
    auswahl_kategorie = mo.ui.multiselect(
        options=_kategorien,
        value=_kategorien[:2],
        label="Kategorien (leer = alle)",
    )
    return auswahl_kategorie, auswahl_region


@app.cell
def _(auswahl_kategorie, auswahl_region, mo, verkauf):
    _maske_region = (
        True
        if auswahl_region.value == "Alle"
        else verkauf["Region"].eq(auswahl_region.value)
    )
    _gewählte_kategorien = auswahl_kategorie.value or _kategorien
    _maske_kategorie = verkauf["Kategorie"].isin(_gewählte_kategorien)
    _treffer = verkauf.loc[
        _maske_region & _maske_kategorie,
        ["Produkt", "Kategorie", "Region", "Umsatz"],
    ]
    mo.vstack(
        [
            mo.hstack(
                [auswahl_region, auswahl_kategorie], widths=[1, 2], gap=1
            ),
            mo.md(
                f"**{len(_treffer):,} Treffer · erste 8 Zeilen**".replace(
                    ",", "."
                )
            ),
            _treffer.head(8),
        ],
        gap=1,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Neue Spalten berechnen

    Eine neue Spalte entsteht durch eine Zuweisung mit eckigen Klammern. Rechts steht ein Ausdruck, der für alle Zeilen berechnet wird.

    ```python
    df["Umsatz_neu"] = df["Preis"] * df["Menge"]
    ```

    Pandas führt die Multiplikation für jedes Wertepaar aus. Eine `for`-Schleife ist dafür nicht nötig.
    """)
    return


@app.cell
def _(beispiel, verkauf):
    _mit_umsatz = verkauf.assign(
        Umsatz_neu=verkauf["Preis"] * verkauf["Menge"]
    )
    beispiel(
        "Umsatz aus Preis und Menge berechnen",
        "`assign` erstellt eine Kopie mit zusätzlicher Spalte. So bleibt die geladene Tabelle unverändert.",
        'mit_umsatz = verkauf.assign(Umsatz_neu=verkauf["Preis"] * verkauf["Menge"])\nmit_umsatz[["Preis", "Menge", "Umsatz_neu"]].head()',
        _mit_umsatz[["Preis", "Menge", "Umsatz_neu"]].head(),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusammenfassen: Aggregationen

    Aggregationen reduzieren viele Werte auf Kennzahlen:

    - `sum()` addiert Werte.
    - `mean()` berechnet den Mittelwert.
    - `min()` und `max()` finden kleinsten und größten Wert.
    - `count()` zählt vorhandene Werte.

    `describe()` liefert mehrere Kennzahlen auf einmal. Fehlende Werte werden bei vielen numerischen Aggregationen automatisch ausgelassen.
    """)
    return


@app.cell
def _(beispiel, verkauf):
    _summen = (
        verkauf[["Umsatz", "Menge"]]
        .agg(["sum", "mean", "min", "max"])
        .round(2)
    )
    beispiel(
        "Kennzahlen auf einer Auswahl",
        "Mit `agg` wenden wir mehrere Methoden auf zwei numerische Spalten an.",
        'verkauf[["Umsatz", "Menge"]].agg(["sum", "mean", "min", "max"])',
        _summen,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mit `groupby` vergleichen

    `groupby` teilt die Zeilen nach einem Merkmal in Gruppen. Danach berechnet eine Aggregation Kennzahlen für jede Gruppe.

    ```python
    verkauf.groupby("Kategorie")["Umsatz"].sum()
    ```

    So vergleichen wir beispielsweise den Gesamtumsatz verschiedener Produktkategorien.
    """)
    return


@app.cell
def _(beispiel, verkauf):
    _umsatz_nach_kategorie = (
        verkauf.groupby("Kategorie")["Umsatz"]
        .sum()
        .sort_values(ascending=False)
        .round(2)
    )
    beispiel(
        "Umsatz pro Kategorie",
        "Jede Kategorie erhält eine eigene Summe. `sort_values` ordnet sie vom größten Umsatz an.",
        'verkauf.groupby("Kategorie")["Umsatz"].sum().sort_values(ascending=False)',
        _umsatz_nach_kategorie,
    )
    return


@app.cell
def _(beispiel, verkauf):
    _vergleich = (
        verkauf.groupby(["Region", "Kategorie"])["Umsatz"]
        .mean()
        .round(2)
        .head(10)
    )
    beispiel(
        "Nach zwei Merkmalen gruppieren",
        "Eine Liste in `groupby` bildet Gruppen aus jeder Kombination von Region und Kategorie.",
        'verkauf.groupby(["Region", "Kategorie"])["Umsatz"].mean()',
        _vergleich,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Häufigkeiten zählen

    `value_counts()` zählt, wie oft jeder Wert in einer Spalte vorkommt. Das ist eine schnelle Antwort auf Fragen wie „Wie viele Bestellungen gibt es pro Zahlungsmethode?“.

    Die gleiche Auswertung lässt sich mit `groupby(...).size()` schreiben.
    """)
    return


@app.cell
def _(beispiel, verkauf):
    _haeufigkeit = verkauf["Zahlungsmethode"].value_counts()
    beispiel(
        "Zahlungsmethoden zählen",
        "Das Ergebnis wird standardmäßig von häufig nach selten sortiert.",
        'verkauf["Zahlungsmethode"].value_counts()',
        _haeufigkeit,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Pivot oder Pivot-Tabelle?

    - `pivot()` ordnet Daten neu. Jede Kombination aus Zeilen- und Spaltenmerkmal darf nur einmal vorkommen.
    - `pivot_table()` kann wiederholte Kombinationen mit einer Aggregation zusammenfassen.

    Nutze `pivot`, wenn die Kombinationen eindeutig sind. Nutze `pivot_table`, wenn Werte zusammengefasst werden müssen.
    """)
    return


@app.cell
def _(beispiel, pd):
    _tageswerte = pd.DataFrame(
        {
            "Tag": ["Mo", "Mo", "Di", "Di"],
            "Region": ["Nord", "Süd", "Nord", "Süd"],
            "Bestellungen": [4, 3, 5, 2],
        }
    )
    _breit = _tageswerte.pivot(
        index="Tag", columns="Region", values="Bestellungen"
    )
    beispiel(
        "Eine Tabelle ohne Aggregation umstellen",
        "Die Kombination aus Tag und Region kommt nur einmal vor. `pivot` kann sie deshalb eindeutig anordnen.",
        'daten.pivot(index="Tag", columns="Region", values="Bestellungen")',
        _breit,
    )
    return


@app.cell
def _(beispiel, pd, verkauf):
    _kreuztabelle = pd.pivot_table(
        verkauf,
        index="Region",
        columns="Kategorie",
        values="Umsatz",
        aggfunc="sum",
        fill_value=0,
    ).round(0)
    beispiel(
        "Umsatz nach Region und Kategorie",
        "Hier gibt es mehrfach Bestellungen je Kombination. `pivot_table` fasst sie mit `sum` zusammen.",
        'pd.pivot_table(verkauf, index="Region", columns="Kategorie", values="Umsatz", aggfunc="sum", fill_value=0)',
        _kreuztabelle,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Häufige Stolperstellen

    - Für mehrere Spalten: `df[["A", "B"]]` mit zwei Paar eckigen Klammern.
    - Bei `loc` sind Zeilen- und Spaltenauswahl durch ein Komma getrennt.
    - Bei mehreren Bedingungen: jede Bedingung einklammern und `&` oder `|` verwenden.
    - `pivot()` schlägt fehl, wenn Zeilen- und Spaltenmerkmale nicht eindeutig sind. Dann `pivot_table()` mit `aggfunc` nutzen.
    - Wenn du Spalten ergänzt, arbeite bei Bedarf mit `df.copy()` oder `assign()`, damit das Ausgangsobjekt erhalten bleibt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Das nehmen wir mit

    - Eine Series ist eine beschriftete Spalte; ein DataFrame ist eine Tabelle.
    - `head`, `info` und `describe` helfen, neue Daten zu prüfen.
    - `loc` nutzt Labels, `iloc` nutzt Positionen.
    - Bedingungen filtern Zeilen; Ausdrücke erzeugen neue Spalten.
    - `groupby` und `pivot_table` machen Vergleiche zwischen Gruppen sichtbar.

    **Rückblick:** Welche Frage würdest du mit den heutigen Werkzeugen an eine Tabelle stellen?
    """)
    return


@app.cell
def _(beispiel, verkauf):
    _loesung_auswahl = verkauf.loc[
        verkauf["Region"].eq("Hamburg"), ["Produkt", "Umsatz"]
    ]
    beispiel(
        "Lösung · Zeilen und Spalten auswählen",
        "Erst filtern wir die Region. Dann wählen wir zwei benannte Spalten aus.",
        'verkauf.loc[verkauf["Region"] == "Hamburg", ["Produkt", "Umsatz"]]',
        _loesung_auswahl.head(8),
    )
    return


@app.cell
def _(beispiel, verkauf):
    _loesung_neue_spalte = verkauf.assign(
        Umsatz_neu=verkauf["Preis"] * verkauf["Menge"]
    )
    beispiel(
        "Lösung · Eine Spalte berechnen",
        "Preis mal Menge ergibt den Umsatz der jeweiligen Bestellung.",
        'verkauf.assign(Umsatz_neu=verkauf["Preis"] * verkauf["Menge"])',
        _loesung_neue_spalte[["Preis", "Menge", "Umsatz_neu"]].head(),
    )
    return


@app.cell
def _(beispiel, verkauf):
    _loesung_gruppierung = (
        verkauf.groupby("Kategorie")["Umsatz"].sum().sort_index().round(2)
    )
    beispiel(
        "Lösung · Gruppieren und summieren",
        "`groupby` bildet eine Gruppe pro Kategorie; `sum` addiert deren Umsätze.",
        'verkauf.groupby("Kategorie")["Umsatz"].sum()',
        _loesung_gruppierung,
    )
    return


@app.cell
def _(beispiel, pd, verkauf):
    _loesung_pivot = pd.pivot_table(
        verkauf,
        index="Kategorie",
        columns="Region",
        values="Umsatz",
        aggfunc="sum",
        fill_value=0,
    ).round(0)
    beispiel(
        "Lösung · Pivot-Tabelle erstellen",
        "Die Pivot-Tabelle vergleicht Umsätze für jede Kategorie und Region.",
        'pd.pivot_table(verkauf, index="Kategorie", columns="Region", values="Umsatz", aggfunc="sum", fill_value=0)',
        _loesung_pivot,
    )
    return


if __name__ == "__main__":
    app.run()
