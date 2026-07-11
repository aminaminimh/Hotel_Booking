import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

categorical_cols = [
    "hotel",
    "arrival_date_month",
    "meal",
    "market_segment",
    "distribution_channel",
    "reserved_room_type",
    "assigned_room_type",
    "deposit_type",
    "customer_type",
    "country"
]

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.drop(
        columns=["company", "agent", "reservation_status_date", "reservation_status"],
        inplace=True,
        errors="ignore"
    )

    return df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    country_imputer = SimpleImputer(strategy="most_frequent")
    df["country"] = country_imputer.fit_transform(df[["country"]]).ravel()

    children_imputer = SimpleImputer(strategy="median")
    df["children"] = children_imputer.fit_transform(df[["children"]]).ravel()

    return df

def reduce_country_cardinality(
    df: pd.DataFrame,
    top_countries
) -> pd.DataFrame:

    df = df.copy()

    df["country"] = df["country"].apply(
        lambda x: x if x in top_countries else "Other"
    )

    return df

def build_imputers():

    country_imputer = SimpleImputer(
        strategy="most_frequent"
    )

    children_imputer = SimpleImputer(
        strategy="median"
    )

    return country_imputer, children_imputer

def build_encoder():

    return ColumnTransformer(

        transformers=[(
                "ohe",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                categorical_cols
            )],
        remainder="passthrough"

    )