# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo==0.25.2",
#     "pandas==2.3.3",
#     "openpyxl==3.1.5",
# ]
# ///

# Zellenausdrücke und Rückgaben gehören zum marimo-Notebook-Format.
# ruff: noqa: B018

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
            mo.md(f"**Noch nicht ganz · {aufgabe}**\n\n{hinweis}"),
            kind="warn",
        )

    return (pruefhinweis,)




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Kurstag 4 · Mein Pandas-Arbeitsheft

    **Daten laden · auswählen · auswerten**

    Dieses Arbeitsheft begleitet die Folien. Arbeite die Beispiele durch und bearbeite danach die vier Basisübungen. Die Mustervarianten werden im Unterricht besprochen und stehen in der Folienpräsentation.

    ## So arbeitest du mit dem Notebook

    - Im Ordner `kurstag_04` starten: `uvx --from "marimo==0.25.2" marimo edit kurstag_04_teilnehmende.py`.
    - Eine Codezelle mit **Shift+Enter** ausführen.
    - Erst überlegen, welche Zeilen und Spalten du brauchst, dann Code schreiben und das Ergebnis prüfen.
    - **Neutral:** Aufgabe noch offen · **Orange:** Hinweis beachten · **Grün:** Prüfung bestanden.
    - Die vorgegebenen Antwortvariablen in den Übungszellen beibehalten, damit die Rückmeldung sie findet.

    Die Beispieldaten stammen aus `online_shop_verkaufsdaten.xlsx` im selben Ordner. Deine Änderungen werden in dieser Datei gespeichert; für einen frischen Start vorher eine Kopie anlegen.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Unser Weg heute · zwei Termine

    **Termin 5:** Series und DataFrames, Dateien laden und prüfen, Spalten auswählen und Zeilen filtern.

    **Termin 6:** Fehlende Werte, berechnete Spalten, Gruppierungen und Pivot-Tabellen.
    """)
    return




@app.cell
def _():
    import pandas as pd

    return (pd,)




@app.cell
def _(pd):
    df_verkauf = pd.read_excel("online_shop_verkaufsdaten.xlsx", sheet_name="Verkaufsdaten")
    df_verkauf.head()
    return (df_verkauf,)




@app.cell(hide_code=True)
def _(mo):
    mo.vstack([
        mo.md("""
    ## Series und DataFrames

    Eine **Series** speichert eine Spalte mit Werten und einem Index. Ein **DataFrame** verbindet mehrere benannte Series zu einer Tabelle.

    ```python
    pd.Series([12, 18, 15], name="Besuche")
    ```

    ```python
    pd.DataFrame({"Kurs": ["Python", "Excel"], "Teilnehmende": [12, 16]})
    ```

    Der Index kennzeichnet Zeilen. Spaltennamen beschreiben, welche Werte die Tabelle enthält.
            """),
        mo.hstack([
                mo.image(src="public/01_table_series.svg", alt="Schematische Darstellung einer Pandas-Series als einzelne beschriftete Spalte", width=300),
                mo.image(src="public/01_table_dataframe.svg", alt="Schematische Darstellung eines Pandas-DataFrames mit Zeilen, Spalten und Index", width=460),
        ], widths=[1, 1], gap=1),
        mo.md("*Eine Series ist eine Spalte; ein DataFrame bündelt mehrere Spalten.*"),
    ], gap=1)
    return




@app.cell
def _(mo, pd):
    _besuche = pd.Series(
        [12, 18, 15], index=["Montag", "Dienstag", "Mittwoch"], name="Besuche"
    )
    _kurse = pd.DataFrame(
        {"Kurs": ["Python", "Excel"], "Teilnehmende": [12, 16]}
    )
    mo.vstack([_besuche, _kurse], gap=1)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Eine neue Tabelle zuerst prüfen

    - `head()` zeigt die ersten Zeilen; `tail()` zeigt die letzten.
    - `shape` gibt die Anzahl der Zeilen und Spalten zurück.
    - `info()` zeigt Spalten, Datentypen und fehlende Werte.
    - `describe()` fasst numerische Werte zusammen.

    Nutze diese Methoden, bevor du filterst oder Kennzahlen berechnest.
    """)
    return




