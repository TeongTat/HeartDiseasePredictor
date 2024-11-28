import streamlit as st


st.title("Heart Disease Prediction")

st.subheader("This is an example case study using Heart Disease Prediction to create web app")

st.write(
  """ The dataset is obtained from Kaggle: https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset .
  Upon obtaining the data, the data science methodolgy is applied to create the modelling.
  Data cleaning includes null value identification is processed. We added a new column which is BMI as convertion from height and weight from the dataset.
  The following infographic will provide useful information prior using the Heart Disease Preditor""")
