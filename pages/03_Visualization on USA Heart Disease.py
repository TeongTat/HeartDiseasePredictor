import streamlit as st

st.title("USA Heart Disease Visualization")

# Embed the USA Visualization in the Streamlit app
st.subheader("Visualization on USA Heart Disease example")
# Embed CDC widget using iframe
iframe_code = """
<iframe src="https://tools.cdc.gov/api/v2/resources/media/CountyMapsTemplate?default-state=Alabama&default-dataset=Heart%20Disease"
        width="100%"
        height="700"
        style="border:none;">
</iframe>
"""

st.components.v1.html(iframe_code, height=700, scrolling=True)
