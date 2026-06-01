# Machine-Learning Modeling of Flue Gas Desulfurization — SO₂ Outlet-Concentration Prediction

Supplementary **code, dataset, and reviewer response** for the *Scientific Reports* article:

> **Modeling based on machine learning to investigate flue gas desulfurization
> performance by calcium silicate absorbent in a sand bed reactor**
> DOI: [10.1038/s41598-024-51586-7](https://doi.org/10.1038/s41598-024-51586-7)

The study evaluates several machine-learning models — **ANN, MLP, RBFNN, Random
Forest (RF), ETR, and SVR** — for predicting the **outlet SO₂ concentration** of
a sand-bed flue gas desulfurization (FGD) reactor packed with a calcium-silicate
absorbent. This repository provides the **Random Forest** implementation,
together with the dataset and the point-by-point reviewer response.

---

## ⚠️ What the model actually predicts

The target variable is the **SO₂ concentration (ppm) at the *outlet* of the
reactor**, as measured continuously by the downstream SO₂ gas analyzer. It is
**not** adsorption capacity or removal efficiency. The modeled behaviour is:

- **Start:** fresh absorbent removes SO₂ → outlet concentration *decreases*.
- **Over time:** the absorbent saturates → outlet concentration *rises* toward
  the inlet value.
- **≈ 20 min:** absorbent saturated → outlet concentration *plateaus* near the
  baseline inlet level.

> Any reading of the figures as adsorption efficiency or material regeneration is
> a misinterpretation of this measured outlet-concentration signal.

---

## 📁 Repository contents

| File | Description |
|------|-------------|
| [`RF.py`](RF.py) | Main script: the full Random Forest regression pipeline. |
| [`RF_code.pdf`](RF_code.pdf) | **Typeset, ready-to-read version of the code** (article-standard, line-numbered, syntax-highlighted). *Start here for a quick review.* |
| [`RF_code.tex`](RF_code.tex) | LaTeX source for `RF_code.pdf` (recompiles with plain `pdflatex`). |
| [`41598_2024_51586_MOESM1_ESM.xlsx`](41598_2024_51586_MOESM1_ESM.xlsx) | Experimental dataset (Electronic Supplementary Material). |
| [`Naderi-ScientificReports-Response.docx`](Naderi-ScientificReports-Response.docx) | Point-by-point response to the reviewers. |

---

## 📊 Dataset

The dataset (`Sheet1`, **323 samples**) holds four input features and one target.
The values are outlet SO₂ concentrations over time, drawn from published
experimental measurements of calcium-silicate FGD (see Reference [1]).

| Column | Symbol | Unit | Role |
|--------|--------|------|------|
| Relative humidity | RH | % | feature |
| Absorbent weight | — | g | feature |
| Temperature | T | °C | feature |
| Time | t | min | feature |
| **SO₂ concentration (outlet)** | — | ppm | **target** |

---

## ⚙️ What the code does

`RF.py` implements the complete modelling workflow:

1. **Load** the experimental data from Excel.
2. **Normalise** features and target with `MinMaxScaler` (0–1 range).
3. **Split** the data 70 % / 20 % / 10 % into train / validation / test sets
   (`random_state=20` for reproducibility).
4. **Train** a tuned `RandomForestRegressor`
   (`n_estimators=9`, `max_depth=16`, `criterion='poisson'`).
5. **Evaluate** with MSE, RMSE, R², and MAE on the training and validation sets.
6. **Plot** a 5-fold cross-validated **learning curve** (RMSE vs. training size).

---

## ▶️ How to reproduce

**Requirements** (Python 3.8+):

```bash
pip install pandas numpy scikit-learn matplotlib openpyxl
```

**Run:**

```bash
python RF.py
```

> **⚠️ One small note on the data file.**
> `RF.py` expects the dataset to be named `data.xlsx`. The dataset in this
> repository keeps its official supplementary-material name. Before running,
> either copy or rename it:
>
> ```bash
> cp 41598_2024_51586_MOESM1_ESM.xlsx data.xlsx
> ```

Running the script prints the evaluation metrics to the console and opens the
learning-curve figure.

### Expected output (normalised scale, `random_state=20`)

| Metric | Training set | Validation set |
|--------|:------------:|:--------------:|
| RMSE   | 0.0525       | 0.085          |
| R²     | 0.988        | 0.967          |
| MAE    | 0.0395       | 0.064          |

The small train↔validation gap and the converging, flattening learning curve
indicate the Random Forest model **generalises well and is not overfitting**.

---

## 📄 Viewing / recompiling the code PDF

The typeset code is already provided as [`RF_code.pdf`](RF_code.pdf). To rebuild
it from source (keep `RF.py` in the same folder):

```bash
pdflatex RF_code.tex
```

No special packages or `-shell-escape` are required — it uses the standard
`listings` package, so it compiles with any TeX Live / MiKTeX installation.

---

## ✒️ Citation

If you use this code or data, please cite:

> Modeling based on machine learning to investigate flue gas desulfurization
> performance by calcium silicate absorbent in a sand bed reactor.
> *Scientific Reports* (2024). DOI: 10.1038/s41598-024-51586-7

**Reference**
[1] L. F. Arthur, *Silicate sorbents for flue gas cleaning*, The University of
Texas at Austin, 1998.

---

## 👤 Authors & contact

- **Dr. Ahad Ghaemi** (corresponding author) — Iran University of Science and
  Technology — <aghaemi@iust.ac.ir>
- **Mohammad Sadegh Kalami Yazdi** — <Kalami1378@yahoo.com>
