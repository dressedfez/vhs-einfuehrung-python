import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Python für Daten und KI
    ## – Programmieren lernen für die Zukunft -
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Funktionen

    /// note | Definition

    Funktionen erlauben einem zusammenhängende Logik zu gliedern und wiederverwendbar zu machen. Können aus anderen Stellen des Programmes aufgerufen werden. Mit **Parametern** können Werte beliebiger Art an Funktionen übergeben werden. Rückgabewerte werden dazu benutzt Werte von der Funktion an den Aufrufer zurückzugeben.

    ```python
    def funktionen_name(parameter_1,...,parameter_n, parameter_with_default_1 = default_1, parameter_with_default_2 = default_2 ):
        <Funktionen Körper>
        return <Rückgabewert>
    ```

    **Funktionen** können ebenfalls als Parameter an Funktionen übergeben werden (Funktionen höherer Ordnung).

    ///

    ### Beispiele
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Defintion einer einfachen Funktion mit **einem** Parameter: """)
    return


@app.function
def ein_parameter_funktion(name):
    print(f"Mein Name ist {name}")


@app.cell
def _():
    ein_parameter_funktion("Frank")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Definition einer Funktion mit zwei Parametern und einem Rückgabewert:""")
    return


@app.function
def addiere_zahlen(x, y: float) -> float:
    print(f"x=", x)
    print(f"y=", y)
    return x + y


@app.cell
def _():
    addiere_zahlen(1, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Funktion mit **Keyword**-Parameter""")
    return


@app.cell
def _():
    _zahl1 = 2
    _zahl2 = 3
    addiere_zahlen(y=_zahl1, x=_zahl2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Funktion höherer Ordnung mit `default`-Verhalten: """)
    return


@app.function
def tue_was(name, fun=print):
    fun(name)


@app.cell
def _():
    tue_was("Frank", ein_parameter_funktion)
    return


@app.cell
def _():
    tue_was("Egon")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Funktion mit mehreren Rückgabewerten: """)
    return


@app.function
def first_and_rest(liste):
    return liste[0], liste[1 : len(liste)]


@app.cell
def _():
    _namens_liste = ["Frank", "Egon", "Karl", "Gernot", "Stefan"]
    first_and_rest(_namens_liste)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
