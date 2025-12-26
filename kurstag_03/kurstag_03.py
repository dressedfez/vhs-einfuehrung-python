import marimo

__generated_with = "0.18.3"
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

    Funktionen erlauben einem zusammenhängende Logik zu gliedern und wiederverwendbar zu machen. Sie können aus anderen Stellen des Programmes aufgerufen werden. Mit **Parametern** können Werte beliebiger Art an Funktionen übergeben werden. Rückgabewerte werden dazu benutzt Werte von der Funktion an den Aufrufer zurückzugeben.

    ```python
    def funktionen_name(parameter_1,...,parameter_n, parameter_with_default_1 = default_1, parameter_with_default_2 = default_2 ):
        <Funktionen Körper>
        return <Rückgabewert>
    ```

    **Funktionen** können ebenfalls als Parameter an Funktionen übergeben werden (Funktionen höherer Ordnung).

    ///

    ### Beispiele
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Defintion einer einfachen Funktion mit **einem** Parameter:
    """)
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
    mo.md(r"""
    Definition einer Funktion mit zwei Parametern und einem Rückgabewert:
    """)
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
    Funktion höherer Ordnung mit `default`-Verhalten:
    """)
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
    mo.md(r"""
    /// note | Übungen
    1. Schreibe eine Funktion, die eine Liste von Worten als ersten Parameter annimmt und diese als `default`-Verhalten alle Elemente in `UpperCase` umwandet. Die Funktion soll als Keyword-Parameter (Name `transform`) auch andere Transformationnen erlauben.
    2. Erstelle eine Funktion, die das  arithmetische Mittel einer Liste von Zahlen bestimmt, wobei die **äußere** Funktion `mean` und die innere `total` heißen soll (letztere soll die Summe bestimmen).
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
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
    **Beispiel:** Lambda Funktion mit mehreren Argumenten und Namen
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
    mo.md(r"""
    Beispiel einer anonyomen Lambda-Funktion, die die gegebene Zahl quadriert:
    """)
    return


@app.cell
def _():
    _liste = [1, 2, 3, 4, 5]
    # Transformiere Liste durch Quadrieren der Elemente
    quadrierer = lambda a: a**2
    # transformiere Liste mittels der Quadrierer-Funktion
    transformiere_liste(_liste, quadrierer)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Übungen
    1. Schreibe eine  Lamdba-Funktion mit zwei Parametern, die prüft, ob eine Zeichenkette (erster Parameter) länger ist als ein bestimmter ganzzahliger Wert (zweiter Parameter).
    2. Schreibe eine Funktion, die als Parameter eine Zeichenkette annimmt und als Rückgabewert eine Lambda-Funktion zurückgibt. Im Fall, dass die Zeichenkette `add` ist, soll eine Lambda-Funktion für die Addition zweiter Werte zurückgegeben werden. Im Fall, dass die Zeichenkette `sub` ist, soll eine Lambda-Funktion für die Substraktion zürückgegeben werde. Ansonten soll die Identitätsfunktion zurückgegeben werden.
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Map, Filter und Reduce Funktionen

    Die Funktionen `map`, `filter` und `reduce` gehören vor allem in den Bereich funktionale Programmierung. Alle Funktione nehmen neben einem Iterable auch eine Funktion an, die auf jedes Element des Iterables angewandt wird.

    **Beispiel** für `map`
    """)
    return


