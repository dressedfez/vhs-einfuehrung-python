# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.19.2",
#     "matplotlib==3.10.8",
#     "numpy==2.4.2",
#     "pillow==12.0.0",
#     "scikit-learn==1.8.0",
# ]
# ///

import marimo

__generated_with = "0.23.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _():
    import io

    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    from PIL import ImageOps

    from sklearn.datasets import load_digits
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import ConfusionMatrixDisplay
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import classification_report
    from sklearn.model_selection import train_test_split
    from sklearn.neural_network import MLPClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler

    return (
        ConfusionMatrixDisplay,
        Image,
        ImageOps,
        LogisticRegression,
        MLPClassifier,
        Pipeline,
        StandardScaler,
        accuracy_score,
        classification_report,
        io,
        load_digits,
        np,
        plt,
        train_test_split,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Kurstag 6: Maschinelles Lernen mit Scikit-Learn
    ## Ziffernerkennung als vollständiges Machine-Learning-Projekt

    In diesem Notebook bauen wir ein erstes Machine-Learning-Projekt vollständig durch:

    1. Daten laden und verstehen
    2. Trainings- und Testdaten trennen
    3. Modell auswählen und trainieren
    4. Modell bewerten
    5. Fehler untersuchen

    Die Theorie eignet sich gut für die Keynote-Folien. Das Notebook konzentriert sich auf die praktische Umsetzung.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Was ist maschinelles Lernen?

    Bei klassischer Programmierung formulieren wir Regeln direkt:

    ```text
    Daten + Regeln -> Ergebnis
    ```

    Beim maschinellen Lernen drehen wir die Idee um:

    ```text
    Daten + bekannte Ergebnisse -> gelernte Regeln / Modell
    ```

    Das trainierte Modell kann anschließend für neue Daten eine Vorhersage machen.

    In unserem Beispiel:

    - **Daten:** kleine Bilder von handgeschriebenen Ziffern
    - **Label:** die richtige Ziffer `0` bis `9`
    - **Modell:** ein Klassifikationsmodell aus Scikit-Learn
    - **Vorhersage:** welche Ziffer auf einem neuen Bild zu sehen ist
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Scikit-Learn im Überblick

    Scikit-Learn nutzt ein sehr einheitliches Muster:

    - `fit(X, y)`: Modell mit Trainingsdaten lernen lassen
    - `predict(X)`: Vorhersagen für neue Daten berechnen
    - `score(X, y)`: Modell auf bekannten Beispielen bewerten

    Dabei ist:

    - `X` die Merkmalsmatrix mit den Eingabedaten
    - `y` der Zielvektor mit den richtigen Antworten

    Für saubere Projekte nutzen wir häufig eine `Pipeline`, die mehrere Schritte verbindet, z.B. Skalierung der Daten und Modelltraining.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Datenbasis: `load_digits`

    Für die Ziffernerkennung nutzen wir den eingebauten Scikit-Learn-Datensatz `load_digits`.

    Vorteile für den Kurs:

    - kein Download nötig
    - reproduzierbar
    - klein genug für schnelle Experimente
    - anschaulich, weil jedes Beispiel ein kleines Bild ist

    Jedes Bild besteht aus `8 x 8` Pixeln. Für Scikit-Learn wird dieses Bild zusätzlich als Vektor mit `64` Merkmalen gespeichert.
    """)
    return


@app.cell
def _(load_digits):
    digits = load_digits()
    X_digits = digits.data
    y_digits = digits.target
    digit_images = digits.images
    digit_names = digits.target_names
    return X_digits, digit_images, digit_names, y_digits


@app.cell(hide_code=True)
def _(X_digits, digit_images, digit_names, mo):
    mo.md(f"""
    **Datensatz-Überblick**

    - Anzahl Beispiele: `{X_digits.shape[0]}`
    - Anzahl Merkmale pro Beispiel: `{X_digits.shape[1]}`
    - Bildgröße: `{digit_images.shape[1]} x {digit_images.shape[2]}`
    - Klassen: `{list(digit_names)}`
    """)
    return


@app.cell
def _(digit_images, plt, y_digits):
    fig_digits, axes_digits = plt.subplots(2, 5, figsize=(8, 4))
    for image, label, digit_axis in zip(
        digit_images[:10], y_digits[:10], axes_digits.flat
    ):
        digit_axis.imshow(image, cmap="gray_r")
        digit_axis.set_title(f"Label: {label}")
        digit_axis.axis("off")

    fig_digits.suptitle("Beispiele aus dem Digits-Datensatz")
    fig_digits.tight_layout()
    fig_digits
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Features und Labels

    Ein einzelnes Bild ist für Menschen leicht als Bild erkennbar. Das Modell erhält aber keine Bilddatei, sondern Zahlen:

    - jedes Pixel wird zu einem Merkmal
    - jedes Beispiel hat `64` Merkmale
    - das Label ist die richtige Ziffer

    Damit wird aus dem Bildproblem ein Tabellenproblem: Jede Zeile ist ein Bild, jede Spalte ist ein Pixel.
    """)
    return


