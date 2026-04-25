# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo>=0.19.11",
#     "mcp==1.27.0",
# ]
# ///

import marimo

__generated_with = "0.23.2"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python für Daten und KI
    ## – Programmieren lernen für die Zukunft -
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Funktionen

    /// note | Definition

    Funktionen erlauben es, zusammenhängende Logik zu gliedern und wiederverwendbar zu machen. Sie können von anderen Stellen im Programm aufgerufen werden. Mit **Parametern** können Werte beliebiger Art an Funktionen übergeben werden. Rückgabewerte werden dazu benutzt, Werte von der Funktion an den Aufrufer zurückzugeben.

    ```python
    def funktionen_name(parameter_1,...,parameter_n, parameter_with_default_1 = default_1, parameter_with_default_2 = default_2 ):
        <Funktionskörper>
        return <Rückgabewert>
    ```

    **Funktionen** können ebenfalls als Parameter an andere Funktionen übergeben werden. Man spricht dann von Funktionen höherer Ordnung.

    ///

    /// warning | Achtung
    Hat die Funktion mehr als ein Parameter, kommt es bei Aufruf der Funktion auf die Reihenfolge
    an, d.h. die Reihenfolge der Parameter im Aufruf muss mit der Reihenfolge in der Funktionsdefinition
    übereinstimmen. **Keyword-Parameter** können hierbei hilfreich sein (siehe Beispiele später).
    ///

    ### Beispiele
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Definition einer einfachen Funktion mit **einem** Parameter:
    """)
    return


@app.function
def ein_parameter_funktion(name):
    print(f"Mein Name ist {name}.")


@app.cell
def _():
    ein_parameter_funktion("Frank")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Definition einer Funktion mit zwei Parametern und einem Rückgabewert:
    """)
    return


@app.function
def addiere_zahlen(x, y: float) -> float:
    """
    Addiere gegebene Zahlen und gib das Resultat zurück.
    Argumente:
    - x: Zahl vom Typ float
    - y: Zahl vom Typ float

    Returns: Summe der beiden Zahlen
    """
    print(f"x=", x)
    print(f"y=", y)
    print(f"Summe =", x + y)
    return x + y


@app.cell
def _():
    addiere_zahlen(1, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Funktion mit **Keyword**-Parameter

    Nutzt man Keyword-Parameter, kommt es nicht mehr auf die Reihenfolge an, sondern man nutzt die Namen,
    die in der Funktionsdefiniton benutzt werden.
    """)
    return


@app.cell
def _():
    _zahl1 = 2
    _zahl2 = 3
    addiere_zahlen(y=_zahl1, x=_zahl2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Funktion höherer Ordnung mit `Default`-Verhalten:
    """)
    return


@app.function
def tue_was(name, fun=print):
    fun(name)


@app.cell
def _():
    # Nutzung von Keyword-Parameter bei Funktion höherer Ordnung
    tue_was(fun=ein_parameter_funktion, name="Frank")
    return


@app.cell
def _():
    # Funktion nutzt Default-Verhalten
    tue_was("Egon")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Funktion mit mehreren Rückgabewerten:
    """)
    return


@app.function
def first_and_rest(liste):
    return liste[0], liste[1 : len(liste)]


@app.cell
def _():
    _namens_liste = ["Frank", "Egon", "Karl", "Gernot", "Stefan"]
    first_and_rest(_namens_liste)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Definition von äußeren und inneren Funktionen**

    Die Nutzung von _inneren Funktionen_ ist eine Design-Entscheidung. Wenn man die Funktion nur im Zusammenhang mit **einer** anderen Funktion nutzt, kann man sich auch dafür entscheiden diese als
    innere Funktion dieser Funktion zu definieren.
    """)
    return


@app.function
def aeussere_funktion():
    print("Hallo aus der äußeren Funktion vor dem Aufruf der inneren Funktion")

    # Definition der inneren Funktion
    def innere_funktion():
        print("Hallo aus der inneren Funktion")

    innere_funktion()  # Aufruf der inneren Funktion

    print(
        "Hallo aus der äußeren Funktion nach dem Aufruf der inneren Funktion"
    )