@app.cell
def _(df_verkauf, mo):
    _kennzahlen = df_verkauf[["Preis", "Menge", "Umsatz"]].describe().round(2)
    mo.vstack(
        [
            mo.md(f"**Form:** {df_verkauf.shape[0]} Zeilen und {df_verkauf.shape[1]} Spalten"),
            df_verkauf.head(4),
            _kennzahlen,
        ],
        gap=1,
    )
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Dateien lesen und speichern

    ```python
    df_csv = pd.read_csv("verkauf.csv")
    df_excel = pd.read_excel("verkauf.xlsx", sheet_name="Tabelle1")
    ```

    Der Pfad ist relativ zum Arbeitsordner. Beim Schreiben verhindert `index=False`, dass der Zeilenindex als zusätzliche Spalte gespeichert wird:

    ```python
    df_verkauf.to_csv("auswertung.csv", index=False)
    df_verkauf.to_excel("auswertung.xlsx", index=False)
    ```

    Ohne Dateinamen liefert `to_csv(index=False)` den CSV-Text zurück, ohne eine Datei zu schreiben.
    """)
    return




@app.cell
def _(df_verkauf):
    df_verkauf.head(3).to_csv(index=False)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.vstack([
        mo.md("""
    ## Spalten auswählen

    ```python
    df_verkauf["Produkt"]
    df_verkauf[["Produkt", "Umsatz"]]
    ```

    Ein einzelner Spaltenname ergibt eine **Series**. Eine Liste von Spaltennamen ergibt einen **DataFrame**.
            """),
        mo.center(mo.image(src="public/03_subset_columns.svg", alt="Grafik zur Auswahl bestimmter DataFrame-Spalten", width=700)),
        mo.md("*Die Abbildung zeigt, welche Spalten die Auswahl enthält.*"),
    ], gap=1)
    return




@app.cell
def _(df_verkauf):
    df_verkauf[["Produkt", "Umsatz"]].head()
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zeilen und Spalten mit `loc` auswählen

    `loc` arbeitet mit Labels. In `df.loc[zeilen, spalten]` stehen Zeilen- und Spaltenauswahl durch ein Komma getrennt.

    ```python
    df_verkauf.loc[0:4, ["Produkt", "Umsatz"]]
    ```

    Beim Label-Slicing mit `loc` ist das Ende eingeschlossen.
    """)
    return




@app.cell
def _(df_verkauf):
    df_verkauf.loc[0:4, ["Produkt", "Umsatz"]]
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zeilen und Spalten mit `iloc` auswählen

    `iloc` arbeitet mit Positionen, die bei 0 beginnen. Das Ende eines Bereichs ist ausgeschlossen.

    ```python
    df_verkauf.iloc[0:5, [1, 5]]
    ```

    Die Spaltenpositionen hängen von der aktuellen Spaltenreihenfolge ab. Für gut lesbaren, stabilen Code sind Namen mit `loc` oft die bessere Wahl.
    """)
    return




@app.cell
def _(df_verkauf):
    df_verkauf.iloc[0:5, [1, 5]]
    return




@app.cell(hide_code=True)
def _(mo):
    mo.vstack([
        mo.md("""
    ## Zeilen filtern

    Ein Vergleich wie `df_verkauf["Umsatz"] > 500` ergibt eine Series aus `True` und `False`. Mit dieser Maske wählen wir die passenden Zeilen aus.

    ```python
    maske = df_verkauf["Umsatz"] > 500
    df_verkauf.loc[maske]
    ```
            """),
        mo.center(mo.image(src="public/03_subset_rows.svg", alt="Grafik zum Filtern passender DataFrame-Zeilen", width=700)),
        mo.md("*Die Bedingung entscheidet für jede Zeile, ob sie in der Auswahl bleibt.*"),
    ], gap=1)
    return




@app.cell
def _(df_verkauf):
    _maske_umsatz = df_verkauf["Umsatz"] > 500
    df_verkauf.loc[_maske_umsatz, ["Produkt", "Region", "Umsatz"]].head()
    return




@app.cell(hide_code=True)
def _(mo):
    mo.vstack([
        mo.md("""
    ## Bedingungen verbinden

    - `&` bedeutet **und**.
    - `|` bedeutet **oder**.
    - Jede Bedingung steht in Klammern.

    ```python
    df_verkauf.loc[
        (df_verkauf["Region"] == "Hamburg") & (df_verkauf["Umsatz"] > 500)
    ]
    ```

    Bei Pandas-Series verwenden wir `&` und `|` statt `and` und `or`.
            """),
        mo.center(mo.image(src="public/03_subset_columns_rows.svg", alt="Grafik zur gemeinsamen Auswahl von Zeilen und Spalten", width=700)),
        mo.md("*Zeilen filtern und Spalten wählen lassen sich kombinieren.*"),
    ], gap=1)
    return




@app.cell
def _(df_verkauf):
    _hamburg_hoch = df_verkauf.loc[
        (df_verkauf["Region"] == "Hamburg") & (df_verkauf["Umsatz"] > 500),
        ["Produkt", "Kategorie", "Umsatz"],
    ]
    _hamburg_hoch.head()
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Interaktiv filtern

    Wähle hier eine Stadt und Produktkategorien aus. Die Trefferliste wird direkt unter den Auswahlfeldern angezeigt und aktualisiert sich mit deiner Auswahl.
    """)
    return




