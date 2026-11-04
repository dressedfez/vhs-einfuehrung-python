# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo==0.25.2",
#     "matplotlib",
#     "openpyxl",
#     "pandas",
#     "plotly",
#     "seaborn",
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
    import matplotlib.pyplot as plt
    import pandas as pd
    import plotly.express as px
    import seaborn as sns

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

    return pd, plt, pruefhinweis, px, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Kurstag 5 · Mein Arbeitsheft zur Datenvisualisierung

    **Aus Tabellen werden Diagramme**

    Dieses Arbeitsheft begleitet die Folien. Arbeite erst die Beispiele durch und bearbeite anschließend die vier Basisübungen.

    ## So arbeitest du mit dem Notebook

    - Im Ordner `kurstag_05` starten: `uvx --from "marimo==0.25.2" marimo edit kurstag_05_teilnehmende.py`.
    - Codezellen mit **Shift+Enter** ausführen.
    - Ersetze in jeder Übungszelle `None` durch deinen eigenen Ausdruck.
    - **Neutral:** Aufgabe noch offen · **Orange:** Ergebnis prüfen · **Grün:** Rückmeldung bestanden.
    - Auswahlfelder und das dazugehörige Diagramm werden gemeinsam auf derselben Notebook-Seite angezeigt.

    Die Beispieldaten stammen aus `data/online_shop_verkaufsdaten.xlsx`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Diagrammtyp und Frage

    - Ein **Liniendiagramm** zeigt einen Verlauf über die Zeit.
    - Ein **Balkendiagramm** vergleicht Gruppen.
    - Ein **Histogramm** zeigt die Häufigkeit von Zahlenwerten.
    - Ein **Boxplot** vergleicht Werteverteilungen.
    - Ein **Streudiagramm** zeigt die Beziehung zweier Zahlen.

    Die Grafik soll zu der Frage passen, die wir beantworten möchten.
    """)
    return


@app.cell
def _(pd):
    df = pd.read_excel(
        "data/online_shop_verkaufsdaten.xlsx", sheet_name="Verkaufsdaten"
    )
    df["Datum"] = pd.to_datetime(df["Datum"])
    df.head()
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Matplotlib mit Figure und Axes

    - Eine **Figure** enthält die gesamte Abbildung.
    - Eine **Axes** ist ein Zeichenbereich mit Daten und Beschriftungen.
    - `plt.subplots()` erstellt beides.

    ```python
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(title="Titel", xlabel="x-Achse", ylabel="y-Achse")
    ```

    Achsentitel und Einheiten gehören zur Erklärung der Grafik.
    """)
    return


@app.cell
def _(df, plt):
    _monat = (
        df.assign(Monat=df["Datum"].dt.to_period("M").astype(str))
        .groupby("Monat", as_index=False)["Umsatz"]
        .sum()
    )
    _fig, _ax = plt.subplots(figsize=(8, 3.6), layout="constrained")
    _ax.plot(_monat["Monat"], _monat["Umsatz"], marker="o")
    _ax.set(
        title="Monatlicher Umsatz", xlabel="Monat", ylabel="Umsatz in Euro"
    )
    _ax.tick_params(axis="x", rotation=45)
    _ax.grid(axis="y", alpha=0.3)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Balkendiagramm nach Region

    Gruppiere die Tabelle zunächst nach Region. Danach zeichnest du je Region einen Balken. `sort_values()` kann die Balken nach Umsatz ordnen.

    ```python
    umsatz_region = df.groupby("Region")["Umsatz"].sum()
    umsatz_region.sort_values().plot(kind="barh")
    ```

    Bei Balkendiagrammen sollte die Zahlenachse gewöhnlich bei null beginnen.
    """)
    return


@app.cell
def _(df, plt):
    _region = df.groupby("Region")["Umsatz"].sum().sort_values()
    _fig_region, _ax_region = plt.subplots(
        figsize=(8, 3.8), layout="constrained"
    )
    _region.plot(kind="barh", ax=_ax_region, color="#17668e")
    _ax_region.set(
        title="Umsatz nach Region", xlabel="Umsatz in Euro", ylabel="Region"
    )
    _fig_region
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Histogramm

    Ein Histogramm teilt Zahlen in Wertebereiche ein. Die Balkenhöhe zeigt die Anzahl der Bestellungen pro Bereich.

    `bins=20` teilt die Werte in 20 Intervalle ein. Probiere später auch weniger Intervalle aus und vergleiche, wie sich das Bild verändert.
    """)
    return


