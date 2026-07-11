# Data Preprocessing

## Overview

The quality of a Machine Learning model highly depends on the quality of the input data. This project applies several preprocessing techniques to clean the dataset and prepare it for training.

---

# Pipeline

```
Raw Dataset
      │
      ▼
Remove Unnecessary Columns
      │
      ▼
Handle Missing Values
      │
      ▼
Reduce Country Cardinality
      │
      ▼
One-Hot Encoding
      │
      ▼
Processed Dataset
```

---

# 1. Removing Unnecessary Features

The following features were removed before training:

| Feature | Reason |
|----------|--------|
| company | More than 90% missing values |
| agent | High cardinality with many missing values |
| reservation_status | Data leakage (contains target information) |
| reservation_status_date | Available only after booking outcome |

---

# 2. Missing Value Handling

Different strategies were selected depending on the feature type.

## Country

Method:

```
Most Frequent Value
```

Reason:

Country is a categorical feature and using the most common country preserves the existing data distribution.

---

## Children

Method:

```
Median Imputation
```

Reason:

Children is a numerical feature.

Median is less sensitive to outliers than the mean.

---

# 3. Country Cardinality Reduction

The original dataset contains 177 different countries.

Using One-Hot Encoding directly would generate 177 additional features.

Instead, the preprocessing pipeline keeps only the 10 most frequent countries.

```
 Top 10 Countries

        ↓

Remaining Countries

        ↓

      Other
```

Benefits

- Lower dimensionality
- Faster training
- Better generalization
- Reduced memory usage

---

# 4. Categorical Encoding

Categorical variables are transformed using

```
OneHotEncoder
```

Parameters

```python
handle_unknown="ignore"
```

This allows the application to predict unseen categories during inference.

---

# Saved Objects

The preprocessing stage stores several reusable objects.

| Object | Purpose |
|---------|----------|
| encoder.pkl | One-Hot Encoder |
| country_imputer.pkl | Country imputer |
| children_imputer.pkl | Children imputer |
| top_countries.pkl | Top countries list |

These objects are reused during prediction to guarantee identical preprocessing.