import os

import os
import time
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
anthropic_chat_model = os.getenv("ANTHROPIC_CHAT_MODEL_NAME")

start = time.time()
try:
    chat_model = ChatAnthropic(
        api_key=anthropic_api_key,
        model=anthropic_chat_model,
        temperature=0.2,
        max_tokens=100,
        streaming=True,
        # reasoning_effort="low"
    )
    response = chat_model.invoke("write a poem for football")
    print(response.content)
except Exception as e:
    print(e)
finally:
    end = time.time()
    print(f"execution time: {end - start} seconds")
