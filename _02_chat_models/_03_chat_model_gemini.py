import os

import os
import time
from dotenv import load_dotenv
from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_chat_model = os.getenv("GEMINI_CHAT_MODEL")


def list_available_gemini_models():
    client = genai.Client(api_key=gemini_api_key)

    for model in client.models.list():
        print(model.name)


list_available_gemini_models()
start = time.time()
try:
    chat_model = ChatGoogleGenerativeAI(
        api_key=gemini_api_key,
        model=gemini_chat_model,
        # temperature=0.2,
        # max_tokens=100,
        # streaming=True,
        # reasoning_effort="low"
    )
    response = chat_model.invoke("write a morning inspiration note")
    print(response.content)
except Exception as e:
    print(e)
finally:
    end = time.time()
    print(f"execution time: {end - start} seconds")
