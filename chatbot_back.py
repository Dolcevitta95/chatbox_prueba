import openai

# Configuración de la clave de API
openai.api_key = "3hLIllIcCvKwYGkndjpvpBF1xj27Bc6ofRlKwAMFQXcu9cmUWFFTJQQJ99BAACHYHv6XJ3w3AAAAACOGljs3"  # Reemplaza con tu clave de Azure OpenAI

# Función para interactuar con el modelo GPT
def generar_respuesta(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # O el modelo configurado en tu recurso de Azure
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error al generar respuesta: {e}"