@app.cell
def _():
    namen = ["frank", "egon", "karl", "gustav"]
    list(map(lambda e: e.title(), namen))
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

    Die Funktion `reduce` ist nicht Teil des Kern-Python-Moduls, aber Teil der Standard-Python-Installation.
    Aus diesem Grund müssen wir die Funktion der Umgebung durch Importieren bekannt machen.

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
    1. Schreibe mit Hilfe der `reduce`-Funktion eine Funktion, die die Fakultät für eine natürliche Zahl $n \in \mathbb{N}$ via

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

    burger = reduce(lambda so_far, zutat: f"{so_far} + {zutat}", zutaten)

    print("🍔 Burger-Bauplan:")
    print(burger)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
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
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tupel werden mit runden Klammen erzeugt:
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
    )  # hier könnten auch andere Kontainertypen verwendet werden
    t2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    wie bei Listen können die Elemente über Indizes referenziert werden
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
    # t2[0] = "Karl" # enterne das Hash am Anfang der Zeile
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tupel sind gut dafür zusammengehörende Daten zu speichern. Der Nachteil ist:

    1. das man die Felder **nicht** mittels eines Namens adressieren kann und
    2. das **kein Verhalten** einem Tupel zugeordnet werden kann sowie diese
    3. **nicht** geändert werden können (dies ist auch manchmal ein Vorteil).

    Diese **Beschränkungen** und einige mehr lassen sich durch die Einführung von Klassen beseitigen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Definition
    Eine Klasse ist wie eine Blaupause/Schablone (Vorlage) für ein Ding, dass man erzeugen will. Wobei dieses Ding auch Verhalten und veränderbare Eigenschaften haben kann.
    ///
    Hier zum Beispiel eine Schablone eines Buchstabens:

    <div align="center">
        <img alt="Blaupause Buchstabe" src="https://upload.wikimedia.org/wikipedia/commons/e/ee/Metal_Stencil_W.jpg"/>
    </div>
    sowie eine konkreter Buchstabe W.

    Der Buchstabe könnte z.B. die Eigenschaften:

    - Farbe
    - Größe
    - Schriftart
    - etc

    haben. Außerdem könnte er das Verhalten haben, dass man:

    - die Farbe und Schriftart ändert sowie
    - die Größe skaliert.


    Grafisch kannn dies mittels eines Klassen-(-UML)-Diagrammes dargestellt werden
    <div align="center">
    <img alt="Klassendiagramm" src="public/Klassendiagramm.png"/>
    </div>

    In Python lässt sich eine **Klasse** folgendermaßen definieren:

    /// note | Definition
    Eine Klasse ist durch das Keyword **class** gekennzeichnet

    ```python
     class KlassenName:
    ```
    Dies definiert ein minimale Klasse, die aber noch nicht sehr nützlich ist.

    ///

    **Beispiel**
    """)
    return


@app.class_definition
class MyClass:
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    die Klasse `MyClass` kann mittels dem folgende Ausdruck **erzeugt** werden:
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Damit haben wir noch nicht wirklich was gewonnen. Dies ändert sich, wenn wir den Klassen:

    - Eigenschaften und
    - Verhalten


    geben.

    /// note | Definition
    Eine Klasse mit Eigenschaften und Verhalten kann, wie folgt definiert werden:

    ```python
    class Buchstabe:

        def __init__(self, buchstabe, farbe = "Scharz", schriftart = "Times New Roman", groesse = 12):
            # Eigenschaften
            self._fahrzeug_typ = fahrzeug_typ # gilt via Vereinbarung als interne Variable
            self.farbe = farbe

            // weiterere Initialisierungsanweisungen


        # Verhalten -- Funktion wird in diesem Zusammenhang Methode genannt
        def fahre(self):
            print(f"Car of type {self._fahrzeug_typ} is driving")

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
        Methode, die erlaubt die Farbe des Buchstabens zu ändern.
        """
        self.farbe = neue_farbe
        print(
            f"Der Buchstabe {self._buchstabe} hat jetzt die Farbe {self.farbe}."
        )

    def set_schriftart(self, neue_schriftart):
        """
        Methode, die erlaubt die Schriftart zu für den Buchstaben zu ändern.
        """
        self.schriftart = neue_schriftart

    def skaliere_groesse(self, skalierungs_faktor):
        """
        Methode, die erlaubt die Größe des Buchstabens anzupassen.
        """
        self.groesse = skalierungs_faktor * self.groesse


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Bemerkung
    Eine wichtiger Gesichtspunkt in der Objekt-Orientierten Programmierung (OOP) ist die **Kapselung von Daten**.
    Sprachen, wie z.B. Java, erlauben für die Kapselung für Daten mit eigenen Sprachkonstrukten, wie **private**, **protected** oder **public**  zu kontrollieren. Dies ist bei Python nicht so. Hier wir auf **Vereinbarung** gesetzt, d.h.

    - Variablen, die mit einem Unterstrich beginnen, wie z.B. `_buchstaben` in dem obigen Beispiel, gelten als **protected** die eigenen Klasse und deren Unterklassen (siehe nächster Abschnitt) können/sollen darauf zugreifen.
    - Variable, die mit zwei Unterstrichen beginnen, gelten als **private**, d.h. man kann/soll nur aus der Klasse selbst auf die Variable zugreifen.
    - alle anderen Variablen gelten als **public**
    ///
    """)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Übung
    1. Was passiert, wenn man in der obigen Klasse `Buchstaben` die Methode `__str(...)__` auskommentiert?
    2. Wie ändert sich der das `print` eines Buchstabens?
    3. Was bedeutet das Überscheiben einer Methode?
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Vererbung und Komposition von Klassen

    Vererbung ist ein Konzept, dass sehr verbreitet ist, wenn man von Objekt-Orientierten Programmiersprachen spricht. Vererbung erlaubt es

    - Daten und
    - Verhalten

    an Objekte weiterzugeben, die von einer anderen Klasse abstammen (erben). Hier ein Beispiel, dass verschiedene Beziehungen darstellt.
    Die `Ist-eine-Relation` wird durch Vererbung modelliert. Die `Hat-eine-Relation` wird nicht durch Vererbung modelliert, sondern durch Komposition.

    <div align="center">
    <img src="public/KlassendiagrammVererbung.png"/>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Vererbung von Klassen

    Klassen können von anderen Klassen erben. Dies wird durch das Angeben der Elternklasse in Klammern nach dem Klassennamen gemacht.
    Im folgenden Beispiel erbt die Klasse `Student` von der Klasse `Person` und damit obiges Diagramm umgesetzt. Die **Vererbung** wird durch eine **Ist-eine**-Relation dargestellt  (Der Student ist eine Person).
    """)
    return


