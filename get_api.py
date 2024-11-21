import streamlit as st
import os

# Function to get api key from user if not already set
@st.dialog("Enter Your API Key")
def get_api():
    nvidia = st.text_input("NVIDIA API Key", type="password", help="Your API key remains secure and is not saved.")
    st.markdown("[Create your NVIDIA API Key](https://build.nvidia.com/meta/llama-3_1-70b-instruct)", unsafe_allow_html=True)

    if st.button("Submit"):
        if nvidia:
            st.session_state["NVIDIA_API_KEY"] = nvidia
            st.success("API key set successfully!")
            st.rerun()
        else:
            st.error("API key cannot be empty.")