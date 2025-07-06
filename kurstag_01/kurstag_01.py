import marimo

__generated_with = "0.14.9"
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Python hat einige Konvenntionen und Regeln, die für Variablennamen gelten. Hier zunächst die Regeln: 

    /// tip | Regeln 
    1. Eine Variable darf nur aus Buchstaben (a-z,A-Z), Ziffern (0-9) und Unterstrichen bestehen.
    2. Eine Variable darf **nicht** mit einer Ziffer beginnen.
    3. Leer- und Sonderzeichen sind **nicht** erlaubt.
    4. Groß- und Kleinschreibung wird beachtet
    5. Python Keywörter sind **nicht** erlaubt (z.B. if-else, while, etc)
    ///
    Folgende Variablenname sind nicht erlaubt:

    - Regel 1:  1name ❌
    - Regel 3: mein name ❌
    - Regel 3: mein&name ❌
    - Regel 5: while ❌

    /// tip | Konventionen
    Die Konventionen wurden in [PEP8](https://peps.python.org/pep-0008/) festgelegt.
    Zusammegefasst besagt diese Konvention für Variablen:

    1. Variablennamen sollten **beschreibend und in Kleinbuchstaben** geschrieben sein:
    z. B. benutzername, anzahl_karten, max_wert.

    2. **Unterstriche** werden verwendet, um Wörter lesbar zu trennen:
    z. B. gesamt_summe statt gesamtsumme oder gesamtsumme123.

    3. Für Konstanten (feste Werte) verwendet man **GROẞBUCHSTABEN**:
    z. B. PI = 3.1415
    ///
    """
    )
    return


@app.cell
def _():
    # gültige Variablen mit Werten
    benutzer_name = "Frank"
    anzahl_karten = 2
    max_wert = 3

    PI = 3.415
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Datentypen

    **Was sind Datentypen?**

    /// note | Definition
    Ein Datentyp ist eine Zusammenfassung von Objekten/Dingen, die vorbestimmte Operationen erfüllt und eine bestimmten Datenbereich abdeckt.
    ///



    Python unterstützt eine große Zahl bereits vorgefertigter Datentypen.

    **Beispiele**

    1. **int** - ganze Zahlen mit den mathematischen Operationen, z.B. Plus, Minus, etc
    2. **str** - Zeichenketten mit verschiedenen Operationen, z.B. Verbinden von Zeicheketten


    | Type | Python-Ausdruck |
    | - | - |
    |Text Type |	str |
    | Numeric Types|	int, float, complex|
    | Boolean Type | 	bool | 
    | None Type|	NoneType |
    | Sequence Types |	list, tuple, range |
    | Mapping Type |	dict |
    | Set Types |	set, frozenset |
    | Binary Types |	bytes, bytearray, memoryview|

    Weitere Datentypen können von uns definiert werden, mehr dazu später.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Zeichenketten-Datentyp (str)

    Mit Zeichenketten (str = Strings) lassen sich Buchstaben, Worte und Sätze abspeichern  und manipulieren.
    """
    )
    return


@app.cell
def _():
    s1 = "ein"  # können mit einfachem Apostroph
    s2 = "String"  # oder mit Gänsefüßschen erzeugt werden
    return s1, s2


@app.cell
def _(s1, s2):
    s1 + s2  # das + erlaubt Zeichenketten zu verbinden (concatonate)
    return


@app.cell
def _(s1, s2):
    (
        s1 + " " + s2
    )  # hier haben wir nur noch eine dritten leeren String zur Lesbarkeit hinzugefügt
    return


@app.cell
def _():
    multiline_string = """
    Dies ist ein ein 
    sehr 
    langer String, der über 
    mehrere Zeilen geht.
    """
    multiline_string
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Interessant sind auch noch formatierte Strings, die wie folgt definiert werden können:""")
    return


@app.cell
def _():
    zahl = 2
    sf = f"Dies ist ein formatiertier String, mit Variable-Interpolation, wie z.B. dieer Zahl {zahl} oder {zahl:.2f}, wobei letztere zwei Nachkommastellen hat."
    sf
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Numerische Datentypen
    ### Ganze Zahlen

    Sind alles natürlichen Zahlen ${\mathbb N}$, d.h. ...-2,-1,0,1,2,...., wobei der Computer nur einen endlichen Speicher hat und diese deshalb eingeschränkt sind auf einen endlichen Bereich. Bei Python, anders als bei Java, ist die Einschränkung nur durch den RAM-Speicher des benutzten Computer begrenzt. Es gibt keine obere Schranke innerhalb der Programmierspache.
    """
    )
    return


