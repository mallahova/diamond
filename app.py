import streamlit as st
import pandas as pd
import numpy as np
import pickle
from xgboost import XGBRegressor


import warnings

warnings.filterwarnings("ignore", category=UserWarning)


with open("model/xgb_model.pkl", "rb") as file:
    model = pickle.load(file)


def predict(carat, cut, color, clarity, table, x, y, z, depth=0.0):
    cut_mapping = {"fair": 0, "good": 1, "very good": 2, "premium": 3, "ideal": 4}
    color_mapping = {"j": 0, "i": 1, "h": 2, "g": 3, "f": 4, "e": 5, "d": 6}
    clarity_mapping = {
        "i1": 0,
        "si2": 1,
        "si1": 2,
        "vs2": 3,
        "vs1": 4,
        "vvs2": 5,
        "vvs1": 6,
        "if": 7,
    }
    if y == 0.0 or x == 0.0 or z == 0.0 or table == 0.0:
        return 0.0
    if depth == 0:
        depth = 2 * z / x + y
    x_test = np.zeros(11)
    x_test[0] = carat
    x_test[1] = cut_mapping[cut]
    x_test[2] = color_mapping[color]
    x_test[3] = clarity_mapping[clarity]
    x_test[4] = depth
    x_test[5] = table
    x_test[6] = x
    x_test[7] = y
    x_test[8] = z
    x_test[9] = table / (x + y)
    x_test[10] = x * y * z
    return round(float(model.predict([x_test])[0]), 2)


col1, col2 = st.columns([2, 1])
with col1:
    st.markdown(
        """
     <style>
     .title {
            margin-top: -9%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h1 class='title'>Diamond Price Prediction</h1>", unsafe_allow_html=True
    )
    st.write(
        "[Kaggle Notebook](https://www.kaggle.com/code/alisamalakhova/diamond-price-prediction-eda-regression-models) | [GitHub](https://github.com/mallahova/diamond)"
    )

with col2:
    st.image("data/diamond.jpg", width=184)


col3, col4 = st.columns([1, 1])
with col3:
    carat = st.number_input("Carat weight", 0.20, 10.01, step=0.15)
    cut = st.selectbox("Cut quality", ["fair", "good", "very good", "premium", "ideal"])
    color = st.selectbox("Color", ["j", "i", "h", "g", "f", "e", "d"])
    clarity = st.selectbox(
        "Clarity", ["i1", "si2", "si1", "vs2", "vs1", "vvs2", "vvs1", "if"]
    )


with col4:
    x = st.number_input("x (length in mm)", 0.20, 20.01, step=0.15)
    y = st.number_input("y (width in mm)", 0.20, 20.01, step=0.15)
    z = st.number_input("z (depth in mm)", 0.20, 20.01, step=0.15)
    table = st.number_input("Table", 0.20, 20.01, step=0.15)
    depth_checked = st.checkbox("Depth (optional)")
    depth = 0
    if depth_checked:
        depth = st.number_input("Depth %", 0.20, 20.01, step=0.15, key="depth")
with col3:
    if st.button("Predict Price", key="predict"):
        predicted_price = predict(carat, cut, color, clarity, table, x, y, z, depth)
        st.write(
            "<strong>Predicted Price:</strong> $" + str(predicted_price),
            unsafe_allow_html=True,
        )