@app.cell
def _():
    aeussere_funktion()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Übungen
    1. Schreibe eine Funktion, die eine Liste von Worten als ersten Parameter annimmt und diese als `default`-Verhalten alle Elemente in `UpperCase` umwandelt. Die Funktion soll als Keyword-Parameter (Name `transform`) auch andere Transformationen erlauben.
    2. Erstelle eine Funktion, die das arithmetische Mittel einer Liste von Zahlen bestimmt. Die **äußere** Funktion soll `mean` heißen, die innere `total`; letztere soll die Summe bestimmen.
    ///
    """)
    return


@app.cell(hide_code=True)
def _():
    # mögliche Lösung zu Aufgabe 1
    def transform_list(list, transform=str.upper):
        return [transform(el) for el in list]


    _input_list = ["frank", "egon", "karl"]
    # nutze Default-Verhalten
    _list1 = transform_list(_input_list)
    # nutze Keyword-Parameter, um Default-Verhalten zu ändern
    _list2 = transform_list(_input_list, transform=str.capitalize)
    return


@app.cell(hide_code=True)
def _():
    # mögliche Lösung zu Aufgabe 2 (erweitert)
    from statistics import mean, random


    def my_mean(liste):
        def total(liste):
            sum = 0
            for el in liste:
                sum += el
            return sum

        return total(liste) / len(liste)


    # Vergleich mit Python eigener Implementierung

    # erzeuge Tausend Zufallszahlen im Bereich 0 bis 1
    _data = [random.gauss(0, 1) for _ in range(1000)]

    # berechnen mit beiden Methoden den Mittelwert
    # my_mean(_data), mean(_data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lambda- oder Anonyme-Funktionen

    Lambda- oder anonyme Funktionen sind kurze Funktionen, die die folgende Struktur haben:

    /// note | Definition

    Eine Lambda-Funktion hat den Aufbau:
    ```python
    lambda argumente: ausdruck
    ```

    In dieser Form ist sie auch anonym, da sie **keinen** Namen hat. Eine Lambda-Funktion ist **nicht**
    mehr anonym, wenn man ihr einen Namen gibt.
    ///

    **Beispiel:** Lambda-Funktion mit Namen
    """)
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
    mo.md(r"""
    **Beispiel:** Lambda-Funktion mit mehreren Argumenten und Namen
    """)
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
    mo.md(r"""
    **Beispiel:** Anonyme Lambda-Funktion
    """)
    return


@app.function
def transformiere_liste(liste, transformer=lambda a: a):
    """
    Transformiert alle Elemente einer Liste mit der übergebenen Funktion `transformer`.
    Wenn kein Transformer übergeben wird, wird eine identisch aussehende Liste zurückgegeben,
    d.h. `transformer` ist in diesem Fall lediglich eine Identitätsabbildung.

    Argumente:
    - liste: Liste, die transformiert werden soll
    - transformer: Funktion, die jedes Element transformiert

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
    mo.md(r"""
    Beispiel einer anonymen Lambda-Funktion, die die gegebene Zahl quadriert:
    """)
    return


@app.cell
def _():
    _liste = [1, 2, 3, 4, 5]
    # Transformiere Liste durch Quadrieren der Elemente
    quadrierer = lambda a: a**2
    # Transformiere die Liste mithilfe der Quadrierer-Funktion
    transformiere_liste(_liste, quadrierer)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Übungen
    1. Schreibe eine Lambda-Funktion mit zwei Parametern, die prüft, ob eine Zeichenkette (erster Parameter) länger ist als ein bestimmter ganzzahliger Wert (zweiter Parameter).
    2. Schreibe eine Funktion, die als Parameter eine Zeichenkette annimmt und als Rückgabewert eine Lambda-Funktion zurückgibt. Im Fall, dass die Zeichenkette `add` ist, soll eine Lambda-Funktion für die Addition zweier Werte zurückgegeben werden. Im Fall, dass die Zeichenkette `sub` ist, soll eine Lambda-Funktion für die Subtraktion zurückgegeben werden. Ansonsten soll die Identitätsfunktion zurückgegeben werden.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Map, Filter und Reduce Funktionen

    Die Funktionen `map`, `filter` und `reduce` gehören vor allem in den Bereich der funktionalen Programmierung. Alle Funktionen nehmen neben einem Iterable auch eine Funktion an, die auf jedes Element des Iterables angewandt wird.

    **Beispiel** für `map`
    """)
    return


