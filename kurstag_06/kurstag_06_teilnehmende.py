# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.25.2",
#     "matplotlib==3.10.8",
#     "numpy==2.4.2",
#     "pillow==12.0.0",
#     "scikit-learn==1.8.0",
#     "scipy>=1.17.1",
# ]
# ///

# Zellenausdrücke und Rückgaben gehören zum marimo-Notebook-Format.
# ruff: noqa: B018

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    import io
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image, ImageOps
    from sklearn.datasets import load_digits
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler

    def pruefhinweis(status, aufgabe, hinweis):
        if status is None:
            return mo.callout(
                mo.md(f"**Noch offen · {aufgabe}**\n\n{hinweis}"),
                kind="neutral",
            )
        if status:
            return mo.callout(
                mo.md(f"**✓ Richtig · {aufgabe}**\n\n{hinweis}"),
                kind="success",
            )
        return mo.callout(
            mo.md(f"**Noch nicht ganz · {aufgabe}**\n\n{hinweis}"),
            kind="warn",
        )

    return (
        ConfusionMatrixDisplay,
        Image,
        ImageOps,
        LogisticRegression,
        Pipeline,
        StandardScaler,
        accuracy_score,
        io,
        load_digits,
        np,
        plt,
        pruefhinweis,
        train_test_split,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Kurstag 6 · Mein Arbeitsheft zum maschinellen Lernen

    **Ziffern erkennen mit Scikit-Learn**

    Dieses Arbeitsheft begleitet die Folien. Wir bereiten Beispieldaten vor, trainieren ein Modell und prüfen seine Vorhersagen. Danach kannst du es mit einem eigenen Ziffernfoto ausprobieren.

    ## So arbeitest du mit dem Notebook

    - Im Ordner `kurstag_06` starten: `uvx --from "marimo==0.25.2" marimo edit kurstag_06_teilnehmende.py`.
    - Codezellen mit **Shift+Enter** ausführen.
    - Ersetze in jeder Übungszelle `None` durch deinen Ausdruck.
    - **Neutral:** Aufgabe noch offen · **Orange:** Ergebnis prüfen · **Grün:** Rückmeldung bestanden.
    - Beim Fotoexperiment stehen Upload, Einstellungen, Vorhersage und verarbeitetes Bild gemeinsam auf derselben Notebook-Seite.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Überwachtes Lernen

    Das Modell lernt mit Beispielen, deren richtige Antworten bereits bekannt sind.

    - `X` enthält die Merkmale, hier die Pixelwerte der Bilder.
    - `y` enthält die richtigen Ziffern von `0` bis `9`.
    - `fit(X, y)` passt das Modell an die Trainingsbeispiele an.
    - `predict(X)` berechnet Vorhersagen für neue Bilder.
    """)
    return


@app.cell
def _(load_digits):
    digits = load_digits()
    X_digits = digits.data
    y_digits = digits.target
    digit_images = digits.images
    digit_names = digits.target_names
    return X_digits, digit_images, digit_names, digits, y_digits


@app.cell
def _(X_digits, digit_names, mo):
    mo.vstack(
        [
            mo.md(
                f"**{X_digits.shape[0]} Bilder** · "
                f"**{X_digits.shape[1]} Pixelmerkmale pro Bild** · "
                f"**Ziffern:** {list(digit_names)}"
            ),
            mo.md("Jedes Bild ist 8 × 8 Pixel groß. Scikit-Learn liefert den Datensatz direkt mit."),
        ],
        gap=1,
    )
    return


@app.cell
def _(digit_images, plt, y_digits):
    _fig, _achsen = plt.subplots(2, 5, figsize=(8, 3.7))
    for _bild, _label, _ax in zip(digit_images[:10], y_digits[:10], _achsen.flat):
        _ax.imshow(_bild, cmap="gray_r", vmin=0, vmax=16)
        _ax.set_title(f"Ziffer {_label}")
        _ax.axis("off")
    _fig.tight_layout()
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Trainings- und Testdaten

    Wir reservieren einen Teil der Beispiele. Das Modell sieht diese Bilder beim Training nicht und kann später daran geprüft werden.

    ```python
    X_train, X_test, y_train, y_test = train_test_split(
        X_digits, y_digits, test_size=0.2,
        random_state=42, stratify=y_digits
    )
    ```

    `stratify` hält die Ziffern in beiden Gruppen ähnlich verteilt. `random_state` macht dieselbe Aufteilung wiederholbar.
    """)
    return


