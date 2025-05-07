# core/sandbox.py
import os
from e2b_code_interpreter import Sandbox

def initialize_sandbox():
    if 'e2b_key' in os.environ:
        st.session_state.sandbox = Sandbox(timeout=60)

def execute_code_in_sandbox(code: str) -> dict:
    if not st.session_state.sandbox:
        initialize_sandbox()
    
    execution = st.session_state.sandbox.run_code(code)
    return {
        "logs": execution.logs,
        "files": st.session_state.sandbox.files.list("/")
    }
