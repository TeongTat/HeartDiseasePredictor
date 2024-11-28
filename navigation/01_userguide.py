import streamlit as st
import requests
import streamlit.components.v1 as components
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import PIL
from PIL import Image

st.tittle("User Guide")

st.write(
  """ This page will gives some idea to user how to fill up """)



  # Load an image from a local file
    image_bp = "Bloodpressure.png"
st.write("Source: https://www.healthline.com/health/blood-pressure-chart")

 # Load an image from a local file
    image_cholesterol = "Cholesterol level.webp"
st.write("Source: https://medicinemarketplace.com/controlling-cholestrol/")

# Load an image from a local file
  image_glucose = "Glucose_level.webp"
st.write("Source: https://www.cmihealth.com/blogs/news/what-your-blood-glucose-test-results-mean-cmi-health-blog")
