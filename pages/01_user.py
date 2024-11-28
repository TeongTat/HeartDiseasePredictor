import streamlit as st
import requests
import streamlit.components.v1 as components
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import PIL
from PIL import Image

st.title("User Guide")

st.write(
  """ This page will gives guidance to user some information prior to using the Heart Disease Predictor""")


# Embed the Adult BMI Calculator in the Streamlit app
st.subheader("Adult BMI Calculator")
components.iframe("https://www.cdc.gov/bmi/adult-calculator/calculator.html", height=640,scrolling=True)

#write description:
st.write("User can find fill up the information below to obtain the BMI for the predictor.")

# Display the Blood Pressure image and source
st.subheader("Blood Pressure: Showing Systolic and Diastolic")
image_path_bp = "bloodpressure.jpg"
st.image(Image.open(image_path_bp), caption="Blood Pressure Chart", use_column_width=True)
st.write("Source: [Heart Org](https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings)")


# Display the Cholesterol Level image and source
st.subheader("Cholesterol Level")
image_path_chol = "Cholesterol level.webp"
st.image(Image.open(image_path_chol), caption="Cholesterol Level Chart", use_column_width=True)
st.write("Source: [Medicine Marketplace](https://medicinemarketplace.com/controlling-cholestrol/)")
/
/
st.write("Level 1:Normal, Level 2:Borderline, Level 3: High")

# Display the Glucose Level image and source
image_path_glucose = "Glucose_level.webp"
st.image(Image.open(image_path_glucose), caption="Glucose Level Chart", use_column_width=True)
st.write("Source: [CMI Health](https://www.cmihealth.com/blogs/news/what-your-blood-glucose-test-results-mean-cmi-health-blog)")
/
/
st.write("Level 1:Normal, Level 2:Borderline, Level 3: High")