@app.cell
def _(df, plt):
    _fig_hist, _ax_hist = plt.subplots(figsize=(8, 3.6), layout="constrained")
    _ax_hist.hist(df["Umsatz"], bins=20, color="#39a5d6", edgecolor="white")
    _ax_hist.set(
        title="Umsatz pro Bestellung",
        xlabel="Umsatz in Euro",
        ylabel="Anzahl Bestellungen",
    )
    _fig_hist
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Boxplot mit Seaborn

    Seaborn erzeugt statistische Diagramme auf Basis von Matplotlib. Der Median ist die Linie in der Box. Die Box umfasst den mittleren Bereich der Daten.

    ```python
    sns.boxplot(data=df, x="Kategorie", y="Umsatz", ax=ax)
    ```

    Ein Boxplot eignet sich, um Verteilungen mehrerer Kategorien miteinander zu vergleichen.
    """)
    return


@app.cell
def _(df, plt, sns):
    _fig_box, _ax_box = plt.subplots(figsize=(8, 3.8), layout="constrained")
    sns.boxplot(
        data=df,
        x="Kategorie",
        y="Umsatz",
        hue="Kategorie",
        legend=False,
        ax=_ax_box,
    )
    _ax_box.set(
        title="Umsatzverteilung nach Kategorie",
        xlabel="Kategorie",
        ylabel="Umsatz pro Bestellung in Euro",
    )
    _ax_box.tick_params(axis="x", rotation=20)
    _fig_box
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Streudiagramm

    Jeder Punkt stellt eine Bestellung dar. Seine x-Position steht für den Preis, seine y-Position für die Bestellmenge.

    Ein Muster kann einen Zusammenhang zeigen. Daraus allein folgt nicht, dass der Preis die Bestellmenge verursacht.
    """)
    return


@app.cell
def _(df, plt):
    _fig_streu, _ax_streu = plt.subplots(
        figsize=(8, 3.7), layout="constrained"
    )
    _ax_streu.scatter(df["Preis"], df["Menge"], alpha=0.65, color="#147e9e")
    _ax_streu.set(
        title="Preis und Bestellmenge",
        xlabel="Preis pro Stück in Euro",
        ylabel="Menge pro Bestellung",
    )
    _ax_streu.grid(alpha=0.2)
    _fig_streu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Interaktive Diagramme mit Plotly

    Plotly zeigt beim Überfahren mit der Maus die genauen Werte. Eine Grafik lässt sich außerdem vergrößern oder verschieben.

    ```python
    fig = px.bar(umsatz_region, x="Region", y="Umsatz")
    fig
    ```

    Für eine interaktive Ausgabe muss die Figure als letzter Ausdruck der Zelle stehen.
    """)
    return


@app.cell
def _(df, px):
    _plotly_region = df.groupby("Region", as_index=False)["Umsatz"].sum()
    _fig_plotly = px.bar(
        _plotly_region,
        x="Region",
        y="Umsatz",
        color="Region",
        title="Umsatz nach Region",
        labels={"Umsatz": "Umsatz in Euro"},
    )
    _fig_plotly.update_layout(showlegend=False)
    _fig_plotly
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Vier Basisübungen

    In den folgenden Zellen ersetzt du `None` durch einen Ausdruck. Führe die Zelle aus und lies die Rückmeldung darunter.

    | Aufgabe | Ziel |
    | --- | --- |
    | 1 | Monatliche Umsätze als Tabelle zusammenfassen |
    | 2 | Regionen nach Umsatz vergleichen |
    | 3 | Die Umsatzverteilung als Histogramm zeigen |
    | 4 | Produktkategorien mit Plotly interaktiv vergleichen |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Aufgabe 1 · Monatsumsätze

    Fasse die Umsätze je Monat zusammen. Erzeuge einen DataFrame mit den Spalten `Monat` und `Umsatz`.

    Hinweis: `dt.to_period("M").astype(str)` macht aus einem Datum die Zeichenkette für Jahr und Monat.
    """)
    return


