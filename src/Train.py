import pandas as pd
import xgboost as xgb

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import os
import joblib

from preprocessing import (
    clean_data,
    build_imputers,
    reduce_country_cardinality,
    build_encoder
)

booking = pd.read_csv(r"data/hotel_bookings.csv")

X = booking.drop("is_canceled", axis=1)
y = booking["is_canceled"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

X_train = clean_data(X_train)
X_test = clean_data(X_test)

country_imputer, children_imputer = build_imputers()

country_imputer.fit(X_train[["country"]])
children_imputer.fit(X_train[["children"]])

X_train["country"] = country_imputer.transform(X_train[["country"]]).ravel()

X_train["children"] = children_imputer.transform(X_train[["children"]]).ravel()

top_countries = (
    X_train["country"]
    .value_counts()
    .head(10)
    .index
)

X_train = reduce_country_cardinality(X_train, top_countries)

X_test = reduce_country_cardinality(X_test, top_countries)

encoder = build_encoder()

X_train = encoder.fit_transform(X_train)

X_test = encoder.transform(X_test)

model = xgb.XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=123
)

model.fit(
    X_train,
    y_train
)

pred = model.predict(
    X_test
)

print(
    classification_report(
        y_test,
        pred
    )
)

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/xgb_model.pkl")
joblib.dump(encoder, "model/encoder.pkl")

joblib.dump(country_imputer, "model/country_imputer.pkl")
joblib.dump(children_imputer, "model/children_imputer.pkl")

joblib.dump(top_countries, "model/top_countries.pkl")