@app.cell
def _():
    namen = ["frank", "egon", "karl", "gustav"]
    list(map(lambda name: name.title(), namen))
    return (namen,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Beispiel** für `filter`
    """)
    return


@app.cell
def _(namen):
    contains_a = lambda elem: elem.find("a") != -1
    list(filter(contains_a, namen))
    return (contains_a,)


@app.cell
def _():
    "Frank".find("Z")
    return


@app.cell
def _():
    return


@app.cell
def _():
    title_element = lambda e: e.title()
    return (title_element,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Beispiel** für `filter` und `map` kombiniert
    """)
    return


@app.cell
def _(contains_a, namen, title_element):
    list(map(title_element, filter(contains_a, namen)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Reduce-Funktion

    Die Funktion `reduce` ist nicht Teil des Python-Kerns, aber Bestandteil der Standardbibliothek.
    Aus diesem Grund müssen wir sie zunächst importieren.

    /// attention | Bemerkung

    `reduce()` nimmt eine Liste und schrumpft sie auf einen Wert – mit einer Funktion, die jeweils zwei Werte zusammenführt.
    ///
    """)
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
    mo.md(r"""
    /// note | Übungen
    1. Schreibe mithilfe der `reduce`-Funktion eine Funktion, die die Fakultät für eine natürliche Zahl $n \in \mathbb{N}$ nach

        $$n! = n\cdot (n-1)\cdot(n-2)\cdot\dots\cdot 2\cdot 1$$
        berechnet.

    3. Burger mit reduce() bauen 🍔: Gegeben ist eine Liste von Zutaten, die in der richtigen Reihenfolge

        übereinandergeschichtet werden sollen. Verwende die Funktion reduce() aus dem Modul functools, um daraus eine lesbare Bauanleitung für einen Burger zu erzeugen.

        Die Ausgabe soll eine Textkette sein, in der alle Zutaten mit einem „+“ verbunden sind – zum Beispiel:
       > Brötchen unten + Salat + Tomate + Patty + Käse + Brötchen oben

        Was muss man machen, wenn man `+` durch `->` ersetzen möchte?
    ///
    """)
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

    burger = reduce(lambda bisher, zutat: f"{bisher} + {zutat}", zutaten)

    print("🍔 Burger-Bauplan:")
    print(burger)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Klassen

    In objektorientierten Programmiersprachen, zu denen Python gehört, werden Klassen unter anderem dafür genutzt:

    1. Daten zu kapseln, sodass sie nicht von jedem geändert werden können, und
    2. spezielles Verhalten zu sammeln und mit dieser Kategorie von Dingen zu assoziieren.


    Bevor wir uns Klassen und Objekten zuwenden, betrachten wir zunächst den Python-internen Typ `Tupel`.

    ### Kurzer Ausflug: Tupel

    /// note | Definition
    Tupel sind wie Listen und Mengen (Sets) Containertypen, d.h. man kann in ihnen `Daten` speichern. Tupel haben dabei verschiedene Eigenschaften, die sie von Listen und Mengen unterscheiden:

    1. Ein Tupel kann nach der Erstellung nicht mehr geändert werden (**unchangeable**).
    2. Ein Tupel ist geordnet, d.h. die Reihenfolge ist fest.
    ///

    Gleiche Einträge können auch **mehrfach** in einem Tupel vorkommen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tupel werden mit runden Klammern erzeugt:
    """)
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
    )  # hier könnten auch andere Containertypen verwendet werden
    t2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wie bei Listen können die Elemente über Indizes referenziert werden.
    """)
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
    mo.md(r"""
    Man kann Tupel **nicht** ändern
    """)
    return


@app.cell
def _():
    # t2[0] = "Karl" # entferne das Hash am Anfang der Zeile
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tupel eignen sich gut dafür, zusammengehörende Daten zu speichern. Der Nachteil ist:

    1. dass man die Felder **nicht** über einen Namen adressieren kann,
    2. dass einem Tupel **kein Verhalten** zugeordnet werden kann und
    3. dass Tupel **nicht** geändert werden können; das ist manchmal allerdings auch ein Vorteil.

    Diese **Beschränkungen** und einige mehr lassen sich durch die Einführung von Klassen beseitigen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Definition
    Eine Klasse ist wie eine Blaupause oder Schablone (Vorlage) für ein Ding, das man erzeugen will. Dieses Ding kann auch Verhalten und veränderbare Eigenschaften haben.
    ///
    Hier zum Beispiel eine Schablone eines Buchstabens:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.image(
            "https://upload.wikimedia.org/wikipedia/commons/e/ee/Metal_Stencil_W.jpg",
            alt="Blaupause Buchstabe",
        )
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    sowie ein konkreter Buchstabe W.

    Der Buchstabe könnte z.B. folgende Eigenschaften haben:

    - Farbe
    - Größe
    - Schriftart
    - etc

    Außerdem könnte er das folgende Verhalten haben:

    - die Farbe und Schriftart ändert sowie
    - die Größe skaliert.


    Grafisch kann dies mittels eines Klassen-(-UML)-Diagramms dargestellt werden.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(alt="Klassendiagram", src="public/Klassendiagramm.png"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In Python lässt sich eine **Klasse** folgendermaßen definieren:

    /// note | Definition
    Eine Klasse ist durch das Keyword **class** gekennzeichnet

    ```python
     class KlassenName:
    ```
    """)
    return


