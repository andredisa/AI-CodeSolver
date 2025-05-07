import re

def extract_code_from_response(text: str) -> str:
    match = re.search(r"```python\s+([\s\S]+?)```", text)
    if match:
        return match.group(1).strip()
    return "# Nessun codice trovato nel testo."
