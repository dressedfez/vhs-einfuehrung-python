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
# ruff: noqa: B018, PLR1711, UP003

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", layout_file="layouts/kurstag_06_folien.slides.json")


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

    def beispiel(titel, erklaerung, code, ergebnis):
        return mo.vstack(
            [
                mo.md(
                    f"## {titel}\n\n{erklaerung}\n\n"
                    f"**Python-Code**\n\n```python\n{code}\n```"
                ),
                ergebnis,
            ],
            gap=1,
        )

    return (
        ConfusionMatrixDisplay,
        Image,
        ImageOps,
        LogisticRegression,
        Pipeline,
        StandardScaler,
        accuracy_score,
        beispiel,
        io,
        load_digits,
        mo,
        np,
        plt,
        train_test_split,
    )


@app.cell(hide_code=True)
def _(mo):
    from base64 import b64encode as _b64encode
    from pathlib import Path as _Path

    _logo_data = _b64encode(_Path("public/vhs-dresden-logo.png").read_bytes()).decode("ascii")
    _cover_html = """
    <style>
      .vhs-kursstart { box-sizing: border-box; min-height: 440px; padding: 2.2rem 2.5rem; overflow: hidden; position: relative; border: 1px solid #d7e3ef; border-left: 10px solid #082f5b; border-radius: 24px; background: radial-gradient(circle at 92% 8%, rgba(255,184,40,.22) 0 15%, transparent 15.5%), linear-gradient(125deg,#fbfdff 0%,#f0f5fb 58%,#e4eef7 100%); color: #102f51; font-family: system-ui,sans-serif; }
      .vhs-copy { position: relative; z-index: 1; max-width: calc(100% - 270px); }
      .vhs-logo { display: inline-block; margin-bottom: 1.4rem; padding: .5rem .8rem; border-radius: 12px; background: #fff; box-shadow: 0 6px 20px rgba(7,40,74,.08); }
      .vhs-logo img { display: block; width: min(290px,62vw); height: auto; }
      .vhs-series { margin: 0 0 .4rem; color: #147e9e; font-size: .86rem; font-weight: 800; letter-spacing: .16em; text-transform: uppercase; }
      .vhs-title { margin: 0; color: #082f5b; font-size: clamp(2.1rem,4.3vw,3.6rem); font-weight: 800; line-height: 1.05; }
      .vhs-title span { display: block; margin-top: .25rem; color: #17668e; font-size: .68em; }
      .vhs-summary { max-width: 39rem; margin: 1rem 0 1.25rem; color: #38526d; font-size: 1.08rem; line-height: 1.5; }
      .vhs-motto { display: inline-block; padding: .55rem .85rem; border: 1px solid #cfdeeb; border-radius: 999px; background: rgba(255,255,255,.78); color: #173a5d; font-size: .9rem; font-weight: 650; }
      .vhs-motto b { padding: 0 .35rem; color: #ed6a32; }
      .vhs-art { position: absolute; top: 50%; right: 4%; transform: translateY(-50%); display: grid; place-items: center; width: 220px; height: 220px; border: 1px solid rgba(8,47,91,.12); border-radius: 50%; background: rgba(255,255,255,.48); box-shadow: inset 0 0 0 15px rgba(255,255,255,.28); }
      .vhs-core { display: grid; place-items: center; width: 134px; height: 134px; border-radius: 50%; background: #082f5b; box-shadow: 0 16px 30px rgba(8,47,91,.2); color: white; font-size: 3rem; font-weight: 850; letter-spacing: -.08em; }
      .vhs-dot { position: absolute; display: block; width: 34px; height: 34px; border-radius: 50%; box-shadow: 0 4px 14px rgba(8,47,91,.12); }
      .vhs-dot.one { top: 10px; left: 91px; width: 29px; height: 29px; background: #f6b627; }
      .vhs-dot.two { top: 72px; right: 5px; background: #e84b3c; }
      .vhs-dot.three { right: 31px; bottom: 17px; width: 27px; height: 27px; background: #39a5d6; }
      .vhs-dot.four { bottom: 31px; left: 12px; width: 39px; height: 39px; background: #ef6d32; }
      .vhs-dot.five { top: 50px; left: 20px; width: 22px; height: 22px; background: #318fc0; }
      @media (max-width:680px) { .vhs-kursstart { min-height:390px; padding:1.5rem; } .vhs-copy { max-width:none; } .vhs-art { display:none; } }
    </style>
    <section class="vhs-kursstart">
      <div class="vhs-copy">
        <div class="vhs-logo"><img src="data:image/png;base64,__VHS_LOGO__" alt="Volkshochschule Dresden e.V."></div>
        <p class="vhs-series">Python für Daten und KI</p>
        <h1 class="vhs-title">Kurstag 6<span>Maschinelles Lernen</span></h1>
        <p class="vhs-summary">Wie ein Modell aus Beispielen lernt und Ziffern auf Bildern erkennt.</p>
        <div class="vhs-motto">Daten <b>·</b> Modell <b>·</b> Vorhersage</div>
      </div>
      <div class="vhs-art" aria-hidden="true"><div class="vhs-core">ML</div><i class="vhs-dot one"></i><i class="vhs-dot two"></i><i class="vhs-dot three"></i><i class="vhs-dot four"></i><i class="vhs-dot five"></i></div>
    </section>
    """
    mo.Html(_cover_html.replace("__VHS_LOGO__", _logo_data))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Unser Weg heute

    1. **Beispiele verstehen:** Bilder als Zahlen und Labels darstellen.
    2. **Daten vorbereiten:** Trainings- und Testdaten trennen.
    3. **Modell trainieren:** Scikit-Learn mit `fit` und `predict` verwenden.
    4. **Ergebnisse prüfen:** Accuracy, Confusion Matrix und Fehlbeispiele lesen.
    5. **Ausprobieren:** Das Modell mit einem eigenen Ziffernfoto testen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Regeln oder Beispiele

    Bei einer regelbasierten Lösung schreiben wir die Regeln selbst. Das funktioniert gut, wenn sich ein Problem klar beschreiben lässt.

    Bei handgeschriebenen Ziffern sehen dieselben Zahlen sehr unterschiedlich aus. Statt jede mögliche Form als Regel aufzuschreiben, zeigen wir dem Modell viele Beispiele mit den richtigen Antworten.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Überwachtes Lernen

    Beim überwachten Lernen kennen wir für jedes Trainingsbeispiel die richtige Antwort.

    - **Eingabe `X`:** die Merkmale, zum Beispiel die Helligkeit der Bildpunkte.
    - **Ziel `y`:** die richtige Ziffer.
    - **Modell:** lernt eine Zuordnung von den Merkmalen zur Ziffer.

    Nach dem Training kann das Modell für ein neues Bild eine Vorhersage berechnen.
    """)
    return


@app.cell
def _(beispiel, load_digits, mo):
    digits = load_digits()
    X_digits = digits.data
    y_digits = digits.target
    digit_images = digits.images
    digit_names = digits.target_names
    _ueberblick = mo.vstack(
        [
            mo.md(
                f"**{X_digits.shape[0]:,} Bilder** · "
                f"**{X_digits.shape[1]} Pixelmerkmale pro Bild** · "
                f"**Ziffern:** {list(digit_names)}"
            ),
            mo.md("Der Beispieldatensatz ist in Scikit-Learn enthalten. Ein Download ist nicht nötig."),
        ],
        gap=1,
    )
    beispiel(
        "Der Digits-Datensatz",
        "Scikit-Learn enthält kleine Bilder handgeschriebener Ziffern samt richtiger Beschriftung.",
        'digits = load_digits()\nX = digits.data\ny = digits.target',
        _ueberblick,
    )
    return X_digits, digit_images, digit_names, digits, y_digits


@app.cell
def _(beispiel, digit_images, plt, y_digits):
    _fig_bilder, _achsen_bilder = plt.subplots(2, 5, figsize=(8, 3.7))
    for _bild, _label, _ax in zip(
        digit_images[:10], y_digits[:10], _achsen_bilder.flat
    ):
        _ax.imshow(_bild, cmap="gray_r", vmin=0, vmax=16)
        _ax.set_title(f"Ziffer {_label}")
        _ax.axis("off")
    _fig_bilder.tight_layout()
    beispiel(
        "Bilder und richtige Antworten",
        "Jedes Bild hat ein Label. Diese Paare bilden die Beispiele, aus denen ein überwachtes Modell lernt.",
        'digits = load_digits()\nfor bild, label in zip(digits.images[:10], digits.target[:10]):\n    ax.imshow(bild, cmap="gray_r")',
        _fig_bilder,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Pixel werden zu Merkmalen

    Ein Bild besteht aus `8 × 8` Pixeln. Jeder Pixelwert ist ein Merkmal. Das Modell erhält eine Zeile mit 64 Zahlen und als Ziel die richtige Ziffer.

    ```text
    Bild (8 × 8) → 64 Pixelwerte → Label 0 bis 9
    ```

    Das Modell verarbeitet also Zahlen. Es sieht nicht dasselbe Bild wie ein Mensch.
    """)
    return


