# 🛡️ Market Shock Early Warning System

**Python | Machine Learning | Streamlit**

---

## 🚀 Project Overview

The Market Shock Early Warning System is a data-driven solution designed to identify abnormal movements in stock market returns using statistical analysis and machine learning techniques.

Unlike traditional approaches that focus on predicting exact stock prices, this project emphasizes **risk detection** by identifying high-impact events (market shocks). These shocks are defined as significant deviations from normal market behavior using statistical indicators such as the **Z-score**.

The system acts as an **early warning mechanism** to detect high-risk market conditions in advance.

---

## 🎯 Problem Statement

Financial markets are highly volatile and often experience sudden and extreme fluctuations known as market shocks. These events can expose investors and institutions to significant risk.

Traditional models focus on price prediction, which is often unreliable due to the stochastic nature of financial markets.

This project shifts the focus toward a **risk-oriented approach**, aiming to classify whether the next trading period will exhibit:
- **Normal market behavior (0)**
- **Shock event (1)**

The problem is formulated as a **time-series binary classification task** using statistical thresholds.

---

## 📊 Key Features

- **Statistical Shock Detection** using Z-score thresholds  
- **Machine Learning Models**:
  - Logistic Regression  
  - Random Forest  
- **Explainability** using feature importance  
- **Interactive Dashboard** using Streamlit  
- **Real-time Prediction** of next-period shock probability  

---

## 🧭 Project Architecture

Data Collection → Data Preprocessing → Feature Engineering → Shock Detection → Machine Learning Model → Prediction → Streamlit Dashboard

---

## 📂 Data Description

- **Source:** Yahoo Finance  
- **Time Period:** January 2018 – January 2024  

### Original Features:
- Open Price  
- High Price  
- Low Price  
- Close Price  
- Volume  

👉 Close Price is used for analysis  

### Derived Features:
- Daily Return  
- Rolling Mean  
- Rolling Standard Deviation (Volatility)  
- Z-score  

### Target Variable:
- 1 → Market Shock  
- 0 → Normal Movement  

### Data Characteristics:
- Time-series (chronologically ordered)  
- Contains volatility and extreme deviations  
- Reflects real-world market behavior  

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Data collected from Yahoo Finance  
- Missing values removed  
- Sorted in chronological order  
- Close price selected  

---

### 2. Feature Engineering
- Daily Return calculated from closing prices  
- Rolling Mean captures short-term trends  
- Rolling Standard Deviation measures volatility  
- Z-score standardizes returns  

---

### 3. Shock Definition
Market shocks are defined using Z-score:

- If |Z-score| > Threshold → Shock (1)  
- Else → Normal (0)  

---

### 4. Machine Learning Formulation

The problem is modeled as a **binary classification task**.

#### Input Features:
- Return  
- Rolling Mean  
- Rolling Standard Deviation  

#### Target:
- Shock Variable  

Models Used:

**Logistic Regression**
- Simple and interpretable  
- Uses class_weight='balanced'  

**Random Forest**
- Captures non-linear relationships  
- Provides feature importance  

#### Data Processing:
- Features scaled using StandardScaler  
- Models trained on historical data  

---

### 5. Mathematical Formulation

Return:
Rₜ = (Pₜ - Pₜ₋₁) / Pₜ₋₁  

Z-score:
Z = (Rₜ - μ) / σ  

Where:
- μ = Rolling Mean  
- σ = Rolling Standard Deviation  

Shock Condition:
|Z| > Threshold ⇒ Shock  

---

### 6. Prediction Mechanism

- Latest data point is selected  
- Features extracted and scaled  
- Model predicts:
  - Shock / Normal  
  - Probability of shock  

---

## 📊 System Implementation

### Streamlit Dashboard

An interactive dashboard is developed using Streamlit.

#### Inputs:
- Stock ticker  
- Date range  
- Rolling window size  
- Z-score threshold  

#### Visualizations:
- Price trends  
- Rolling mean and volatility  
- Shock points highlighted  

#### Outputs:
- Next-day prediction  
- Probability of shock  
- Feature importance

### 📊 Dashboard Preview

<img width="1877" height="1036" alt="image" src="https://github.com/user-attachments/assets/bf73dc70-4db5-4740-bcc7-f773740b31af" />

<img width="1886" height="972" alt="image" src="https://github.com/user-attachments/assets/13e8e1b9-eb04-469f-b982-ac7fe98f0515" />



---

## 📈 Model Evaluation

Models are evaluated using:

- **Accuracy** – Overall correctness  
- **Precision** – Correct shock predictions  
- **Recall** – Ability to detect actual shocks  

👉 Special emphasis is placed on **Recall**, as market shocks are rare and high-impact events.

---

## 🔍 Explainability

- Feature importance derived from Random Forest  
- Helps identify key drivers of predictions  

### Key Findings:
- Volatility (Rolling Std Dev) is most influential  
- Daily Return also significant  
- Rolling Mean contributes to trend detection  

---

## 📈 Key Insights

- Market shocks are strongly linked to volatility  
- Z-score effectively detects abnormal behavior  
- Random Forest captures complex patterns better  
- Risk-based classification is more practical than price prediction  

---

## ⚠️ Limitations

- Uses only historical price data  
- No news or macroeconomic indicators  
- Sensitive to Z-score threshold  
- Class imbalance affects predictions  

---

## 🔮 Future Improvements

- Integrate news sentiment analysis  
- Include macroeconomic indicators  
- Explore advanced time-series models  
- Deploy as a real-time web application  

---

## 🎯 Conclusion

This project demonstrates a practical approach to financial risk analysis by focusing on market shock detection rather than price prediction.

By combining statistical techniques (Z-score) with machine learning models (Logistic Regression and Random Forest), the system effectively identifies abnormal market conditions and provides early warning signals.

The Streamlit dashboard enhances usability by enabling real-time visualization and prediction.

---

## ✍️ Personal Note

As a Data Science student, I aimed to apply mathematical concepts to solve real-world financial problems.

Instead of predicting exact stock prices, this project focuses on detecting **risk**, acting as a “smoke detector” for the market.

### Challenges:
- Class imbalance → solved using `class_weight='balanced'`  
- Understanding Z-score as core feature  

---

## ⭐ Acknowledgment

This project reflects practical learning in:
- Data Analysis  
- Machine Learning  
- Financial Risk Modeling  
- Dashboard Development  

---
