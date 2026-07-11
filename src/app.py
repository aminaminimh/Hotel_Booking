from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path

import joblib
import pandas as pd

from src.preprocessing import clean_data, reduce_country_cardinality


BASE_DIR = Path(__file__).resolve().parent.parent


app = FastAPI(
    title="Hotel Booking Cancellation Prediction API",
    version="1.0.0"
)
templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


model = joblib.load(BASE_DIR / "model" / "xgb_model.pkl")

encoder = joblib.load(BASE_DIR / "model" / "encoder.pkl")

country_imputer = joblib.load(BASE_DIR / "model" / "country_imputer.pkl")

children_imputer = joblib.load(BASE_DIR / "model" / "children_imputer.pkl")

top_countries = joblib.load(BASE_DIR / "model" / "top_countries.pkl")


class BookingInput(BaseModel):
    hotel: str
    lead_time: int
    arrival_date_year: int
    arrival_date_month: str
    arrival_date_week_number: int
    arrival_date_day_of_month: int
    stays_in_weekend_nights: int
    stays_in_week_nights: int
    adults: int
    children: float
    babies: int
    meal: str
    country: str
    market_segment: str
    distribution_channel: str
    is_repeated_guest: int
    previous_cancellations: int
    previous_bookings_not_canceled: int
    reserved_room_type: str
    assigned_room_type: str
    booking_changes: int
    deposit_type: str
    days_in_waiting_list: int
    customer_type: str
    adr: float
    required_car_parking_spaces: int
    total_of_special_requests: int


def preprocess(df: pd.DataFrame):

    df = clean_data(df)

    df["country"] = country_imputer.transform(
        df[["country"]]
    ).ravel()

    df["children"] = children_imputer.transform(
        df[["children"]]
    ).ravel()

    df = reduce_country_cardinality(
        df,
        top_countries
    )

    X = encoder.transform(df)

    return X


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/predict")
def predict(data: BookingInput):

    df = pd.DataFrame([data.model_dump()])

    X = preprocess(df) 

    prediction = model.predict(X)

    probability = model.predict_proba(X)

    return {
        "prediction": int(prediction[0]),
        "cancel_probability": round(float(probability[0][1]), 3),
        "not_cancel_probability": round(float(probability[0][0]), 3)
    }