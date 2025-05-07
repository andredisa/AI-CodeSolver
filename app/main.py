# app/main.py
import streamlit as st
from core.agent import create_agents
from core.execution import execute_code_with_agent
from core.vision import process_image_with_gemini
from core.sandbox import initialize_sandbox
from PIL import Image

def main():
    st.title("AI-CodeSolver")

    # Initialize session state
    initialize_session_state()

    # Sidebar setup for API keys
    setup_sidebar()

    vision_agent, coding_agent, execution_agent = create_agents()

    uploaded_image = st.file_uploader("Upload an image of your coding problem (optional)", type=["png", "jpg", "jpeg"])

    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

    user_query = st.text_area("Or type your coding problem here:", placeholder="Example: Write a function to find the sum of two numbers.")

    if st.button("Generate & Execute Solution"):
        if uploaded_image and not user_query:
            with st.spinner("Processing image..."):
                image = Image.open(uploaded_image)
                extracted_query = process_image_with_gemini(vision_agent, image)

                if extracted_query.startswith("Failed"):
                    st.error(extracted_query)
                    return

                st.info("📝 Extracted Problem:")
                st.write(extracted_query)

                with st.spinner("Generating solution..."):
                    response = coding_agent.run(extracted_query)

        elif user_query and not uploaded_image:
            with st.spinner("Generating solution..."):
                response = coding_agent.run(user_query)

        elif user_query and uploaded_image:
            st.error("Please use either image upload OR text input, not both.")
            return
        else:
            st.warning("Please provide either an image or text description of your coding problem.")
            return

        if 'response' in locals():
            st.divider()
            st.subheader("💻 Solution")

            code_blocks = response.content.split("```python")
            if len(code_blocks) > 1:
                code = code_blocks[1].split("```")[0].strip()

                st.code(code, language="python")

                with st.spinner("Executing code..."):
                    initialize_sandbox()
                    if st.session_state.sandbox:
                        execution_results = execute_code_with_agent(execution_agent, code, st.session_state.sandbox)
                        st.divider()
                        st.subheader("🚀 Execution Results")
                        st.markdown(execution_results)

if __name__ == "__main__":
    main()
