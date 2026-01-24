# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.19.2",
#     "matplotlib==3.10.8",
#     "mcp==1.25.0",
#     "openpyxl==3.1.5",
#     "pandas==2.3.3",
#     "polars==1.36.1",
# ]
# ///

import marimo

__generated_with = "0.19.6"
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

    Die Abbildungen in diesem Notebook habe ich von der Pandas Dokumentation übernommen: https://pandas.pydata.org/docs/index.html


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Auswahl und Filtern in DataFrames

    #### Auswahl von Spalten

    Die Auswahl von Spalten geschieht in Pandas DataFrames typischerweise durch Angabe des Spaltennamens in eckigen Klammern. Es ist auch möglich mehrere Spalten gleichzeitig auszuwählen.

    <div align="center">
    <img src="./public/03_subset_columns.svg"/>
    </div>

    **Beispiele:**
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic[["Name", "Age"]].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Man kann Spalten auch mithilfe des Attributzugriffs auswählen (gehr nur für eine Spalte):
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic.Name.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wichtig für die Auswahl von Spalten (und Zeilen) sind die Methoden `loc` und `iloc`. Mittels `iloc` können Zeilen und Spalten über ihre integer-basierten Positionen ausgewählt werden und mit `loc` über ihre Labels (Namen).
    """)
    return


@app.cell
def _(df_titanic):
    # Auswahl aller Zeilen, aber nur der Spalten "Name" und "Age"
    df_titanic.loc[:, ["Name", "Age"]].head()
    return


@app.cell
def _(df_titanic):
    # Auswahl aller Zeilen, aber nur der Spalten an Position 3 und 5
    # ACHTUNG: wenn sich die Spaltenreihenfolge ändert, ändert sich auch die Auswahl!
    df_titanic.iloc[:, [3, 5]].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Auswahl von Zeilen

    <div align="center">
    <img src="./public/03_subset_rows.svg"/>
    </div>

    **Beispiele:**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Die ersten Beispiele nutzten `iloc`, um Zeilen basierend auf ihrer Position auszuwählen. Dem Thema `loc` widmen wir uns später.
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic.iloc[0:5]  # Auswahl der ersten 5 Zeilen
    return


@app.cell
def _(df_titanic):
    # Auswahl der ersten Zeile (Zeilenindex 0) und der Spalte "Name" (Spaltenindex 3) und "Age" (Spaltenindex 5)
    df_titanic.iloc[[0], [3, 5]]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wenn man sich den letzten Befehl genau anschaut, sieht man eine unerwartete Notation, die
    Aufgrund von Dimensionalitätsregeln in Pandas notwendig ist.

    /// tip
    Merksatz 🧠

    In Pandas lieber „Listen statt Skalar“, wenn du Dimensionen behalten willst.
    ///
    """)
    return


@app.cell
def _(df_titanic):
    # Auswahl der ersten Zeile (Zeilenlabel 0) und der Spalte "Name" und "Age"
    df_titanic.iloc[[0, 5], [3, 5]]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Für `iloc` und `loc` gilt:
    - `df.iloc[zeilen_index, spalten_index]`
    - `df.loc[zeilen_label, spalten_label]`
    - Beide Methoden unterstützen sowohl einzelne Indizes/Labels als auch Listen von Indizes/Labels.
    - Sowohl `iloc` als auch `loc` unterstützen Slicing (Bereichsauswahl) für Zeilen und Spalten.
    - Bei `loc` sind die Endindizes im Slicing inklusive, während bei `iloc` die Endindizes exklusiv sind.
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic.loc[[0], ["Name", "Age"]]
    return


@app.cell
def _(df_titanic):
    df_titanic.index
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wie man sieht wird die Auswahl der Zeile über die `Index` - Spalte durchgeführt.

    Interessant wird es, wenn man die Auswahl der Zeilen über Bedingungen (Filter) durchführt. Diese Filterung kann
    mittels boolescher Arrays oder Bedingungen erfolgen.

    Hier zunächst ein Beispiel mit eines booleschen Arrays:
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic_bool = df_titanic["Age"] > 30
    df_titanic_bool.head()
    return (df_titanic_bool,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Mittels dieser booleschen Serie können wir nun den DataFrame filtern:
    """)
    return


@app.cell
def _(df_titanic, df_titanic_bool):
    df_titanic_older_than_30 = df_titanic.loc[df_titanic_bool]
    df_titanic_older_than_30.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **2-dimensionalle Filterung**

    Auswählen von Zeilen und Spalten mittels Pandas ist auch möglich und erlaubt einem zusammen mit *marimo* interaktive Tabellen zu erzeugen.

    <div align="center">
    <img src="./public/03_subset_columns_rows.svg"/>
    </div>

    Zum Beispiel kann man mittels Multiselect-Widget Spalten auswählen und mittels eines Filters Zeilen auswählen.
    Dies wird unten gemacht.
    """)
    return


@app.cell
def _(df_titanic, mo):
    ausgewaehlte_spalten = mo.ui.multiselect(df_titanic.columns)
    ausgewaehlte_spalten
    return (ausgewaehlte_spalten,)


