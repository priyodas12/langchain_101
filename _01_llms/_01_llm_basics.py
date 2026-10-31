import os
import time
import logging
from openai import OpenAI as OpenAIClient
from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv

# load dotenv
load_dotenv()


# print(os.getenv("OPENAI_API_KEY") is not None)
def print_available_model():
    client = OpenAIClient()
    models = client.models.list()
    print("*" * 20)
    for model in models.data:
        print(model.id)
    print("*" * 20)


try:
    start = time.perf_counter()
    # print_available_model()
    openai_llm = OpenAI(
        model="gpt-3.5-turbo-instruct", api_key=os.getenv("OPENAI_API_KEY")
    )

    result = openai_llm.invoke("what is capital of Italy?")

    print(result)
except Exception as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
finally:
    elapsed = time.perf_counter() - start
    print(f"Elapsed time: {elapsed:.6f} seconds")
