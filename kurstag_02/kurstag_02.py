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
    1 + 1
    return


@app.cell
def _():
    type(1 + 1)
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
    1 + 1.1
    return


@app.cell
def _():
    type(1 + 1.1)
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
    float(1) + 1.1  # ausführt
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Subtraktion

    Das Verhalten bezüglich Typen ist analog der Addition.
    """
    )
    return


@app.cell
def _():
    1 - 1
    return


@app.cell
def _():
    1.1 - 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Achtung
    Das Rechnen mit **float**-Zahlen kann, wegen der Binärdarstellung der Zahlen und der Endlichkeit des Computerspeichers zu Ungenauigkeiten (Rundungsfehlern) führen.
    ///

    **Beispiel**

    $\frac{1}{3}=0.\overline{3}$

    aber im Computer kann dies nicht dargestellt werden, da er nicht unendlich viel Speicher hat, d.h.

    $\frac{1}{3}\approx0.3333$

    Im obigen Beispiel von 0.1 ist die Binärdarstellung im Computer 0.0001100110011... 
    und muss deshalb auch irgendwann abgeschnitten werden. Dies führt zu dem "Fehler".
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Multiplikation

    Für die Multiplikation wird in Python der Operator `*` genutzt. 

    /// attention | Achtung
    Der Operator `*` wird auch im Zusammenhang mit dem Verbinden (Concatanation) von zwei oder mehreren Zeichenketten (str) genutzt.
    ///
    """
    )
    return


@app.cell
def _():
    2 * 2
    return


@app.cell
def _():
    type(2 * 2)
    return


@app.cell
def _():
    2 * 2.2, type(2 * 2.2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Division

    Für die Division (Teilen) wird der Opertor / genutzt.
    """
    )
    return


@app.cell
def _():
    6/2
    return


@app.cell
def _():
    7/2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    in diesem Fall kommt immer ein **float** als Ergbnis aus, auch, wenn man die Zahl ohne Rest teilen kann.
    Bei der Division gibt es neben dem Standard-Operator noch zwei weitere Operatoren:

    - die Division ohne Rest //
    - der Modulo-Opertor % zur Bestimmung des Restes 

    **Beispiele**
    """
    )
    return


@app.cell
def _():
    14//3

    return


@app.cell
def _():
    14 % 3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Rechnen mit komplexen Zahlen

    Komplexe Zahlen sind Zahlen in der Ebene, die "erweitererte" Standard-Opertoren nutzen.

    __Addition von komplexen Zahlen:__

    Wenn $a_1=x_1+j y_1$ und $a_2=x_2+j y_2$ zwei komplexe Zahlen sind, dann ist ihre Summe gegeben durch

    $$a_1+a_2 = x_1+x_2 + j (y_1+y_2)$$

    __Multiplikation von komplexen Zahlen:__

    Wenn $a_1=x_1+j y_1$ und $a_2=x_2+j y_2$ zwei komplexe Zahlen sind, dann ist ihre Produkt gegeben durch

    $$a_1 a_2 = x_1x_2 - y_1 y_2+ j (x_1 y_2 +x_2 y_1)$$

    __Division von komplexen Zahlen:__

    Wenn $a_1=x_1+j y_1$ und $a_2=x_2+j y_2$ zwei komplexe Zahlen sind, dann ist ihre Division gegeben durch

    $$\frac{a_1}{a_2} = \frac{x_1 x_2 + y_1 y_2+ j (y_1 x_2 - x_1 y_2)}{x_2^2+y_2^2}$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Beispiele

    **Definition der komplexen Zahlen**
    """
    )
    return


@app.cell
def _():
    a_1 = 1+1j*2
    return (a_1,)


@app.cell
def _():
    a_2 = complex(2,1)
    return (a_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Addition**""")
    return


@app.cell
def _(a_1, a_2):
    a_1+a_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Multiplikation**""")
    return


@app.cell
def _(a_1, a_2):
    a_1*a_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Division**""")
    return


@app.cell
def _(a_1, a_2):
    a_1/a_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// note  | Übungen

     1. Definiere Höhe $h$ und Grundseite $g$ eines Dreieckes und berechne den Flächeninhalt mittels $$A_D = \frac{1}{2} \cdot g\cdot  h$$
     1. Informiere Dich über die eigebaute Funktion `pow` [hier](https://docs.python.org/3/library/functions.html) und erkläre, was sie macht.
     1. Berechne den folgenden Ausdrück:
        $$\left(\frac{2+5}{5}\right)^{2}, \left((2+5) \% 5\right)^{2}$$
     1. Berechne den Absolutwert einer komplexen Zahl $a = x+ j y$ über
        $$|a|=\sqrt{x^{2}+y^{2}}$$
        und die eingebaute Funktion `abs`.
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Bedingungen oder bedingte Ausführung von Programmteilen

    ### `if-elif-else`-Ausdruck
    Wenn bestimmte Bedingungen gegeben (erfüllt) sind, möchte man haben das ein bestimmter Programmzweig ausgeführt oder nicht ausgeführt wird. In Python und anderen Programmiersprachen gibt es dafür den `if`-Ausdruck. Der in Python wie folgt definiert wird:

    /// note | Definition

    Eine bedingte Ausführung wird durch den `if-elif-else`-Ausdruck definiert

    >  if Bedingung_1:
    >  
    >     //Programmteil, der ausgeführt wird, wenn Bedingung_1 erfüllt ist
    >
    >  elif Bedingung_2:
    >
    >  //Programmteil, der ausgeführt wird, wenn Bedingung_1 erfüllt ist
    >  
    >  .
    >  
    >  .
    >  
    >  else:
    >  
    >  //Programmteil, der ausgeführt wird, wenn keine der obigen Bedingungen erfüllt ist

      Der `elif`- und `else`-Zweig ist optional in obiger Definition.
    ///
    """
    )
    return


app._unparsable_cell(
    r"""
    **Beispiel**
    """,
    column=None, disabled=False, hide_code=True, name="_"
)


@app.cell
def _(mo):
    number = mo.ui.number(start=1, stop=99, step=1)
    number
    return (number,)


@app.cell
def _(number):
    if number.value<16:
        print("Du darfst nicht alleine in die Eisdiele gehen.")
    elif 16 <= number.value < 18 :
        print("Du darfst alleine in die Eisdiele gehen.")
    else:
        print("Du musst das Eis in der Eisdiele alleine bezahlen.")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
