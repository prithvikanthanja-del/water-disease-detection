import streamlit as st

st.title("💧 Water-Borne Disease Detection Demo")
st.write("Enter water quality parameters to check if the water is safe for drinking.")

# User inputs
pH = st.number_input("pH Value (6.5 - 8.5 safe range)", min_value=0.0, max_value=14.0, value=7.0)
turbidity = st.number_input("Turbidity (NTU, <=5 safe)", min_value=0.0, value=1.0)
tds = st.number_input("TDS (ppm, <=500 safe)", min_value=0.0, value=100.0)
bacteria = st.number_input("Bacteria Count (CFU/ml, <=100 safe)", min_value=0, value=50)

# Prediction logic
if st.button("Check Water Quality"):
    if (pH < 6.5 or pH > 8.5) or turbidity > 5 or tds > 500 or bacteria > 100:
        st.error("⚠️ Water Contaminated! Possible Disease Risk.")
        if bacteria > 100:
            st.write("→ High bacterial load detected. Possible Cholera/Typhoid risk.")
        if turbidity > 5:
            st.write("→ Turbidity too high. May cause diarrhea-related diseases.")
        st.warning("Suggested Action: Chlorination + Boil water before drinking.")
    else:
        st.success("✅ Water is Safe for Drinking.")
