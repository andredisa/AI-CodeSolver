import streamlit as st

def execute_code_with_agent(agent, code: str, sandbox) -> str:
    try:
        sandbox.set_timeout(30)
        execution = sandbox.run_code(code)

        if execution.error:
            if "TimeoutException" in str(execution.error):
                return "⚠️ Timeout: codice troppo lento (>30s)."
            response = agent.run(f"L'esecuzione ha dato errore: {execution.error}")
            return f"⚠️ Errore:\n{response.content}"

        files = []
        try:
            files = sandbox.files.list("/")
        except:
            pass

        prompt = f"Logs: {execution.logs}\nFiles: {files}"
        response = agent.run(prompt)
        return response.content
    except Exception as e:
        return f"⚠️ Sandbox Error: {str(e)}"
