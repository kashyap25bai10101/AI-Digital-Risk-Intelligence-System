import streamlit as st
import matplotlib.pyplot as plt

from model import train_model
from phishing_detector import detect_phishing
from url_analyzer import analyze_url
from recommendations import get_recommendations

# Page config (UI improvement)
st.set_page_config(page_title="AI Digital Risk System", layout="centered")

# Load model + accuracy
model, acc = train_model()

st.title("AI Digital Risk Intelligence System")

# ---------------------------
# USER INPUT SECTION
# ---------------------------
st.header("Behavior Analysis")

password_reuse = st.selectbox("Reuse Passwords?", ["Yes", "No"])
public_wifi = st.selectbox("Use Public WiFi?", ["Yes", "No"])
click_links = st.selectbox("Click Unknown Links?", ["Yes", "No"])
social_media = st.selectbox("Share Personal Info?", ["Yes", "No"])
two_fa = st.selectbox("Use 2FA?", ["Yes", "No"])

if st.button("Predict Risk"):
    input_data = [[
        1 if password_reuse=="Yes" else 0,
        1 if public_wifi=="Yes" else 0,
        1 if click_links=="Yes" else 0,
        1 if social_media=="Yes" else 0,
        0 if two_fa=="Yes" else 1
    ]]

    prediction = model.predict(input_data)[0]

    st.subheader(f"Predicted Risk Level: {prediction}")

    # Show model accuracy
    st.write(f"Model Accuracy: {round(acc*100,2)}%")

    # Recommendations
    st.subheader("Recommendations")
    tips = get_recommendations(prediction)
    for tip in tips:
        st.write("- " + tip)

    # ---------------------------
    # SIMPLE VISUALIZATION
    # ---------------------------
    st.subheader("Risk Visualization")

    risk_map = {"Low": 30, "Medium": 60, "High": 90}
    risk_value = risk_map.get(prediction, 50)

    labels = ["Safe Level", "Risk Level"]
    values = [100 - risk_value, risk_value]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylabel("Percentage")

    st.pyplot(fig)

# ---------------------------
# PHISHING DETECTOR
# ---------------------------
st.header("Phishing Detector")

text = st.text_area("Enter message or email text")

if st.button("Check Phishing"):
    result = detect_phishing(text)
    st.subheader(f"Result: {result}")

# ---------------------------
# URL ANALYZER
# ---------------------------
st.header("URL Risk Analyzer")

url = st.text_input("Enter URL")

if st.button("Analyze URL"):
    result = analyze_url(url)
    st.subheader(f"URL Risk: {result}")
