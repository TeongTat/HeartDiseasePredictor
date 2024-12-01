import streamlit as st


st.title("Heart Disease Prediction")

st.subheader("This is a case study using Heart Disease dataset for prediction modelling.")

st.write(
  """ The dataset is obtained from Kaggle: https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset .""")
st.write(
  """Upon obtaining the data, the data science methodolgy is applied to create the modelling.
  - Data cleaning includes null value identification is processed.
  - We added a new column which is BMI as convertion from height and weight from the dataset.
  - On the top left there is " > " which user can click to go to different pages.
  - The pages will provide some guidance and also the prediction for user to use. """)