@app.class_definition
class MyClass:
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Die Klasse `MyClass` kann mit dem folgenden Ausdruck **erzeugt** werden:
    """)
    return


@app.cell
def _():
    x = MyClass()
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wir haben damit unsere erste Klasse erfolgreich definiert!
    """)
    return


@app.cell
def _(x):
    type(x)
    return


@app.cell
def _():
    type(1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Damit haben wir noch nicht viel gewonnen. Das ändert sich, wenn wir Klassen

    - Eigenschaften und
    - Verhalten

    geben.

    /// note | Definition
    Eine Klasse mit Eigenschaften und Verhalten kann wie folgt definiert werden:

    ```python
    class Buchstabe:

        def __init__(
            self,
            buchstabe,
            farbe="Schwarz",
            schriftart="Times New Roman",
            groesse=12,
        ):
            # Eigenschaften
            self._buchstabe = buchstabe  # gilt per Vereinbarung als interne Variable
            self.farbe = farbe
            self.schriftart = schriftart
            self.groesse = groesse

        # Verhalten -- eine Funktion wird in diesem Zusammenhang Methode genannt
        def setze_farbe(self, neue_farbe):
            self.farbe = neue_farbe

    ```

    Das Keyword `self` bezieht sich auf die erzeugte Instanz.
    ///

    **Beispiel**:
    """)
    return


@app.class_definition
class Buchstabe:
    def __init__(
        # wie Funktionsparameter können auch Klassenkonstruktoren Default-Werte haben
        self,
        buchstabe,
        farbe="Schwarz",
        schriftart="Helvetica",
        groesse=12,
    ):
        self._buchstabe = buchstabe
        self.farbe = farbe
        self.schriftart = schriftart
        self.groesse = groesse

    def __str__(self):
        # Überschreiben der Standard-String-Repräsentation
        return f"Buchstabe {self._buchstabe} wird mit der Schriftart {self.schriftart} und Größe {self.groesse} mit Farbe {self.farbe} dargestellt."

    def set_farbe(self, neue_farbe):
        """
        Methode, die es erlaubt, die Farbe des Buchstabens zu ändern.
        """
        self.farbe = neue_farbe
        print(
            f"Der Buchstabe {self._buchstabe} hat jetzt die Farbe {self.farbe}."
        )

    def set_schriftart(self, neue_schriftart):
        """
        Methode, die es erlaubt, die Schriftart des Buchstabens zu ändern.
        """
        self.schriftart = neue_schriftart

    def skaliere_groesse(self, skalierungs_faktor):
        """
        Methode, die es erlaubt, die Größe des Buchstabens anzupassen.
        """
        self.groesse = skalierungs_faktor * self.groesse


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Bemerkung
    Ein wichtiger Gesichtspunkt in der objektorientierten Programmierung (OOP) ist die **Kapselung von Daten**.
    Sprachen wie z.B. Java erlauben es, die Kapselung von Daten mit eigenen Sprachkonstrukten wie **private**, **protected** oder **public** zu kontrollieren. Dies ist bei Python nicht so. Hier wird auf **Vereinbarung** gesetzt, d.h.

    - Variablen, die mit einem Unterstrich beginnen, wie z.B. `_buchstabe` im obigen Beispiel, gelten als **protected**. Die eigene Klasse und deren Unterklassen (siehe nächster Abschnitt) können oder sollen darauf zugreifen.
    - Variablen, die mit zwei Unterstrichen beginnen, gelten als **private**, d.h. man kann oder soll nur aus der Klasse selbst auf sie zugreifen.
    - Alle anderen Variablen gelten als **public**.
    ///
    """)
    return


