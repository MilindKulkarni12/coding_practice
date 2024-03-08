import os
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI

API_KEY = os.environ.get('OPENAI_API_KEY')
llm = OpenAI(api_token=API_KEY)

st.title("File Analyser with Pandas AI")
uploaded_file = st.file_uploader("Upload a file for analysis", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    sdf = SmartDataframe(df, config= {'llm': llm})
    st.write(df.head())

    prompt = st.text_area("Enter Prompt")
    if st.button("Submit"):
        if prompt:
            st.write("PandasAI is generating answer...")
            st.write(sdf.chat(prompt))
        else:
            st.warning("Please enter a prompt.")