@app.class_definition
class Person:
    def __init__(
        self, name: str, alter, telefonnummer=None, email_adresse=None
    ):
        self.name = name
        self.alter = alter
        self.telefonnummer = telefonnummer
        self.email_adresse = email_adresse
        self._adresse = None

    def _validiere_email_adresse(self, email_adresse):
        if "@" in email_adresse:
            return True
        return False

    def setze_gueltig_email_adresse(self, neue_email_adresse):
        if _validiere_email_adresse(self, neue_email_adresse):
            self.email_adresse = neue_email_adresse
            return
        print(
            f"{neue_email_adresse} ist gültig. Alte E-Mail-Adresse wird nicht ersetzt."
        )


@app.class_definition
class Student(Person):
    kurse = []

    def __init__(self, name, alter, studenten_id):
        super().__init__(name, alter)
        self.hat_bezahlt = False
        self.studenten_id = studenten_id

    def darf_sich_einschreiben(self):
        return self.hat_bezahlt

    def set_hat_bezahlt(self, hat_bezahlt):
        self.hat_bezahlt = hat_bezahlt

    def get_alle_kurse(self):
        return self.kurse

    def schreibt_sich_in_kurs_ein(self, kurs):
        if self.darf_sich_einschreiben():
            self.kurse.append(kurs)
            print(f"{self.name} hat sich in Kurs {kurs} eingeschrieben")
        else:
            print(f"{self.name} muss erst die Gebühr bezahlen")

    def get_alle_seminare(self):
        return self.kurse


@app.class_definition
class Professor(Person):
    def __init__(self, name, alter, einkommen):
        super().__init__(name, alter)
        self.einkommen = einkommen


@app.cell
def _():
    frank = Professor(name="Frank Zimmer", alter=51, einkommen=20000)
    anna = Student("Anna Müller", 47, 2)
    return (anna,)


@app.cell
def _(anna):
    anna.schreibt_sich_in_kurs_ein("Python für Anfänger")
    anna.set_hat_bezahlt(True)
    anna.schreibt_sich_in_kurs_ein("Python für Anfänger")
    anna.get_alle_kurse()
    anna.schreibt_sich_in_kurs_ein("Datenanalyse mit Python")
    anna.get_alle_kurse()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Kompisition von Klassen

    Neben der Vererbung ist ein anderes wichtiges Konzept die **Kompistion** von Klassen. Kompistion bedeutet, dass eine Klasse eine andere Klasse als Eigenschaft hat. Dies wurde im obigen Beispiel bereits durch die Klasse `Adresse` gezeigt. Hier ist diese Eigenschaft als Programmcode umgesetzt. Die **Komposition** wird durch eine **Hat-eine**-Relation dargestellt Die Person **hat** eine Adresse.
    """)
    return


@app.class_definition
class Adresse:
    def __init__(self, strasse, postleitzahl, stadt, land):
        self.strasse = strasse
        self.postleitzahl = postleitzahl
        self.stadt = stadt
        self.land = land

    def addresse_ausgeben(self):
        print(f"{self.strasse}, {self.postleitzahl} {self.stadt}, {self.land}")


@app.cell
def _(anna):
    addresse_anna = Adresse(
        strasse="Hauptstraße 5",
        postleitzahl="12345",
        stadt="Musterstadt",
        land="Deutschland",
    )
    anna.adresse = addresse_anna
    return


@app.cell
def _(anna):
    print(f"{anna.name} wohnt in der Stadt {anna.adresse.stadt}")
    return


@app.cell
def _(anna):
    anna.adresse.addresse_ausgeben()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Übungen
    1. **Einfache Vererbung - Fahrzeuge (Leicht)**
       Erstelle eine Basisklasse `Fahrzeug` mit den Attributen marke und baujahr. Implementiere eine Methode
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

        Erstelle eine Funktion tier_konzert(tiere), die eine Liste von Tieren erhält und jedes Tier seinen Laut
       geben lässt.

    3. **Komposition - Computer und Komponenten (Mittel)**

         Erstelle Klassen für Computer-Komponenten:

         - `Prozessor` mit Attributen `modell` und `ghz`
         - `Arbeitsspeicher` mit Attributen `groesse_gb` und `typ`
         - `Festplatte` mit Attributen `kapazitaet_gb` und `ist_ssd` (Boolean)

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


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
