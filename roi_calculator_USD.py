
import streamlit as st

def calculate_roi(investment_cost, tangible_benefits, intangible_benefits):
    # Calculate total tangible benefits
    total_tangible_benefits = sum(tangible_benefits.values())
    
    # Calculate adjusted intangible benefits
    adjusted_intangible_benefits = sum(value * (confidence / 100) for value, confidence in intangible_benefits.values())
    
    # Calculate risk-adjusted benefits
    risk_adjusted_benefits = total_tangible_benefits + adjusted_intangible_benefits
    
    # Calculate ROI
    roi = ((risk_adjusted_benefits - investment_cost) / investment_cost) * 100
    
    return total_tangible_benefits, adjusted_intangible_benefits, risk_adjusted_benefits, roi

# Streamlit app
st.title("ROI Calculator")

# Input investment cost
investment_cost = st.number_input("Investment Cost (USD)", min_value=0.0, step=1000.0)

# Input tangible benefits
st.header("Tangible Benefits")
tangible_benefits = {}
num_tangible = st.number_input("Number of Tangible Benefits", min_value=1, step=1)
for i in range(num_tangible):
    name = st.text_input(f"Tangible Benefit {i+1} Name")
    value = st.number_input(f"Tangible Benefit {i+1} Value (USD)", min_value=0.0, step=1000.0)
    tangible_benefits[name] = value

# Input intangible benefits
st.header("Intangible Benefits")
intangible_benefits = {}
num_intangible = st.number_input("Number of Intangible Benefits", min_value=1, step=1)
for i in range(num_intangible):
    name = st.text_input(f"Intangible Benefit {i+1} Name")
    value = st.number_input(f"Intangible Benefit {i+1} Value (USD)", min_value=0.0, step=1000.0)
    confidence = st.slider(f"Intangible Benefit {i+1} Confidence Level (%)", min_value=0, max_value=100, step=1)
    intangible_benefits[name] = (value, confidence)

# Calculate ROI
if st.button("Calculate ROI"):
    total_tangible_benefits, adjusted_intangible_benefits, risk_adjusted_benefits, roi = calculate_roi(investment_cost, tangible_benefits, intangible_benefits)
    
    st.subheader("Results")
    st.write(f"Total Tangible Benefits: {total_tangible_benefits} USD")
    st.write(f"Adjusted Intangible Benefits: {adjusted_intangible_benefits} USD")
    st.write(f"Risk-Adjusted Benefits: {risk_adjusted_benefits} USD")
    st.write(f"ROI: {roi:.2f}%")