@app.cell(hide_code=True)
def _(df_verkauf, mo):
    _regionen = ["Alle"] + sorted(df_verkauf["Region"].dropna().unique().tolist())
    _kategorien = sorted(df_verkauf["Kategorie"].dropna().unique().tolist())
    region_auswahl = mo.ui.dropdown(options=_regionen, value="Alle", label="Region")
    kategorie_auswahl = mo.ui.multiselect(
        options=_kategorien, value=_kategorien[:2], label="Kategorien (leer = alle)"
    )
    return kategorie_auswahl, region_auswahl




@app.cell
def _(df_verkauf, kategorie_auswahl, mo, region_auswahl):
    _kategorien = sorted(df_verkauf["Kategorie"].dropna().unique().tolist())
    _gewaehlte_kategorien = kategorie_auswahl.value or _kategorien
    _maske_region = (
        True
        if region_auswahl.value == "Alle"
        else df_verkauf["Region"].eq(region_auswahl.value)
    )
    _treffer = df_verkauf.loc[
        _maske_region & df_verkauf["Kategorie"].isin(_gewaehlte_kategorien),
        ["Produkt", "Kategorie", "Region", "Umsatz"],
    ]
    mo.vstack(
        [
            mo.hstack([region_auswahl, kategorie_auswahl], widths=[1, 2], gap=1),
            mo.md(f"**{len(_treffer):,} Treffer · erste 8 Zeilen**".replace(",", ".")),
            _treffer.head(8),
        ],
        gap=1,
    )
    return




@app.cell(hide_code=True)
def _(mo):
    mo.vstack([
        mo.md("""
    ## Termin 6 · Fehlende Werte und neue Spalten

    Prüfe mit `isna().sum()`, welche Werte in der Verkaufstabelle fehlen. Fehlende Mengen kannst du nicht ohne Begründung als null interpretieren. In der folgenden Übung probierst du zwei bewusste Behandlungen an einer kleinen Kopie.

    ```python
    mini = pd.DataFrame({
        "Region": ["Dresden", None, "Leipzig"],
        "Menge": [2, 1, None],
        "Preis": [12.0, 12.0, 2.5],
    })
    mini.isna().sum()
    ```

    Ersetze fehlende Regionen durch `"Unbekannt"`. Erzeuge zusätzlich eine zweite Tabelle ohne Zeilen, deren Menge fehlt. Vergleiche die Zeilenzahlen, bevor du Umsatz berechnest.

    ### Neue Spalten berechnen

    Rechts von der Zuweisung steht der Ausdruck für die neue Spalte:

    ```python
    df["Umsatz_neu"] = df["Preis"] * df["Menge"]
    ```

    Pandas berechnet das Ergebnis zeilenweise. Für die folgenden Übungen erstellen wir eine Kopie, damit die Originaldaten unverändert bleiben.
            """),
        mo.hstack([
                mo.image(src="public/05_newcolumn_1.svg", alt="Grafik zur Berechnung einer neuen DataFrame-Spalte", width=700),
                mo.image(src="public/05_newcolumn_2.svg", alt="Grafik zur Berechnung einer neuen DataFrame-Spalte mit einem weiteren Beispiel", width=700),
        ], widths=[1, 1], gap=1),
        mo.md("*Die Bilder veranschaulichen das Berechnen zusätzlicher Spalten.*"),
    ], gap=1)
    return




@app.cell
def _(df_verkauf):
    _beispiel_spalte = df_verkauf.assign(
        Umsatz_neu=df_verkauf["Preis"] * df_verkauf["Menge"]
    )
    _beispiel_spalte[["Preis", "Menge", "Umsatz_neu"]].head()
    return




