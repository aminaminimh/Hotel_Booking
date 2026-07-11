# 🏨 Hotel Booking Cancellation Prediction

A Machine Learning web application that predicts whether a hotel reservation is likely to be cancelled using an XGBoost classifier.

The project includes a complete Machine Learning pipeline from data preprocessing to model deployment through a FastAPI backend and an interactive web interface.

---


# 🚀 Features

- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Country Cardinality Reduction
- One-Hot Encoding
- Hyperparameter Tuning
- XGBoost Classification
- Model Persistence using Joblib
- FastAPI REST API
- Interactive HTML/CSS/JavaScript Frontend

---

# 📊 Dataset

**Dataset Name**

Hotel Booking Demand Dataset

**Source**

https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

### Dataset Information

- 119,390 hotel bookings
- Binary Classification
- 30+ original features
- Real-world reservation data

Target Variable

```
is_canceled
```

- 0 → Booking Not Cancelled
- 1 → Booking Cancelled

---

# ⚙️ Machine Learning Pipeline

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Missing Value Imputation
      │
      ▼
Country Cardinality Reduction
      │
      ▼
One-Hot Encoding
      │
      ▼
Train/Test Split
      │
      ▼
Hyperparameter Tuning
      │
      ▼
XGBoost Training
      │
      ▼
Save Model
      │
      ▼
FastAPI Backend
      │
      ▼
Web Prediction
```

---

# 📂 Project Structure

```
Hotel_Booking/
│
├── README.md
├── requirements.txt
│
│
├── data/
│   └── hotel_bookings.csv
│
├── docs/
│   ├── preprocessing.md
│   ├── training.md
│   ├── api.md
│   └── deployment.md
│
├── images/
│
├── models/
│   ├── xgb_model.pkl
│   ├── encoder.pkl
│   ├── country_imputer.pkl
│   ├── children_imputer.pkl
│   └── top_countries.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── predict.py
│   ├── app.py
│   └── __init__.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

# 🧹 Data Preprocessing

The preprocessing pipeline consists of the following steps:

- Removing unnecessary columns
- Handling missing values
- Country grouping (Top 10 + Other)
- One-Hot Encoding categorical features
- Saving preprocessing objects for inference

Removed columns:

- company
- agent
- reservation_status
- reservation_status_date

Missing Values:

| Feature | Method |
|----------|---------|
| country | Most Frequent |
| children | Median |

Country encoding:

```
Top 10 Countries

↓

All Remaining Countries

↓

Other
```

---

# 🤖 Machine Learning Model

Algorithm:

```
XGBoost Classifier
```

Why XGBoost?

- High Accuracy
- Handles mixed features
- Robust to noisy data
- Excellent performance on tabular datasets

Hyperparameter tuning was applied to improve the model performance.

---

# 📈 Model Performance

| Metric | Score |
|---------|------:|
| Accuracy | **87%** |
| Precision | **88%** |
| Recall | **92%** |
| F1 Score | **90%** |

Classification Report

```
              precision    recall    f1-score

Not Cancelled     0.88      0.92      0.90
Cancelled         0.85      0.78      0.81

Accuracy                        0.87
```

---

# 🌐 Web Application

The project includes a complete web application built using:

- FastAPI
- HTML
- CSS
- JavaScript

Users can enter booking information through the web interface and receive an instant prediction.

---

# 🔌 API

Endpoint

```
POST /predict
```

Example Request

```json
{
  "hotel":"City Hotel",
  "lead_time":30,
  "arrival_date_year":2016,
  "arrival_date_month":"May",
  "country":"PRT",
  "...":"..."
}
```

Example Response

```json
{
  "prediction":0,
  "cancel_probability":0.12,
  "not_cancel_probability":0.88
}
```

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/aminaminimh/Hotel_Booking.git
```

Go to project directory

```bash
cd Hotel_Booking
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn src.app:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

# 🛠 Technologies

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- FastAPI
- Joblib
- HTML
- CSS
- JavaScript

---

# 🔮 Future Improvements

- Deploy on Render
- Docker Support
- SHAP Explainability
- Responsive UI Improvements
- Model Monitoring
- Feature Importance Visualization
- Automatic Data Validation

---

# 👨‍💻 Author

**Amin Amini**

Computer Engineering Student

Interested in:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Large Language Models

GitHub:

```
https://github.com/aminaminimh/HOTEL_BOOKING.git
```