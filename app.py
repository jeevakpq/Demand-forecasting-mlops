from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "Demand Forecasting API is running"}

@app.post("/predict")
def predict(
    Store: int,
    Dept: int,
    IsHoliday: int,
    year: int,
    month: int,
    day: int,
    week: int,
    lag_1: float,
    lag_4: float,
    lag_12: float,
    rolling_mean_4: float
):
    features = np.array([[Store, Dept, IsHoliday, year, month, day, week,
                          lag_1, lag_4, lag_12, rolling_mean_4]])

    prediction = model.predict(features)

    return {"Predicted Sales": float(prediction[0])}