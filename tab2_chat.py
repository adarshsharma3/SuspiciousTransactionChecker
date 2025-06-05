import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[])

def get_chat_response(user_input):
    prompt = f"""
You are an officer who explains about bank frauds. So whatever is asked, just answer in detail.
Now give an answer of: {user_input}
"""
    return chat.send_message(prompt, stream=True)

def tab2_chat_ai():
    st.header("Know about suspicious patterns & more")
    user_input = st.text_input("Enter your message here:", key="chat_input")
    if st.button("Send", key="send_btn"):
        if user_input.strip():
            with st.spinner("Waiting for response..."):
                response = get_chat_response(user_input)
                for chunk in response:
                    st.write(chunk.text)