@app.cell
def _(X_digits, y_digits):
    beispiel_index = 0
    beispiel_features = X_digits[beispiel_index]
    beispiel_label = y_digits[beispiel_index]

    beispiel_features.reshape(8, 8), beispiel_label
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Trainings- und Testdaten

    Wir trainieren das Modell nicht auf allen Daten. Ein Teil wird zurückgelegt und erst am Ende für die Bewertung genutzt.

    Das schützt uns vor einer typischen Falle:

    > Ein Modell kann auf bekannten Daten gut aussehen, aber bei neuen Daten schlecht funktionieren.

    Deshalb nutzen wir:

    - **Trainingsdaten:** zum Lernen
    - **Testdaten:** zur ehrlichen Bewertung

    `stratify=y` sorgt dafür, dass alle Ziffern in Training und Test ungefähr gleich verteilt bleiben.
    """)
    return


@app.cell
def _(X_digits, train_test_split, y_digits):
    test_size = 0.2
    random_state = 42

    X_train, X_test, y_train, y_test = train_test_split(
        X_digits,
        y_digits,
        test_size=test_size,
        random_state=random_state,
        stratify=y_digits,
    )
    return X_test, X_train, random_state, test_size, y_test, y_train


@app.cell(hide_code=True)
def _(X_test, X_train, mo, test_size):
    mo.md(f"""
    **Train/Test-Split**

    - Testgröße: `{test_size:.0%}`
    - Trainingsbeispiele: `{X_train.shape[0]}`
    - Testbeispiele: `{X_test.shape[0]}`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Übung
    Ändere `test_size` von `0.2` auf `0.3`.

    Beobachte:

    1. Wie viele Trainings- und Testbeispiele gibt es danach?
    2. Ändert sich die spätere Modellbewertung?
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Was passiert beim Lernen?

    Bevor wir unser Hauptmodell trainieren, schauen wir uns eine Verlustkurve an.

    Die Idee:

    - Zu Beginn macht das Modell viele Fehler.
    - Während des Trainings wird der Verlust kleiner.
    - Eine fallende Verlustkurve zeigt, dass das Modell aus den Trainingsdaten lernt.

    Für diesen Einschub nutzen wir kurz ein kleines neuronales Netz mit `MLPClassifier`, weil Scikit-Learn dort direkt eine `loss_curve_` bereitstellt.
    """)
    return


@app.cell
def _(MLPClassifier, Pipeline, StandardScaler, random_state):
    loss_curve_model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                MLPClassifier(
                    hidden_layer_sizes=(32,),
                    max_iter=120,
                    early_stopping=True,
                    random_state=random_state,
                ),
            ),
        ]
    )
    return (loss_curve_model,)


@app.cell
def _(X_train, loss_curve_model, y_train):
    loss_curve_model.fit(X_train, y_train)
    mlp_classifier = loss_curve_model.named_steps["classifier"]
    training_loss_curve = mlp_classifier.loss_curve_
    validation_scores = mlp_classifier.validation_scores_
    return training_loss_curve, validation_scores


@app.cell
def _(plt, training_loss_curve, validation_scores):
    fig_loss, ax_loss = plt.subplots(figsize=(7, 4))
    ax_loss.plot(training_loss_curve, label="Trainingsverlust", color="tab:blue")
    ax_loss.set_xlabel("Iteration")
    ax_loss.set_ylabel("Loss")
    ax_loss.set_title("Verlustkurve während des Trainings")

    ax_validation = ax_loss.twinx()
    ax_validation.plot(
        validation_scores,
        label="Validierungs-Accuracy",
        color="tab:orange",
    )
    ax_validation.set_ylabel("Accuracy")

    handles_loss, labels_loss = ax_loss.get_legend_handles_labels()
    handles_validation, labels_validation = ax_validation.get_legend_handles_labels()
    ax_loss.legend(
        handles_loss + handles_validation,
        labels_loss + labels_validation,
        loc="center right",
    )
    fig_loss.tight_layout()
    fig_loss
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Interpretation**

    - Sinkt der Trainingsverlust, lernt das Modell aus den Daten.
    - Die Validierungsgenauigkeit zeigt, ob das Gelernte auch auf unbekanntere Daten wirkt.
    - Eine Verlustkurve ist hilfreich, um den Trainingsprozess sichtbar zu machen.

    Für unser Hauptprojekt bleiben wir trotzdem bei `LogisticRegression`, weil dieses Modell für den Einstieg leichter zu erklären ist.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Modelltraining

    Wir verwenden als erstes Modell eine logistische Regression.

    Trotz des Namens wird sie hier für **Klassifikation** genutzt, also für die Auswahl einer Klasse `0` bis `9`.

    Die Pipeline enthält zwei Schritte:

    1. `StandardScaler`: bringt die Merkmale auf eine vergleichbare Skala
    2. `LogisticRegression`: lernt das Klassifikationsmodell
    """)
    return