@app.cell(hide_code=True)
def _(mo):
    mo.vstack([
        mo.md("""
    ## Aggregationen und `groupby`

    `sum`, `mean`, `min`, `max` und `count` fassen Werte zusammen. Mit `groupby` lassen sich diese Kennzahlen getrennt für jede Gruppe berechnen.

    ```python
    df_verkauf.groupby("Kategorie")["Umsatz"].sum()
    ```

    Die Gruppen werden aus den verschiedenen Werten in `Kategorie` gebildet.
            """),
        mo.hstack([
                mo.image(src="public/06_aggregate.svg", alt="Grafik zur Zusammenfassung vieler Werte durch Aggregationen", width=650),
                mo.image(src="public/06_valuecounts.svg", alt="Grafik zum Zählen von Häufigkeiten mit value_counts", width=650),
        ], widths=[1, 1], gap=1),
        mo.md("*Aggregation und Häufigkeitszählung fassen die Tabelle auf unterschiedliche Weise zusammen.*"),
    ], gap=1)
    return




@app.cell
def _(df_verkauf):
    df_verkauf.groupby("Kategorie")["Umsatz"].sum().sort_values(ascending=False).round(2)
    return




@app.cell
def _(df_verkauf):
    df_verkauf["Zahlungsmethode"].value_counts()
    return




@app.cell(hide_code=True)
def _(mo):
    mo.vstack([
        mo.md("""
    ## Pivot und Pivot-Tabelle

    `pivot()` stellt Daten um, wenn jede Kombination aus Zeilen- und Spaltenmerkmal eindeutig ist.

    `pivot_table()` kann gleiche Kombinationen zusammenfassen. Die Angabe `aggfunc="sum"` bestimmt, wie mehrere Werte behandelt werden.

    ```python
    pd.pivot_table(
        df_verkauf,
        index="Region",
        columns="Kategorie",
        values="Umsatz",
        aggfunc="sum",
        fill_value=0,
    )
    ```
            """),
        mo.hstack([
                mo.image(src="public/07_pivot.svg", alt="Grafik zum Umstellen einer Tabelle mit pivot", width=650),
                mo.image(src="public/07_pivot_table.svg", alt="Grafik zur Zusammenfassung mit pivot_table", width=650),
        ], widths=[1, 1], gap=1),
        mo.md("*Die Diagramme zeigen den Unterschied zwischen Umordnen und Aggregieren.*"),
    ], gap=1)
    return




@app.cell
def _(df_verkauf, pd):
    pd.pivot_table(
        df_verkauf,
        index="Region",
        columns="Kategorie",
        values="Umsatz",
        aggfunc="sum",
        fill_value=0,
    ).round(0)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Übung 1 · Zeilen und Spalten auswählen

    Erstelle ein DataFrame mit den Spalten `Produkt` und `Umsatz`, aber nur mit Bestellungen aus Hamburg.

    **Tipp:** `df_verkauf.loc[bedingung, ["Spalte1", "Spalte2"]]`
    """)
    return




@app.cell
def _(df_verkauf):
    antwort_auswahl = None
    # Ergänze die Auswahl nach Region und Spaltennamen.
    antwort_auswahl
    return (antwort_auswahl,)




@app.cell(hide_code=True)
def _(antwort_auswahl, df_verkauf, mo, pd, pruefhinweis):
    _erwartet = df_verkauf.loc[
        df_verkauf["Region"].eq("Hamburg"), ["Produkt", "Umsatz"]
    ]
    _richtig = (
        isinstance(antwort_auswahl, pd.DataFrame)
        and list(antwort_auswahl.columns) == ["Produkt", "Umsatz"]
        and antwort_auswahl.reset_index(drop=True).equals(
            _erwartet.reset_index(drop=True)
        )
    )
    pruefhinweis(
        True if _richtig else None if antwort_auswahl is None else False,
        "Hamburger Bestellungen auswählen",
        "Filtere zuerst die Region und übergib dann eine Liste mit genau den beiden Spaltennamen.",
    )
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Übung 2 · Eine neue Spalte berechnen

    Erstelle eine Kopie von `df_verkauf` und ergänze `Umsatz_neu` mit `Preis * Menge`.

    **Tipp:** `df.copy()` erstellt eine Kopie. Danach kannst du `df["Neue_Spalte"] = Ausdruck` verwenden.
    """)
    return




@app.cell
def _(df_verkauf):
    antwort_umsatz = None
    # Erstelle eine Kopie und ergänze Umsatz_neu aus Preis und Menge.
    antwort_umsatz
    return (antwort_umsatz,)




