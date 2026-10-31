from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import time

load_dotenv()


def generate_embeddings(query: str):
    try:
        embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)
        result = embeddings.embed_query(query)
        print(str(result))
    except Exception as e:
        print(e)


generate_embeddings("this is just a test")