@app.cell
def _(x):
    print(x)
    return


@app.cell
def _():
    groesses_A = Buchstabe(buchstabe="A")
    groesses_A._buchstabe
    return (groesses_A,)


@app.cell
def _(groesses_A):
    print(groesses_A)
    return


@app.cell
def _(groesses_A):
    groesses_A.skaliere_groesse(2)
    groesses_A.set_farbe("Blau")
    print(groesses_A)
    return


@app.cell
def _(groesses_A):
    groesses_A
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Übung
    1. Was passiert, wenn man in der obigen Klasse `Buchstaben` die Methode `__str(...)__` auskommentiert?
    2. Wie ändert sich das `print` eines Buchstabens?
    3. Was bedeutet das Überschreiben einer Methode?
    4. Was passiert, wenn die Methode `__repr(...)__` überschrieben wird? Wie ändert sich die letzte Ausgabe?
    5. Schreibe einen Taschenrechner als Klasse, der die vier Grundrechenarten unterstützt. Er soll eine Methode `eingabe` haben, die einen String wie "10 + 5" entgegennimmt, die Operation und die Operanden extrahiert und speichert. Eine weitere Methode `berechnen` soll dann die gespeicherte Operation ausführen und das Ergebnis ausgeben.
    ///
    """)
    return


@app.cell(hide_code=True)
def _():
    # Lösung für Aufgabe 1 und 2
    # es wird die Speicheradresse der Klasse ausgegeben, da die Methode __str__ nicht definiert ist
    return


@app.cell(hide_code=True)
def _():
    # Lösung von Aufgabe 3
    # Das Überschreiben einer Methode bedeutet, dass eine Unterklasse eine Methode mit demselben Namen wie eine Methode der Elternklasse definiert. Dadurch wird die Methode der Elternklasse in der Unterklasse ersetzt, d.h. die Logik der
    return


@app.cell(disabled=True, hide_code=True)
def _():
    # mögliche Lösung für Aufgabe 4
    class Aufgabe4OhneRepr:
        pass


    class Aufgabe4MitReplr:
        def __repr__(self):
            return "Aufgabe4MitRepr()"


    Aufgabe4OhneRepr(), Aufgabe4MitReplr()

    # Die Ausgabe in Marimo wird durch diese Überschreibung angepasst.
    return


@app.cell(hide_code=True)
def _():
    # mögliche Lösung für Aufgabe 5
    class Taschenrechner:
        def __init__(self):
            self.ergebnis = 0
            self.eingabe1 = 0
            self.eingabe2 = 0
            self.operator = None

        def eingabe(self, eingabe):
            [eingabe1, op, eingabe2] = eingabe.split(" ")
            self.eingabe1 = float(eingabe1)
            self.eingabe2 = float(eingabe2)
            self.operator = op
            print(eingabe1)
            print(op)
            print(eingabe2)

        def ausgabe(self):
            print(f"Ergebnis: {self.ergebnis}")

        def addiere(self, a, b):
            return a + b

        def subtrahiere(self, a, b):
            return a - b

        def multipliziere(self, a, b):
            return a * b

        def dividiere(self, a, b):
            if b != 0:
                return a / b
            else:
                raise ValueError("Division durch Null ist nicht erlaubt.")

        def berechnen(self):
            if self.operator == "+":
                print("Addition wird ausgeführt.")
                self.ergebnis = self.addiere(self.eingabe1, self.eingabe2)
                print("Addition abgeschlossen.")
            elif self.operator == "-":
                self.ergebnis = self.subtrahiere(self.eingabe1, self.eingabe2)
            elif self.operator == "*":
                self.ergebnis = self.multipliziere(self.eingabe1, self.eingabe2)
            elif self.operator == "/":
                self.ergebnis = self.dividiere(self.eingabe1, self.eingabe2)
            else:
                raise ValueError(f"Unbekannter Operator: {self.operator}")
            self.ausgabe()

    #t = Taschenrechner() # erstelle Taschenrechner
    #t.eingabe("1 + 2") # führe Eingabe durch
    #t.berechnen() # starte Berechnung inklusive Ausgabe
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Vererbung und Komposition von Klassen

    Vererbung ist ein Konzept, das sehr verbreitet ist, wenn man über objektorientierte Programmiersprachen spricht. Vererbung erlaubt es,

    - Daten und
    - Verhalten

    an Objekte weiterzugeben, die von einer anderen Klasse abstammen, also von ihr erben. Hier ist ein Beispiel, das verschiedene Beziehungen darstellt.
    Die `Ist-eine-Relation` wird durch Vererbung modelliert. Die `Hat-eine-Relation` wird nicht durch Vererbung modelliert, sondern durch Komposition.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/KlassendiagrammVererbung.png"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Vererbung von Klassen

    Klassen können von anderen Klassen erben. Dies wird durch das Angeben der Elternklasse in Klammern nach dem Klassennamen gemacht.
    Im folgenden Beispiel erbt die Klasse `Student` von der Klasse `Person`; damit wird das obige Diagramm umgesetzt. Die **Vererbung** wird durch eine **Ist-eine**-Relation dargestellt: Der Student ist eine Person.
    """)
    return


