import streamlit as st
import pandas as pd
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[])

def analyze_transactions(df, selected_patterns="", Additional_info=""):
    csv_data = df.to_csv(index=False)
    patterns_text = ", ".join(selected_patterns) if selected_patterns else ""
    note_text = f"\nPattern you must focus on :\n{patterns_text}\n" if patterns_text else ""

    pattern_checklist = "" if selected_patterns else """
Please identify if the following patterns are present:
1. matched_credit_debit_same_day
2. find_daisy_chains
3. detect_mule_setups
4. ind_similar_narrations_across_accounts
5. matched_credit_debit_ignore_date
"""

    prompt = f"""
You are a forensic financial analyst. The following is a CSV of transaction data:

{csv_data[:15000]}

{note_text}
{pattern_checklist}
{Additional_info}
Give your analysis in a concise way.
"""
    return chat.send_message(prompt, stream=True)

def tab1_analyze_excel():
    st.header("Upload Excel & Analyze Fraud Patterns")
    uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])
    selected_patterns = st.multiselect(
        "Choose fraud patterns to check:",
        [
            "matched_credit_debit_same_day",
            "find_daisy_chains",
            "detect_mule_setups",
            "ind_similar_narrations_across_accounts",
            "matched_credit_debit_ignore_date"
        ]
    )
    Additional_info = st.text_area("Optional: Add any context or concerns you want Gemini to focus on")
    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)
            st.write("Preview of Uploaded Transactions:")
            st.dataframe(df.head())
            if st.button("Analyze for Fraud Patterns"):
                with st.spinner("Analyzing..."):
                    response = analyze_transactions(df, selected_patterns, Additional_info)
                    st.subheader("🧠 AI Agent's Analysis")
                    for chunk in response:
                        st.write(chunk.text)
        except Exception as e:
            st.error(f"Error reading file: {e}")