@app.cell
def _(X_digits, beispiel, y_digits):
    _index_beispiel = 0
    _werte_beispiel = X_digits[_index_beispiel].reshape(8, 8)
    beispiel(
        "Ein Bild als Zahlenmatrix",
        f"Das ausgewählte Bild gehört zur Ziffer **{y_digits[_index_beispiel]}**. Jeder Eintrag liegt zwischen 0 und 16.",
        'bild = digits.images[0]\nmerkmale = bild.reshape(64)\nlabel = digits.target[0]',
        _werte_beispiel,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Trainingsdaten und Testdaten

    Wir halten einen Teil der Beispiele zurück. Das Modell sieht diese Testdaten beim Training nicht.

    - **Trainingsdaten:** zum Anpassen des Modells.
    - **Testdaten:** zum Prüfen an unbekannten Beispielen.

    `stratify=y` verteilt die Ziffern ähnlich auf beide Gruppen. `random_state` macht die Aufteilung reproduzierbar.
    """)
    return


@app.cell
def _(X_digits, beispiel, mo, train_test_split, y_digits):
    test_size = 0.2
    random_state = 42
    X_train, X_test, y_train, y_test = train_test_split(
        X_digits,
        y_digits,
        test_size=test_size,
        random_state=random_state,
        stratify=y_digits,
    )
    _aufteilung = mo.md(
        f"**Training:** {len(X_train):,} Bilder  \n"
        f"**Test:** {len(X_test):,} Bilder  \n"
        f"**Testanteil:** {test_size:.0%}"
    )
    beispiel(
        "Daten aufteilen",
        "Wir teilen die Daten vor dem Training. So können wir das fertige Modell fair an zurückgelegten Beispielen prüfen.",
        'X_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=42, stratify=y\n)',
        _aufteilung,
    )
    return X_test, X_train, random_state, test_size, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Drei zentrale Methoden

    - `fit(X_train, y_train)` lernt aus den Trainingsbeispielen.
    - `predict(X_test)` sagt Labels für neue Beispiele voraus.
    - `score(X_test, y_test)` vergleicht Vorhersagen mit den bekannten Antworten.

    Scikit-Learn verwendet bei vielen Modellen dasselbe Muster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Eine Pipeline für Vorverarbeitung und Modell

    Eine Pipeline verbindet mehrere Schritte. Hier skaliert `StandardScaler` die Pixelwerte. Danach klassifiziert `LogisticRegression` das Bild.

    Die Vorverarbeitung wird nur an den Trainingsdaten angepasst. Beim Testen wendet die Pipeline dieselbe Skalierung an. Dadurch gelangen Informationen aus dem Testdatensatz nicht ins Training.
    """)
    return


