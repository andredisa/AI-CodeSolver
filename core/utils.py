import os
from dotenv import load_dotenv

def load_api_keys() -> dict:
    """Carica le chiavi API dal file .env"""
    load_dotenv()  # Carica variabili da .env
    api_keys = {
        "openai_key": os.getenv("OPENAI_API_KEY"),
        "gemini_key": os.getenv("GEMINI_API_KEY"),
        "e2b_key": os.getenv("E2B_API_KEY")
    }
    return api_keys

def clean_temp_files(temp_path: str) -> None:
    """Rimuove i file temporanei creati durante l'elaborazione."""
    if os.path.exists(temp_path):
        os.remove(temp_path)

def validate_api_keys(api_keys: dict) -> bool:
    """Verifica che tutte le chiavi API siano presenti."""
    return all(api_keys.values())