@app.cell
def _():
    ganze_zahl = 3
    return (ganze_zahl,)


@app.cell
def _(ganze_zahl):
    type(ganze_zahl)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""folgendes zeigt, dass die riesige Zahlen darstellen kann:""")
    return


@app.cell
def _():
    10**100  # ein Google kann ohne Probleme mit Python dargestellt werden
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""man kann auch einfach von Gleitkommazahlen oder String (siehe nächste Abschnitt) nach in **int** konvertieren:""")
    return


@app.cell
def _():
    int(3.14)
    return


@app.cell
def _():
    anzahl_studenten = "2"
    int(anzahl_studenten)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Operationen mit **int** werden wir am nächsten Kurstag besprechen.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Gleitkommazahlen

    Gleitkommazahlen sind Zahlen, die einen Nachkommaanteil haben. Dies können einfach mit Python erstellt werden.
    """
    )
    return


@app.cell
def _():
    2.5
    return


@app.cell
def _():
    1 / 127
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Es gibt auch einige bekannte Konstanten, die in Pyhton eingebaut sind:""")
    return


@app.cell
def _():
    import math

    math.pi, math.e
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Wie bei **int** kann man von Strings und ganzen Zahlen nach Gleitkommazahlen konvertieren:""")
    return


@app.cell
def _():
    float(3)
    return


@app.cell
def _():
    float("3.14")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Listen und Mengen (set)

    Python kennt einige Datentypen, die es erlauben mehrere Elemente eines **bestimmten** Datentypen zusammenzufassen. Wir stellen hier als wichtigste Vertreter den `List` und `Set`-Type vor.

    ### Listen
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Listen haben Eigenschaften, die Sie von anderen Kontainertypen unterscheiden.

    /// tip | Eigenschaften von Listen
    Folgende Eigenschaften unterscheiden Listen gegenüber anderen Kontainertypen, wie z. B. Mengen und Dictionares (Schlüssel-Wert-Paare):

    1. Listen sind geordnet, d.h. die Reihenfolge der Elemente in einer Liste ist festgelegt und kann nur durch Operationen auf der Liste geändert werden.
    2. Listen können Elemente von unterschiedlichen Typen enthalten.
    3. Listen haben keine fest Länge, d.h. sie können wachsen und schrumpfen.
    ///

    Punkt 3. zeigt, dass **Listen**, nicht wie Strings, veränderbar sind.


    Hier eine grafische Darstellung eines Liste (Arrays) von Strings (str)
    <img src="./public/str_memory.svg" width="200">
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### Erzeugung von Listen:

    Eine leere Liste kann auf diese Weisen:
    """
    )
    return


@app.cell
def _():
    # 1. Möglichkeit
    leere_liste_1 = list()
    # 2. Möglichkeit
    leere_liste_2 = []
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""und eine Liste, die schon Elemente enthält, kann so erzeugt werden:""")
    return


@app.cell
def _():
    liste_mit_zeichenketten = ["Hallo", "Welt"] # Liste mit Zeichenketten als Elemente
    liste_mit_zahlen = [1,2,3] # Liste mit Zahlen als Elemente
    liste_mit_unterschielicher_datentypen = [1, "Hallo", 3.14] # Liste, die Elemente enthält, die unterschiedliche Datentypen haben
    return (liste_mit_zeichenketten,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Bemerkung
    Eine Liste kann beliebige Elemente enthalten, die auch nicht unbedingt vom gleichen Typ sein müssen. Im Allgemeinen ist es aber üblich, dass die Elemente den gleichen Datentyp haben.
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Operationen auf Listen""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Über die **append**-Methode können Elemente an das Ende einer Liste angehängt werden:""")
    return


