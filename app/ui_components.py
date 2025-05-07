# app/ui_components.py
import streamlit as st

def setup_sidebar():
    with st.sidebar:
        st.title("API Configuration")
        st.session_state.openai_key = st.text_input("OpenAI API Key", type="password")
        st.session_state.gemini_key = st.text_input("Gemini API Key", type="password")
        st.session_state.e2b_key = st.text_input("E2B API Key", type="password")
