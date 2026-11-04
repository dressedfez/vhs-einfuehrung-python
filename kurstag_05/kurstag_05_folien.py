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
# ruff: noqa: B018, PLR1711, UP003

import marimo

__generated_with = "0.25.2"
app = marimo.App(
    width="medium",
    layout_file="layouts/kurstag_05_folien.slides.json",
)


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
    def beispiel(titel, erklaerung, code, ergebnis):
        return mo.vstack(
            [
                mo.md(
                    f"## {titel}\n\n{erklaerung}\n\n"
                    f"**Python-Code**\n\n```python\n{code}\n```"
                ),
                ergebnis,
            ],
            gap=1,
        )

    return beispiel, pd, plt, px, sns


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
        <h1 class="vhs-kursstart-title">Kurstag 5<span>Daten visualisieren</span></h1>
        <p class="vhs-kursstart-summary">Mit Matplotlib, Seaborn und Plotly aus Tabellen verständliche Diagramme machen.</p>
        <div class="vhs-kursstart-motto">Frage <b>·</b> Diagramm <b>·</b> Aussage</div>
      </div>
      <div class="vhs-kursstart-art" aria-hidden="true"><div class="vhs-kursstart-core">vis</div><i class="vhs-kursstart-dot one"></i><i class="vhs-kursstart-dot two"></i><i class="vhs-kursstart-dot three"></i><i class="vhs-kursstart-dot four"></i><i class="vhs-kursstart-dot five"></i></div>
    </section>
    """
    mo.Html(_cover_html.replace("__VHS_LOGO__", _logo_data))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Unser Weg heute

    1. **Fragen sichtbar machen:** Welcher Diagrammtyp passt zu welcher Frage?
    2. **Diagramme erstellen:** Matplotlib und Pandas für Linien, Balken, Histogramme und Streudiagramme.
    3. **Verteilungen vergleichen:** Seaborn für übersichtliche statistische Grafiken.
    4. **Ergebnisse erkunden:** Plotly und Marimo für interaktive Auswahlen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Eine Frage bestimmt das Diagramm

    Wir arbeiten mit den Verkaufsdaten aus Kurstag 4. Ein Diagramm soll eine konkrete Frage beantworten, zum Beispiel:

    **Wie verändert sich der Umsatz im Laufe des Jahres?**

    Dafür brauchen wir zuerst eine passende Zusammenfassung der Tabelle und danach eine Darstellung, die den zeitlichen Verlauf zeigt.
    """)
    return


