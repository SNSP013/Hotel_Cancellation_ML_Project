import streamlit as st
import pandas as pd
from app.predict import predict_single

st.title("Hotel Booking Cancellation Predictor")
st.write("Enter booking details to estimate cancellation probability.")

# All the input fields:

hotel = st.selectbox("Hotel Type", ["City Hotel", "Resort Hotel"])
lead_time = st.number_input("Lead Time (days)", min_value=0, max_value=500)
arrival_month_num = st.selectbox("Arrival Month", list(range(1, 13)))
deposit_type = st.selectbox("Deposit Type", ["No Deposit", "Refundable", "Non Refundable"])
days_in_waiting_list = st.number_input("Days in Waiting List", min_value=0, max_value=365)
adr = st.number_input("ADR (Average Daily Rate)", min_value=0.0)
total_of_special_requests = st.number_input("Special Requests", min_value=0, max_value=10)
total_guests = st.number_input("Total Guests", min_value=1, max_value=10)
total_stay = st.number_input("Total Stay (nights)", min_value=1, max_value=30)
repeat_ratio = st.number_input("Repeat Ratio", min_value=0.0)
seasonal_adr = st.number_input("Seasonal ADR", min_value=-500.0)
stability = st.number_input("Stability Score", min_value=-10.0)
price_vs_month = st.number_input("Price vs Month", min_value=-500.0)
has_deposit = st.selectbox("Has Deposit?", [0, 1])
low_cancellation_season = st.selectbox("Is Low Cancellation Season?", [0, 1])
lead_time_bin = st.selectbox("Lead Time Bin", ["short", "mid", "long", "very_long", "extreme"])
lead_deposit_interaction = st.text_input("Lead-Deposit Interaction")
guest_category = st.selectbox("Guest Category", ["solo", "couple", "family", "group"])

if st.button("Predict Cancellation"):
    sample = {
        "hotel": hotel,
        "lead_time": lead_time,
        "arrival_month_num": arrival_month_num,
        "deposit_type": deposit_type,
        "days_in_waiting_list": days_in_waiting_list,
        "adr": adr,
        "total_of_special_requests": total_of_special_requests,
        "total_guests": total_guests,
        "total_stay": total_stay,
        "repeat_ratio": repeat_ratio,
        "seasonal_adr": seasonal_adr,
        "stability": stability,
        "price_vs_month": price_vs_month,
        "has_deposit": has_deposit,
        "low_cancellation_season": low_cancellation_season,
        "lead_time_bin": lead_time_bin,
        "lead_deposit_interaction": lead_deposit_interaction,
        "guest_category": guest_category
    }

    result = predict_single(sample)

    st.subheader(f"Prediction: {'Canceled' if result['prediction']==1 else 'Not Canceled'}")
    st.subheader(f"Probability: {result['probability']:.2f}")
