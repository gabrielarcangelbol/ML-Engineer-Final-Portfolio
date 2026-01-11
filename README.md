# ML-Engineer-Final-Portfolio: Market Trend Predictor

An end-to-end machine learning workflow for predictive analysis on the Invesco S&P 500 Equal Weight ETF (RSP).

## Project Overview
This project predicts whether the next day's market close will be higher than the current day's. It implements a rigorous machine learning lifecycle—from ETL and feature engineering to dimensionality reduction and hyperparameter tuning—to achieve a predictive edge over a random baseline.

### 🚀 Key Highlights
* **Sentiment Integration**: Combined price action with the VIX "Fear Index" to capture market psychology.
* **Noise Reduction**: Used PCA to retain 95% of variance while discarding statistical noise.
* **Production-Ready**: Architecture built using **modular Python scripts (`src/`)** and **Scikit-Learn Pipelines** for easy deployment and zero data leakage.

## Workflow & Methodology
This project follows the **Codecademy Machine Learning Workflow** standard:

* **ETL & Cleaning**: Extracted historical price data (RSP) and market sentiment data (^VIX) using the Yahoo Finance API.
* **Split Strategy**: Implemented a **chronological** Train-Validation-Test split (80/10/10) to prevent data leakage.
* **Feature Engineering**: 
    * Developed technical indicators (Price Ratios and Trends) across multiple time horizons.
    * Applied `StandardScaler` to normalize feature magnitudes.
    * Implemented **PCA (Principal Component Analysis)**, reducing 12 features to 9 while retaining 95% variance to filter out market noise.
* **Modeling & Tuning**: Utilized a **Random Forest Classifier**, optimized via Grid Search on the Validation Set to find the best `n_estimators`, `max_depth`, and `min_samples_split`.

## Final Performance
The model was evaluated on a completely unseen **Test Set**, representing the final stage of the validation workflow.

| Metric | Result | Note |
| :--- | :--- | :--- |
| **Final Precision** | **54.28%** | ~4% edge over random baseline |
| **Recall (Up Days)** | **96%** | High sensitivity to growth periods |
| **Model Type** | Optimized Random Forest | Final fit on Train + Val data |

### Classification Insights
The model shows high **Recall (0.96)** for upward trends, indicating it is highly effective at identifying growth periods. The **Confusion Matrix** analysis suggests that the model is naturally "optimistic," which provides a significant edge in catching upward moves.

## Future Roadmap & Next Steps
Being a machine learning engineer is about continual progress. Future extensions include:
* **Time-Series Cross-Validation**: Implement rolling windows for more robust testing across different market regimes.
* **Alternative Data**: Integrate NLP sentiment analysis from financial news headlines.
* **Advanced Algorithms**: Explore XGBoost and LSTMs to capture non-linear temporal dependencies.

## Repository Structure

* `src/`: Core logic containing `model_pipeline.py` for modular architecture.
* `models/`: Trained and serialized model files (`.joblib`) ready for instant inference.
* `notebooks/`: Research, EDA, and the end-to-end training pipeline.
* `presentation/`: Executive summary, architecture diagrams, and stakeholder findings.
* `data/`: Processed market datasets (RSP + VIX).
* `requirements.txt`: Project dependencies for environment reproducibility.

## Conclusion
By following a structured ML workflow, we successfully integrated external market sentiment (VIX) and transformed noisy financial data into a predictive model with a verified **54.28% precision**. The move to a modular `src/` structure and serialized `models/` ensures this project follows industry-standard Engineering practices.