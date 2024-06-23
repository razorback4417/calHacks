import os
import streamlit as st
import time
import numpy as np



# Streamlit app layout
# st.set_page_config(initial_sidebar_state="collapsed", page_title="CAD-Eng", page_icon="🖨️", layout="wide")
st.set_page_config(page_title="CAD-Eng", page_icon="🖨️", layout="wide")

import streamlit as st

left_column, right_column = st.columns(2)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }

    .main-title {
        font-size: 2.5em;
        font-weight: bold;
    }

    .sub-title {
        font-size: 1.5em;
        font-weight: normal;
    }

    .description {
        font-size: 16px;
        font-weight: normal;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main content
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("<div class='text-container'>", unsafe_allow_html=True)

with left_column:
    # Title and subtitle
    st.markdown("   ")
    st.markdown("   ")
    st.markdown("<div class='main-title'>Meet CAD-Eng 🖨️</div>", unsafe_allow_html=True)
    st.markdown("   ")
    st.markdown("   ")
    st.markdown("<div class='sub-title'>English to CAD. If you think of something that can be built, we will 3D print it!</div>", unsafe_allow_html=True)
    st.markdown("   ")
    st.markdown("   ")
    st.markdown("   ")

    # Description
    st.markdown("<div class='description'>Use our AI chatbot, Oski, to explain what you need. We will show you a preview before we print it.</div>", unsafe_allow_html=True)
    st.markdown("   ")
    st.markdown("   ")
    st.markdown("   ")
    st.markdown("   ")

    # Get started button
    if st.button("GET STARTED", key='get_started', help='Click to get started'):
        # st.write("Thank you for clicking the Get Started button!")
        st.query_params(page="prompt")
        st.rerun()

# Removed the closing div for the left column (</div>)

with right_column:
    # Image container
    st.markdown("<div class='image-container'>", unsafe_allow_html=True)
    st.image("imagehome.png", caption="App and laptop display")  # Update the image path if necessary
    st.markdown("</div>", unsafe_allow_html=True)  #