from PIL import Image
import os
import streamlit as st

def process_image_with_gemini(agent, image: Image) -> str:
    prompt = """Analyze this image and extract any coding problem or code snippet shown..."""
    temp_path = "temp_image.png"
    try:
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image.save(temp_path)

        response = agent.run(prompt, images=[{"filepath": temp_path}])
        return response.content
    except Exception as e:
        st.error(f"Errore nell'analisi immagine: {e}")
        return "Failed to process image."
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
