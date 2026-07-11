import joblib
import pandas as pd

model = joblib.load("model/xgb_model.pkl")
encoder = joblib.load("model/encoder.pkl")

country_imputer = joblib.load("model/country_imputer.pkl")
children_imputer = joblib.load("model/children_imputer.pkl")

top_countries = joblib.load("model/top_countries.pkl")

def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.drop(
        columns=["company", "agent", "reservation_status", "reservation_status_date"],
        inplace=True,
        errors="ignore"
    )


    df["country"] = country_imputer.transform(df[["country"]]).ravel()
    df["children"] = children_imputer.transform(df[["children"]]).ravel()

    df["country"] = df["country"].apply(
        lambda x: x if x in top_countries else "Other"
    )

    return df

new_booking = pd.DataFrame([{
    "hotel": "City Hotel",
    "lead_time": 120,
    "arrival_date_year": 2024,
    "arrival_date_month": "July",
    "arrival_date_week_number": 30,
    "arrival_date_day_of_month": 15,
    "stays_in_weekend_nights": 2,
    "stays_in_week_nights": 5,
    "adults": 2,
    "children": 0,
    "babies": 0,
    "meal": "BB",
    "country": "PRT",
    "market_segment": "Online TA",
    "distribution_channel": "TA/TO",
    "is_repeated_guest": 0,
    "previous_cancellations": 0,
    "previous_bookings_not_canceled": 1,
    "reserved_room_type": "A",
    "assigned_room_type": "A",
    "booking_changes": 0,
    "deposit_type": "No Deposit",
    "days_in_waiting_list": 0,
    "customer_type": "Transient",
    "adr": 110,
    "required_car_parking_spaces": 0,
    "total_of_special_requests": 1
}])

new_booking = preprocess_input(new_booking)

X = encoder.transform(new_booking)

prediction = model.predict(X)
probability = model.predict_proba(X)


if prediction[0] == 1:
    print("It will probably be cancelled")
else:
    print("Probably not canceled")


print("Probability Cancel:", probability[0][1])
print("Probability Not Cancel:", probability[0][0])