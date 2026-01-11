# Project Scoping: Stock Market Directional Trend Prediction

## 1. Goals
The objective of this project is to build an end-to-end machine learning pipeline to predict the daily price movement of a specific stock ticker using historical data from the Yahoo Finance API.

* **Business Objective:** To provide a tool that helps identify whether a stock is likely to close higher or lower the following day, assisting in automated trading decision-making.
* **Technical Objective:** Develop a production-ready pipeline using `scikit-learn Pipeline` objects to automate data scaling, dimensionality reduction (PCA), and model inference without data leakage.
* **Success Metric:** Aim for **Precision > 53%**. *Note: In high-noise financial environments, a consistent edge over the 50% random baseline is considered a successful predictive signal.*

## 2. Data
* **Source:** Yahoo Finance API (via `yfinance` Python library).
* **Tickers:** `RSP` (Target: Invesco S&P 500® Equal Weight ETF) & `^VIX` (CBOE Volatility Index).
* **Rationale:** Adding the VIX provides a sentiment layer (market fear) that complements the price action of the RSP, helping the model identify regime changes.
* **Type:** Time-series OHLCV data (Open, High, Low, Close, Volume).
* **Timeframe:** From 2003-05-01 (Inception) to Present.
* **Key Characteristics:**
    * **Features:** A 12-dimensional vector including Daily returns, multi-horizon Price Ratios (5, 60, 250 days), Moving Average trends, and VIX volatility levels.
    * **Dimensionality Reduction:** Implementation of **PCA** to condense features into 9 principal components while retaining 95% of variance.
    * **Target:** Binary classification (1 if Tomorrow's Close > Today's Close, else 0).

## 3. Analysis & Workflow 
1. **Data Ingestion:** Automated fetching and merging of historical RSP price data and VIX sentiment data.
2. **Exploratory Data Analysis (EDA):** Visualizing price trends, volatility clusters, and the inverse correlation between the VIX and RSP returns.
3. **Feature Engineering & Noise Reduction:** * Creation of lagged variables and momentum indicators.
    * **PCA Implementation** to filter out market noise and focus on the most significant variance components.
4. **Modeling:** Optimized **Random Forest Classifier** integrated into a modular `scikit-learn Pipeline`.
5. **Evaluation:** * Hyperparameter tuning using a dedicated Validation Set.
    * Use of a strict **Blind Test Set** (final 10% of data) to verify real-world performance and generalizability.
6. **Productionalization:** Modular architecture designed to handle raw input and produce daily directional inferences automatically.