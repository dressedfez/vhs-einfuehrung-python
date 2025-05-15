import marimo

__generated_with = "0.13.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Python-Kurs: Python für Daten und KI – Programmieren lernen für die Zukunft

    An diesem Kurstag werden wir verschiedene Punkte, die essentiell für die Programmierung in Python (oder auch jeder anderen Programmiersprache) wichtig sind. Wir behandeln:

    - mathematische Standard-Operatoren, wie: ➕, ➖,✖️, ➗ und andere
    - Bedingungen oder bedingte Ausführung von Programmteilen
    - Schleife oder wiederholende Ausführung von Programmteilen
    - Einführung von Interaktivität durch Nutzung von **marimo**-Elementen


    ## Mathematische Standard-Opertoren/Operationen

    Die Lösungen von naturwissenschaftlichen oder mathematischen Problemen macht es erforderlich, dass man mit Programmiersprachen auch Berechnungen durchführen kann. Hier sollen zunächst die einfachsten mathematischen Operationen einführen und uns kurz über die Reihenfolge der Ausführung unterhalten.

    ### Addition

    Die Addition von zwei **int**-Werten führt wieder zu einem **int**-Wert:
    """
    )
    return


@app.cell
def _():
    1+1
    return


@app.cell
def _():
    type(1+1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Die Addition von **int** und **float** führt zu einem **float**-Wert. Dies nennt man:

    /// note | Definition **Widening**
    Widening bedeutet, dass ein Wert eines Datentyps implizit in einen "größeren" oder allgemeineren Datentyp umgewandelt wird – ohne Informationsverlust.
    ///

    **Beispiel**
    """
    )
    return


@app.cell
def _():
    1+1.1
    return


@app.cell
def _():
    type(1+1.1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip | Bemerkung
    **Widening** wird bei Python und vielen anderen höheren Programmiersprachen implizit durchgeführt, d.h.
    man muss sich nicht selbst um die Konvertierung in den "größeren" Datentyp kümmern. 
    ///

    Man kann mittels **float(zahl)** auch explizit konvertieren, d.h. man erhält das gleichen Ergebnis, wenn man 
    """
    )
    return


@app.cell
def _():
    float(1)+1.1 # ausführt
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
