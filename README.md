# Supplementary Code & Data — Random Forest Model for SO₂ Concentration Prediction

This repository contains the **code, dataset, and reviewer response** supporting
the manuscript submitted to *Scientific Reports* (Ms. **41598-2024-51586**).
It is provided so that reviewers and readers can inspect and reproduce the
Random Forest regression model used to predict **SO₂ concentration** from four
experimental variables.

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

The dataset (`Sheet1`, **323 samples**) contains four input features and one target:

| Column | Symbol | Unit | Role |
|--------|--------|------|------|
| Relative humidity | RH | % | feature |
| Absorbent weight | — | g | feature |
| Temperature | T | °C | feature |
| Time | t | min | feature |
| **SO₂ concentration** | — | ppm | **target** |

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

If you use this code or data, please cite the associated *Scientific Reports*
article (Ms. 41598-2024-51586).

## Contact

**Mohammad Sadegh Kalami Yazdi** — Kalami1378@yahoo.com