@app.class_definition
class Person:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email
        self.adresse = None

 #   def __repr__(self):
  #      return f"Person(name={self.name}, email={self.email})"

    def setze_adresse(self, adresse):
        self.adresse = adresse

    def adresse_ausgeben(self):
        if self.adresse is not None:
            self.adresse.adresse_ausgeben()
        else:
            print(f"{self.name} hat keine Adresse gesetzt.")


@app.class_definition
class Student(Person):
    def __init__(self, name, student_id, email=None):
        super().__init__(name, email=email)
        self.student_id = student_id

    def __repr__(self):
        return f"Student(name={self.name}, student_id={self.student_id}, email={self.email})"


@app.class_definition
class Dozent(Person):
    def __init__(self, name, fachgebiet, email=None):
        super().__init__(name, email=email)
        self.fachgebiet = fachgebiet

  #  def __repr__(self):
  #      return f"Dozent(name={self.name}, fachgebiet={self.fachgebiet}, email={self.email})"


@app.cell
def _():
    frank = Dozent("Frank Zimmer", "Informatik")
    frank
    return


@app.cell
def _():
    anna = Student("Anna Müller", 47, "anna.mueller@mail.de")
    anna
    return (anna,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// attention | Merken
    Klassen erben von der Basis-Klasse:
       - Attribute (oben name, etc)
       - Verhalten / Methoden (oben z.B. __repr__)
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Komposition von Klassen

    Neben der Vererbung ist die **Komposition** ein weiteres wichtiges Konzept von Klassen. Komposition bedeutet, dass eine Klasse eine andere Klasse als Eigenschaft besitzt. Dies wurde im obigen Beispiel bereits durch die Klasse `Adresse` gezeigt. Hier ist diese Eigenschaft als Programmcode umgesetzt.
    - Die **Komposition** wird durch eine **Hat-eine**-Relation dargestellt. Die Person **hat** eine Adresse.
    - Wenn man Komposition nutzt, kann man Aufgaben an Komponenten delegieren, was die Wartbarkeit und Wiederverwendbarkeit des Codes verbessert.
    """)
    return


@app.class_definition
class Adresse:
    def __init__(self, strasse, postleitzahl, stadt, land):
        self.strasse = strasse
        self.postleitzahl = postleitzahl
        self.stadt = stadt
        self.land = land

    def adresse_ausgeben(self):
        print(f"{self.strasse}, {self.postleitzahl} {self.stadt}, {self.land}")


@app.cell
def _(anna):
    adresse_anna = Adresse(
        strasse="Hauptstraße 5",
        postleitzahl="12345",
        stadt="Musterstadt",
        land="Deutschland",
    )
    anna.setze_adresse(adresse_anna)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Die Ausgabe der Adresse wird durch den Aufruf der Methode `adresse_ausgeben` delegiert, die in der Klasse `Adresse` definiert ist.
    """)
    return


