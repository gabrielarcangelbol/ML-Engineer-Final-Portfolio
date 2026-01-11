from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

def create_market_pipeline(n_estimators=100, max_depth=None, min_samples_split=2, n_components=0.95):
    """
    Creates a modular Scikit-Learn Pipeline for market prediction.
    Includes: Scaling -> PCA -> Random Forest Classifier.
    """
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=n_components)),
        ('rf', RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            random_state=42,
            n_jobs=-1
        ))
    ])
    return pipeline