import json
import numpy as np
import pandas as pd
from catboost import CatBoostClassifier

# Load model
model = CatBoostClassifier()
model.load_model("catboost_hotel_cancellation.cbm")

# Load threshold
with open("best_threshold.json", "r") as f:
    best_threshold = json.load(f)["threshold"]

# Define categorical features (same order you used in training)
categorical_cols = [
    'hotel',
    'deposit_type',
    'lead_deposit_interaction',
    'lead_time_bin',
    'guest_category'
]

def predict_single(sample_dict):
    # Convert to dataframe
    df = pd.DataFrame([sample_dict])

    # Predict probability
    prob = model.predict_proba(df)[0][1]

    # Apply threshold
    pred = int(prob >= best_threshold)

    return {
        "prediction": pred,
        "probability": float(prob)
    }