@app.cell
def _(LogisticRegression, Pipeline, StandardScaler, random_state):
    digit_model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                LogisticRegression(max_iter=2_000, random_state=random_state),
            ),
        ]
    )

    digit_model
    return (digit_model,)


@app.cell
def _(X_test, X_train, digit_model, y_test, y_train):
    digit_model.fit(X_train, y_train)
    y_pred = digit_model.predict(X_test)
    train_score = digit_model.score(X_train, y_train)
    test_score = digit_model.score(X_test, y_test)

    train_score, test_score
    return test_score, train_score, y_pred


@app.cell(hide_code=True)
def _(mo, test_score, train_score):
    mo.md(f"""
    **Ergebnis**

    - Genauigkeit auf Trainingsdaten: `{train_score:.3f}`
    - Genauigkeit auf Testdaten: `{test_score:.3f}`

    Die Testgenauigkeit ist wichtiger, weil sie auf Daten gemessen wird, die das Modell beim Training nicht gesehen hat.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Modellbewertung

    Die Accuracy gibt an, welcher Anteil der Testbeispiele richtig klassifiziert wurde.

    Sie ist ein guter erster Wert, aber sie sagt nicht, **welche** Ziffern verwechselt werden.

    Dafür verwenden wir eine Confusion Matrix.
    """)
    return


@app.cell
def _(accuracy_score, y_pred, y_test):
    accuracy = accuracy_score(y_test, y_pred)
    accuracy
    return


@app.cell
def _(ConfusionMatrixDisplay, X_test, digit_model, plt, y_test):
    fig_confusion, ax_confusion = plt.subplots(figsize=(7, 7))
    ConfusionMatrixDisplay.from_estimator(
        digit_model,
        X_test,
        y_test,
        ax=ax_confusion,
        cmap="Blues",
        colorbar=False,
    )
    ax_confusion.set_title("Confusion Matrix")
    fig_confusion
    return


@app.cell
def _(classification_report, y_pred, y_test):
    report_text = classification_report(y_test, y_pred)
    print(report_text)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note | Übung
    Betrachte die Confusion Matrix:

    1. Welche Ziffern werden häufig richtig erkannt?
    2. Welche Ziffern werden verwechselt?
    3. Warum könnten diese Verwechslungen entstehen?
    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Falsch klassifizierte Beispiele

    Eine Metrik zeigt uns eine Zahl. Für das Lernen ist es oft hilfreicher, konkrete Fehler anzuschauen.

    Die nächste Zelle zeigt einige falsch erkannte Ziffern.
    """)
    return


@app.cell
def _(np, y_pred, y_test):
    wrong_indices = np.flatnonzero(y_pred != y_test)
    wrong_indices[:10]
    return (wrong_indices,)


@app.cell
def _(X_test, plt, wrong_indices, y_pred, y_test):
    if len(wrong_indices) == 0:
        print("Keine falsch klassifizierten Beispiele im Testdatensatz gefunden.")
        wrong_examples_output = None
    else:
        n_examples = min(10, len(wrong_indices))
        fig_wrong, axes_wrong = plt.subplots(2, 5, figsize=(9, 4))
        for wrong_axis in axes_wrong.flat:
            wrong_axis.axis("off")

        for wrong_plot_axis, index in zip(
            axes_wrong.flat, wrong_indices[:n_examples]
        ):
            wrong_plot_axis.imshow(X_test[index].reshape(8, 8), cmap="gray_r")
            wrong_plot_axis.set_title(
                f"wahr: {y_test[index]}, vorher: {y_pred[index]}"
            )
            wrong_plot_axis.axis("off")

        fig_wrong.suptitle("Falsch klassifizierte Beispiele")
        fig_wrong.tight_layout()
        wrong_examples_output = fig_wrong
    wrong_examples_output
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Eigenes Foto ausprobieren

    Jetzt testen wir die Idee mit einem eigenen Foto.

    Vorgehen:

    1. Schreibe eine einzelne Ziffer möglichst groß und dunkel auf helles Papier.
    2. Fotografiere die Ziffer mit der Kamera-App deines Laptops oder Smartphones.
    3. Lade das Bild hier hoch.
    4. Das Notebook sucht die dunkelste zusammenhängende Struktur im Bild.
    5. Diese Struktur wird auf ein `8 x 8`-Bild gebracht.
    6. Das trainierte Modell sagt eine Ziffer vorher.

    Das ist bewusst nur eine einfache Vorverarbeitung. Bei echten Bildprojekten ist dieser Schritt oft ein eigener wichtiger Projektteil.

    /// attention | Wichtig
    Das Modell wurde auf **aufrechten** Ziffern trainiert. Ein liegendes `8` oder ein Unendlichkeitszeichen ist für das Modell ein anderes Bild.
    ///
    """)
    return


