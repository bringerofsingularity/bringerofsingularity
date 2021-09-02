# Configure the main page by setting its title and icon that will be displayed in a browser tab.
# Import the streamlit Python module.
import streamlit as st
# Configure your home page.

st.set_page_config(page_title = "Census Visualisation Web App", page_icon = ":car:", layout = "centered", initial_sidebar_state = "auto")
# Set the title to the home page contents.
st.title("Census Visuealisation Web App")
# Provide a brief description for the web app.
st.subheader("This web app allows a user to explore and visualise the census data")