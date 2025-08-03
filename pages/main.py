import streamlit as st
import random
import time
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logics.user_query_handler import response_generator_from_crewai

st.title("StressLess Bot 🧘🏻‍♂️😌🍃 - Your Work Wellness Chatbot")

st.markdown("""
Welcome to the **StressLess Bot**!  
You can use this chatbot if you are feeling down at work, or if you need guidance on how to approach mental health in the workplace! 
""")

#initialise chat history - session_state helps to store data persistently across reruns of the app (like chat history)
if "messages" not in st.session_state:
    st.session_state.messages = []

#display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    #display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    #display and capture assistant response
    with st.chat_message("assistant"):
        full_response = ""
        response_stream = response_generator_from_crewai(prompt)
        for chunk in st.write_stream(response_stream):
            full_response += chunk

    #add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
