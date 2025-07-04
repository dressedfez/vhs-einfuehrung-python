import marimo

__generated_with = "0.14.9"
app = marimo.App(width="full")


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

    Funktionen erlauben einem zusammenhängende Logik zu gliedern und wiederverwendbar zu machen. Sie können aus anderen Stellen des Programmes aufgerufen werden. Mit **Parametern** können Werte beliebiger Art an Funktionen übergeben werden. Rückgabewerte werden dazu benutzt Werte von der Funktion an den Aufrufer zurückzugeben.

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
    mo.md(r"""Defintion einer einfachen Funktion mit **einem** Parameter:""")
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
    mo.md(
        r"""Definition einer Funktion mit zwei Parametern und einem Rückgabewert:"""
    )
    return


@app.function
def addiere_zahlen(x, y: float) -> float:
    """
    Addiere gegebene Zahlen von und gebe Resultat zurück.
    Argumente:
    - x: Zahl vom Typ float
    - y: Zahl vom Typ float

    Returns: Summe der beiden Zahlen
    """
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
    mo.md(r"""Funktion höherer Ordnung mit `default`-Verhalten:""")
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
    mo.md(r"""Funktion mit mehreren Rückgabewerten:""")
    return


@app.function
def first_and_rest(liste):
    return liste[0], liste[1 : len(liste)]


@app.cell
def _():
    _namens_liste = ["Frank", "Egon", "Karl", "Gernot", "Stefan"]
    first_and_rest(_namens_liste)
    return


@app.function
def aeuser_funktion():
    print(
        "Hallo aus der äußeren Funktion vor dem Aufrauf der inneren Funktion"
    )

    # Definition der inneren Funktion
    def innere_funktion():
        print("Hallo aus der inneren Funktion")

    innere_funktion()  # Aufruf der inneren Funktion

    print(
        "Hallo aus der äußeren Funktion nach dem Aufrauf der inneren Funktion"
    )


@app.cell
def _():
    aeuser_funktion()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// note | Übungen
    1. Schreibe eine Funktion, die eine Liste von Worten als ersten Parameter annimmt und diese als `default`-Verhalten alle Elemente in `UpperCase` umwandet. Die Funktion soll als Keyword-Parameter (Name `transform`) auch andere Transformationnen erlauben.
    2. Erstelle eine Funktion, die das  arithmetische Mittel einer Liste von Zahlen bestimmt, wobei die **äußere** Funktion `mean` und die innere `total` heißen soll (letztere soll die Summe bestimmen).
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Lambda- oder Anonyme-Funktionen

    Lambda- oder Anonyme-Funktionen sind kurze Funktionen, die die folgende Struktur haben: 

    /// note | Definition

    Eine Lambda-Funktion hat den Aufbau: 
    ```python
    lambda: argumente : ausdruck
    ```

    In dieser Form ist er auch eine anonym, da sie **keinen** Namen hat. Eine Lambda-Funktion ist **nicht**
    mehr anonym, wenn man sie einen Namen hat.
    ///

    **Beispiel:** Lambda Funktion mit Namen
    """
    )
    return


@app.cell
def _():
    add2 = lambda a: a + 2
    return (add2,)


@app.cell
def _(add2):
    add2(5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Beispiel:** Lambda Funktion mit mehreren Argumenten und Namen""")
    return


@app.cell
def _():
    adder = lambda a, b: a + b
    subtractor = lambda a, b: a - b
    return adder, subtractor


@app.cell
def _(adder):
    adder(1, 2)
    return


@app.cell
def _(subtractor):
    subtractor(1, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Beispiel:** Anonyme Lambda-Funktion""")
    return


@app.function
def transformiere_liste(liste, transformer=lambda a: a):
    """
    Transformiert alle Elemente einer Liste mit dem gegebenen Transformer `transformer`.
    Wenn kein Transformer übergeben wird, wir eine identisch aussehende Liste zurückgegeben,
    d.h. der Tranformer ist lediglich ein Identitäts-Abbildung.

    Argumente:
    - liste: Liste, die transformiert werden soll
    - transformer: Funktion, die jedes Element tranformiert

    Rückgabe:
    - Transformierte Liste
    """
    rueckgabe_liste = []
    for el in liste:
        rueckgabe_liste.append(transformer(el))
    return rueckgabe_liste


@app.cell
def _():
    _liste = [1, 2, 3, 4, 5]
    transformiere_liste(_liste)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Beispiel einer anonyomen Lambda-Funktion, die die gegebene Zahl quadriert:"""
    )
    return


