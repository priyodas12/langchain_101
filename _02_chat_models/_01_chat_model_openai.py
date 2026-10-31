import os
import time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# load env variable
load_dotenv()

chat_model = os.getenv("OPENAI_CHAT_MODEL_NAME")
start = time.perf_counter()

# temperature controls how random or varied a ChatOpenAI model’s responses are.
# -----------------------------------------------------------------------------
# temperature=0 → most consistent and predictable; best for code, extraction, factual answers, and structured output.
# temperature=0.2–0.4 → slightly varied, while staying focused.
# temperature=0.7 → more creative and diverse.
# temperature=1.0+ → highly varied; more likely to be imaginative but also inconsistent.

try:
    chat_model_llm = ChatOpenAI(
        model=chat_model,
        temperature=0.2,  # Randomness / creativity
        # max_tokens=100,  # Maximum response length
        # timeout=30,  # Maximum wait time in seconds
        # max_retries=2,  # Retries for temporary API/network errors
        # streaming=True,  # Receive output gradually
        # reasoning_effort="low",  # Reasoning level, for supported reasoning models
    )
    response = chat_model_llm.invoke("write a poem for football in 20 words?")
    print(response.content)
except Exception as e:
    print(f"Error: {e}")
finally:
    end = time.perf_counter()
    print(f"Elapsed time: {end - start}")
