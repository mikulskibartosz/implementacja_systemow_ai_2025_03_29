import streamlit as st
import requests


API_URL = "http://localhost:3000/predict"

st.title("Klasyfikator irysów")

st.image("iris.png", caption="https://www.embedded-robotics.com/iris-dataset-classification/")

with st.form("iris_form"):
    sepal_length = st.slider("Długość działki kielicha", min_value=4.0, max_value=8.0, value=5.8, step=0.1)
    sepal_width = st.slider("Szerokość działki kielicha", min_value=2.0, max_value=5.0, value=3.0, step=0.1)
    petal_length = st.slider("Długość płatka", min_value=1.0, max_value=7.0, value=3.7, step=0.1)
    petal_width = st.slider("Szerokość płatka", min_value=0.1, max_value=2.5, value=1.2, step=0.1)

    submit_button = st.form_submit_button("Przewiduj")

if submit_button:
    data = {"features": {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }}

    with st.spinner("Przewiduję..."):
        try:
            response = requests.post(API_URL, json=data)
            result = response.json()
            st.success(f"Przewidziano: {result['species']}")
        except Exception as e:
            st.error(f"Wystąpił błąd: {e}")
