import streamlit as st
import pandas as pd
import joblib

# 1. Set page configuration
st.set_page_config(page_title="CO2 Emissions Predictor", layout="centered")

# 2. Load the pre-trained model with caching to prevent reloading on every run
@st.cache_resource
def load_model():
    return joblib.load('co2_emission_model.pkl')

model = load_model()

# 3. Application Heading
st.title("🚗 Vehicle CO2 Emissions Predictor")
st.write("""
This interactive application uses a Multiple Linear Regression model to predict a vehicle's 
CO2 emissions based on its engine parameters and fuel consumption metrics.
""")

st.markdown("---")

# 4. Create Sidebar Input Controls for Features
st.sidebar.header("🔧 Modify Vehicle Parameters")

engine_size = st.sidebar.slider("Engine Size (L)", min_value=0.9, max_value=8.4, value=2.0, step=0.1)
cylinders = st.sidebar.slider("Cylinders", min_value=3, max_value=16, value=4, step=1)
fuel_city = st.sidebar.number_input("Fuel Consumption City (L/100 km)", min_value=4.0, max_value=31.0, value=10.0, step=0.1)
fuel_hwy = st.sidebar.number_input("Fuel Consumption Hwy (L/100 km)", min_value=4.0, max_value=21.0, value=7.5, step=0.1)
fuel_comb_l = st.sidebar.number_input("Fuel Consumption Comb (L/100 km)", min_value=4.0, max_value=27.0, value=8.5, step=0.1)
fuel_comb_mpg = st.sidebar.slider("Fuel Consumption Comb (mpg)", min_value=11, max_value=69, value=33, step=1)

# 5. Compile inputs into a DataFrame matching your model's exact column names
input_features = pd.DataFrame({
    'Engine Size(L)': [engine_size],
    'Cylinders': [cylinders],
    'Fuel Consumption City (L/100 km)': [fuel_city],
    'Fuel Consumption Hwy (L/100 km)': [fuel_hwy],
    'Fuel Consumption Comb (L/100 km)': [fuel_comb_l],
    'Fuel Consumption Comb (mpg)': [fuel_comb_mpg]
})

# 6. Display User Selections
st.subheader("Selected Vehicle Configuration")
st.dataframe(input_features, hide_index=True)

# 7. Automated or Button-triggered Predictions
st.markdown("### Prediction Result")

# Streamlit updates automatically when sliders change, making this real-time!
try:
    prediction = model.predict(input_features)
    predicted_value = max(0.0, prediction[0]) # Clip negative values if they occur on extreme inputs
    
    st.success(f"💨 **Estimated CO2 Emissions:** `{predicted_value:.2f}` g/km")
    
    # Optional Visual indicator
    if predicted_value < 150:
        st.info("☘️ This vehicle has relatively low carbon emissions.")
    elif predicted_value < 250:
        st.warning("⚠️ This vehicle has moderate carbon emissions.")
    else:
        st.error("🚨 This vehicle has heavy carbon emissions.")
        
except Exception as e:
    st.error(f"An error occurred during prediction: {e}")