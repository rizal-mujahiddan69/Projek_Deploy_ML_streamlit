import numpy as np
import numpy as np
import pickle
import sklearn
import streamlit as st
import time
import warnings

# Disable all warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Deploy Machine", page_icon="⚙️")
st.title("Deploy Machine Learning")

model_data = pickle.load(open("models/model_logreg.pkl", "rb"))

left_col, right_col = st.columns(2)

with left_col:
    input1 = st.number_input("Sepal Length (cm)", min_value=0.001)
    input2 = st.number_input("Sepal Width (cm)", min_value=0.001)
with right_col:
    input3 = st.number_input("Petal Length (cm)", min_value=0.001)
    input4 = st.number_input("Petal Width (cm)", min_value=0.001)

inputan = np.array([input1, input2, input3, input4])
inputan = np.array([inputan])
jawabannya = model_data.predict(inputan)

st.write(f"hasilnya adalah {jawabannya}")

st.button("Re-run")