@app.cell
def _(beispiel, mo, pd):
    verkauf = pd.read_excel(
        "data/online_shop_verkaufsdaten.xlsx", sheet_name="Verkaufsdaten"
    )
    verkauf["Datum"] = pd.to_datetime(verkauf["Datum"])
    _ueberblick = mo.vstack(
        [
            mo.md(
                f"**{len(verkauf)} Bestellungen**  \n"
                f"**Zeitraum:** {verkauf['Datum'].min():%d.%m.%Y} bis "
                f"{verkauf['Datum'].max():%d.%m.%Y}"
            ),
            verkauf[["Datum", "Produkt", "Kategorie", "Umsatz"]].head(5),
        ],
        gap=1,
    )
    beispiel(
        "Die Beispieldaten",
        "Wir verwenden die Verkaufsdaten aus Kurstag 4. Die Spalte `Datum` wird in Datumswerte umgewandelt.",
        'verkauf = pd.read_excel("data/online_shop_verkaufsdaten.xlsx", sheet_name="Verkaufsdaten")\nverkauf["Datum"] = pd.to_datetime(verkauf["Datum"])\nverkauf.head()',
        _ueberblick,
    )
    return (verkauf,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Diagrammtyp und Frage

    - **Zeitlicher Verlauf:** Ein Liniendiagramm zeigt, wie sich Werte über die Zeit verändern.
    - **Vergleich von Gruppen:** Ein Balkendiagramm vergleicht Kategorien oder Regionen.
    - **Verteilung:** Histogramm und Boxplot zeigen, wie Werte verteilt sind.
    - **Zusammenhang zweier Zahlen:** Ein Streudiagramm zeigt, ob zwei Größen gemeinsam variieren.

    Die Wahl des Diagramms hängt davon ab, was die Daten beantworten sollen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Bausteine eines Matplotlib-Diagramms

    - **Figure:** die gesamte Abbildung, in die alles gezeichnet wird.
    - **Axes:** der eigentliche Zeichenbereich mit Daten und Achsen.
    - **Axis:** eine einzelne x- oder y-Achse mit Skala und Teilstrichen.

    In der üblichen Schreibweise erzeugt `plt.subplots()` Figure und Axes gemeinsam. Über `ax` ergänzen wir Daten, Titel und Beschriftungen.
    """)
    return


@app.cell
def _(beispiel, pd, plt, verkauf):
    _umsatz_monat = (
        verkauf.assign(Monat=verkauf["Datum"].dt.to_period("M").astype(str))
        .groupby("Monat", as_index=False)["Umsatz"]
        .sum()
    )
    _fig_monat, _ax_monat = plt.subplots(figsize=(8, 3.6), layout="constrained")
    _ax_monat.plot(_umsatz_monat["Monat"], _umsatz_monat["Umsatz"], marker="o")
    _ax_monat.set_title("Monatlicher Umsatz")
    _ax_monat.set_xlabel("Monat")
    _ax_monat.set_ylabel("Umsatz in Euro")
    _ax_monat.tick_params(axis="x", rotation=45)
    _ax_monat.grid(axis="y", alpha=0.3)
    beispiel(
        "Umsatz im Jahresverlauf",
        "Wir fassen die Bestellungen zunächst je Monat zusammen. Die Linie macht den zeitlichen Verlauf sichtbar.",
        'verkauf.assign(Monat=verkauf["Datum"].dt.to_period("M").astype(str))\n    .groupby("Monat", as_index=False)["Umsatz"].sum()\n\nfig, ax = plt.subplots()\nax.plot(monat["Monat"], monat["Umsatz"], marker="o")\nax.set(xlabel="Monat", ylabel="Umsatz in Euro", title="Monatlicher Umsatz")',
        _fig_monat,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Achsen und Einheiten

    Eine lesbare Grafik beantwortet drei Fragen sofort:

    - Was wird verglichen oder gemessen?
    - Welche Einheit haben die Werte?
    - Welchen Zeitraum oder welche Gruppe zeigt die Grafik?

    Beschriftungen wie `Umsatz in Euro` sind genauer als ein allgemeines `Wert`. Ein Titel sollte den Inhalt nennen, nicht nur `Diagramm`.
    """)
    return


@app.cell
def _(beispiel, pd, plt, verkauf):
    _umsatz_region = (
        verkauf.groupby("Region", as_index=False)["Umsatz"]
        .sum()
        .sort_values("Umsatz", ascending=False)
    )
    _fig_region, _ax_region = plt.subplots(figsize=(8, 3.8), layout="constrained")
    _ax_region.bar(_umsatz_region["Region"], _umsatz_region["Umsatz"], color="#17668e")
    _ax_region.set_title("Umsatz nach Region")
    _ax_region.set_xlabel("Region")
    _ax_region.set_ylabel("Umsatz in Euro")
    _ax_region.tick_params(axis="x", rotation=25)
    beispiel(
        "Umsatz nach Region vergleichen",
        "Balken eignen sich, wenn wir Gruppen vergleichen. Vor dem Zeichnen ordnen wir die Regionen nach Umsatz.",
        'umsatz_region = verkauf.groupby("Region", as_index=False)["Umsatz"].sum()\numsatz_region = umsatz_region.sort_values("Umsatz", ascending=False)\n\nfig, ax = plt.subplots()\nax.bar(umsatz_region["Region"], umsatz_region["Umsatz"])\nax.set(xlabel="Region", ylabel="Umsatz in Euro", title="Umsatz nach Region")',
        _fig_region,
    )
    return