@app.cell
def _(liste_mit_zeichenketten):
    liste_mit_zeichenketten.append("und")
    liste_mit_zeichenketten.append("Kurs")
    liste_mit_zeichenketten.append("Kurs") # ein Element kann auch zwei Mal hinzugefügt werden
    liste_mit_zeichenketten
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip 
    `append` hängt Element am Ende der Liste an.
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""über die **remove**-Methode können Elemente entfernt werden:""")
    return


@app.cell
def _(liste_mit_zeichenketten):
    liste_mit_zeichenketten.remove("und")
    liste_mit_zeichenketten
    return


@app.cell
def _(liste_mit_zeichenketten):
    liste_mit_zeichenketten.remove("Kurs") # remove entfernt das erste Element, das in der Liste gefunden wird, wenn man von vorne sucht
    liste_mit_zeichenketten
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip 
    `remove` entfernt das erste Element, das in der Liste gefunden wird.
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Zum Entfernen des letzten Elements einer Liste gibt es den Befehl **pop**:""")
    return


@app.cell
def _(liste_mit_zeichenketten):
    el = liste_mit_zeichenketten.pop()
    el
    return


@app.cell
def _(liste_mit_zeichenketten):
    liste_mit_zeichenketten
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip
    `pop` entfernt ohne weiteres Argument das letzte Element der Liste.
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### Indizieren in Listen

    Dies bedeutet, dass ich Elemente der Liste aus dieser dediziert auslese. Da eine Liste geordnet ist, kann ich jedes Listenelement direkt anspechen. Die Indizierung der Liste beginnt bei 0 und geht bis Länger der Liste minus 1. Hier ein Beispiel: 
    """
    )
    return


@app.cell
def _():
    indizieren_in_liste = ["erste Element", "zweites Element", "drittes Element", "viertes Element"]
    return (indizieren_in_liste,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Das erste Element erhalte ich, in dem ich auf das Elemnt mit dem Index 0 zugreife: """)
    return


@app.cell
def _(indizieren_in_liste):
    indizieren_in_liste[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""das letzte Element erhalte ich, in dem ich auf das Element mit dem Index **Länge der Liste minus 1** zugreife: """)
    return


@app.cell
def _(indizieren_in_liste):
    len(indizieren_in_liste) #Länge der Liste
    return


@app.cell
def _(indizieren_in_liste):
    indizieren_in_liste[len(indizieren_in_liste)-1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""andere Möglichkeit ist: """)
    return


@app.cell
def _(indizieren_in_liste):
    indizieren_in_liste[-1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// note | Definition:
    Der Slice-Operator : wird in Python verwendet, um einen zusammenhängenden Teil (Ausschnitt) einer Sequenz wie einer Liste, einem String oder einem Tupel auszuwählen. Mit ihm können Bereiche über Start-, End- und optionalen Schrittwerten spezifiziert werden, sodass ein neuer Teilbereich (Slice) der Sequenz zurückgegeben wird, ohne das Original zu verändern.

    **Synatax:**

    - Syntax: sequence[start:stop:step]
    - start: Index, an dem der Ausschnitt beginnt (inklusive)
    - stop: Index, an dem der Ausschnitt endet (exklusive)
    - step: Schrittweite (optional)


    Wenn Werte fehlen, werden Standardwerte verwendet (start=0, stop=Ende der Sequenz, step=1).
    ///

    **Beipiele:**
    """
    )
    return


@app.cell
def _(indizieren_in_liste):
    indizieren_in_liste[0:3] 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Achtung
    Bei dem **Slice**-Operator wird der letzte der **stop**-Wert nicht angenommen.
    ///
    """
    )
    return


@app.cell
def _(indizieren_in_liste):
    indizieren_in_liste[0:4] 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Mit dem **step** kann man jedes **x**-te Element extrahieren: """)
    return


@app.cell
def _(indizieren_in_liste):
    indizieren_in_liste[0:4:2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Ist der **step** negativ, wird die Liste rückwärts durchlaufen: """)
    return