@app.cell
def _():
    monat_umsatz = None
    monat_umsatz
    return (monat_umsatz,)


@app.cell
def _(df, mo, monat_umsatz, pd, pruefhinweis):
    _erwartet_monat = (
        df.assign(Monat=df["Datum"].dt.to_period("M").astype(str))
        .groupby("Monat", as_index=False)["Umsatz"]
        .sum()
        .sort_values("Monat")
        .reset_index(drop=True)
    )
    _status_monat = None
    if monat_umsatz is not None:
        _status_monat = (
            isinstance(monat_umsatz, pd.DataFrame)
            and list(monat_umsatz.columns) == ["Monat", "Umsatz"]
            and monat_umsatz.sort_values("Monat")["Umsatz"].round(2).tolist()
            == _erwartet_monat["Umsatz"].round(2).tolist()
        )
    _rueckmeldung_monat = pruefhinweis(
        _status_monat,
        "Monatsumsätze",
        "Prüfe, ob du die Daten nach Monat gruppiert und `Umsatz` summiert hast.",
    )
    if monat_umsatz is None:
        _ausgabe_monat = _rueckmeldung_monat
    else:
        _ausgabe_monat = mo.vstack(
            [_rueckmeldung_monat, monat_umsatz.head()], gap=1
        )
    _ausgabe_monat
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Aufgabe 2 · Umsatz nach Region

    Berechne eine Series `region_umsatz`, deren Index die Region und deren Wert der aufsummierte Umsatz ist. Sortiere die Series vom höchsten zum niedrigsten Umsatz.
    """)
    return


@app.cell
def _():
    region_umsatz = None
    region_umsatz
    return (region_umsatz,)


@app.cell
def _(df, mo, pd, plt, pruefhinweis, region_umsatz):
    _erwartet_region = (
        df.groupby("Region")["Umsatz"].sum().sort_values(ascending=False)
    )
    _status_region = None
    if region_umsatz is not None:
        _status_region = (
            isinstance(region_umsatz, pd.Series)
            and region_umsatz.sort_values(ascending=False).round(2).to_dict()
            == _erwartet_region.round(2).to_dict()
        )
    _rueckmeldung_region = pruefhinweis(
        _status_region,
        "Umsatz nach Region",
        "Nutze `groupby` und `sum`. Sortiere für die Rückmeldung absteigend.",
    )
    if region_umsatz is None:
        _ausgabe_region = _rueckmeldung_region
    else:
        _fig_region, _ax_region = plt.subplots(
            figsize=(8, 3.5), layout="constrained"
        )
        region_umsatz.sort_values().plot(kind="barh", ax=_ax_region)
        _ax_region.set(xlabel="Umsatz in Euro", ylabel="Region")
        _ausgabe_region = mo.vstack([_rueckmeldung_region, _fig_region], gap=1)
    _ausgabe_region
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Aufgabe 3 · Umsatzverteilung

    Zeichne ein Histogramm mit 20 Intervallen. Speichere die Rückgabe der Plot-Methode in `hist_umsatz`.

    Hinweis: `df["Umsatz"].plot(kind="hist", bins=20)` liefert eine Axes zurück.
    """)
    return


@app.cell
def _():
    hist_umsatz = None
    hist_umsatz
    return (hist_umsatz,)


