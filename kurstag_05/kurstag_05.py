# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.19.2",
#     "matplotlib==3.10.8",
#     "mcp==1.25.0",
#     "openpyxl==3.1.5",
#     "pandas==2.3.3",
#     "polars==1.36.1",
# ]
# ///

import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    import polars as pl
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Beispielanalyse
    """)
    return


@app.cell
def _(df_titanic):
    df_titanic["Age"].plot(
        kind="hist",
        bins=20,
        xlabel="Age",
        ylabel="Anzahl Personen",
        title="Altersverteilung",
    )
    return


@app.cell
def _(df_titanic):
    ax = df_titanic["Survived"].value_counts().plot(kind="bar")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Nicht überlebt", "Überlebt"])
    ax.set_ylabel("Anzahl Personen")
    ax.set_title("Überlebensstatus")
    return


@app.cell
def _(df_titanic):
    df_titanic.boxplot(column="Fare", by="Pclass")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
