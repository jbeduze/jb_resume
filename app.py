import streamlit as st

image_path = "sidebarimg.png"

# Convert the image to base64
base64_image = get_base64_image(image_path)

# Create CSS to set the sidebar background
sidebar_style = f"""
<style>
[data-testid="stSidebar"] {{
    background-image: url("data:image/png;base64,{base64_image}");
    background-size: cover;
}}
</style>
"""

# Apply the CSS
st.markdown(sidebar_style, unsafe_allow_html=True)

# Rest of your app
st.title("My Streamlit App")
st.write("This is an example of setting a sidebar background image.")