@app.cell
def _(X_digits, mo, train_test_split, y_digits):
    test_size = 0.2
    random_state = 42
    X_train, X_test, y_train, y_test = train_test_split(
        X_digits,
        y_digits,
        test_size=test_size,
        random_state=random_state,
        stratify=y_digits,
    )
    mo.md(
        f"**Training:** {len(X_train)} Bilder  \n"
        f"**Test:** {len(X_test)} Bilder  \n"
        f"**Testanteil:** {test_size:.0%}"
    )
    return X_test, X_train, random_state, test_size, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Vier Basisübungen

    Ersetze `None` in den Antwortzellen und führe die Zellen erneut aus. Die Rückmeldung darunter prüft das Ergebnis.

    1. Eine Pipeline aus Skalierung und Klassifikation erstellen und trainieren.
    2. Ziffern für die Testdaten vorhersagen.
    3. Die Accuracy der Vorhersagen berechnen.
    4. Eine Confusion Matrix zeichnen und ihre Werte untersuchen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Aufgabe 1 · Pipeline trainieren

    Erzeuge eine Pipeline `modell` mit den Schritten `scaler` und `classifier`. Trainiere sie mit `X_train` und `y_train`.

    ```python
    modell = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=2000)),
    ]).fit(X_train, y_train)
    ```
    """)
    return


@app.cell
def _(Pipeline, LogisticRegression, StandardScaler, X_train, y_train):
    modell = None
    modell
    return (modell,)


@app.cell
def _(modell, mo, pruefhinweis, X_train, y_train):
    _status_modell = None
    if modell is not None:
        _status_modell = (
            hasattr(modell, "named_steps")
            and list(modell.named_steps) == ["scaler", "classifier"]
            and hasattr(modell.named_steps["classifier"], "classes_")
        )
    _hinweis_modell = pruefhinweis(
        _status_modell,
        "Pipeline trainiert",
        "Prüfe Reihenfolge, Modellnamen und ob du `.fit(X_train, y_train)` aufgerufen hast.",
    )
    if modell is None:
        _ausgabe_modell = _hinweis_modell
    else:
        _ausgabe_modell = mo.vstack(
            [
                _hinweis_modell,
                mo.md(f"**Genauigkeit im Training:** {modell.score(X_train, y_train):.1%}"),
            ],
            gap=1,
        )
    _ausgabe_modell
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Aufgabe 2 · Testbilder vorhersagen

    Berechne mit `modell` die Vorhersagen für `X_test` und speichere sie als `vorhersagen`.

    ```python
    vorhersagen = modell.predict(X_test)
    ```
    """)
    return


@app.cell
def _(modell, X_test):
    vorhersagen = None
    vorhersagen
    return (vorhersagen,)


