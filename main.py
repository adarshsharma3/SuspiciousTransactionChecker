from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import pandas as pd
import google.generativeai as genai

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[])

def analyze_transactions(df):
    csv_data = df.to_csv(index=False)
    prompt = f"""
You are a forensic financial analyst. The following is a CSV of transaction data:

{csv_data[:15000]}  # Limit large data input, chunk if needed

Please identify if the following patterns are present:
1. matched_credit_debit_same_day
2. find_daisy_chains
3. detect_mule_setups
4. ind_similar_narrations_across_accounts
5. matched_credit_debit_ignore_date

Give your analysis in a concise way.
"""
    response = chat.send_message(prompt, stream=True)
    return response

def get_chat_response(user_input):
    response = chat.send_message(user_input, stream=True)
    return response

st.set_page_config(page_title="Fraud Detection & Chat App")

st.title("💼 Fraud Detection & Gemini Chat")

tab1, tab2 = st.tabs(["Upload & Analyze Excel", "Chat with Gemini"])

with tab1:
    st.header("Upload Excel & Analyze Fraud Patterns")
    uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)
            st.write("Preview of Uploaded Transactions:")
            st.dataframe(df.head())

            if st.button("Analyze for Fraud Patterns"):
                with st.spinner("Analyzing..."):
                    response = analyze_transactions(df)
                    st.subheader("🧠 Gemini's Analysis")
                    for chunk in response:
                        st.write(chunk.text)
        except Exception as e:
            st.error(f"Error reading file: {e}")

with tab2:
    st.header("Know about suspicious patterns &  more")
    user_input = st.text_input("Enter your message here:", key="chat_input")
    if st.button("Send", key="send_btn"):
        if user_input.strip() != "":
            with st.spinner("Waiting for response..."):
                response = get_chat_response(user_input)
                for chunk in response:
                    st.write(chunk.text)
