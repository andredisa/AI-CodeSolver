import streamlit as st
from PIL import Image
from agents.factory import create_agents
from agents.vision import process_image_with_gemini
from agents.execution import execute_code_with_agent
from utils.sandbox_utils import initialize_sandbox
from utils.helpers import extract_code_from_response
from app.ui import setup_sidebar, initialize_session_state

def main():
    st.title("🧠 AI Code Solver")

    initialize_session_state()
    setup_sidebar()

    if not (st.session_state.openai_key and 
            st.session_state.gemini_key and 
            st.session_state.e2b_key):
        st.warning("🔐 Inserisci tutte le chiavi API nella sidebar.")
        return

    vision_agent, coding_agent, execution_agent = create_agents()

    uploaded_image = st.file_uploader("📷 Carica un'immagine del problema (opzionale)", type=['png', 'jpg', 'jpeg'])
    if uploaded_image:
        st.image(uploaded_image, caption="Immagine caricata", use_container_width=True)

    user_query = st.text_area("✍️ Oppure scrivi il problema qui:", height=100)

    if st.button("✅ Genera ed Esegui"):
        if uploaded_image and not user_query:
            with st.spinner("Estrazione dal contenuto dell'immagine..."):
                image = Image.open(uploaded_image)
                extracted_query = process_image_with_gemini(vision_agent, image)

                if extracted_query.startswith("Failed"):
                    st.error(extracted_query)
                    return

                st.info("📝 Problema Estratto:")
                st.write(extracted_query)

                with st.spinner("Generazione soluzione..."):
                    response = coding_agent.run(extracted_query)

        elif user_query and not uploaded_image:
            with st.spinner("Generazione soluzione..."):
                response = coding_agent.run(user_query)

        elif user_query and uploaded_image:
            st.error("⚠️ Usa solo testo OPPURE immagine, non entrambi.")
            return
        else:
            st.warning("📩 Fornisci un'immagine o un problema testuale.")
            return

        if 'response' in locals():
            st.subheader("💻 Soluzione Generata")
            code = extract_code_from_response(response.content)
            st.code(code, language="python")

            initialize_sandbox()
            if st.session_state.sandbox:
                with st.spinner("Esecuzione del codice..."):
                    execution_results = execute_code_with_agent(
                        execution_agent, code, st.session_state.sandbox
                    )
                st.subheader("🚀 Risultati Esecuzione")
                st.markdown(execution_results)

if __name__ == "__main__":
    main()
