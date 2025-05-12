import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Einführung von Klassen in Pyhton""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Die foglenden Zelle zeigt die einfachste Definition einer Klasse in Python. Aber was ist eine Klasse überhaupt?`

    /// note | Definition
    Eine Klasse ist eine Vorlage für eine konkretes Ding, dass wir Objekt nennen. 
    Ein Objekt kann verschiedene Eigenheiten besitzen, wie: 

    - Eigenschaften (Properties), wie: Alter, Name, Geschlecht und
    - Verhalten, wie: `logged_sich_ein`, `kauft_Wahre`

    ///
    """
    )
    return


@app.class_definition
class User:
    age: int
    name: str

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def logged_sich_ein(self):
        print(f"Nutzer {self.name} logged sich ein")

    def kauft_wahre(self, wahre:str):
        print(f"Nutzer {self.name} kauft {wahre} ein")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Über die folgende Operartion erzeugt man eine `Instanz` eines Objektes:""")
    return


@app.cell
def _():
    frank = User(age=51, name="Frank")
    return (frank,)


@app.cell
def _(frank):
    frank.logged_sich_ein()
    return


@app.cell
def _(frank):
    frank.kauft_wahre('Bananen')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Genauso kann man natürlich beliebige Instanzen erzeugen""")
    return


@app.cell
def _():
    eva = User(age=30, name="Eva")
    return (eva,)


@app.cell
def _(eva):
    eva.age
    return


@app.cell
def _(eva):
    eva.last_name = "Müller"
    return


@app.cell
def _(eva):
    eva.last_name
    return


@app.cell
def _():
    from abc import ABC, abstractmethod

    class Animal(ABC):
        @abstractmethod
        def make_sound(self):
            raise Exception("Needs to be implemented")
    return (Animal,)


@app.cell
def _(Animal):
    class Dog(Animal):

        def make_sound(self):
            print("I make wau wau")
    return (Dog,)


@app.cell
def _(Dog):
    dog = Dog()
    dog.make_sound()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