@app.cell
def _(indizieren_in_liste):
    indizieren_in_liste[3:0:-1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// note | Übungen

    1. Welche weiteren Operationen kann man mit Listen noch machen (tab-completion)?
    2. Prüfe mittels des Vergleichsoperators (==), ob ein Wort ein Palindrom ist. Zum Beispiel ist das Wort `ANNA` ist ein Palindrom. Ein Wort besteht aus einer Liste von Buchstaben und man kann eine Operation die von Listen.
    3. Erzeuge mit dem Ausdruck
    ```python
    zahlen_eins_bis_100 = list(range(1,101))
    ```
    alle Zahlen von 1 bis hundert und extrahiere mittels indizieren alle geraden und ungeraden Zahlen aus dieser Liste.
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):

    test_wort = "ANNA"
    test_wort
    wort = list(test_wort)
    wort.reverse()
    "".join(wort) == test_wort
    mo.md(text="# (mögliche) Lösung zu 2.")
    return


@app.cell(hide_code=True)
def _(mo):

    zahlen_eins_bis_100 = list(range(1,101))
    ungeraden_zahlen_bis_100 = zahlen_eins_bis_100[0:101:2]
    geraden_zahlen_bis_100 = zahlen_eins_bis_100[1:101:2]
    mo.md("(mögliche) Lösung für 3")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Sets/Mengen

    Mengen (Sets) haben Eigenschaften, die Sie von anderen Kontainertypen unterscheiden.

    /// tip | Eigenschaften von Mengen/Sets
    Folgende Eigenschaften unterscheiden Sets gegenüber anderen Kontainertypen, wie z. B. Listen und Dictionares (Schlüssel-Wert-Paare):

    1. Listen sind **nicht** geordnet, d.h. die Reihenfolge der Elemente in einer Menge ist **nicht** festgelegt.
    2. Sets können Elemente von unterschiedlichen Typen enthalten.
    3. Sets haben keine feste Größe, d.h. sie können wachsen und schrumpfen.
    4. Mengen haben die Eigenschaft, dass jedes Element nur ein Mal in der Menge vorkommen kann. Ein doppeltes Element, wie bei Listen möglich ist, ist hier nicht erlaubt.
    ///

    Eine leere Menge wird analog zu der Liste mit:
    """
    )
    return


@app.cell
def _():
    menge_1 = set() 
    return (menge_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""erzeugt.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Achtung
    Eine leere Menge kann **nicht** mit dem Befehl `{}` erzeugt werden. Die Konstruktion  `{}` erzeugt einen leeren Dictionary (Schlüssel-Wert-Paar).
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Man kann Elemente hinzufügen:""")
    return


@app.cell
def _(menge_1):
    menge_1.add("Hallo")
    menge_1
    return


@app.cell
def _(menge_1):
    menge_1.add("Hallo") # nochmaliges Hinzufügen ist nicht möglich
    menge_1
    return


@app.cell
def _():
    menge_2 = set(['Welt'])
    menge_2
    return (menge_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Mengenoperationen""")
    return


@app.cell
def _(menge_1, menge_2):
    # Vereinigung von zwei Mengen
    vereinigungs_menge = menge_1.union(menge_2)
    vereinigungs_menge
    return (vereinigungs_menge,)


@app.cell
def _(menge_1, vereinigungs_menge):
    # Teilmengenprüfung
    menge_1.issubset(vereinigungs_menge)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// note | Übungen
    1. Wir haben zwei Listen mit Schülern, die in GTAs gehen wollen, die zur gleichen Zeit stattfinden. Welche Schüler müssen sich nur für eine GTA entscheiden?
    ```python  
    volleyball = ["Frank", "Egon", "Markus", "Georg", "Frank"]
    fussball = ["Egon", "Franz","Steffi","Markus"]
    ```
    Was machen die Befehle `intersection`, `difference` und `symmetric_difference`?
    2. Was passiert, wenn man eine Zeichenkette (einen String) in als Argument `set(arg)` 
    übergibt?
    3. Bestimme die Buchstaben, die sowohl in
    ```python
    text1 = "Hallo Welt"
    ```
    also auch 
    ```python
    text2 = "Weltraum"
    ```
    enthalten sind. Welche sind nicht in `text1`, aber in `text2` unumgekehrt enthalten?
    ///
    """
    )
    return


if __name__ == "__main__":
    app.run()
