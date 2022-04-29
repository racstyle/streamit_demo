import streamlit as st
import demo_1
import demo_2_page_1
import demo_2_page_2

# Some configurations for Streamlit
st.set_page_config(page_title="Streamlit Demo", layout="wide")

# This appears in each page
st.info("Hello, welcome to my Streamlit demo!  This demo will show the basics of Streamlit.")

# This appears only in the sidebar
st.sidebar.header("Hi there, choose a page where you want to go:")

# Nav options
pages = {
    "Demo 1 - Basics": demo_1,
    "Demo 2 - Statefulness, Page 1": demo_2_page_1,
    "Demo 2 - Statefulness, Page 2": demo_2_page_2
}

# Navigation radios, appear in the sidebar
nav = st.sidebar.radio(label="", options=pages)     # nav buttons
pages[nav].app()    # call the selected page's app() function

# See the code!
st.sidebar.info("You can see the code in my [GitHub repo](https://github.com/racstyle/streamlit_demo)!")