@app.cell
def _(beispiel, pd, plt, verkauf):
    _umsatz_kategorie = (
        verkauf.groupby("Kategorie")["Umsatz"].sum().sort_values()
    )
    _fig_kategorie, _ax_kategorie = plt.subplots(
        figsize=(8, 3.8), layout="constrained"
    )
    _ax_kategorie.barh(
        _umsatz_kategorie.index, _umsatz_kategorie.values, color="#ed6a32"
    )
    _ax_kategorie.set_title("Umsatz nach Produktkategorie")
    _ax_kategorie.set_xlabel("Umsatz in Euro")
    _ax_kategorie.set_ylabel("Kategorie")
    beispiel(
        "Balken horizontal anordnen",
        "Bei längeren Kategorienamen bleibt ein horizontales Balkendiagramm leichter lesbar.",
        'umsatz_kategorie = verkauf.groupby("Kategorie")["Umsatz"].sum().sort_values()\numsatz_kategorie.plot(kind="barh")\nplt.xlabel("Umsatz in Euro")',
        _fig_kategorie,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Verteilung und Histogramm

    Ein Histogramm teilt eine Zahlenachse in Intervalle ein. Die Höhe eines Balkens zeigt, wie viele Werte in das jeweilige Intervall fallen.

    `bins` legt die Anzahl oder Lage der Intervalle fest. Sehr wenige Intervalle verbergen Unterschiede. Sehr viele machen das Muster unruhig.
    """)
    return


@app.cell
def _(beispiel, plt, verkauf):
    _fig_hist, _ax_hist = plt.subplots(figsize=(8, 3.6), layout="constrained")
    _ax_hist.hist(verkauf["Umsatz"], bins=20, color="#39a5d6", edgecolor="white")
    _ax_hist.set_title("Verteilung der Umsätze pro Bestellung")
    _ax_hist.set_xlabel("Umsatz in Euro")
    _ax_hist.set_ylabel("Anzahl Bestellungen")
    beispiel(
        "Viele Bestellumsätze zusammenfassen",
        "Die Grafik zeigt die Häufigkeit der einzelnen Umsatzbereiche. Jeder Datensatz trägt zu genau einem Balken bei.",
        'fig, ax = plt.subplots()\nax.hist(verkauf["Umsatz"], bins=20)\nax.set(xlabel="Umsatz in Euro", ylabel="Anzahl Bestellungen")',
        _fig_hist,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Boxplots mit Seaborn

    Ein Boxplot vergleicht Verteilungen zwischen Gruppen. Die Linie in der Box markiert den Median. Die Box zeigt den mittleren Bereich der Werte.

    Seaborn baut auf Matplotlib auf und bietet Funktionen für statistische Diagramme. Mit `hue` können wir eine zusätzliche Gruppierung kenntlich machen.
    """)
    return


@app.cell
def _(beispiel, plt, sns, verkauf):
    _fig_box, _ax_box = plt.subplots(figsize=(8, 3.8), layout="constrained")
    sns.boxplot(
        data=verkauf,
        x="Kategorie",
        y="Umsatz",
        hue="Kategorie",
        legend=False,
        ax=_ax_box,
    )
    _ax_box.set_title("Umsatzverteilung nach Kategorie")
    _ax_box.set_xlabel("Kategorie")
    _ax_box.set_ylabel("Umsatz pro Bestellung in Euro")
    _ax_box.tick_params(axis="x", rotation=20)
    beispiel(
        "Umsatzverteilungen vergleichen",
        "Der Boxplot zeigt, wie stark einzelne Bestellungen innerhalb einer Kategorie streuen. Punkte außerhalb der Whisker sind auffällige Werte.",
        'sns.boxplot(data=verkauf, x="Kategorie", y="Umsatz", hue="Kategorie", legend=False, ax=ax)\nax.set_ylabel("Umsatz pro Bestellung in Euro")',
        _fig_box,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Zusammenhänge mit Streudiagrammen

    Jeder Punkt steht für eine Bestellung. Die Lage zeigt Preis und Menge gemeinsam.

    Ein Streudiagramm kann einen Zusammenhang sichtbar machen. Es beweist für sich allein nicht, dass eine Größe die andere verursacht.
    """)
    return


@app.cell
def _(beispiel, plt, verkauf):
    _fig_streu, _ax_streu = plt.subplots(figsize=(8, 3.7), layout="constrained")
    _ax_streu.scatter(
        verkauf["Preis"], verkauf["Menge"], alpha=0.65, color="#147e9e"
    )
    _ax_streu.set_title("Preis und Bestellmenge")
    _ax_streu.set_xlabel("Preis pro Stück in Euro")
    _ax_streu.set_ylabel("Menge pro Bestellung")
    _ax_streu.grid(alpha=0.2)
    beispiel(
        "Preis und Menge als Punkte",
        "Die Punktwolke zeigt die Kombinationen aus Einzelpreis und Bestellmenge. Ein einzelner Punkt entspricht einer Zeile der Tabelle.",
        'fig, ax = plt.subplots()\nax.scatter(verkauf["Preis"], verkauf["Menge"], alpha=0.65)\nax.set(xlabel="Preis pro Stück in Euro", ylabel="Menge pro Bestellung")',
        _fig_streu,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Schneller zeichnen mit Pandas

    Für eine schnelle erste Grafik kann Pandas direkt die Daten zeichnen:

    ```python
    umsatz_region.set_index("Region")["Umsatz"].plot(kind="bar")
    ```

    Pandas verwendet dafür Matplotlib. Wenn wir Titel, Achsen und Layout genauer anpassen möchten, greifen wir auf Figure und Axes zu.
    """)
    return


