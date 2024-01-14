import streamlit as st

def model_page():
    st.write("#### Upload chest x-ray image here...")
    uploaded_file = st.file_uploader("Upload chest x-ray image here...", type=["jpg", "png", "jpeg"], label_visibility="hidden")
    if uploaded_file:
        predict_button = st.button("ㅤㅤPredictㅤㅤ")
        if predict_button:
            st.error("No models found!")