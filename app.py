import streamlit as st
from model import train_model
from phishing_detector import detect_phishing
from url_analyzer import analyze_url
from recommendations import get_recommendations

model = train_model()

st.title("🧠 AI Digital Risk Intelligence System")

# USER INPUT
st.header("🔐 Behavior Analysis")

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

    st.subheader(f"Risk Level: {prediction}")

    tips = get_recommendations(prediction)
    for tip in tips:
        st.write("- " + tip)

# PHISHING CHECK
st.header("🎣 Phishing Detector")
text = st.text_area("Enter message/email")

if st.button("Check Phishing"):
    result = detect_phishing(text)
    st.write(result)

# URL CHECK
st.header("🌐 URL Analyzer")
url = st.text_input("Enter URL")

if st.button("Analyze URL"):
    result = analyze_url(url)
    st.write(result)
