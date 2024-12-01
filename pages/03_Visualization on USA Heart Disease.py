import streamlit as st

st.title("USA Heart Disease Visualization")

# Embed the USA Visualization in the Streamlit app
st.subheader("Visualization on USA Heart Disease example")
cdc_widget_code = """
<div data-cdc-widget="CountyMaps" data-instance-name="HeartDiseaseAndStroke"></div>
<br/>
<script src="https://tools.cdc.gov/1M1B"></script>
"""

# Use st.components.v1.html to render the widget
st.components.v1.html(cdc_widget_code, height=600, scrolling=True)
