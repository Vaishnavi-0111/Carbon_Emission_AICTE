import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('forecasting_co2_emmision.pkl')

st.title("🌍 CO₂ Emissions Forecasting App")
st.write("Predict the carbon emissions based on input features and country name")

# Country dropdown
countries = [
    "United States", "China", "India", "Russia", "Germany", "Brazil", 
    "Japan", "Canada", "France", "United Kingdom"
]
country = st.selectbox("Select Country", countries)

# Input features
cereal_yield = st.number_input("Cereal Yield (e.g. 1.2)", 0.0, 10.0)
gni_per_cap = st.number_input("GNI per Cap (e.g. 2.5)", 0.0, 10.0)
en_per_cap = st.number_input("Energy per Capita (e.g. 3.0)", 0.0, 10.0)
pop_urb_aggl_perc = st.number_input("Urban Agglomeration Population (%)", 0.0, 100.0)
prot_area_perc = st.number_input("Protected Area (%)", 0.0, 100.0)
pop_growth_perc = st.number_input("Population Growth (%)", 0.0, 100.0)
urb_pop_growth_perc = st.number_input("Urban Population Growth (%)", 0.0, 100.0)

# Prediction trigger
if st.button("Predict"):
    input_data = np.array([[cereal_yield, gni_per_cap, en_per_cap, pop_urb_aggl_perc, 
                            prot_area_perc, pop_growth_perc, urb_pop_growth_perc]])
    
    prediction = model.predict(input_data)
    
    st.success(f"🌱 Predicted CO₂ emission for **{country}** is **{prediction[0]:.2f} MtCO₂**")
