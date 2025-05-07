# core/vision.py
from PIL import Image

def process_image_with_gemini(vision_agent, image: Image) -> str:
    prompt = """Analyze this image and extract any coding problem or code snippet shown. 
    Describe it in clear natural language, including any:
    1. Problem statement
    2. Input/output examples
    3. Constraints or requirements
    Format it as a proper coding problem description."""

    temp_path = "temp_image.png"
    try:
        image.save(temp_path, format="PNG")
        response = vision_agent.run(prompt, images=[{"filepath": temp_path}])
        return response.content
    except Exception as e:
        return f"Error processing image: {str(e)}"
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
