# 🛡️ Market Shock Early Warning System (MSEWS)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)](https://streamlit.io/)

### 🚀 Project Overview
This project presents a **Market Shock Early Warning System** aimed at identifying abnormal movements in stock market returns using statistical analysis and machine learning. Unlike traditional price prediction, this study emphasizes the detection of **high-risk events** (shocks) characterized by significant deviations (Z-scores) from normal market behavior.

---

### 📊 Key Features
- **Statistical Detection:** Uses rolling Z-scores to identify abnormal market returns.
- **ML Forecasting:** Implements **Logistic Regression** and **Random Forest** to predict the probability of a shock for the next trading day.
- **Explainability:** Visualizes feature importance to show what drives market risk (e.g., Volatility).
- **Interactive Dashboard:** Built with Streamlit for real-time monitoring and analysis.

---

### 📐 Mathematical Formulation
The system identifies shocks based on the standardized deviation of returns:
- **Return Calculation:** $R_t = \frac{P_t - P_{t-1}}{P_{t-1}}$
- **Z-Score:** $Z = \frac{R_t - \mu}{\sigma}$
- **Shock Condition:** $|Z| > \text{Threshold} \Rightarrow \text{Shock (1)}$

---

### 🛠️ Tech Stack
- **Languages:** Python
- **Libraries:** yfinance, Pandas, Scikit-Learn, Matplotlib
- **Deployment:** Streamlit

---

### 🏃 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the dashboard:
   ```bash
   python -m streamlit run market_shock_dashboard.py
   ```

---

### 📈 Results & Insights
- **Volatility ($\sigma$)** was found to be the most significant driver for predicting market shocks.
- The **Z-score method** effectively identifies abnormal historical movements.
- Focusing on **Risk Classification** provides more practical value for investors than simple price prediction.
