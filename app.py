import streamlit as st
import requests

st.title("Churn Prediction App")
st.subheader("Enter Customer Details")

age = st.number_input("Age", 10, 100, 30)
tenure = st.number_input("Tenure", 0, 130, 10)
monthly_charges = st.number_input("Monthly Charges", 30, 150)
gender = st.selectbox("Gender", ["male", "female"])

if st.button("Predict"):

    data = {
        "age": age,
        "gender": gender,
        "tenure": tenure,
        "monthly_charges": monthly_charges
    }

    try:
        res = requests.post("http://127.0.0.1:8000/predict", json=data)

        if res.status_code == 200:
            result = res.json()

            if result["confidence"] > 0.8:
                level = "High Risk"
            elif result["confidence"] > 0.6:
                level = "Medium Risk"
            else:
                level = "Low Risk"

            st.success(
                f"Prediction: {result['label']} | Confidence: {result['confidence']} ({level})"
            )

            if level == "High Risk":
                st.warning("Customer is highly likely to churn. Immediate action recommended.")
            elif level == "Medium Risk":
                st.info("Moderate risk of churn. Monitor customer behavior.")
            else:
                st.success("Low risk. Customer likely to stay.")

        else:
            st.error("API Error")

    except:
        st.error("FastAPI server is not running")