import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

clave_api = os.getenv("GEMINI_API_KEY")

print("API KEY LEÍDA:", clave_api)   # <-- Esto nos va a decir si .env funciona

client = genai.Client(api_key=clave_api)

def ejecutar_consulta():
    print("🚀 Conectando con el motor de Gemini ...")

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents="Mani aqui tu  asistente de IA configurado para apoyar el curso de  IA"
        )

        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")

    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")

if __name__ == "__main__":
    ejecutar_consulta()