@app.cell
def _(ausgewaehlte_spalten, df_titanic, df_titanic_bool):
    df_titanic.loc[df_titanic_bool, ausgewaehlte_spalten.value]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Übungen
    1. Filtere den DataFrame `df_people`, so dass nur Personen mit einem Alter über 30 Jahren enthalten sind.`
    2. Filtere den DataFrame `df_people`, so dass nur weibliche Personen über 30 Jahren enthalten sind.
    3. Filtere den DataFrame `students`, so dass nur Zeilen für Wintersemester enthalten sind.
    4. Erstelle ein DataFrame, der aus dem `students`-DataFrame nur die Studenten-ID und Note enthalten sind.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Erstellen von Spalten
    ### Erstellen einer Spalte mittels einer Ausgangsspalte

    Aus bereits bestehenden Spalten können neue Spalten erstellt werden. Zunächst schauen wir uns an, wie man mittels einer Spalte eine neue Spalte erstellt.
    <div align="center">
    <img src="./public/05_newcolumn_1.svg"/>
    </div>

    /// tip
    Merksatz 🧠
    Eine neue Spalte wird erstellt, indem man auf der linken Seite den neuen Spaltennamen in eckigen Klammern angibt und auf der rechten Seite den Ausdruck, der die Werte für die neue Spalte definiert.

    ```python
    df["new_column"] = <expression>
    ```
    ///
    **Beispiel:**
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic["percentage_fare"] = (
        df_titanic["Fare"] / df_titanic["Fare"].mean()
    ) * 100
    return


@app.cell
def _(df_titanic):
    df_titanic.columns
    return


@app.cell
def _(df_titanic):
    df_titanic[["Fare", "percentage_fare"]].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Erstellen einer Spalte mittels mehrerer Ausgangsspalten

    Der Normalfall ist das Erstellen einer neuen Spalte mittels mehrerer Ausgangsspalten. Hierfür können verschiedene Methoden genutzt werden, wie z.B. arithmetische Operationen, bedingte Logik oder Funktionen.

    <div align="center">
    <img src="./public/05_newcolumn_2.svg"/>
    </div>

    Analog zu dem Fall mit einer Ausgangsspalte können wir auch hier eine neue Spalte erstellen, indem wir auf der linken Seite den neuen Spaltennamen in eckigen Klammern angeben und auf der rechten Seite den Ausdruck, der die Werte für die neue Spalte definiert.

    **Beispiele:**
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic["age_fare_ratio"] = df_titanic["Age"] / df_titanic["Fare"]
    df_titanic[["Age", "Fare", "age_fare_ratio"]].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Statistische Auswertungen

    ### Aggregationen

    Der `DataFrame` stellt verschiedene Methoden zur Verfügung, um statistische Auswertungen durchzuführen. Dazu gehören Methoden wie `mean()`, `sum()`, `min()`, `max()`, `count()`, `std()` und viele mehr. Diese Methoden können auf den gesamten DataFrame oder auf einzelne Spalten angewendet werden. Sie machen natürlich nur  für numerische Spalten Sinn.
    """)
    return


@app.cell
def _(df_titanic):
    # Achtung: die Methode mean() ignoriert automatisch fehlende Werte (NaN)
    # und liefert eine Serie mit dem Mittelwert für jede numerische Spalte zurück.
    (
        df_titanic[["Age"]].mean(),
        df_titanic[["Age"]].sum() / df_titanic[["Age"]].count(),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Man kann diese statistischen Methoden auch auf mehrere Spalten gleichzeitig anwenden:
    """)
    return


@app.cell
def _(df_titanic):
    # Standardabweichung für mehrere Spalten
    df_titanic[["Age", "Fare"]].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Agregationen von gruppierten Daten

    Das Gruppieren von Daten nach Kategorien ist eine wichtige Funktion in Pandas. Mit der `groupby()`-Methode können Daten nach einer oder mehreren Spalten gruppiert werden, um aggregierte Statistiken für jede Gruppe zu berechnen.

    /// tip
     **Merksätze** 🧠

    Daten ohne Gruppierung sind Zahlen – Daten mit Gruppierung erzählen Geschichten.

    groupby ist der Übergang von Deskription zu Erklärung.
    ///

    **Beispiele:**
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic.groupby("Pclass")["Fare"].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Der preisliche Unterschied zwischen den Passagierklassen ist deutlich zu erkennen. Die erste Klasse war ca. 5-6 mal teurer als die dritte Klasse.
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic.groupby("Sex")["Survived"].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Die Wahrscheinlichkeit zu überleben hing stark vom Geschlecht ab. Frauen hatten eine deutlich höhere Überlebensrate als Männer.
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic.groupby(["Sex", "Pclass"])["Survived"].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Der Klassenunterschied zeigt sich auch hier deutlich. Frauen in der ersten Klasse hatten die höchste Überlebensrate, während Männer in der dritten Klasse die niedrigste Überlebensrate hatten.

    Als Frau in der dritten Klasse war die Überlebensrate immer noch höher als die der Männer in der ersten Klasse.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Anzahl pro Kategorie

    Für manche Auswertungen ist es interessnat die **Anzahl der Einträge pro Kategorie** zu kennen.

    **Beispiel**:

    Wir möchte wissen wie viele Personen jeweils in einer Klasse auf der Titanic waren.
    Dazu nutzt man:
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic["Pclass"].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    dies ist eine Abkürzung für
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic.groupby("Pclass")["Pclass"].count()
    return


@app.cell
def _(mo):
    mo.md(r"""
    /// note | Übungen
    1. Bestimme die Anzahl der Personen gruppiert nach Sex und pro Kabinenklasse.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pivotieren von Tabelle (DataFrames)

    Um die Beziehungen zwischen mehreren Variablen in einem DataFrame zu analysieren, kann es hilfreich sein, die Daten in eine Pivot-Tabelle umzuwandeln. Eine Pivot-Tabelle ermöglicht es, Daten zu aggregieren und neu zu organisieren, um Muster und Trends leichter erkennen zu können.

    Man unterscheited im Rahmen von Pandas zwischen den beiden Funktionen `pivot()` und `pivot_table()`. Erstere erlaubt nur die Umstrukturierung von Daten ohne Aggregation, während `pivot_table()` auch Aggregationsfunktionen unterstützt.

    /// tip
    **Merksätze** 🧠

    Das Pivotieren von Tabellen dient zur Umstruktierung (mit und ohne Aggregation), um tiefere Einblicke in die Struktur der
    Daten zu erlangen.

    1. pivot() dient zur Umstrukturierung von Daten ohne Aggregation.
    2. pivot_table() ermöglicht die Aggregation von Daten während der Umstrukturierung.

    ///

    Hier ein graphisches Beispiel für das reine Pivotieren ohne Aggregation:

    <div align="center">
        <img src="./public/07_pivot.svg"/>
    </div>

    Wie man sieht werden katogorische Daten aus aus Zeilen einer Spalte in Spalten umgewandelt, um die Tabelle (DataFrame) neu zu strukturieren.
    """)
    return


@app.cell
def _(df_titanic, pd):
    pivot_name_pclass_fare = pd.pivot(
        df_titanic, index="Name", columns="Pclass", values="Fare"
    )
    pivot_name_pclass_fare.head()
    # Das Problem mit den Integer Spaltennamen lösen wir im nächsten Beispiel.
    return


@app.cell
def _():
    # Folgendes funktioniert nicht, da es mehrere Werte pro Index gleich sind, d.h. die Zeilen der Tabelle nicht eindeutig sind.

    # pivot_sex_pclass_fare = pd.pivot(
    #    df_titanic,
    #    index="Sex",
    #    columns="Pclass",
    #    values="Fare"
    # )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Diese Grafik erläutern nochmals wo hier das Problem liegt. Wenn man als Spalte den Name wählt ist im gezeigten Beispiel der Name nicht eindeutig (nicht so in den Originaldaten der Titanic). Deshalb kann man in dem Beispiel, wie auch für den Fall, dass man `Sex` als Spalte nimmt, nicht pivotieren.

    <div align="center">
      <img alt="Test" src="./public/pivot_titanic_fehler.png"/>
    </div>

    /// warning | Achtung:
    Ein **Ausweg** ist die Nutzung von `pivot_table()`, da hier eine Aggregationsfunktion angegeben werden kann, die die Mehrdeutigkeit auflöst.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Pivot-Tabellen mit Aggregationen

    Wie schon oben beschrieben, können wir das Problem der Mehrdeutigkeit durch die Nutzung von `pivot_table()` lösen, da hier eine Aggregationsfunktion angegeben werden kann, die die Mehrdeutigkeit auflöst. In der folgenden Grafik wird dies nochmals verdeutlicht:

    <div align="center">
        <img src="./public/07_pivot_table.svg"/>
    </div>

    Es kann jede Aggregationsfunktion verwendet werden, die auch bei `groupby()` genutzt werden kann, wie z.B. `mean()`, `sum()`, `count()`, `min()`, `max()` etc.

    Ebenfalls können mehrere Aggregationsfunktionen gleichzeitig angewendet werden, indem eine Liste von Funktionen angegeben wird.

    **Beispiel:**
    """)
    return


@app.cell
def _(df_titanic, pd):
    pivot_sex_pclass_fare = pd.pivot_table(
        df_titanic, index="Sex", columns="Pclass", values="Fare", aggfunc="mean"
    )
    pivot_sex_pclass_fare.columns = pivot_sex_pclass_fare.columns.astype(str)
    pivot_sex_pclass_fare
    return


@app.cell
def _(df_titanic, pd):
    pivot_sex_pclass_fare_2 = pd.pivot_table(
        df_titanic,
        index="Sex",
        columns="Pclass",
        values="Fare",
        aggfunc=["count", "mean"],
    )
    pivot_sex_pclass_fare_2
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
