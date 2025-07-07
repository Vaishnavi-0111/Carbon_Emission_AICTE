import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('forecasting_co2_emmision.pkl')

# App title and description
st.title("🌍 CO₂ Emissions Predictor")
st.write("Predict the carbon emissions based on input features and country name")

# Country dropdown
countries = [
    "United States", "China", "India", "Russia", "Germany", "Brazil", 
    "Japan", "Canada", "France", "United Kingdom"
]
country = st.selectbox("Select Country",
                       options= ["United States", "China", "India", "Russia", "Germany", "Brazil", 
                        "Japan", "Canada", "France", "United Kingdom"],
                        index=2 #Default to India
                    )

# Year selector
year = st.selectbox(
    "Select Year for Prediction",
    options=[2020, 2021, 2022, 2023, 2024, 2025],
    index=2  # Default to 2022
)

# Default values for India (can customize for other countries too)
defaults = {
    "India": {
        "cereal_yield": 2.07,
        "gni_per_cap": 2.8,
        "en_per_cap": 3.0,
        "pop_urb_aggl_perc": 34.0,
        "prot_area_perc": 5.43,
        "pop_growth_perc": 1.1,
        "urb_pop_growth_perc": 2.0
    }
}

# Use defaults if available for selected country
cereal_yield = st.number_input(
    "Cereal Yield (tons per hectare)",
    min_value=0.0,
    max_value=10.0,
    value=defaults.get(country, {}).get("cereal_yield", 2.0),
    help="Average cereal production per hectare (e.g., India ≈ 2.1, U.S. ≈ 7.5)"
)

gni_per_cap = st.number_input(
    "GNI per Capita (in $1000 USD)",
    min_value=0.0,
    max_value=100.0,
    value=defaults.get(country, {}).get("gni_per_cap", 10.0),
    help="Gross National Income per capita in thousands of USD (e.g., 2.8 = $2,800)"
)

en_per_cap = st.number_input(
    "Energy per Capita (MWh per person)",
    min_value=0.0,
    max_value=150.0,
    value=defaults.get(country, {}).get("en_per_cap", 5.0),
    help="Average annual energy consumption per person (e.g., India ≈ 3.0)"
)

pop_urb_aggl_perc = st.number_input(
    "Urban Agglomeration Population (%)",
    min_value=0.0,
    max_value=100.0,
    value=defaults.get(country, {}).get("pop_urb_aggl_perc", 50.0),
    help="Percentage of population in urban agglomerations (e.g., India ≈ 34%)"
)

prot_area_perc = st.number_input(
    "Protected Area (% of land area)",
    min_value=0.0,
    max_value=100.0,
    value=defaults.get(country, {}).get("prot_area_perc", 5.0),
    help="Land area under protection (e.g., India ≈ 5.43%)"
)

pop_growth_perc = st.number_input(
    "Population Growth Rate (%)",
    min_value=0.0,
    max_value=10.0,
    value=defaults.get(country, {}).get("pop_growth_perc", 1.0),
    help="Annual population growth rate (e.g., India ≈ 1.1%)"
)

urb_pop_growth_perc = st.number_input(
    "Urban Population Growth Rate (%)",
    min_value=0.0,
    max_value=10.0,
    value=defaults.get(country, {}).get("urb_pop_growth_perc", 2.0),
    help="Annual urban population growth (e.g., India ≈ 2.0%)"
)

# Prediction
if st.button("Predict"):
    input_data = np.array([[cereal_yield, gni_per_cap, en_per_cap, pop_urb_aggl_perc, 
                            prot_area_perc, pop_growth_perc, urb_pop_growth_perc]])
    
    prediction = model.predict(input_data)
    
    st.success(f"🌱 Predicted CO₂ emission for **{country}** in **{year}** is **{prediction[0]:.2f} MtCO₂**")
    st.info("This prediction supports climate-conscious planning using green digital skills.")
