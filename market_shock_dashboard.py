import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import datetime

# --- 1. Basic Page Config (Must be first) ---
st.set_page_config(page_title="Market Shock System", page_icon="📈", layout="wide")

st.title("🚀 Market Shock Early Warning System")

# --- 2. Sidebar for Settings ---
st.sidebar.header("📊 Settings")
ticker = st.sidebar.text_input("Ticker Symbol", value="RELIANCE.NS")
window = st.sidebar.slider("Rolling Window", 3, 20, 5)
threshold = st.sidebar.slider("Z-Score Threshold", 1.0, 4.0, 2.0)

# --- 3. Data Loading Function ---
def get_stock_data(symbol):
    try:
        # Fetching 5 years of data for better ML training
        df = yf.download(symbol, period="5y")
        if df.empty:
            return None
        
        # FIX: yfinance recently changed to MultiIndex columns. 
        # This flattens them to simple names like 'Close', 'Open', etc.
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
            
        return df
    except Exception as e:
        st.error(f"Error downloading data: {e}")
        return None

# --- 4. Main Execution ---
data_load_state = st.info(f"Checking data for {ticker}...")

df = get_stock_data(ticker)

if df is not None:
    data_load_state.empty() # Remove the info message
    
    # Feature Engineering
    df['Return'] = df['Close'].pct_change()
    df['Mean'] = df['Return'].rolling(window).mean()
    df['Std'] = df['Return'].rolling(window).std()
    df['Z_Score'] = (df['Return'] - df['Mean']) / (df['Std'] + 1e-9)
    df['Shock'] = (df['Z_Score'].abs() > threshold).astype(int)
    
    # Predict the NEXT day's shock
    df['Target'] = df['Shock'].shift(-1)
    df = df.dropna()

    # Layout: Tabs
    tab_viz, tab_ml = st.tabs(["📉 Visual Analysis", "🤖 Risk Prediction"])

    with tab_viz:
        st.subheader(f"Price Analysis: {ticker}")
        # Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Current Price", f"₹{df['Close'].iloc[-1]:,.2f}")
        col2.metric("Shocks Detected", int(df['Shock'].sum()))
        col3.metric("Current Volatility", f"{df['Std'].iloc[-1]:.4f}")

        # Price Plot
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(df.index, df['Close'], label="Price")
        # Mark shocks with red dots
        shocks = df[df['Shock'] == 1]
        ax.scatter(shocks.index, shocks['Close'], color='red', label="Shock Event", s=20)
        ax.legend()
        st.pyplot(fig)

    with tab_ml:
        st.subheader("Predictive Risk Model")
        
        # Prepare ML Data
        features = ['Return', 'Mean', 'Std', 'Z_Score']
        X = df[features]
        y = df['Target']

        if len(y.unique()) < 2:
            st.warning("Not enough shock events found. Try lowering the 'Z-Score Threshold' in the sidebar.")
        else:
            # Train model
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)

            model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
            model.fit(X_train, y_train)

            # Prediction for Tomorrow
            latest_data = scaler.transform(X.iloc[[-1]])
            prediction = model.predict(latest_data)[0]
            prob = model.predict_proba(latest_data)[0][1]

            # Results
            st.markdown("---")
            if prediction == 1:
                st.error(f"### 🚨 ALERT: HIGH SHOCK RISK FOR TOMORROW")
                st.write(f"The model predicts a **{prob:.1%}** probability of an abnormal market movement.")
            else:
                st.success(f"### ✅ STABLE: LOW RISK FOR TOMORROW")
                st.write(f"The model predicts a **{prob:.1%}** probability of a shock. Conditions appear stable.")
            
            # Feature Importance Chart
            st.subheader("Key Risk Drivers")
            importance = pd.DataFrame({'Indicator': features, 'Weight': model.feature_importances_})
            st.bar_chart(importance.set_index('Indicator'))

else:
    st.error(f"Failed to load data for {ticker}. Please check your internet connection and ticker symbol.")
