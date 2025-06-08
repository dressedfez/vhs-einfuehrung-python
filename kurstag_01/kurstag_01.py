import marimo

__generated_with = "0.13.15"
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
    und hier eine grafische Darstellung eines Arrays von Strings (str)
    <img src="./public/str_memory.svg" width="200">
    """
    )
    return


@app.cell
def _():
    meldung = ["Hallo", "Welt"]
    meldung
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
    s1 = 'ein' # können mit einfachem Apostroph
    s2 = "String" # oder mit Gänsefüßschen erzeugt werden
    return s1, s2


@app.cell
def _(s1, s2):
    s1+s2 # das + erlaubt Zeichenketten zu verbinden (concatonate)
    return


@app.cell
def _(s1, s2):
    s1+' '+s2 # hier haben wir nur noch eine dritten leeren String zur Lesbarkeit hinzugefügt
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


@app.cell
def _():
    10**100 # ein Google kann ohne Probleme mit Python dargestellt werden
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Operationen mit **int** werden wir am nächsten Kurstag besprechen.""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Gleitkommazahlen

    Gleitkommazahlen
    """
    )
    return


@app.cell
def _():
    a = 1
    b = 2
    a + b
    return


@app.cell
def _():
    mein_name = 1
    return


if __name__ == "__main__":
    app.run()
