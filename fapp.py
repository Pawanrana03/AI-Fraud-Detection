import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("fraud_detection_pipeline.pkl")


# -----------------------------
# Page settings
# -----------------------------
st.set_page_config(
    page_title="AI Fraud Detection",
    page_icon="💳",
    layout="centered"
)


# -----------------------------
# Compact design
# -----------------------------
st.markdown("""
<style>

.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    max-width: 800px;
}

h1 {
    font-size: 28px !important;
    margin-bottom: 5px !important;
}

p, label {
    font-size: 14px !important;
}

.stButton button {
    font-size: 15px;
    padding: 5px 20px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Title
# -----------------------------
st.title("💳 AI Fraud Detection System")

st.write("Enter transaction details below:")


# -----------------------------
# Input fields
# -----------------------------
col1, col2 = st.columns(2)


with col1:

    transaction_type = st.selectbox(
        "Transaction Type",
        ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
    )

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=0.0
    )

    oldbalanceOrg = st.number_input(
        "Old Balance (Origin)",
        min_value=0.0,
        value=0.0
    )


with col2:

    newbalanceOrig = st.number_input(
        "New Balance (Origin)",
        min_value=0.0,
        value=0.0
    )

    oldbalanceDest = st.number_input(
        "Old Balance (Destination)",
        min_value=0.0,
        value=0.0
    )

    newbalanceDest = st.number_input(
        "New Balance (Destination)",
        min_value=0.0,
        value=0.0
    )


# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict Fraud", use_container_width=True):

    # Create input DataFrame
    data = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest]
    })


    # Make prediction
    prediction = model.predict(data)


    # Calculate fraud probability
    probability = model.predict_proba(data)[0][1]


    # -----------------------------
    # Show probability
    # -----------------------------
    st.write(
        f"### Fraud Probability: {probability * 100:.2f}%"
    )


    # -----------------------------
    # Show result
    # -----------------------------
    if prediction[0] == 1:

        st.error("⚠️ FRAUDULENT TRANSACTION")

    else:

        st.success("✅ LEGITIMATE TRANSACTION")