@app.cell
def _(beispiel, plt, verkauf):
    _umsatz_zahlungsmittel = verkauf.groupby("Zahlungsmethode")["Umsatz"].sum()
    _fig_pandas, _ax_pandas = plt.subplots(
        figsize=(8, 3.8), layout="constrained"
    )
    _umsatz_zahlungsmittel.sort_values().plot(
        kind="barh", ax=_ax_pandas, color="#f6b627"
    )
    _ax_pandas.set_title("Umsatz nach Zahlungsmethode")
    _ax_pandas.set_xlabel("Umsatz in Euro")
    _ax_pandas.set_ylabel("Zahlungsmethode")
    beispiel(
        "Pandas für einen schnellen Entwurf",
        "Die `plot`-Methode zeichnet die Gruppensummen direkt. Wir übergeben `ax`, damit die Grafik in unserem vorbereiteten Zeichenbereich erscheint.",
        'umsatz_zahlungsmittel = verkauf.groupby("Zahlungsmethode")["Umsatz"].sum()\nfig, ax = plt.subplots()\numsatz_zahlungsmittel.sort_values().plot(kind="barh", ax=ax)',
        _fig_pandas,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Interaktive Diagramme mit Plotly

    Plotly zeigt beim Überfahren mit der Maus zusätzliche Werte. Je nach Diagrammtyp können Teilnehmende zoomen, Bereiche auswählen und die Darstellung verschieben.

    Die pandas-Auswertung bleibt gleich. Wir übergeben die zusammengefasste Tabelle an Plotly Express.
    """)
    return


@app.cell
def _(beispiel, pd, px, verkauf):
    _plotly_region = (
        verkauf.groupby("Region", as_index=False)["Umsatz"]
        .sum()
        .sort_values("Umsatz", ascending=False)
    )
    _fig_plotly_region = px.bar(
        _plotly_region,
        x="Region",
        y="Umsatz",
        color="Region",
        title="Umsatz nach Region",
        labels={"Umsatz": "Umsatz in Euro", "Region": "Region"},
        hover_data={"Umsatz": ":.2f"},
    )
    _fig_plotly_region.update_layout(showlegend=False)
    beispiel(
        "Dieselbe Auswertung mit Plotly",
        "Die Balken zeigen dieselben Gruppensummen. Beim Überfahren erscheint der genaue Umsatz.",
        'region = verkauf.groupby("Region", as_index=False)["Umsatz"].sum()\nfig = px.bar(region, x="Region", y="Umsatz", color="Region", title="Umsatz nach Region")',
        _fig_plotly_region,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Eine gemeinsame Auswahl

    Wähle eine Region und eine Kategorie. Die Monatsgrafik und die Tabelle gehören zur selben Auswahl und aktualisieren sich gemeinsam.

    **Beobachte:** Wie verändert sich der Verlauf, wenn du statt einer Kategorie `Alle` auswählst?
    """)
    return


@app.cell(hide_code=True)
def _(mo, verkauf):
    _regionen = ["Alle"] + sorted(verkauf["Region"].dropna().unique().tolist())
    _kategorien = ["Alle"] + sorted(verkauf["Kategorie"].dropna().unique().tolist())
    auswahl_region = mo.ui.dropdown(
        options=_regionen, value="Alle", label="Region"
    )
    auswahl_kategorie = mo.ui.dropdown(
        options=_kategorien, value="Alle", label="Kategorie"
    )
    return auswahl_kategorie, auswahl_region


