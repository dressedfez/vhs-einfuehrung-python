import marimo

__generated_with = "0.13.6"
app = marimo.App(layout_file="layouts/kurstag_01.slides.json")


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


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Installation

    In diesem Kurs benutzen wir als Paketmanager `uv`

    <img src="public/uv_python.png" width=200 class="center">

    Damit können wir fast alle relevanten Schritte zur Installation, Delinstallation  von Python und Bibliotheken (Packages) vornehmen.
    """
    )
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
