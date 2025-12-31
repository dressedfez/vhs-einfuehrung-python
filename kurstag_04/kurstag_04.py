# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "openpyxl==3.1.5",
#     "pandas==2.3.3",
#     "polars==1.36.1",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    import polars as pl
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Datenanalyse mit Pandas
    ## Einführung in Pandas Konzepte

    Das normale Vorgehen ist Daten aus Dateien, wie z.B. CSV oder Excel einzulesen und mittels Pandas zu analysieren und/oder darzustellen.

    Damit wir aber verschiedene Konzepte von Pandas besser verstehen können, werden wir hier Daten "manuell" erstellen und
    so die Hauptdatenstrukturen kennenlernen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Die Hauptdatenstruktur bei Pandas (und Polars) sind DataFrames, welche aus mehreren Series (bzw. Spalten) bestehen.

    <div align="center">
    <img src="./public/01_table_dataframe.svg"/>
    </div>

    Eine Serie (Series) ist eine eindimensionale Datenstruktur, die eine Liste von Werten mit einem zugehörigen Index darstellt.

    > Jede Spalte (column) in einem DataFrame ist eine Serie (Series).

    <div align="center">
    <img src="./public/01_table_series.svg"/>
    </div>

    ### Erzeugung einer Series
    """)
    return


@app.cell
def _(pd):
    _series = pd.Series(
        data=[10, 20, 30, 40]
        # , index=['a', 'b', 'c', 'd']
    )
    _series
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In dieser Form können wir eine Series erzeugen, indem wir eine Liste von Werten angeben. Optional können wir auch einen Index angeben. Um einen DataFrame zu erzeugen, benötigen wir mehrere Series. Außerdem wäre es wichtig, den Spalten Name zu geben.

    Erzeugen wir als nächstes einen DataFrame mit mehreren Series.
    """)
    return


@app.cell
def _(pd):
    age_series = pd.Series(data=[25, 30, 35, 40], name="Age")
    name_series = pd.Series(data=["Alice", "Bob", "Charlie", "David"], name="Name")
    weight_series = pd.Series(data=[55.0, 75.5, 68.0, 82.3], name="Weight")
    sex_series = pd.Series(data=["F", "M", "M", "M"], name="Sex")
    df_people = pd.DataFrame(
        {
            age_series.name: age_series,
            name_series.name: name_series,
            weight_series.name: weight_series,
            sex_series.name: sex_series,
        }
    )
    df_people
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// admonition
    **Übungen**
    1. Untersuche welche Methoden auf dem DataFrame-Objekt zur Verfügung stehen.
    2. Was macht `describe()`?
    3. Was macht `info()`?
    4. Finde den `max` und `min`-Wert in den numerischen Spalten.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Einlesen von Daten

    Für das Einlesen von Daten wird von Pandas eine Vielzahl von Funktionen bereitgestellt, die es ermöglichen, Daten aus verschiedenen Formaten zu laden. Die am häufigsten verwendeten Funktionen sind:
    - `pd.read_csv()`: Zum Einlesen von CSV-Dateien.
    - `pd.read_excel()`: Zum Einlesen von Excel-Dateien.
    - `pd.read_json()`: Zum Einlesen von JSON-Dateien.
    - `pd.read_sql()`: Zum Einlesen von Daten aus SQL-Datenbanken.
    - `pd.read_parquet()`: Zum Einlesen von Parquet-Dateien.
    - `pd.read_feather()`: Zum Einlesen von Feather-Dateien.
    -  etc


    /// tip
    Neben dem Einlesen von lokalen Dateien können Daten auch direkt aus dem Internet geladen werden. Hier Beispiele für das lokale und internet-basierte Einlesen:
    - **lokales Einlesen**:
      ```python
      df_titanic = pd.read_csv("c:\daten\titanic.csv")
      ```
    - **internet-basiertes** Einlesen:
      ```python
       df_titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
      ```
    ///
    """)
    return


@app.cell
def _(pd):
    df_titanic = pd.read_csv(
        "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
    )
    return (df_titanic,)


@app.cell
def _(df_titanic):
    df_titanic.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// admonition
    **Übung:**
    1. Lese die lokalen Dateien CSV- und Excel-Dateien ein und führe die Methoden `describe()` und `info()` darauf aus.
    2. Was machen die Mehtoden `head()` und `tail()` auf den `DataFrame`?
    3. Welche Argumente nehmen diese Methoden an?
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Schreiben von Daten

    Das Schreiben von Daten ist ebenso wichtig wie das Einlesen. Pandas bietet verschiedene Funktionen zum Exportieren von DataFrames in verschiedene Formate. Die am häufigsten verwendeten Funktionen sind:
    - `df.to_csv()`: Zum Exportieren von DataFrames in CSV-Dateien.
    - `df.to_excel()`: Zum Exportieren von DataFrames in Excel-Dateien.
    - `df.to_json()`: Zum Exportieren von DataFrames in JSON-Dateien.
    - `df.to_sql()`: Zum Exportieren von DataFrames in SQL-Datenbanken.
    - `df.to_parquet()`: Zum Exportieren von DataFrames in Parquet-Dateien.
    - `df.to_feather()`: Zum Exportieren von DataFrames in Feather-Dateien.
    - etc

    Das folgende Beispiel zeigt, wie man den `DataFrame` zu den Studenten-Noten in eine
    Excel-Datei exportiert und eine Parquet-Datei speichert.

    ```python
    students.to_excel("students_grades.xlsx", index=False)
    ```

    und in eine Parquet-Datei:

    ```python
    students.to_parquet("students_grades.parquet", index=False)
    ```

    /// admonition
    **Übung:**
    1. Exportiere den `df_titanic` DataFrame in eine Parquet und eine Excel-Datei.
    2. Nutze den `timer` aus dem `timeit` Paket, um die Zeit für das Schreiben der Dateien zu messen.
       Was dauert länger?
    3. Wie groß sind die Dateien im Dateisystem? Welche ist kleiner?
    ///
    """)
    return


@app.cell
def _():
    from timeit import default_timer as timer
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
