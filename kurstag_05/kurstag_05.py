# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.19.2",
#     "matplotlib==3.10.8",
#     "mcp==1.25.0",
#     "numpy==2.4.2",
#     "openpyxl==3.1.5",
#     "pandas==2.3.3",
#     "polars==1.36.1",
# ]
# ///

import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import pandas as pd
    import polars as pl
    import numpy as np

    return np, pd


@app.cell
def _():
    import matplotlib.pyplot as plt

    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Einführung matplotlib

    ### Matplotlib

    Matplotlib ist eine weit verbreitete Bibliothek zur Erstellung von statischen, animierten und interaktiven Visualisierungen in Python. Sie bietet eine Vielzahl von Funktionen zur Erstellung von Diagrammen wie Linien-, Balken-, Kreisdiagrammen und mehr.

    Matplotlib ist besonders nützlich für die Erstellung von wissenschaftlichen Grafiken und bietet umfangreiche Anpassungsmöglichkeiten.

    Es wird häufig in Kombination mit Pandas verwendet, um Daten direkt aus DataFrames zu visualisieren, aber kann auch mit anderen Datenquellen genutzt werden.

    Darstellungen in Matplotlib haben einen bestimmten Aufbau, den die folgende Abbildung zeigt:

    <div align="center">
      <img src="https://matplotlib.org/stable/_images/anatomy.png" alt="Matplotlib Diagramm Aufbau" width="500"/>
    </div>

    Folgende Komponenten sind dabei wichtig:
    - **Figure**: Das gesamte Diagramm oder die gesamte Grafik.
    - **Axes**: Der Bereich, in dem die Daten dargestellt werden (kann mehrere pro Figure geben).
    - **Axis**: Die Achsen innerhalb der Axes (x-Achse, y-Achse).
    - **Artist**: Die eigentlichen grafischen Elemente wie Linien, Texte, etc.
    - **Plot**: Die spezifische Darstellung der Daten (z.B. Linien, Balken).
    - **Subplot**: Ein spezieller Bereich innerhalb der Figure, der eine einzelne Axes enthält.
    - **Tick**: Die Markierungen auf den Achsen, die die Skala anzeigen.
    - **Legend**: Die Legende, die die Bedeutung der verschiedenen grafischen Elemente erklärt.
    - **Grid**: Das Raster, das die Lesbarkeit der Daten verbessert.
    - **Title**: Der Titel des Diagramms.
    - **Label**: Die Beschriftungen der Achsen.
    - **Annotation**: Zusätzliche Informationen, die zu bestimmten Punkten im Diagramm hinzugefügt werden können.
    - **Colorbar**: Eine Leiste, die die Farbskala für bestimmte Diagrammtypen anzeigt.
    - **Layout**: Die Anordnung der verschiedenen Komponenten innerhalb der Figure.

    Eine Figure lässt sich mit folgenden Schritten erstellen:
    """)
    return


@app.cell
def _(plt):
    fig1 = plt.figure(
        figsize=(4, 2), facecolor="lightskyblue", layout="constrained"
    )
    fig1
    return (fig1,)


@app.cell
def _(fig1):
    fig1.suptitle("A nice Matplotlib Figure")
    return


@app.cell
def _(fig1):
    ax1 = fig1.add_subplot()
    ax1
    return (ax1,)


@app.cell
def _(ax1):
    ax1.set_title("Axes", loc="left", fontstyle="oblique", fontsize="medium")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Lasst uns zunächst eine einfache Grafik mit den bis hier her gelernten Methoden erstellen.
    """)
    return


@app.cell
def _(plt):
    # Funktion vorbereiten
    delta_x = 0.1
    x_range = [x * delta_x for x in range(-100, 101)]
    y = [x**2 for x in x_range]

    # Zufallsdaten erstellen
    import random

    y_random = [x**2 + random.uniform(-10, 10) for x in x_range]


    # Erlaube die Verwendung von LaTeX in den Texten
    plt.rcParams["text.usetex"] = True

    # Grafik erstellen
    fig2 = plt.figure(figsize=(10, 5))
    ax2 = fig2.add_subplot()

    # Funktion plotten
    ax2.plot(x_range, y, color="blue")
    # Messpunkte plotten
    ax2.scatter(x_range, y_random, color="red", s=10)

    ax2.set_xlabel(r"$x$", fontsize=16)
    ax2.set_ylabel(r"$f(x) = x^2$", fontsize=16, color="blue")
    ax2_label_x = 11.4  # x-Position für die y-Achsenbeschriftung
    ax2_label_y = 50  # y-Position für die y-Achsenbeschriftung
    ax2.text(
        ax2_label_x,
        ax2_label_y,
        r"Messpunkte",
        rotation=90,
        fontsize=17,
        color="red",
        ha="center",
    )

    ax2.grid(True, which="both", linestyle="--", linewidth=0.5)


    fig2
    return


@app.cell
def _(np, plt):
    plt.rcParams["text.usetex"] = False
    # Create some fake data.
    x1 = np.linspace(0.0, 5.0)
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    x2 = np.linspace(0.0, 5.0, 100)
    y2 = np.cos(2 * np.pi * x2)

    fig3, (ax31, ax32) = plt.subplots(2, 1)
    fig3.suptitle("A tale of 2 subplots")

    ax31.plot(x1, y1, "o-")
    ax31.set_ylabel("Damped oscillation")

    ax32.plot(x2, y2, ".-")
    ax32.set_xlabel("time (s)")
    ax32.set_ylabel("Undamped")
    fig3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Übungen
    1. Erstellen Sie ein Histogramm der Altersverteilung der Passagiere auf der Titanic.
    2. Erstellen Sie ein Balkendiagramm, das die Anzahl der überlebenden und nicht überlebenden Passagiere zeigt.
    3. Erstellen Sie ein Boxplot, das die Verteilung der Fahrpreise (Fare) für jede Passagierklasse (Pclass) zeigt.
    ///
    """)
    return


@app.cell
def _(pd):
    df_titanic = pd.read_csv(
        "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
    )
    return (df_titanic,)


@app.cell(disabled=True, hide_code=True)
def _(df_titanic):
    # Lösung zu Übung 1
    df_titanic["Age"].plot(
        kind="hist",
        bins=20,
        xlabel="Age",
        ylabel="Anzahl Personen",
        title="Altersverteilung",
    )
    return


@app.cell(disabled=True, hide_code=True)
def _(df_titanic):
    # Lösung zu Übung 2
    ax = df_titanic["Survived"].value_counts().plot(kind="bar")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Nicht überlebt", "Überlebt"])
    ax.set_ylabel("Anzahl Personen")
    ax.set_title("Überlebensstatus")
    return


@app.cell(disabled=True, hide_code=True)
def _(df_titanic, plt):
    # Lösung zu Übung 3: Erstellen Sie ein Boxplot, das die Verteilung der Fahrpreise (Fare) für jede Passagierklasse (Pclass) zeigt.

    df_titanic.boxplot(column="Fare", by="Pclass")
    plt.suptitle("Fahrpreise nach Passagierklasse")
    plt.xlabel("Passagierklasse")
    plt.ylabel("Fahrpreis (Fare)")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Beispielanalyse
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
