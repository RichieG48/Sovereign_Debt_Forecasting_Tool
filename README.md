# 🇫🇷 Sovereign Debt Forecasting Tool

**Author**: Gabriel Richard  
**Institution**: CentraleSupélec | Tikehau Capital  
**Status**: In development

---

## Overview

This project aims to forecast the **debt-to-GDP ratio** of sovereign countries, starting with **France**, using macroeconomic indicators and a modular, extensible framework. The final goal is to provide:

- Robust **forecasts** of sovereign debt dynamics.
- Flexible **scenario simulation** capabilities (e.g., rising rates, fiscal changes).
- An interactive **Dash-based frontend** to visualize and explore results.

---

## Objective

> **Predict the sovereign debt level of a country (e.g. France) using macroeconomic fundamentals and test counterfactual scenarios.**

The tool can help analysts, economists, and investors assess fiscal sustainability, stress-test debt evolution under various policy decisions, and monitor public finance risk in real time.

---

## Models Considered

| Model                  | Description                                                | Status       |
|-----------------------|------------------------------------------------------------|--------------|
| **NeuralProphet**     | Deep time series model (Facebook Prophet + LSTM features)  |  Used for initial prototype |
| **XGBoost Regressor** | Gradient Boosting for tabular macro features               |  Planned (to improve robustness) |
| **VAR/ARIMAX**         | Classic econometric models                                 |  Optional |
| **LSTM**              | For fine-grained monthly/quarterly modeling                |  Optional |

---

## Features Considered

### Currently Used
- `DeficitPctGDP`: Annual fiscal deficit as % of GDP
- `ECBRate`: Annual average of ECB policy rate
- Target: `DebtPctGDP` — the public debt as % of GDP

### To Be Added

| Feature               | Type           | Reason                                  |
|----------------------|----------------|-----------------------------------------|
| Inflation (CPI/Core) | Macro variable | Impacts real debt burden                |
| Real GDP Growth      | Macro          | Denominator effect in Debt/GDP          |
| Primary Balance      | Fiscal         | Shows structural position               |
| Long-term Rates      | Financial      | Reflects debt refinancing pressure      |
| Unemployment         | Labor market   | Proxy for recessionary periods          |
| Sentiment Score      | NLP            | Captures market/political environment   |

---

## Project Structure

```
Sovereign_Debt_Forecasting_Tool/
│
├── data/
│   ├── raw/                      # Raw CSVs per country
│   └── processed/                # Preprocessed input datasets
│
├── models/
│   ├── prophet_model.py         # NeuralProphet training and inference logic
│   └── trained_models/          # Saved .pkl trained models
│
├── utils/
│   ├── data_loader.py           # Load and merge raw data into ML-friendly format
│
├── dashboards/
│   └── debt_forecast_app.py     # Dash interface to explore predictions and scenarios
│
├── notebooks/
│   └── exploration.ipynb        # Data visualization and correlation analysis
│
├── train_and_store_model.py     # Script to train and persist a model
├── forecast_and_plot.py         # Script to test and visualize model forecasts
└── README.md
```

---

## 🚀 How to Use

### 1. Install Requirements

Use a Python 3.10+ environment (preferably with Conda):

```bash
conda create -n debt-env python=3.10
conda activate debt-env
pip install -r requirements.txt
```

Or simply:

```bash
conda install -c conda-forge neuralprophet pandas dash joblib
```

---

### 2. Train the Model

Train a new model for France:

```bash
python train_and_store_model.py
```

This will:

- Load and preprocess raw data from `data/raw/France`
- Train a `NeuralProphet` model
- Save the trained model to `models/trained_models/france_prophet_model.pkl`

---

### 3. Test Forecast and Visualize

In a notebook:

```python
from utils.data_loader import load_and_process_france_data
from models.prophet_model import load_trained_model, forecast_with_model

df = load_and_process_france_data()
model = load_trained_model("models/trained_models/france_prophet_model.pkl")
forecast_df = forecast_with_model(model, df)

# Plot
import matplotlib.pyplot as plt
plt.plot(df["ds"], df["y"], label="Actual Debt")
plt.plot(forecast_df["ds"], forecast_df["yhat1"], label="Forecast")
plt.legend(); plt.show()
```

---

### 4. Run the Dashboard

Start the interactive dashboard:

```bash
python dashboards/debt_forecast_app.py
```

You can:

- Explore historical and forecasted debt
- Modify inputs (deficit, ECB rate) to simulate policy shocks
- Visualize outcomes dynamically

---

## Roadmap

- [ ] Add quarterly frequency and richer macro data
- [ ] Switch to XGBoost for improved forecasting
- [ ] Integrate counterfactual scenario builder
- [ ] Add more countries: 🇮🇹 🇪🇸 🇩🇪 🇺🇸
- [ ] Deploy on Streamlit Cloud or Heroku

---

