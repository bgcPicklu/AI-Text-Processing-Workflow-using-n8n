import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/process"

st.title("AI Text Processing Workflow")

email = st.text_input("Enter Email")
text = st.text_area("Enter Text")

if st.button("Submit"):

    if not email or not text:
        st.warning("Please fill all fields")
    else:
        payload = {
            "email": email,
            "text": text
        }

        try:
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                st.success("Workflow triggered successfully")
                st.json(response.json())
            else:
                st.error("Request failed")
                st.write(response.text)

        except Exception as e:
            st.error(str(e))