import pandas as pd
import matplotlib.pyplot as plt
import joblib

from utils.data_loader import load_and_process_france_data
from models.prophet_model import train_neuralprophet_model
import joblib
# 1. Load historical France macro data
df = load_and_process_france_data()

# 2. Train the Prophet model
model = train_neuralprophet_model(df)


joblib.dump(model, "models/trained_models/france_prophet_model.pkl")
print("Model saved to models/trained_models/france_prophet_model.pkl")
