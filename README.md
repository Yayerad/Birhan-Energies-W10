# Brent Oil Price Analysis & Forecasting System

![Dashboard Preview](./dashboard/dashboard.PNG)

## 📌 Project Overview
Interactive dashboard and machine learning system for analyzing Brent oil prices and correlating economic/political events.

## ✨ Features
- 📈 Interactive price forecasts (ARIMA, LSTM, VAR)
- 📉 Volatility analysis (GARCH models)
- 🗓️ Event correlation visualization
- 📊 Performance metrics (MAE, RMSE)
- 📱 Responsive web interface

## 🚀 Installation

### Backend (Flask)
```bash
cd backend
pip install -r requirements.txt

Frontend (React)
bash
Copy
cd frontend
npm install
⚙️ Configuration
Create .env in frontend directory:

env
Copy
REACT_APP_API_BASE=http://localhost:5000
🏃 Usage
bash
Copy
# Start backend
cd backend && python app.py

# Start frontend
cd ../frontend && npm start
📂 Project Structure
Copy
.
├── backend/               # Flask API
│   ├── app.py             # API routes
│   ├── data_loader.py     # Data processing
│   └── requirements.txt   # Python dependencies
├── frontend/              # React dashboard
│   ├── src/               # UI components
│   │   ├── components/    # (PriceChart, MetricsPanel)
│   │   └── App.js         # Main component
├── notebooks/             # Jupyter analysis
│   ├── data_collection.ipynb
│   ├── eda.ipynb
│   └── models.ipynb       # Model training
├── src/data/              # Datasets
│   ├── merged_data.csv    # Combined dataset
│   └── predictions.csv    # Model outputs
🌐 API Endpoints
Endpoint	Description	Data Format
/api/historical	Historical price data	JSON
/api/forecast	Model predictions	JSON
/api/metrics	Performance metrics	JSON
🧠 Implemented Models
ARIMA - Time series forecasting

LSTM - Deep learning predictions

VAR - Multivariate analysis

GARCH - Volatility modeling

Markov-Switching - Regime detection

🛠️ Technologies
Python
Flask
React
TensorFlow
Pandas

🤝 Contributing
Fork the repository

Create feature branch (git checkout -b feature/new-feature)

Commit changes (git commit -m 'Add feature')

Push to branch (git push origin feature/new-feature)

Open Pull Request

📄 License
MIT License - see LICENSE file

Copy

---

### **How to Use**
1. Copy the entire content above.
2. Create a new file in your repository root called `README.md`.
3. Paste the content into the file.
4. Save the file.

---

### **Key Features of This README**
1. **Clear Structure**: Organized into sections for easy navigation.
2. **Code Blocks**: Highlighted with triple backticks for readability.
3. **Emojis**: Used for visual appeal and quick scanning.
4. **Badges**: Dynamic shields.io badges for technologies.
5. **Table Format**: For API endpoints.
6. **File Structure**: Displayed in a code block for clarity.
7. **Markdown Compatibility**: Fully compatible with GitHub's Markdown renderer.

---

### **Customization**
- Replace `./dashboard/dashboard.PNG` with the actual path to your dashboard screenshot.
- Update the **Technologies** section with your actual versions.
- Add or remove sections as needed for your project.

This Markdown file is optimized for GitHub and will render beautifully in your repository. Let me know if you need further adjustments!
