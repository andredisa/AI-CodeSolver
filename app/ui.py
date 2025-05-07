from dotenv import load_dotenv
import os

def initialize_session_state():
    load_dotenv()  # carica variabili da .env

    st.session_state.openai_key = os.getenv("OPENAI_API_KEY", "")
    st.session_state.gemini_key = os.getenv("GEMINI_API_KEY", "")
    st.session_state.e2b_key = os.getenv("E2B_API_KEY", "")
    st.session_state.sandbox = None

def setup_sidebar() -> None:
    with st.sidebar:
        st.title("🔧 API Configuration")
        st.session_state.openai_key = st.text_input("🔑 OpenAI API Key", value=st.session_state.openai_key, type="password")
        st.session_state.gemini_key = st.text_input("🔑 Gemini API Key", value=st.session_state.gemini_key, type="password")
        st.session_state.e2b_key = st.text_input("🔑 E2B API Key", value=st.session_state.e2b_key, type="password")