@app.cell(hide_code=True)
def _(antwort_umsatz, df_verkauf, mo, pd, pruefhinweis):
    _richtig = False
    if isinstance(antwort_umsatz, pd.DataFrame) and "Umsatz_neu" in antwort_umsatz:
        _soll = (df_verkauf["Preis"] * df_verkauf["Menge"]).round(2)
        _richtig = antwort_umsatz["Umsatz_neu"].round(2).equals(_soll)
    pruefhinweis(
        True if _richtig else None if antwort_umsatz is None else False,
        "Umsatz berechnen",
        'Eine passende Zeile für Zeile-Rechnung ist `df_verkauf["Preis"] * df_verkauf["Menge"]`.',
    )
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Übung 3 · Nach Kategorie gruppieren

    Berechne den Gesamtumsatz pro `Kategorie`. Sortiere anschließend nach dem Namen der Kategorie.

    **Tipp:** `groupby("Kategorie")["Umsatz"].sum().sort_index()`
    """)
    return




@app.cell
def _(df_verkauf):
    antwort_gruppierung = None
    # Gruppiere nach Kategorie und berechne den Gesamtumsatz.
    antwort_gruppierung
    return (antwort_gruppierung,)




@app.cell(hide_code=True)
def _(antwort_gruppierung, df_verkauf, mo, pd, pruefhinweis):
    _soll = df_verkauf.groupby("Kategorie")["Umsatz"].sum().sort_index().round(2)
    _richtig = False
    if isinstance(antwort_gruppierung, pd.Series):
        _richtig = antwort_gruppierung.sort_index().round(2).equals(_soll)
    elif isinstance(antwort_gruppierung, pd.DataFrame) and "Umsatz" in antwort_gruppierung:
        _richtig = antwort_gruppierung["Umsatz"].sort_index().round(2).equals(_soll)
    pruefhinweis(
        True if _richtig else None if antwort_gruppierung is None else False,
        "Umsatz pro Kategorie",
        'Nach `groupby("Kategorie")` wählst du die Umsatzspalte aus und addierst sie mit `sum()`.',
    )
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Übung 4 · Pivot-Tabelle erstellen

    Erstelle eine Pivot-Tabelle mit `Kategorie` als Zeilen, `Region` als Spalten und der Summe von `Umsatz` als Werten. Fehlende Kombinationen sollen den Wert 0 erhalten.

    **Tipp:** `pd.pivot_table(..., aggfunc="sum", fill_value=0)`
    """)
    return




@app.cell
def _(df_verkauf, pd):
    antwort_pivot = None
    # Erstelle die Pivot-Tabelle mit Kategorie, Region und Umsatz.
    antwort_pivot
    return (antwort_pivot,)




@app.cell(hide_code=True)
def _(antwort_pivot, df_verkauf, mo, pd, pruefhinweis):
    _soll = pd.pivot_table(
        df_verkauf,
        index="Kategorie",
        columns="Region",
        values="Umsatz",
        aggfunc="sum",
        fill_value=0,
    )
    _richtig = False
    if isinstance(antwort_pivot, pd.DataFrame):
        _gegeben = antwort_pivot.fillna(0).sort_index().sort_index(axis=1).round(2)
        _erwartet = _soll.sort_index().sort_index(axis=1).round(2)
        _richtig = _gegeben.equals(_erwartet)
    pruefhinweis(
        True if _richtig else None if antwort_pivot is None else False,
        "Umsätze als Pivot-Tabelle anzeigen",
        "Prüfe Index, Spalten, Wertespalte und Aggregation. Für jede Kategorie-Region-Kombination wird der Umsatz addiert.",
    )
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusatzteil · Daten selbst erkunden

    Probiere weitere Fragen an `df_verkauf`:

    - Welche fünf Produkte haben den höchsten Gesamtumsatz?
    - Wie viele Bestellungen gibt es je Zahlungsmethode?
    - Wie hoch ist der durchschnittliche Umsatz je Region?
    - Was ändert sich in einer Pivot-Tabelle, wenn du `sum` durch `mean` ersetzt?

    Verwende bei Bedarf `head()` oder `sort_values()` für eine übersichtliche Ausgabe.
    """)
    return




@app.cell
def _(df_verkauf):
    df_verkauf.groupby("Produkt")["Umsatz"].sum().sort_values(ascending=False).head(5).round(2)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Rückblick

    - Welche Methode verwendest du, wenn du Zeilen anhand einer Bedingung auswählst?
    - Wann ist `iloc` hilfreich, und wann sind Spaltennamen mit `loc` sicherer?
    - Was kann `pivot_table`, das `pivot` nicht kann?

    **Notizen:** Schreibe einen Merksatz auf, der dir beim nächsten Datensatz hilft.
    """)
    return


if __name__ == "__main__":
    app.run()