@app.cell
def _(X_test, mo, pruefhinweis, vorhersagen):
    _status_vorhersage = None
    if vorhersagen is not None:
        _status_vorhersage = (
            len(vorhersagen) == len(X_test)
            and set(vorhersagen).issubset(set(range(10)))
        )
    _hinweis_vorhersage = pruefhinweis(
        _status_vorhersage,
        "Vorhersagen berechnet",
        "Es sollte für jedes Testbild genau eine Ziffer zwischen 0 und 9 vorliegen.",
    )
    if vorhersagen is None:
        _ausgabe_vorhersage = _hinweis_vorhersage
    else:
        _ausgabe_vorhersage = mo.vstack(
            [
                _hinweis_vorhersage,
                mo.md(f"**Erste zehn Vorhersagen:** `{list(vorhersagen[:10])}`"),
            ],
            gap=1,
        )
    _ausgabe_vorhersage
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Aufgabe 3 · Accuracy berechnen

    Vergleiche `vorhersagen` mit den bekannten Labels `y_test` und speichere den Wert als `genauigkeit`.

    ```python
    genauigkeit = accuracy_score(y_test, vorhersagen)
    ```
    """)
    return


@app.cell
def _(accuracy_score, vorhersagen, y_test):
    genauigkeit = None
    genauigkeit
    return (genauigkeit,)


@app.cell
def _(accuracy_score, genauigkeit, mo, pruefhinweis, vorhersagen, y_test):
    _status_genauigkeit = None
    if genauigkeit is not None and vorhersagen is not None:
        _erwartet = accuracy_score(y_test, vorhersagen)
        _status_genauigkeit = abs(genauigkeit - _erwartet) < 1e-12
    _hinweis_genauigkeit = pruefhinweis(
        _status_genauigkeit,
        "Accuracy berechnet",
        "Der Wert ist der Anteil der Testbilder, für die Vorhersage und Label übereinstimmen.",
    )
    if genauigkeit is None:
        _ausgabe_genauigkeit = _hinweis_genauigkeit
    else:
        _ausgabe_genauigkeit = mo.vstack(
            [_hinweis_genauigkeit, mo.md(f"**Accuracy:** {genauigkeit:.1%}")],
            gap=1,
        )
    _ausgabe_genauigkeit
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Aufgabe 4 · Confusion Matrix

    Erzeuge eine Confusion Matrix aus `y_test` und `vorhersagen`. Speichere die Anzeige als `matrix_anzeige`.

    Die Matrix hat zehn Zeilen und zehn Spalten. Ihre Werte zählen zusammen alle Testbilder.
    """)
    return


@app.cell
def _(ConfusionMatrixDisplay, vorhersagen, y_test):
    matrix_anzeige = None
    matrix_anzeige
    return (matrix_anzeige,)


