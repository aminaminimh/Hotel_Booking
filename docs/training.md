# Overview

The goal of this project is to predict whether a hotel booking will be cancelled.

Target variable:

`is_canceled`

```
0 → Not Cancelled

1 → Cancelled
```

# Training Pipeline

```
Load Dataset
      │
      ▼
Preprocessing
      │
      ▼
Train/Test Split
      │
      ▼
Hyperparameter Tuning
      │
      ▼
Model Training
      │
      ▼
Evaluation
      │
      ▼
Save Model
```

# Train/Test Split

The dataset is divided into

| Dataset | Percentage |
|----------|------------|
| Training | 70% |
| Testing | 30% |

Random State

```
123
```

Stratified sampling is used to preserve class distribution.

# Machine Learning Algorithm

`XGBoost Classifier`

Reasons for choosing XGBoost

- Excellent performance on tabular data
- Handles nonlinear relationships
- Robust against noisy features
- Fast inference
- Supports feature importance analysis

# Hyperparameter Tuning

Hyperparameter optimization is performed before the final model is selected.

Typical parameters include

- max_depth
- learning_rate
- n_estimators
- subsample
- colsample_bytree

The best performing model is saved for deployment.

# Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score

Current Performance:

| Metric | Value |
|---------|------:|
| Accuracy | 87% |
| Precision | 88% |
| Recall | 92% |
| F1-score | 90% |

# Saved Model

The trained model is exported using:

`Joblib`

Generated files:

```
xgb_model.pkl

encoder.pkl

country_imputer.pkl

children_imputer.pkl

top_countries.pkl
```

These files are used by the prediction API.