@app.cell
def _(anna):
    anna.adresse_ausgeben()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// attention | Merken
    Komposition hat zwei Hauptmerkmale:
    1. Komponeten werden als Attribute der Klasse gespeichert.
    2. Das Delegieren von Aufgaben an Komponenten
       ist möglich und erlaubt es, die Wartbarkeit und Wiederverwendbarkeit des Codes zu verbessern.
    ///
    """)
    return


@app.cell
def _():
    class Fahrzeug:
        def __init__(self, marke, baujahr):
            self.marke = marke
            self.baujahr = baujahr

        def info(self):
            print(f"Fahrzeug: {self.marke}, Baujahr: {self.baujahr}")


    class Auto(Fahrzeug):

        def __init__(self, marke, baujahr, anzahl_tueren):
            super().__init__(marke, baujahr)
            self.at = anzahl_tueren

        def info(self):
            print(f"Auto der Marke: {self.marke} (Baujahr: {self.baujahr}) mit Anzahl Türen {self.at}")
    

    class Motorrad(Fahrzeug):
        def __init__(self, marke, baujahr, hat_beiwagen):
            super().__init__(marke, baujahr)
            self.hb = hat_beiwagen
        

    return Auto, Motorrad


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Anwendung der Klassen**
    """)
    return


@app.cell
def _(Auto):
    bmw = Auto("BMW", 1999, 2)
    bmw.info()
    return


@app.cell
def _(Motorrad):
    mz = Motorrad("MZ", 1965, False)
    mz.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Übungen
    1. **Einfache Vererbung - Fahrzeuge (Leicht)**
       Erstelle eine Basisklasse `Fahrzeug` mit den Attributen `marke` und `baujahr`. Implementiere eine Methode
       `info()`, die diese Informationen ausgibt.
       Erstelle dann zwei Unterklassen:

       - `Auto` mit dem zusätzlichen Attribut `anzahl_tueren`
       - `Motorrad` mit dem zusätzlichen Attribut `hat_beiwagen` (Boolean)

       Beide Unterklassen sollen die `info()`-Methode erweitern, um ihre spezifischen Attribute anzuzeigen.

    2. **Vererbung mit Methodenüberschreibung - Tiere (Leicht-Mittel)**

        Erstelle eine Basisklasse `Tier` mit:


       - Attribut `name`
       - Methode `laut_geben()`, die "Dieses Tier macht ein Geräusch" ausgibt

        Erstelle drei Unterklassen:

       - `Hund` - überschreibt `laut_geben()` mit "Wuff!"
       - `Katze` - überschreibt `laut_geben()` mit "Miau!"
       - `Kuh` - überschreibt `laut_geben()` mit "Muh!"

       Erstelle eine Funktion `tier_konzert(tiere)`, die eine Liste von Tieren erhält und jedes Tier seinen Laut ausgeben lässt.

    3. **Komposition - Computer und Komponenten (Mittel)**

       Erstelle Klassen für Computer-Komponenten:

       - `Prozessor` mit den Attributen `modell` und `ghz`
       - `Arbeitsspeicher` mit den Attributen `groesse_gb` und `typ`
       - `Festplatte` mit den Attributen `kapazitaet_gb` und `ist_ssd` (Boolean)

       Erstelle dann eine Klasse `Computer`, die diese Komponenten als Attribute enthält (Komposition). Der
       `Computer` soll eine Methode `spezifikationen()` haben, die alle Komponenten übersichtlich ausgibt.


    5. **Vererbung und Komposition kombiniert - Bibliothek (Mittel-Schwer)**

       Erstelle ein System für eine Bibliothek:


       *Vererbung:*
        - Basisklasse Medium mit Attributen titel, jahr und ist_ausgeliehen (Boolean)
        - Methode ausleihen() und zurueckgeben()
        - Unterklassen: Buch (zusätzlich: autor, seiten), DVD (zusätzlich: dauer_minuten, genre)

       *Komposition:*
       - Klasse `Bibliothek`, die eine Liste von Medien verwaltet
       - Methoden: `medium_hinzufuegen(medium)`, `alle_verfuegbaren_medien()`, `suche_nach_titel(titel)`

       Teste dein System, indem du mehrere Bücher und DVDs erstellst, sie zur Bibliothek hinzufügst und verschiedene Operationen durchführst.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Importieren von Modulen


    Meist ist es sinnvoll, Funktionen, Klassen und andere Definitionen in Modulen zu organisieren. Ein Modul ist eine Datei, die Python-Code enthält.
    Module können von anderen Modulen oder Skripten importiert werden, um die darin definierten Funktionen, Klassen und Variablen zu verwenden.

    Packages sind eine Möglichkeit, Module in hierarchischen Verzeichnissen zu organisieren. Ein Package ist ein Verzeichnis, das eine spezielle
    Datei namens `__init__.py` enthält, die es Python ermöglicht, das Verzeichnis als Package zu erkennen.

    Es gibt verschiedene Möglichkeiten, Module zu importieren:
    1. `import modulname`: Importiert das gesamte Modul. Auf Funktionen oder Klassen greift man dann über den Modulnamen zu.
    2. `from modulname import funktionsname`: Importiert eine spezifische Funktion oder Klasse aus einem Modul.
    3. `from modulname import *`: Importiert alle Funktionen und Klassen aus einem Modul (nicht empfohlen, da es zu Namenskonflikten führen kann).
    4. `import modulname as alias`: Importiert ein Modul und gibt ihm einen Alias-Namen, um die Verwendung zu erleichtern.
    5. `from modulname import funktionsname as alias`: Importiert eine spezifische Funktion oder Klasse aus einem Modul und gibt ihr einen Alias-Namen.
    6. `import modulname.submodul`: Importiert ein Submodul aus einem Package.

    In diesem Kurstag nutzen wir zwei getrennte Beispiele:
    - `simple_math_package` als reines Mathematik-Paket
    - `kursverwaltung` als fachliches Paket fuer ein Verwaltungssystem
    """)
    return


@app.cell
def _():
    # nicht erlaubt in Marimo, aber sonst möglich:
    #from simple_math_package import *
    return


@app.cell
def _():
    # Importieren von Funktionen und Klassen aus einem Paket
    from simple_math_package import Matrix
    from simple_math_package import add, subtract

    return Matrix, add, subtract


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    nutzen der importierten Funktionen:
    """)
    return


