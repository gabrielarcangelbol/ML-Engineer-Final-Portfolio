# ML-Engineer-Final-Portfolio: Market Trend Predictor

An end-to-end machine learning workflow for predictive analysis on the Invesco S&P 500 Equal Weight ETF (RSP).

## Project Overview
This project predicts whether the next day's market close will be higher than the current day's. It implements a rigorous machine learning lifecycle—from ETL and feature engineering to dimensionality reduction and hyperparameter tuning—to achieve a predictive edge over a random baseline.



## Workflow & Methodology
This project follows the **Codecademy Machine Learning Workflow** standard:

* **ETL & Cleaning**: Extracted historical price data (RSP) and market sentiment data (^VIX) using the Yahoo Finance API.
* **Split Strategy**: Implemented a **chronological** Train-Validation-Test split (80/10/10) to prevent data leakage and ensure the model only learns from past information.
* **Feature Engineering**: 
    * Developed technical indicators (Price Ratios and Trends) across multiple time horizons.
    * Applied `StandardScaler` to normalize feature magnitudes.
    * Implemented **PCA (Principal Component Analysis)**, reducing 12 features to 9 while retaining 95% variance to filter out market noise.
* **Modeling & Tuning**: Utilized a **Random Forest Classifier**, optimized via Grid Search on the Validation Set to find the best `n_estimators`, `max_depth`, and `min_samples_split`.

## Final Performance
The model was evaluated on a completely unseen **Test Set**, representing the final stage of the validation workflow.

| Metric | Result |
| :--- | :--- |
| **Final Precision** | **54.28%** |
| **Model Type** | Optimized Random Forest |
| **Features** | 9 PCA-Compressed Components |

### Classification Insights
The model shows high **Recall (0.96)** for upward trends, indicating it is highly effective at identifying growth periods. The **Confusion Matrix** analysis suggests that the model is naturally "optimistic," which provides a significant edge in catching upward moves, though future iterations could focus on a probability threshold to minimize false positives.



## Repository Structure
* `notebooks/`: Contains the full EDA, Preprocessing, and Modeling pipeline.
* `data/`: Processed market datasets.
* `requirements.txt`: Python dependencies (scikit-learn, pandas, yfinance, matplotlib).

## Conclusion
By following a structured ML workflow, we successfully integrated external market sentiment (VIX) and transformed noisy financial data into a predictive model with a verified 54.28% precision on unseen data.