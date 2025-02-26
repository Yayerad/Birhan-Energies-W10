from flask import Flask, jsonify
from flask_cors import CORS
from data_loader import load_historical_data, load_metrics, load_predictions
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/historical', methods=['GET'])
def get_historical():
    return jsonify(load_historical_data())

@app.route('/api/forecast', methods=['GET'])
def get_forecast():
    return jsonify(load_predictions())

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    return jsonify(load_metrics())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)