@app.cell
def _(add, subtract):
    add(2, 3), subtract(10, 4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    arbeiten mit Aliasen
    """)
    return


@app.cell
def _():
    # Importieren und Umbenennen eines Pakets
    import simple_math_package as smp

    return (smp,)


@app.cell
def _(smp):
    # Nutzen des Paketalias
    m_1 = smp.Matrix([[3, 2], [3, 4]])
    return (m_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    arbeiten mit importierten Klassen
    """)
    return


@app.cell
def _(Matrix):
    # Nutzen der importierten Klasse
    m_2 = Matrix([[1, 2], [3, 4]])
    m_2
    return (m_2,)


@app.cell
def _(m_1, m_2):
    m_1.add(m_2)
    return


@app.cell
def _(m_1, m_2):
    m_1.subtract(m_2)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Als zweites Beispiel nutzen wir ein eigenes Paket `kursverwaltung`.
    Dort liegen die Klassen fuer Personen, Kurse und die Verwaltungslogik in getrennten Modulen.
    """)
    return


@app.cell
def _():
    from kursverwaltung import Dozent as KursDozent
    from kursverwaltung import Kurs, Kursverwaltung
    from kursverwaltung import Student as KursStudent

    return Kurs, KursDozent, KursStudent, Kursverwaltung


@app.cell
def _(Kurs, KursDozent, KursStudent, Kursverwaltung):
    dozent = KursDozent("Frank Zimmer", "Python")
    kurs = Kurs("Python fuer Anfaenger", dozent=dozent, max_teilnehmende=2)
    student_1 = KursStudent("Anna Mueller", student_id=1)
    student_2 = KursStudent("Egon Meier", student_id=2)
    verwaltung = Kursverwaltung()
    verwaltung.kurs_hinzufuegen(kurs)
    return kurs, student_1, student_2, verwaltung


@app.cell
def _(student_1, student_2, verwaltung):
    verwaltung.student_einschreiben(student_1, "Python fuer Anfaenger")
    verwaltung.student_einschreiben(student_2, "Python fuer Anfaenger")
    verwaltung.kurs_anzeigen()
    return


@app.cell
def _(kurs):
    kurs.teilnehmende_namen()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
