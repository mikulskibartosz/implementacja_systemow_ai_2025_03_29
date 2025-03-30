import streamlit as st
import requests
import json
import pandas as pd

API_URL = "http://localhost:3000/predict"

st.title("Klasyfikator Pingwinów")

penguin_images = {
    "Adelie": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Hope_Bay-2016-Trinity_Peninsula%E2%80%93Ad%C3%A9lie_penguin_%28Pygoscelis_adeliae%29_04.jpg/960px-Hope_Bay-2016-Trinity_Peninsula%E2%80%93Ad%C3%A9lie_penguin_%28Pygoscelis_adeliae%29_04.jpg",
    "Gentoo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Brown_Bluff-2016-Tabarin_Peninsula%E2%80%93Gentoo_penguin_%28Pygoscelis_papua%29_03.jpg/1202px-Brown_Bluff-2016-Tabarin_Peninsula%E2%80%93Gentoo_penguin_%28Pygoscelis_papua%29_03.jpg",
    "Chinstrap": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_%28Pygoscelis_antarctica%29_04.jpg/440px-South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_%28Pygoscelis_antarctica%29_04.jpg"
}

with st.form("penguin_form"):
    st.subheader("Wprowadź cechy pingwina")

    col1, col2 = st.columns(2)

    with col1:
        culmen_length_mm = st.slider("Długość dzioba (mm)", 30, 60, 45)
        culmen_depth_mm = st.slider("Głębokość dzioba (mm)", 10, 25, 17)

    with col2:
        flipper_length_mm = st.slider("Długość płetwy (mm)", 170, 240, 200)
        body_mass_g = st.slider("Masa ciała (g)", 2500, 6500, 4000)

    sex = st.selectbox("Płeć", ["Samiec", "Samica"])

    sex_mapping = {"Samiec": "MALE", "Samica": "FEMALE"}
    sex = sex_mapping[sex]
    island = st.selectbox("Wyspa", ["Torgersen", "Biscoe", "Dream"])

    submit = st.form_submit_button("Przewidź gatunek")

if submit:
    data = {
        "penguin_features": {
            "culmen_length_mm": culmen_length_mm,
            "culmen_depth_mm": culmen_depth_mm,
            "flipper_length_mm": flipper_length_mm,
            "body_mass_g": body_mass_g,
            "sex": sex,
            "island": island
        }
    }

    with st.spinner("Przetwarzanie..."):
        try:
            response = requests.post(API_URL, json=data)

            if response.status_code == 200:
                result = response.json()
                species = result.get('species')

                st.success(f"Gatunek: {species}")

                if species in penguin_images:
                    st.image(penguin_images[species], caption=f"Pingwin {species}", width=400)
                else:
                    st.warning("Nie znaleziono zdjęcia dla tego gatunku.")
            else:
                st.error(f"Błąd API: {response.status_code} - {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("Błąd połączenia: Sprawdź czy serwer API działa")
        except requests.exceptions.Timeout:
            st.error("Timeout: Serwer nie odpowiada")
        except Exception as e:
            st.error(f"Błąd: {e}")