@app.cell
def _(mo):
    digit_photo_upload = mo.ui.file(
        filetypes=[".png", ".jpg", ".jpeg"], kind="area", multiple=False
    )
    digit_photo_upload
    return (digit_photo_upload,)


@app.cell(hide_code=True)
def _(mo):
    digit_photo_rotation = mo.ui.dropdown(
        options=["0", "90", "180", "270"], value="0", label="Rotation in Grad"
    )
    digit_photo_ink_percentile = mo.ui.slider(
        80, 98, value=92, step=1, label="Tinten-Empfindlichkeit"
    )
    mo.vstack([digit_photo_rotation, digit_photo_ink_percentile])
    return digit_photo_ink_percentile, digit_photo_rotation


@app.cell(hide_code=True)
def _(
    digit_model,
    digit_photo_ink_percentile,
    digit_photo_rotation,
    digit_photo_upload,
    mo,
    preprocess_digit_photo,
):
    if not digit_photo_upload.value:
        photo_prediction_output = mo.md("Noch kein Foto hochgeladen.")
    else:
        uploaded_photo = digit_photo_upload.value[0]
        processed_photo = preprocess_digit_photo(
            uploaded_photo.contents,
            rotation_degrees=int(digit_photo_rotation.value),
            ink_percentile=digit_photo_ink_percentile.value,
        )
        photo_prediction = digit_model.predict([processed_photo.ravel()])[0]
        active_pixel_ratio = (processed_photo > 2).mean()
        class_probabilities = digit_model.predict_proba([processed_photo.ravel()])[
            0
        ]
        top_classes = class_probabilities.argsort()[::-1][:3]
        top_class_text = ", ".join(
            f"{class_index}: {class_probabilities[class_index]:.1%}"
            for class_index in top_classes
        )
        photo_prediction_output = mo.md(
            f"""
            **Hochgeladene Datei:** `{uploaded_photo.name}`

            **Vorhersage des Modells:** `{photo_prediction}`

            **Aktive Pixel im `8 x 8`-Bild:** `{active_pixel_ratio:.1%}`

            **Top-3-Wahrscheinlichkeiten:** {top_class_text}

            **Hinweis:** Wenn das `8 x 8`-Bild fast komplett schwarz ist, wurde zu viel Hintergrund erkannt. Erhöhe dann die Tinten-Empfindlichkeit oder fotografiere die Ziffer auf unliniertem Papier. Wenn die Ziffer liegt, probiere eine andere Rotation.
            """
        )
    photo_prediction_output
    return


@app.cell(hide_code=True)
def _(
    digit_photo_ink_percentile,
    digit_photo_rotation,
    digit_photo_upload,
    plt,
    preprocess_digit_photo,
):
    if digit_photo_upload.value:
        uploaded_photo_for_plot = digit_photo_upload.value[0]
        processed_photo_for_plot = preprocess_digit_photo(
            uploaded_photo_for_plot.contents,
            rotation_degrees=int(digit_photo_rotation.value),
            ink_percentile=digit_photo_ink_percentile.value,
        )

        fig_photo, photo_axis = plt.subplots(figsize=(3, 3))
        photo_axis.imshow(processed_photo_for_plot, cmap="gray_r", vmin=0, vmax=16)
        photo_axis.set_title("Vorverarbeitetes Foto (8 x 8)")
        photo_axis.axis("off")
        photo_preview_output = fig_photo
    else:
        photo_preview_output = None
    photo_preview_output
    return


