import streamlit as st

st.title("Visualization on Cardiovascular in World 1950-2022")

st.subheader("Since obtaining data on specifically on Heart Disease are not easy, heart related visualization are obtained to show the trends over the years.")

st.write(
"""According to Harvard Health (31 July 2023), "Cardio" refers to the heart, and "vascular" refers to all the blood vessels in the body. In comparison, heart disease is more specific and refers only to diseases of the heart,
such as coronary artery disease, heart failure, heart valve abnormalities, and abnormal heart rhythms.""")

# Define the iframe code
iframe_code = '<iframe src="https://ourworldindata.org/grapher/cardiovascular-disease-death-rate-males-vs-females?time=2022&tab=chart" loading="lazy" style="width: 100%; height: 600px; border: 0px none;" allow="web-share; clipboard-write"></iframe>'

# Display the iframe
st.components.v1.html(iframe_code, width=800, height=600)

