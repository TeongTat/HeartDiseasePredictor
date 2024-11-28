import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

st.title("Heart Disease Prediction")

st.subheader("User can use the predictor based on Gradient Boosting Regressor to predict their Heart Disease")


# Load your dataset
data = pd.read_csv('ML_Deployment.csv')
data_frame = pd.DataFrame(data)


# Feature columns
features = ['age', 'gender', 'bmi', 'systolic_bp', 'diastolic_bp', 'cholesterol', 'glucose', 'smoke', 'alco', 'active']
target = 'cardio'

# Split the data
X = data_frame[features]
y = data_frame[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Standardize the data
scaler = StandardScaler()
scaler.fit(X_train)

# Save the model and scaler (optional, if you want to reuse them later)
with open('final_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)



# Collect user input
age = st.number_input("Enter Patient Age:", min_value=0, max_value=120, step=1, value=30)
gender = st.selectbox("Enter Patient Gender:", options=[0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
bmi = st.number_input("Enter Patient BMI:", min_value=0.0, max_value=100.0, step=0.1, value=22.0)
systolic_bp = st.number_input("Enter Patient Systolic BP:", min_value=0, max_value=300, step=1, value=120)
diastolic_bp = st.number_input("Enter Patient Diastolic BP:", min_value=0, max_value=200, step=1, value=80)
st.write('For cholesterol and glucose level: Level-1 = 1(normal), Level-2 = 2(above normal), Level-3 = 3(high)')
cholesterol = st.selectbox("Enter Patient Cholesterol Level:", options=[1, 2, 3], format_func=lambda x: f"Level-{x}")
glucose = st.selectbox("Enter Patient Glucose Level:", options=[1, 2, 3], format_func=lambda x: f"Level-{x}")
smoke = st.selectbox("Does Patient Smoke?", options=[0, 1], format_func=lambda x: "Non-Smoker" if x == 0 else "Smoker")
alco = st.selectbox("Enter Patient Alcoholic:", options=[0, 1], format_func=lambda x: "Non-Alcoholic" if x == 0 else "Alcoholic")
active = st.selectbox("Enter Patient Activity Level:", options=[0, 1], format_func=lambda x: "Non-Active" if x == 0 else "Active")

# Prepare input data
val = np.array([[age, gender, bmi, systolic_bp, diastolic_bp, cholesterol, glucose, smoke, alco, active]])
val_scaled = scaler.transform(val)

# Predict and display the result
if st.button("Predict"):
    result = model.predict(val_scaled)[0]
    
    if result == 0:  # Assuming 0.5 is the threshold for classification
        st.success("Good News! The patient is unlikely to suffer from cardiac disease.")
    else:
        st.error("Bad News! The patient is likely to suffer from cardiac disease.")