@app.cell
def _(hist_umsatz, mo, pruefhinweis):
    _status_hist = None
    if hist_umsatz is not None:
        _status_hist = (
            hasattr(hist_umsatz, "patches") and len(hist_umsatz.patches) == 20
        )
    _rueckmeldung_hist = pruefhinweis(
        _status_hist,
        "Histogramm",
        'Verwende die Umsatzspalte, `kind="hist"` und 20 Intervalle.',
    )
    if hist_umsatz is None:
        _ausgabe_hist = _rueckmeldung_hist
    else:
        hist_umsatz.set(
            title="Umsatz pro Bestellung",
            xlabel="Umsatz in Euro",
            ylabel="Anzahl Bestellungen",
        )
        _ausgabe_hist = mo.vstack(
            [_rueckmeldung_hist, hist_umsatz.figure], gap=1
        )
    _ausgabe_hist
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Aufgabe 4 · Interaktiver Vergleich

    Erzeuge mit Plotly ein Balkendiagramm `fig_kategorie`, das den aufsummierten Umsatz je Kategorie zeigt.

    ```python
    umsatz_kategorie = df.groupby("Kategorie", as_index=False)["Umsatz"].sum()
    fig_kategorie = px.bar(umsatz_kategorie, x="Kategorie", y="Umsatz")
    ```

    Beim Überfahren mit der Maus zeigt Plotly die Kategorie und den zugehörigen Umsatz.
    """)
    return


@app.cell
def _():
    fig_kategorie = None
    fig_kategorie
    return (fig_kategorie,)


@app.cell
def _(df, fig_kategorie, mo, pruefhinweis):
    _status_plotly = None
    if fig_kategorie is not None:
        _status_plotly = (
            hasattr(fig_kategorie, "data")
            and len(fig_kategorie.data) == 1
            and len(fig_kategorie.data[0].x) == df["Kategorie"].nunique()
        )
    _rueckmeldung_plotly = pruefhinweis(
        _status_plotly,
        "Plotly-Diagramm",
        "Prüfe, ob die gruppierte Tabelle an `px.bar` übergeben wird.",
    )
    if fig_kategorie is None:
        _ausgabe_plotly = _rueckmeldung_plotly
    else:
        _ausgabe_plotly = mo.vstack(
            [_rueckmeldung_plotly, fig_kategorie], gap=1
        )
    _ausgabe_plotly
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Interaktive Auswahl

    Wähle eine Region und eine Produktkategorie. Die Auswertung wird direkt unter den Auswahlfeldern aktualisiert.
    """)
    return


@app.cell(hide_code=True)
def _(df, mo):
    _regionen = ["Alle"] + sorted(df["Region"].dropna().unique().tolist())
    _kategorien = ["Alle"] + sorted(df["Kategorie"].dropna().unique().tolist())
    region_auswahl = mo.ui.dropdown(
        options=_regionen, value="Alle", label="Region"
    )
    kategorie_auswahl = mo.ui.dropdown(
        options=_kategorien, value="Alle", label="Kategorie"
    )
    return kategorie_auswahl, region_auswahl


@app.cell
def _(df, kategorie_auswahl, mo, pd, px, region_auswahl):
    _maske_region = (
        pd.Series(True, index=df.index)
        if region_auswahl.value == "Alle"
        else df["Region"].eq(region_auswahl.value)
    )
    _maske_kategorie = (
        pd.Series(True, index=df.index)
        if kategorie_auswahl.value == "Alle"
        else df["Kategorie"].eq(kategorie_auswahl.value)
    )
    _auswahl_df = df.loc[_maske_region & _maske_kategorie]
    _auswahl_monat = (
        _auswahl_df.assign(
            Monat=_auswahl_df["Datum"].dt.to_period("M").astype(str)
        )
        .groupby("Monat", as_index=False)["Umsatz"]
        .sum()
    )
    _fig_auswahl = px.line(
        _auswahl_monat,
        x="Monat",
        y="Umsatz",
        markers=True,
        title=f"Umsatz pro Monat · {region_auswahl.value} · {kategorie_auswahl.value}",
        labels={"Monat": "Monat", "Umsatz": "Umsatz in Euro"},
    )
    mo.vstack(
        [
            mo.hstack(
                [region_auswahl, kategorie_auswahl], widths=[1, 1], gap=1
            ),
            mo.md(f"**{len(_auswahl_df)} Bestellungen**"),
            _fig_auswahl,
        ],
        gap=1,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Rückblick

    Gute Diagramme passen zur Frage und beschriften Achsen samt Einheiten. Matplotlib gibt Kontrolle über die Grafik. Seaborn erleichtert statistische Diagramme. Plotly ergänzt Interaktion.

    **Zusatz:** Probiere für Aufgabe 1 ein Linien- oder für Aufgabe 2 ein horizontales Balkendiagramm aus. Ergänze jeweils einen Titel und beschreibe das wichtigste Muster in einem Satz.
    """)
    return


if __name__ == "__main__":
    app.run()
