import streamlit as st
import requests
import numpy as np

url = "http://localhost:8000/email_classification"

############ 2. SETTING UP THE PAGE LAYOUT AND TITLE ############

# `st.set_page_config` is used to display the default layout width, the title of the app, and the emoticon in the browser tab.

if "classification" not in st.session_state:
    st.session_state['classification']  = "None"

st.set_page_config(
    layout="centered", page_title="Zero-Shot Text Classifier", page_icon="❄️"
)

############ CREATE THE LOGO AND HEADING ############

# We create a set of columns to display the logo and the heading next to each other.


def predict(text):
    
    headers = {
    'accept': 'application/json',
    'correlation-id': 'sdskgdsflkdfl',
    'Content-Type': 'application/x-www-form-urlencoded',}

    data = {
        'text': text,
        'token': '4555dfddgdgdgf666',
    }

    response = requests.post(url, headers=headers, data=data)
    
    result = response.json()
    st.session_state.classification = result['classification']
    return  result['classification']
    



c1, c2 = st.columns([0.32, 2])

# The snowflake logo will be displayed in the first column, on the left.

with c1:

    st.image(
        "images/logo.png",
        width=85,
    )


# The heading will be on the right.

with c2:

    st.caption("")
    st.title("Email Text Classifier")

    with st.form("my_form"):
        label_text = st.text_area("Enter Email text for classification", value="", label_visibility="visible")
        classifcation = st.form_submit_button(label="Submit",)
        if classifcation:
            print(label_text)
            classes = predict(label_text)
            print("outs",classes)
            st.write(f"Classification : {classes}")

