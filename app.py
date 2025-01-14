import streamlit as st
from chatbot_backend import generar_respuesta

# Configuración de la página de Streamlit
st.set_page_config(page_title="Chatbot con Azure OpenAI", page_icon="🤖")

# Título
st.title("🤖 Chatbot con Azure OpenAI")
st.write("Interactúa con un chatbot basado en los modelos de Azure OpenAI GPT.")

# Área de entrada de usuario
user_input = st.text_input("Escribe tu mensaje aquí:", placeholder="Hola, ¿cómo puedo ayudarte?")

# Respuesta del chatbot
if st.button("Enviar"):
    if user_input.strip() == "":
        st.warning("Por favor, escribe un mensaje antes de enviar.")
    else:
        with st.spinner("Generando respuesta..."):
            respuesta = generar_respuesta(user_input)
        st.success("Respuesta generada:")
        st.write(respuesta)

# Nota al pie
st.markdown("---")
st.markdown("Desarrollado con ❤️ usando [Azure OpenAI](https://azure.microsoft.com/) y Streamlit.")
