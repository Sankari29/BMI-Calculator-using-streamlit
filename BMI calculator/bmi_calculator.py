import streamlit as st

# Title
st.title("BMI Calculator")

# Gender Selection
gender = st.radio("Select your gender:", ("Male", "Female"))

# Input fields
weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (cm)", min_value=1.0, format="%.2f")

# BMI Calculation
if height > 0:
    bmi = weight / ((height / 100) ** 2)
    st.write(f"### Your BMI: {bmi:.2f}")

    # Categorization based on gender
    if gender == "Male":
        if bmi < 18.5:
            st.warning("Underweight 🏃‍♂️")
        elif 18.5 <= bmi < 24.9:
            st.success("Normal weight ✅")
        elif 25 <= bmi < 29.9:
            st.warning("Overweight ⚠️")
        else:
            st.error("Obese ❌")

    elif gender == "Female":
        if bmi < 18.0:
            st.warning("Underweight 🏃‍♀️")
        elif 18.0 <= bmi < 23.9:
            st.success("Normal weight ✅")
        elif 24 <= bmi < 28.9:
            st.warning("Overweight ⚠️")
        else:
            st.error("Obese ❌")

# Run the app using: streamlit run bmi_calculator.py
