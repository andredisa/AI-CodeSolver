import os
import streamlit as st
from e2b_code_interpreter import Sandbox

def initialize_sandbox():
    try:
        if st.session_state.sandbox:
            try:
                st.session_state.sandbox.close()
            except:
                pass
        os.environ['E2B_API_KEY'] = st.session_state.e2b_key
        st.session_state.sandbox = Sandbox(timeout=60)
    except Exception as e:
        st.error(f"Errore inizializzazione sandbox: {str(e)}")
        st.session_state.sandbox = None
