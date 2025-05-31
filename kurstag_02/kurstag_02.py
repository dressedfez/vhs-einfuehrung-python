import marimo

__generated_with = "0.13.11"
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
    6 / 2
    return


@app.cell
def _():
    7 / 2
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
    14 // 3
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
    a_1 = 1 + 1j * 2
    return (a_1,)


@app.cell
def _():
    a_2 = complex(2, 1)
    return (a_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Addition**""")
    return


@app.cell
def _(a_1, a_2):
    a_1 + a_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Multiplikation**""")
    return


@app.cell
def _(a_1, a_2):
    a_1 * a_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Division**""")
    return


@app.cell
def _(a_1, a_2):
    a_1 / a_2
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

    ```python
      if Bedingung_1:
         # Code Block 1
      elif Bedingung_2:
        # Code Block 2
      else:
        # else Code Block
    ```

      Der `elif`- und `else`-Zweig ist optional in obiger Definition.
    ///

    Man sollte auf folgendes achten, wenn man diese bedingte Ausführung nutzt:

    -  ⚠️ Nur der **erste** Code-Block wird ausgeführt, für den die Bedingung erfüllt ist.
    -  Versuche Bedingungen einfach und lesbar zu formulieren.
    -  Benutze `elif`,wenn  die Bedingungen gegegenseitig ausschließend sind.
    -  Benutze `else`, wenn Du einen Fallback-Fall hast (kann oft auch vermieden werden).
    -  Füge ausreichend Kommentare zu Deinem Programm hinzu, sodass Du die Logik schnell erfassen kannst.
    -  Nutze, wenn von Vorteil, Regeln der boolschen Algebra, um die Bedingungen zu vereinfachen.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Beispiel**""")
    return


@app.cell
def _(mo):
    number = mo.ui.number(start=1, stop=99, step=1)
    number
    return (number,)


@app.cell
def _(number):
    if number.value < 16:
        print("Du darfst nicht alleine in die Eisdiele gehen.")
    elif 16 <= number.value < 18:
        print("Du darfst alleine in die Eisdiele gehen.")
    else:
        print("Du musst das Eis in der Eisdiele alleine bezahlen.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Kurzschreibweise `if-else`-Ausdruck

    Es gibt für den `if-else`-Ausdruck, der sich im Prinzip, wie ein englischer Satz liest. 

    /// note | Definition 
    Die Kurzschreibweise des `if-else`-Ausdruckes hat die Form:
    ```python
    <Code Block 1> if Bedingung else <Code Block 2>
    ```
    ///

    Hier gibt es noch einige kleine Anmerkungen:

    - man kann diesen `if-else`-Ausdruck auch aneinanderhängen
    - dieser Ansatz ist besonders hilfreich, wenn man zwischen zwei Handlungen unterscheiden möchte
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Beispiel**""")
    return


@app.cell
def _(number):
    print("Ich tue...") if number.value < 16 else print("andernfalls tue ich...")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// note | Übungen

    1.	Temperatur-Checker
        Schreibe ein Programm, das eine Temperatur (in Grad Celsius) als Zahl einliest und eine passende Nachricht ausgibt:
        - über 30 °C: “Es ist heiß!”
        - zwischen 20 °C und 30 °C (einschließlich): “Angenehmes Wetter.”
        - unter 20 °C: “Ziemlich kühl heute.”
    2.	Notenrechner
        Lies eine Punktzahl (zwischen 0 und 100) vom Benutzer ein und gib die passende Note aus:
        - 90–100 Punkte: “Note: Sehr gut”
        - 80–89 Punkte: “Note: Gut”
        - 70–79 Punkte: “Note: Befriedigend”
        - unter 70 Punkte: “Note: Verbessern nötig”
    3.	Gerade oder ungerade Zahl
        Schreibe ein Programm, das eine ganze Zahl vom Benutzer einliest und ausgibt, ob sie
        - durch 2 teilbar ist („Gerade Zahl“) oder
        - nicht durch 2 teilbar ist („Ungerade Zahl“).

        Verwende dabei auch else.

    5.	Eintrittspreis berechnen
        Erstelle ein Programm, das anhand des Alters einer Person den Eintrittspreis bestimmt:
        - unter 6 Jahren: “Eintritt frei”
        - 6 bis 17 Jahre: “Kinderpreis: 5 €”
        - 18 bis 64 Jahre: “Normalpreis: 10 €”
        - ab 65 Jahren: “Seniorenpreis: 6 €”
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Schleife oder wiederholende Ausführung von Programmteilen

    Python kennt verschiedene Schleifentypen, die unterschiedliche Anwendungsgebiete haben. Die wichtgiste und verbreiteste Schleife ist die **for-loop**. Weniger oft wird die **while-loop** eingesetzt. Trotzdem behandeln wir diese hier zu erst.

    ### **While-loop**-Schleife

    Die **While-loop** ist wie folgt definiert:

    /// note | Definition

    Einfache Variante: 
    ```python
    while Bedingung:
        <Code Block>
    ```

    Obiger `<Code Block>` wird so lange ausgeführt, wie die Bedingung erfüllt ist. 

    Variante mit `else`-Abschnitt:
    ```python
    while Bedingung:
        <Code Block>
    else:
        <Code Block für Else-Fall>
    ```

    Der `Code Block` wird so lange ausgeführt wie die Bedingung erfüllt ist. Wird diese Bedingung irgendwann nicht mehr erfüllt sein, so wird der `else`-Zweig ein Mal durchlaufen.
    ///

    **Beispiel mit `continue`**
    """
    )
    return


