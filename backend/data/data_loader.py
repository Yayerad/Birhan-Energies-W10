import pandas as pd
import json

def load_historical_data():
    df = pd.read_csv("../src/data/merged_data.csv", parse_dates=['Date'])
    return df.to_dict(orient='records')

def load_predictions():
    df = pd.read_csv("../src/data/predictions.csv", parse_dates=['Date'])
    return df.to_dict(orient='records')

def load_metrics():
    with open('../backend/data/metrics.json') as f:
        return json.load(f)