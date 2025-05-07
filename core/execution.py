# core/execution.py
from core.sandbox import Sandbox

def execute_code_with_agent(execution_agent, code, sandbox):
    sandbox.set_timeout(30)
    execution = sandbox.run_code(code)

    if execution.error:
        return f"⚠️ Execution Error: {execution.error}"
    
    return execution.logs
