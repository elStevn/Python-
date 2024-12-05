# Chatbot básico
def chatbot():
    print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte?")
    print("Escribe 'salir' para terminar la conversación.")

    # Diccionario de respuestas predeterminadas
    respuestas = {
        "hola": "¡Hola! ¿Cómo estás?",
        "cómo estás": "Estoy aquí para ayudarte, ¿y tú?",
        "adiós": "¡Adiós! Que tengas un buen día.",
        "tu nombre": "Soy un chatbot simple creado en Python.",
        "gracias": "¡De nada! ¿Hay algo más en lo que pueda ayudarte?",
        "qué puedes hacer": "Puedo responder preguntas simples, ¡pruébalo!"
    }

    while True:
        # Entrada del usuario
        mensaje = input("\nTú: ").lower()

        if mensaje == "salir":
            print("Chatbot: ¡Hasta luego!")
            break
        # Buscar respuesta en el diccionario
        elif mensaje in respuestas:
            print(f"Chatbot: {respuestas[mensaje]}")
        else:
            print("Chatbot: Lo siento, no entiendo esa pregunta. ¿Puedes intentar de otra manera?")

# Ejecutar el chatbot
chatbot()
