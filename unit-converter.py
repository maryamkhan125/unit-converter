import streamlit as st

st.title("🌎Unit Converter App")

# Select category
category = st.selectbox("Choose a conversion category:", 
                        ["Length", "Temperature", "Weight"])

# Based on category, show options
if category == "Length":
    options = ["Meter to Kilometer", "Kilometer to Meter"]
elif category == "Temperature":
    options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
elif category == "Weight":
    options = ["Kilogram to Gram", "Gram to Kilogram"]

conversion = st.selectbox("Select conversion type:", options)
value = st.number_input("Enter the value:")

# Convert on button click
if st.button("Convert"):
    result = None
    if conversion == "Meter to Kilometer":
        result = value / 1000
        st.success(f"{value} meters = {result} kilometers")
    elif conversion == "Kilometer to Meter":
        result = value * 1000
        st.success(f"{value} kilometers = {result} meters")
    elif conversion == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
        st.success(f"{value}°C = {result}°F")
    elif conversion == "Fahrenheit to Celsius":
        result = (value - 32) * 5/9
        st.success(f"{value}°F = {result}°C")
    elif conversion == "Kilogram to Gram":
        result = value * 1000
        st.success(f"{value} kg = {result} g")
    elif conversion == "Gram to Kilogram":
        result = value / 1000
        st.success(f"{value} g = {result} kg")