@app.cell(hide_code=True)
def _(Image, ImageOps, io, np):
    def _dilate_mask(mask, steps=2):
        dilated_mask = mask
        for _ in range(steps):
            padded_mask = np.pad(
                dilated_mask, 1, mode="constant", constant_values=False
            )
            dilated_mask = (
                padded_mask[:-2, :-2]
                | padded_mask[:-2, 1:-1]
                | padded_mask[:-2, 2:]
                | padded_mask[1:-1, :-2]
                | padded_mask[1:-1, 1:-1]
                | padded_mask[1:-1, 2:]
                | padded_mask[2:, :-2]
                | padded_mask[2:, 1:-1]
                | padded_mask[2:, 2:]
            )
        return dilated_mask


    def _largest_component_mask(mask):
        visited = np.zeros(mask.shape, dtype=bool)
        best_component = []
        rows, columns = mask.shape

        for start_row, start_column in np.argwhere(mask):
            if visited[start_row, start_column]:
                continue

            stack = [(start_row, start_column)]
            visited[start_row, start_column] = True
            component = []

            while stack:
                row, column = stack.pop()
                component.append((row, column))

                for next_row, next_column in (
                    (row - 1, column),
                    (row + 1, column),
                    (row, column - 1),
                    (row, column + 1),
                ):
                    if (
                        0 <= next_row < rows
                        and 0 <= next_column < columns
                        and mask[next_row, next_column]
                        and not visited[next_row, next_column]
                    ):
                        visited[next_row, next_column] = True
                        stack.append((next_row, next_column))

            if len(component) > len(best_component):
                best_component = component

        component_mask = np.zeros(mask.shape, dtype=bool)
        if best_component:
            component_rows, component_columns = zip(*best_component)
            component_mask[component_rows, component_columns] = True
        return component_mask


    def preprocess_digit_photo(
        photo_bytes,
        rotation_degrees=0,
        ink_percentile=92,
        crop_padding=12,
        target_ink_size=6,
    ):
        photo_image = Image.open(io.BytesIO(photo_bytes)).convert("L")
        if rotation_degrees:
            photo_image = photo_image.rotate(rotation_degrees, expand=True)
        photo_image = ImageOps.autocontrast(photo_image)

        photo_array = np.asarray(photo_image)
        ink_strength = 255.0 - photo_array.astype(float)
        # Ignore very light structures such as paper lines and mild shadows before
        # selecting the darkest pixels by percentile.
        ink_strength[ink_strength < 35] = 0
        ink_threshold = np.percentile(ink_strength, ink_percentile)
        ink_mask = (ink_strength >= ink_threshold) & (ink_strength > 0)
        ink_mask = _largest_component_mask(ink_mask)
        ink_mask = _dilate_mask(ink_mask, steps=1)

        if ink_mask.any():
            row_positions, column_positions = np.where(ink_mask)
            top = max(row_positions.min() - crop_padding, 0)
            bottom = min(
                row_positions.max() + crop_padding + 1, photo_array.shape[0]
            )
            left = max(column_positions.min() - crop_padding, 0)
            right = min(
                column_positions.max() + crop_padding + 1, photo_array.shape[1]
            )
            ink_strength = ink_strength[top:bottom, left:right]
            ink_mask = ink_mask[top:bottom, left:right]

        cleaned_digit = np.where(ink_mask, ink_strength, 0.0)
        if cleaned_digit.max() == 0:
            return np.zeros((8, 8), dtype=float)

        cleaned_digit = np.clip(
            cleaned_digit / cleaned_digit.max() * 255.0, 0, 255
        )
        cleaned_image = Image.fromarray(cleaned_digit.astype("uint8"))

        width, height = cleaned_image.size
        if width == 0 or height == 0:
            return np.zeros((8, 8), dtype=float)

        scale = target_ink_size / max(width, height)
        resized_width = max(1, min(8, round(width * scale)))
        resized_height = max(1, min(8, round(height * scale)))
        resized_image = cleaned_image.resize(
            (resized_width, resized_height), Image.Resampling.LANCZOS
        )

        square_size = 8
        square_image = Image.new("L", (square_size, square_size), color=0)
        square_image.paste(
            resized_image,
            (
                (square_size - resized_width) // 2,
                (square_size - resized_height) // 2,
            ),
        )

        digit_array = np.asarray(square_image, dtype=float)
        digit_array = digit_array / 255.0 * 16.0
        return digit_array

    return (preprocess_digit_photo,)


if __name__ == "__main__":
    app.run()