@app.cell
def _(LogisticRegression, Pipeline, StandardScaler, beispiel, mo, random_state):
    digit_model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                LogisticRegression(max_iter=2_000, random_state=random_state),
            ),
        ]
    )
    beispiel(
        "Das Modell zusammensetzen",
        "`LogisticRegression` wird hier als Klassifikationsmodell für die Ziffernklassen genutzt.",
        'digit_model = Pipeline([\n    ("scaler", StandardScaler()),\n    ("classifier", LogisticRegression(max_iter=2000))\n])',
        mo.md("**Pipeline:** `StandardScaler` gefolgt von `LogisticRegression`"),
    )
    return (digit_model,)


@app.cell
def _(X_test, X_train, digit_model, beispiel, mo, y_test, y_train):
    digit_model.fit(X_train, y_train)
    y_pred = digit_model.predict(X_test)
    train_score = digit_model.score(X_train, y_train)
    test_score = digit_model.score(X_test, y_test)
    _scores = mo.md(
        f"**Training:** {train_score:.1%} richtig  \n"
        f"**Test:** {test_score:.1%} richtig"
    )
    beispiel(
        "Trainieren und vorhersagen",
        "`fit` passt die Pipeline an Trainingsdaten an. `predict` klassifiziert anschließend die zurückgelegten Testbilder.",
        "digit_model.fit(X_train, y_train)\ny_pred = digit_model.predict(X_test)\ntrain_score = digit_model.score(X_train, y_train)\ntest_score = digit_model.score(X_test, y_test)",
        _scores,
    )
    return test_score, train_score, y_pred


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Accuracy und Confusion Matrix

    Die Accuracy ist der Anteil der richtig vorhergesagten Testbilder. Sie gibt einen schnellen Überblick, aber zeigt nicht, welche Ziffern das Modell verwechselt.

    In der Confusion Matrix stehen die richtigen Labels in den Zeilen und Vorhersagen in den Spalten. Werte auf der Diagonale sind richtige Vorhersagen.
    """)
    return


@app.cell
def _(ConfusionMatrixDisplay, X_test, accuracy_score, beispiel, mo, plt, y_pred, y_test):
    accuracy = accuracy_score(y_test, y_pred)
    _fig_matrix, _ax_matrix = plt.subplots(figsize=(6.4, 5.4), layout="constrained")
    ConfusionMatrixDisplay.from_predictions(
        y_test, y_pred, ax=_ax_matrix, cmap="Blues", colorbar=False
    )
    _ax_matrix.set_title(f"Confusion Matrix · Accuracy {accuracy:.1%}")
    beispiel(
        "Ergebnisse genauer lesen",
        "Dunkle Zellen auf der Diagonale stehen für viele richtige Vorhersagen. Zellen daneben zeigen Verwechslungen.",
        "accuracy_score(y_test, y_pred)\nConfusionMatrixDisplay.from_predictions(y_test, y_pred)",
        _fig_matrix,
    )
    return (accuracy,)


@app.cell
def _(X_test, beispiel, np, plt, y_pred, y_test):
    _falsch = np.flatnonzero(y_pred != y_test)
    _anzahl = min(10, len(_falsch))
    _fig_fehler, _achsen_fehler = plt.subplots(2, 5, figsize=(8, 3.8))
    for _ax in _achsen_fehler.flat:
        _ax.axis("off")
    for _ax, _index in zip(_achsen_fehler.flat, _falsch[:_anzahl]):
        _ax.imshow(X_test[_index].reshape(8, 8), cmap="gray_r", vmin=0, vmax=16)
        _ax.set_title(f"wahr {y_test[_index]} · Modell {y_pred[_index]}")
        _ax.axis("off")
    _fig_fehler.tight_layout()
    beispiel(
        "Fehler genauer ansehen",
        "Eine Kennzahl fasst viele Fälle zusammen. Hier untersuchen wir einzelne falsch klassifizierte Testbilder.",
        'falsch = np.flatnonzero(y_pred != y_test)\nfor index in falsch[:10]:\n    ax.imshow(X_test[index].reshape(8, 8))',
        _fig_fehler,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Grenzen des Beispiels

    Das Modell ordnet Pixelmuster den Ziffern zu. Es erklärt nicht, warum eine Person eine Ziffer so geschrieben hat.

    Trainings- und Testbilder stammen aus derselben Sammlung. Alltagsfotos können anders aussehen: anderer Stift, Hintergrund oder eine gedrehte Ziffer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Eigenes Ziffernfoto ausprobieren

    Das Modell erwartet ein aufrechtes `8 × 8`-Bild. Ein Foto wird daher zugeschnitten, in Graustufen umgewandelt und in 64 Pixelwerte übersetzt.

    Lade möglichst eine einzelne dunkle Ziffer auf hellem Papier hoch. Auswahlfelder und Ergebnis erscheinen gemeinsam auf dieser Folie.
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
    Image,
    digit_model,
    digit_photo_ink_percentile,
    digit_photo_rotation,
    digit_photo_upload,
    mo,
    plt,
    preprocess_digit_photo,
):
    if not digit_photo_upload.value:
        _ergebnis_foto = mo.callout(
            mo.md("Lade ein Bild mit einer dunklen Ziffer auf hellem Papier hoch."),
            kind="neutral",
        )
    else:
        _datei = digit_photo_upload.value[0]
        _verarbeitet = preprocess_digit_photo(
            _datei.contents,
            rotation_degrees=int(digit_photo_rotation.value),
            ink_percentile=digit_photo_ink_percentile.value,
        )
        _vorhersage = digit_model.predict([_verarbeitet.ravel()])[0]
        _wahrscheinlichkeiten = digit_model.predict_proba([_verarbeitet.ravel()])[0]
        _top = _wahrscheinlichkeiten.argsort()[::-1][:3]
        _top_text = ", ".join(
            f"{_klasse}: {_wahrscheinlichkeiten[_klasse]:.1%}" for _klasse in _top
        )
        _fig_foto, _ax_foto = plt.subplots(figsize=(3, 3))
        _ax_foto.imshow(_verarbeitet, cmap="gray_r", vmin=0, vmax=16)
        _ax_foto.set_title("Verarbeitetes Bild · 8 × 8 Pixel")
        _ax_foto.axis("off")
        _ergebnis_foto = mo.vstack(
            [
                mo.md(
                    f"**Datei:** `{_datei.name}`  \n"
                    f"**Vorhersage:** `{_vorhersage}`  \n"
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
            _ergebnis_foto,
        ],
        gap=1,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Das Wichtigste

    - Beim überwachten Lernen gehören zu jedem Beispiel Merkmale `X` und das bekannte Ziel `y`.
    - Trainingsdaten passen das Modell an. Testdaten prüfen es an unbekannten Beispielen.
    - Scikit-Learn verbindet Vorverarbeitung und Modell in einer Pipeline.
    - Accuracy, Confusion Matrix und einzelne Fehler zeigen unterschiedliche Aspekte der Modellqualität.
    """)
    return


if __name__ == "__main__":
    app.run()
