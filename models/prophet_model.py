from neuralprophet import NeuralProphet
import pandas as pd
import os

MODEL_PATH = "models/saved_model.np"

def train_neuralprophet_model(df: pd.DataFrame) -> NeuralProphet:
    """
    Train a NeuralProphet model using France macro data.
    Expects df with columns: ["ds", "y", "DeficitPctGDP", "ECBRate"]
    """
    model = NeuralProphet(
        yearly_seasonality=False,
        weekly_seasonality=False,
        daily_seasonality=False,
        n_changepoints=10,
        learning_rate=1.0,
        epochs=1000
    )

    model = model.add_future_regressor("DeficitPctGDP")
    model = model.add_future_regressor("ECBRate")

    model.fit(df, freq="Y")

    return model

def forecast_with_model(model: NeuralProphet, df_future: pd.DataFrame) -> pd.DataFrame:
    """
    Forecast future values using trained model.
    Expects df_future with at least ["ds", "DeficitPctGDP", "ECBRate"]
    """
    forecast = model.predict(df_future)
    return forecast