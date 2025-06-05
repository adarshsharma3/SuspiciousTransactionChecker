# main.py
import streamlit as st
from tab1_analysis import tab1_analyze_excel
from tab2_chat import tab2_chat_ai
from tab3_report import tab3_report_fraud
from tab4_visualize import tab4_visualize_data
# import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
# import google.generativeai as genai





# Configure Gemini with your API key


# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))





# model = genai.GenerativeModel("gemini-2.0-flash")


from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)




st.set_page_config(page_title="Fraud Detection & Chat App")

st.title("💼 Fraud Detection & Gemini Chat")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Upload & Analyze Excel",
    "Chat with Ai Officer",
    "Report via mail",
    "📊 Visualize Transactions"
])

# Tab 1
with tab1:
    tab1_analyze_excel()

# Tab 2
with tab2:
    tab2_chat_ai()

# Tab 3
with tab3:
    tab3_report_fraud()

# Tab 4
with tab4:
    tab4_visualize_data()