@app.cell
def _():
    i = 0
    while i < 10:
        i += 1
        if i == 5:
            print(f"keine Behandlung der Nummer {i}")
            continue  # mit diesem Befehl springt man wieder zum "Start" der Schleife ohne den Programmteil danach auszuführen
        print(f"Durchlauf Nummer {i}")
    else:
        print("Hallo aus dem Else-Zweig")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Beispiel mit `break`**

    Der `else`-Zweig wird in diesem Fall nicht durchlaufen. Dies gilt aber nur, wenn es zum `break` kommt.
    """
    )
    return


@app.cell
def _():
    index = 0
    while index < 10:
        index += 1
        if index == 5:
            print(f"keine Behandlung der Nummer {index}")
            break  # mit diesem Befehl springt man aus der Schleife heraus
        print(f"Durchlauf Nummer {index}")
    else:
        print("Hallo aus dem Else-Zweig")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip | Bemerkung

    Die Keywords **break** und **continue** werden auch in anderen Konstruktionen, wie z.B. der **for-loop** benutzt.

    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### **For-loop**-Schleife

    /// note | Definiton

    Die **For**-Schleife wird dazu genutzt über ein Iterable (ein iterierbare Sammlung oder Objekt) zu laufen.
    Die allgemeine Form sieht wie folgt aus:

    ```python
    for x in <Iterable>:
        <Code Block>
    else: # dieser Anteil ist optional
        <Code Block für Else-Zweig>
    ```

    Wie schon bei der **While**-Schleife können die Keyworte **continue** und **break** genutzt werden. Wird das Keyword **break** for dem Ende der Schleife genutzt wird der optionale **else**-Zweig durchlaufen.

    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Beispiel mit Iterable**""")
    return


@app.cell
def _():
    for counter in range(0, 100, 5):
        print(f"{counter} ist gerade") if counter % 2 == 0 else print(
            f"{counter} ist ungerade"
        )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Beispiel mit Liste**""")
    return


@app.cell
def _():
    students = ["Ania", "Magda", "Kasia"]
    for name in students:
        if name.startswith("M"):
            continue
        print(f"{name} nimmt am Kurs teil.")
    else:
        print("Nicht alle Elemente der Studentenliste wurden abgearbeitet.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// note | Übungen
    1. Primzahlprüfung (for-Schleife mit break und else)

        Frage den Benutzer nach einer Zahl größer als 1. Überprüfe mit einer for-Schleife, ob sie eine Primzahl ist.

        - Wenn ein Teiler gefunden wird, gib “Keine Primzahl” aus und beende die Schleife mit break.
        - Falls die Schleife vollständig durchläuft (ohne break), gib im else-Zweig “Ist eine Primzahl” aus.



    2. Zahlensuche in einer Liste (for-Schleife mit break und else)

        Gegeben ist eine Liste von Zahlen.
        Suche nach der Zahl 42.


        - Wenn du sie findest, gib “Zahl gefunden!” aus und verlasse die Schleife mit break.
        - Wenn die Schleife vollständig durchläuft, gib im else-Zweig “Zahl nicht in der Liste” aus.


    4. Positive Zahleneingabe (while-Schleife mit continue, break und else)

        Fordere den Benutzer auf, wiederholt ganze Zahlen einzugeben.


        - Wenn eine negative Zahl eingegeben wird, gib “Nur positive Zahlen erlaubt” aus und fahre mit der nächsten Eingabe fort (continue).
        - Wenn der Benutzer die Zahl 0 eingibt, beende die Schleife mit break.
        - Wenn die Schleife ohne break endet, gib im else-Zweig “Danke für die Eingaben” aus.

    5. Zähle bis 10, überspringe bestimmte Zahlen (for-Schleife mit continue)

        Gib die Zahlen von 1 bis 10 aus, aber überspringe die Zahlen 3 und 7.
        Verwende continue, um diese beiden Zahlen nicht auszugeben.
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Achtung
    Verändere niemals die Sammlung über die Du iterierst! Dies führt zu unerwartete Ergebnisse. Diese Aussage gilt für alle Arten von Schleifen.
    ///

    **Beispiel**
    """
    )
    return


