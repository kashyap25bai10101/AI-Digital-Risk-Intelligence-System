
# AI Digital Risk Intelligence System (DRIS)

## Overview

In today’s digital environment, users interact with multiple online platforms without fully understanding the risks associated with their behavior. Practices such as reusing passwords, clicking unknown links, or ignoring basic security measures often lead to data breaches and privacy issues.

This project is an attempt to address this gap by building a system that analyzes user behavior and provides a risk assessment using basic machine learning techniques. In addition to prediction, the system also evaluates suspicious messages and URLs to promote better digital awareness.

---

## Objective

The main objectives of this project are:

* To analyze user digital habits and estimate their risk level
* To demonstrate the application of machine learning in a real-world scenario
* To provide users with meaningful suggestions to improve their digital safety
* To build an interactive and easy-to-use application

---

## Features

### 1. Behavioral Risk Prediction (Machine Learning Based)

* Accepts user input related to digital habits
* Uses a Decision Tree model to classify risk as Low, Medium, or High

### 2. Phishing Message Detection

* Analyzes user-entered text such as emails or messages
* Detects suspicious patterns using predefined keyword logic

### 3. URL Risk Analyzer

* Evaluates URLs based on:

  * Security protocol (HTTP/HTTPS)
  * Length of the URL
  * Presence of suspicious keywords
* Classifies URLs into risk categories

### 4. Recommendation System

* Provides personalized suggestions based on predicted risk level
* Helps users improve their digital practices

---

## Technology Stack

* Python
* Streamlit
* Scikit-learn
* Pandas

---

## Project Structure

AI-Digital-Risk-System/
│── app.py
│── model.py
│── phishing_detector.py
│── url_analyzer.py
│── recommendations.py
│── dataset.csv
│── requirements.txt
│── README.md

---

## Installation

Clone the repository:

git clone [https://github.com/your-username/AI-Digital-Risk-System.git](https://github.com/kashyap25bai10101/AI-Digital-Risk-Intelligence-System)

Navigate to the project directory:

cd AI-Digital-Risk-System

Install the required dependencies:

pip install -r requirements.txt

---

## How to Run

Run the following command in the terminal:

streamlit run app.py

After running the command, the application will open in your browser.

---

## Working Principle

The system collects user inputs related to their digital behavior and converts them into numerical values. These inputs are then passed to a trained Decision Tree model, which predicts the user’s risk level.

Additionally, rule-based logic is applied to analyze phishing messages and URLs. Based on the results, the system generates recommendations to improve the user's digital safety.

---

## Challenges Faced

* Designing a simple yet meaningful dataset for training the model
* Converting real-world behavior into structured inputs
* Ensuring that the system remains easy to use while incorporating multiple features

---

## Learning Outcomes

* Understanding the practical application of machine learning models
* Experience in building an interactive application using Streamlit
* Improved knowledge of digital safety and cybersecurity concepts
* Experience in structuring a complete project from idea to implementation

---

## Future Improvements

* Integration of a larger and more realistic dataset
* Use of advanced NLP techniques for phishing detection
* Deployment of the application on a cloud platform
* Improved user interface and data visualization features

---

## Conclusion

This project demonstrates how basic machine learning and logical analysis can be combined to address real-world digital safety concerns. It highlights the importance of awareness and provides a simple tool to help users evaluate and improve their online behavior.