@app.cell
def _(matrix_anzeige, mo, pruefhinweis, y_test):
    _status_matrix = None
    if matrix_anzeige is not None:
        _status_matrix = (
            hasattr(matrix_anzeige, "confusion_matrix")
            and int(matrix_anzeige.confusion_matrix.sum()) == len(y_test)
        )
    _hinweis_matrix = pruefhinweis(
        _status_matrix,
        "Confusion Matrix",
        "Zeilen stehen für die richtigen Ziffern; Spalten stehen für die Modellvorhersagen.",
    )
    if matrix_anzeige is None:
        _ausgabe_matrix = _hinweis_matrix
    else:
        _ausgabe_matrix = mo.vstack([_hinweis_matrix, matrix_anzeige.figure_], gap=1)
    _ausgabe_matrix
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Ein eigenes Ziffernfoto ausprobieren

    **Zusatzteil:** Lade eine einzelne dunkle Ziffer auf hellem Papier hoch. Das Notebook bereitet das Bild als `8 × 8`-Pixelmatrix auf und zeigt die Vorhersage samt wahrscheinlichsten Alternativen.

    Fotos aus dem Alltag unterscheiden sich von den Trainingsbeispielen. Drehe die Ziffer bei Bedarf und passe die Tintenempfindlichkeit an.
    """)
    return


@app.cell(hide_code=True)
def _(Image, ImageOps, io, np):
    def preprocess_digit_photo(
        photo_bytes,
        rotation_degrees=0,
        ink_percentile=92,
        crop_padding=12,
        target_ink_size=6,
    ):
        photo = Image.open(io.BytesIO(photo_bytes)).convert("L")
        if rotation_degrees:
            photo = photo.rotate(rotation_degrees, expand=True)
        photo = ImageOps.autocontrast(photo)
        pixels = np.asarray(photo, dtype=float)
        ink = 255.0 - pixels
        ink[ink < 35] = 0
        threshold = np.percentile(ink, ink_percentile)
        mask = (ink >= threshold) & (ink > 0)
        if not mask.any():
            return np.zeros((8, 8), dtype=float)
        rows, columns = np.where(mask)
        top = max(rows.min() - crop_padding, 0)
        bottom = min(rows.max() + crop_padding + 1, pixels.shape[0])
        left = max(columns.min() - crop_padding, 0)
        right = min(columns.max() + crop_padding + 1, pixels.shape[1])
        digit = ink[top:bottom, left:right]
        digit = np.clip(digit / digit.max() * 255.0, 0, 255)
        digit_image = Image.fromarray(digit.astype("uint8"))
        width, height = digit_image.size
        scale = target_ink_size / max(width, height)
        size = (max(1, round(width * scale)), max(1, round(height * scale)))
        digit_image = digit_image.resize(size, Image.Resampling.LANCZOS)
        square = Image.new("L", (8, 8), color=0)
        square.paste(digit_image, ((8 - size[0]) // 2, (8 - size[1]) // 2))
        return np.asarray(square, dtype=float) / 255.0 * 16.0

    return (preprocess_digit_photo,)


@app.cell(hide_code=True)
def _(mo):
    digit_photo_upload = mo.ui.file(
        filetypes=[".png", ".jpg", ".jpeg"], kind="area", multiple=False
    )
    digit_photo_rotation = mo.ui.dropdown(
        options=["0", "90", "180", "270"], value="0", label="Drehung"
    )
    digit_photo_ink_percentile = mo.ui.slider(
        80, 98, value=92, step=1, label="Tintenempfindlichkeit"
    )
    return digit_photo_ink_percentile, digit_photo_rotation, digit_photo_upload


@app.cell
def _(
    digit_photo_ink_percentile,
    digit_photo_rotation,
    digit_photo_upload,
    modell,
    mo,
    plt,
    preprocess_digit_photo,
):
    if modell is None:
        _foto_ergebnis = mo.callout(
            mo.md("Trainiere zuerst das Modell in Aufgabe 1."), kind="neutral"
        )
    elif not digit_photo_upload.value:
        _foto_ergebnis = mo.callout(
            mo.md("Lade ein Bild mit einer dunklen Ziffer auf hellem Papier hoch."),
            kind="neutral",
        )
    else:
        _datei = digit_photo_upload.value[0]
        _bild_8x8 = preprocess_digit_photo(
            _datei.contents,
            rotation_degrees=int(digit_photo_rotation.value),
            ink_percentile=digit_photo_ink_percentile.value,
        )
        _vorhersage_foto = modell.predict([_bild_8x8.ravel()])[0]
        _wahrscheinlichkeiten = modell.predict_proba([_bild_8x8.ravel()])[0]
        _top = _wahrscheinlichkeiten.argsort()[::-1][:3]
        _top_text = ", ".join(
            f"{_klasse}: {_wahrscheinlichkeiten[_klasse]:.1%}" for _klasse in _top
        )
        _fig_foto, _ax_foto = plt.subplots(figsize=(3, 3))
        _ax_foto.imshow(_bild_8x8, cmap="gray_r", vmin=0, vmax=16)
        _ax_foto.set_title("Verarbeitetes Bild · 8 × 8 Pixel")
        _ax_foto.axis("off")
        _foto_ergebnis = mo.vstack(
            [
                mo.md(
                    f"**Datei:** `{_datei.name}`  \n"
                    f"**Vorhersage:** `{_vorhersage_foto}`  \n"
                    f"**Drei wahrscheinlichste Ziffern:** {_top_text}"
                ),
                _fig_foto,
            ],
            gap=1,
        )
    mo.vstack(
        [
            mo.hstack(
                [digit_photo_upload, digit_photo_rotation, digit_photo_ink_percentile],
                widths=[2, 1, 1],
                gap=1,
            ),
            _foto_ergebnis,
        ],
        gap=1,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Rückblick

    Wir haben Beispieldaten mit Labels geladen, Trainings- und Testdaten getrennt, eine Pipeline trainiert und Vorhersagen geprüft.

    Die Accuracy fasst die Zahl der richtigen Antworten zusammen. Confusion Matrix und Fehlbeispiele helfen, Verwechslungen zu erkennen.
    """)
    return


if __name__ == "__main__":
    app.run()