@app.cell
def _():
    teilnehmer = ["George", "Frank", "Ralf", "Udo"]

    for n in teilnehmer:
        if n == "Frank":
            teilnehmer.remove(n)
        print(n)
    return (teilnehmer,)


@app.cell
def _(teilnehmer):
    teilnehmer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### List-Comprehension

    Dies ist eine spezielle Form der **for**-Schleife, die dazu genutzt wird _spezielle_ Listen zu erzeugen. **List-Comprehensions** lassen sich wie folgt definieren: 

    /// note | Definition
    Definition einer **List-Comprehension**:
    ```python
    [f(x) for x in <Iterable> if g(x) ]
    ```

    -  `x`  -  ein Element
    -  `f(x)` - Ausdruck, der auf jedes Element angewandt wird
    -  `g(x)` - wenn Bedigung erfüllt, wie `f(x)` der Liste hinzugefügt 
    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""**Beispiel: Liste mit Quadratzahlen von 1 bis 10**""")
    return


@app.cell
def _():
    liste = [x**2 for x in range(1, 11)]
    print(liste)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// note | Übungen

    1.	Gegeben ist die Liste

        ```python
          obst_liste = ["Apfel", "banane", "Birne", "kirsche", "Melone"]
        ```

        erstelle eine neuen Liste bei der alle ersten Buchstaben groß geschrieben sind.
  
    1.  Gebe von obiger Liste nur die Worte aus, die weniger als sechs Buchstaben haben.
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Einführung von Interaktivität durch Nutzung von **marimo**-Elementen

    **Marimo** verfügt über eine Menge von **interaktiven** Elementen und Darstellungsmöglichkeiten, die wir nicht alle hier ansprechen können. Um für spätere Arbeiten und Manipulationsmöglichkeiten vorbereitetet zu sein, werden hier verschiedene Elemente besprochen.

    Die Dokumentation von **marimo** kann man hier:

    - https://docs.marimo.io/ und insbesondere hier
    - https://docs.marimo.io/api/

    finden.

    Hier ein kurzer Überblick:

    - Slider:  sind z.B. dafür geeignet die Abhängigkeit von Parameter zu realisieren.
    - Dropdown-Multiple-Choice-Menü: sind dafür geeignet kategorische Auswahl zu treffen
    - Radio-Button:
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Slider""")
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 10, label="Erdbebenstärke")
    slider
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Dropdown-Multiple-Choice-Menü""")
    return


@app.cell
def _():
    # erstelle eine Array zum Speichern der Auswahl
    choices = []
    return (choices,)


@app.cell
def _(mo):
    # erzeuge ein Dropdown-Menü und zeige es an
    choice = mo.ui.dropdown(options=["Apfel", "Banane", "Birne"])
    choice
    return (choice,)


@app.cell
def _(choice, choices):
    # wenn die Auswahl (choice) eine Wert enthält, dann Speichern wir ihn
    # in dem Fall aktualisieren wir auch die Anzeige
    if choice.value is not None:
        choices.append(choice.value)
        print(len(choices))
    return


@app.cell
def _(mo):
    clear_choices = mo.ui.run_button(label="Lösche Auswahl")
    clear_choices
    return (clear_choices,)


@app.cell
def _(choices, clear_choices):
    if clear_choices.value:
        print("Lösche Auswahl")
        choices.clear()
    return


@app.cell
def _(choices):
    choices
    return


@app.cell
def _(mo):
    options = ["Äpfel", "Orangen", "Pfirsiche"]
    radio = mo.ui.radio(options=options)
    radio
    return (radio,)


@app.cell
def _(radio):
    radio.value
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// note | Übungen

    Geht zur den folgenden Seiten: 🛜

    - https://docs.marimo.io/examples/
    - https://docs.marimo.io/api/

    und informiert Euch über weitere Möglichkeiten sowie testet dies bei Euch lokal.
    ///
    """
    )
    return


if __name__ == "__main__":
    app.run()