@app.cell
def _(auswahl_kategorie, auswahl_region, mo, pd, px, verkauf):
    _maske_region = (
        pd.Series(True, index=verkauf.index)
        if auswahl_region.value == "Alle"
        else verkauf["Region"].eq(auswahl_region.value)
    )
    _maske_kategorie = (
        pd.Series(True, index=verkauf.index)
        if auswahl_kategorie.value == "Alle"
        else verkauf["Kategorie"].eq(auswahl_kategorie.value)
    )
    _gefiltert = verkauf.loc[_maske_region & _maske_kategorie]
    _monat_auswahl = (
        _gefiltert.assign(Monat=_gefiltert["Datum"].dt.to_period("M").astype(str))
        .groupby("Monat", as_index=False)["Umsatz"]
        .sum()
    )
    _fig_auswahl = px.line(
        _monat_auswahl,
        x="Monat",
        y="Umsatz",
        markers=True,
        title=f"Umsatz pro Monat · {auswahl_region.value} · {auswahl_kategorie.value}",
        labels={"Monat": "Monat", "Umsatz": "Umsatz in Euro"},
    )
    mo.vstack(
        [
            mo.hstack([auswahl_region, auswahl_kategorie], widths=[1, 1], gap=1),
            mo.md(f"**{len(_gefiltert)} Bestellungen · {len(_monat_auswahl)} Monate**"),
            _fig_auswahl,
            _gefiltert[["Datum", "Produkt", "Kategorie", "Region", "Umsatz"]].head(6),
        ],
        gap=1,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Woran gute Diagramme zu erkennen sind

    - Titel und Achsen sagen, was die Zahlen zeigen und welche Einheiten gelten.
    - Die Skala beginnt bei Balkendiagrammen in der Regel bei null.
    - Farben unterscheiden Gruppen, wenn die Farbe dafür eine Bedeutung hat.
    - Die Darstellung passt zur Frage und zum Datentyp.
    - Eine sichtbare Beziehung wird nicht automatisch als Ursache erklärt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Übung: Eine Frage mit einem Diagramm beantworten

    Arbeite in dieser Reihenfolge:

    1. Formuliere die Frage und wähle die nötigen Spalten.
    2. Gruppiere oder filtere die Daten passend zur Frage.
    3. Wähle einen Diagrammtyp.
    4. Ergänze Titel, Achsen und Einheiten.
    5. Beschreibe in einem Satz, was die Grafik zeigt.
    """)
    return


@app.cell
def _(beispiel, pd, plt, verkauf):
    _uebung_umsatz = (
        verkauf.groupby("Kategorie", as_index=False)["Umsatz"]
        .sum()
        .sort_values("Umsatz", ascending=False)
    )
    _fig_uebung, _ax_uebung = plt.subplots(figsize=(8, 3.8), layout="constrained")
    _ax_uebung.bar(
        _uebung_umsatz["Kategorie"],
        _uebung_umsatz["Umsatz"],
        color="#17668e",
    )
    _ax_uebung.set_title("Umsatz nach Produktkategorie")
    _ax_uebung.set_xlabel("Kategorie")
    _ax_uebung.set_ylabel("Umsatz in Euro")
    _ax_uebung.tick_params(axis="x", rotation=20)
    beispiel(
        "Musterlösung: Umsatz nach Kategorie",
        "Die Tabelle fasst zuerst alle Bestellungen je Kategorie zusammen. Die Grafik vergleicht anschließend die Summen.",
        'umsatz = verkauf.groupby("Kategorie", as_index=False)["Umsatz"].sum()\nfig, ax = plt.subplots()\nax.bar(umsatz["Kategorie"], umsatz["Umsatz"])\nax.set(xlabel="Kategorie", ylabel="Umsatz in Euro", title="Umsatz nach Produktkategorie")',
        _fig_uebung,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Das Wichtigste

    - Die Frage bestimmt, wie wir Daten zusammenfassen und darstellen.
    - Matplotlib gibt genaue Kontrolle über Figure und Axes. Pandas bietet einen schnellen Einstieg.
    - Seaborn vereinfacht statistische Diagramme. Plotly ergänzt Mausinteraktion und Zoom.
    - Marimo kann Auswahlfelder direkt mit Diagramm und Tabelle verbinden.

    **Nächster Schritt:** Die gezeigten Auswertungen im Arbeitsheft selbst erstellen und beschreiben.
    """)
    return


if __name__ == "__main__":
    app.run()
