from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict_single

app = FastAPI(title="Hotel Cancellation Prediction API")

class Booking(BaseModel):
    hotel: str
    lead_time: int
    arrival_month_num: int
    deposit_type: str
    days_in_waiting_list: int
    adr: float
    total_of_special_requests: int
    total_guests: float
    total_stay: int
    repeat_ratio: float
    seasonal_adr: float
    stability: float
    price_vs_month: float
    has_deposit: int
    low_cancellation_season: int
    lead_time_bin: str
    lead_deposit_interaction: str
    guest_category: str

@app.post("/predict")
def predict(data: Booking):
    return predict_single(data.dict())
