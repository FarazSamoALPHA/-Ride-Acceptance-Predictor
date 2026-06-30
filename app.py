import streamlit as st
import joblib
import pandas as pd

# Load classifier and feature schema
clf = joblib.load('ride_acceptance_clf.pkl')
features = joblib.load('clf_features.pkl')

st.set_page_config(page_title="Ride Acceptance Predictor", layout="centered")
st.title("🛺 Will the driver accept your price?")

# Sidebar inputs
st.sidebar.header("Enter Ride Details")
dist = st.sidebar.slider("Distance (km)", 1.0, 20.0, 5.0)
hour = st.sidebar.slider("Hour of Day", 0, 23, 12)
offered = st.sidebar.number_input("Your Offered Price", value=int(dist*25))

# Formulate input for prediction
input_df = pd.DataFrame([[dist, offered, hour]], columns=features)

# Predictions
accept = clf.predict(input_df)[0]
accept_prob = clf.predict_proba(input_df)[0][1]

# Show results
st.subheader("Outcome")
st.write(f"🎯 Driver will **{'ACCEPT' if accept else 'REJECT'}** your offer")
st.write(f"Probability: {accept_prob:.1%}")

st.markdown("---")
st.write("Adjust the sliders and offer to test different scenarios.")