@app.cell
def _():
    _liste = [1, 2, 3, 4, 5]
    transformiere_liste(_liste, lambda a: a**2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// note | Übungen
    1. Schreibe eine  Lamdba-Funktion mit zwei Parametern, die prüft, ob eine Zeichenkette (erster Parameter) länger ist als ein bestimmter ganzzahliger Wert (zweiter Parameter).
    2. Schreibe eine Funktion, die als Parameter eine Zeichenkette annimmt und als Rückgabewert eine Lambda-Funktion zurückgibt. Im Fall, dass die Zeichenkette `add` ist, soll eine Lambda-Funktion für die Addition zweiter Werte zurückgegeben werden. Im Fall, dass die Zeichenkette `sub` ist, soll eine Lambda-Funktion für die Substraktion zürückgegeben werde. Ansonten soll die Identitätsfunktion zurückgegeben werden.
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Map, Filter und Reduce Funktionen

    Die Funktionen `map`, `filter` und `reduce` gehören vor allem in den Bereich funktionale Programmierung. Alle Funktione nehmen neben einem Iterable auch eine Funktion an, die auf jedes Element des Iterables angewandt wird.

    **Beispiel** für `map`
    """
    )
    return


@app.cell
def _():
    namen = ["frank", "egon", "karl", "gustav"]
    list(map(lambda e: e.title(), namen))
    return (namen,)


@app.cell
def _(mo):
    mo.md(r"""**Beispiel** für `filter`""")
    return


@app.cell
def _(namen):
    contains_a = lambda elem: elem.find("a") != -1
    list(filter(contains_a, namen))
    return (contains_a,)


@app.cell
def _():
    title_element = lambda e: e.title()
    return (title_element,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Beispiel** für `filter` und `map` kombiniert""")
    return


@app.cell
def _(contains_a, namen, title_element):
    list(map(title_element, filter(contains_a, namen)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Reduce-Funktion

    Die Funktion `reduce` ist nicht Teil des Kern-Python-Moduls, aber Teil der Standard-Python-Installation.
    Aus diesem Grund müssen wir die Funktion der Umgebung durch Importieren bekann machen.

    /// attention | Bemerkung

    `reduce()` nimmt eine Liste und schrumpft sie auf einen Wert – mit einer Funktion, die jeweils zwei Werte zusammenführt.
    ///
    """
    )
    return


@app.cell
def _():
    from functools import reduce
    return (reduce,)


@app.cell
def _(reduce):
    reduce(lambda a, b: a + b, [1, 2, 3])
    return


@app.cell
def _(reduce):
    # mit Anfangswert 5
    reduce(lambda a, b: a + b, [1, 2, 3], 5)
    return


@app.cell
def _(reduce):
    reduce(lambda a, b: a + b, ["F", "r", "a", "n", "k"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// note | Übungen
    1. Schreibe mit Hilfe der `reduce`-Funktion eine Funktion, die die Fakultät für eine natürliche Zahl $n \in \mathbb{N}$ via

        $$n! = n\cdot (n-1)\cdot(n-2)\cdot\dots\cdot 2\cdot 1$$
        berechnet.

    3. Burger mit reduce() bauen 🍔: Gegeben ist eine Liste von Zutaten, die in der richtigen Reihenfolge

        übereinandergeschichtet werden sollen. Verwende die Funktion reduce() aus dem Modul functools, um daraus eine lesbare Bauanleitung für einen Burger zu erzeugen.

        Die Ausgabe soll eine Textkette sein, in der alle Zutaten mit einem „+“ verbunden sind – zum Beispiel:
       > Brötchen unten + Salat + Tomate + Patty + Käse + Brötchen oben

        Was muss man machen, wenn man `+` durch `->` ersetzen möchte?
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(reduce):
    def fac(n):
        return reduce(lambda a, b: a * b, range(1, n + 1))
    return


@app.cell(hide_code=True)
def _(reduce):
    zutaten = [
        "Brötchen unten",
        "Salat",
        "Tomate",
        "Patty",
        "Käse",
        "Brötchen oben",
    ]

    burger = reduce(lambda so_far, zutat: f"{so_far} + {zutat}", zutaten)

    print("🍔 Burger-Bauplan:")
    print(burger)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Klassen

    In objektorientierten Programmiersprachen, zu denen Python gehört, werden Klassen unter anderem dazu genutzt: 

    1. Daten zu kapseln, so dass sie nicht von jedem geändert werden können und
    2. spezielles Verhalten, dass zu dieser Kategorie von Dingen gehört zu sammeln und mit diesen zu assoziieren.


    Bevor wir uns Klassen und Objekten zuwenden, betrachten wir zunächst den Python internen Typ `Tupel`.

    ### Kurzes Ausflug: Tupel

    /// note | Definition
    Tupel sind wie Listen und Mengen (Sets) Kontainertypen, d.h. man kann diesen Tupeln `Daten` speichern. Tupel haben dabei verschiedene Eigenschaften, die sie von Listen und Mengen unterscheiden:

    1. Ein Tupel kann noch der Erstellung nicht mehr geändert werden (**unchangeable**).
    2. Ein Tupel ist geordnet, d.h. die Reihenfolge ist fest.
    ///

    Gleiche Einträge können auch **mehrfach** in einem Tupel vorkommen.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Tupel werden mit runden Klammen erzeugt:""")
    return


@app.cell
def _():
    t1 = ("Frank", "Zimmer", 51)
    t1
    return (t1,)


@app.cell
def _():
    t2 = tuple(
        ["Egon", "Zimmer", 93]
    )  # hier könnten auch andere Kontainertypen verwendet werden
    t2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""wie bei Listen können die Elemente über Indizes referenziert werden"""
    )
    return


@app.cell
def _(t1):
    t1[1]
    return


@app.cell
def _(t1):
    t1[0:2]  # entnehme Elemente 0 und 1
    return


@app.cell
def _(t1):
    t1[-1]  # entnehme letztes Element
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Man kann Tupel **nicht** ändern""")
    return


@app.cell
def _():
    # t2[0] = "Karl" # enterne das Hash am Anfang der Zeile
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Tupel sind gut dafür zusammengehörende Daten zu speichern. Der Nachteil ist: 

    1. das man die Felder nicht mittels einem
    """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
