import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell(hide_code=True)
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
    # Variablen

    Was sind Variablen?

    /// note | Definition
    Variablen sind Verweise auf Speicherorte von Werte, die dort hinterlegt und von dort ausgelesen werden können.
    ///

    Hier ein grafische Darstellung für eine gespeicherte Zahl
    <img src="./public/int_memory.svg" width="200">
    """
    )
    return


@app.cell
def _():
    min_zahl_studenten = 5
    min_zahl_studenten
    return


app._unparsable_cell(
    r"""
    und hier eine grafische Darstellung eines Arrays von Strings (str)
    <img src=\"./public/str_memory.svg\" width=\"200\">
    """,
    column=None, disabled=False, hide_code=True, name="_"
)


@app.cell
def _():
    meldung = ["Hallo","Welt"]
    meldung
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Datentypen

    **Was sind Datentypen?**

    /// note | Definition
    Datentypen sind 

    ///



    Python unterstützt eine große Zahl bereits vorgefertigter Datentypen
    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    a=1
    b=2
    a+b
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
