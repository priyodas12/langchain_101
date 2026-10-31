from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import time

load_dotenv()


def generate_embeddings_docs(query: list[str]):
    try:
        embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)
        result = embeddings.embed_documents(query)
        print(str(result))
    except Exception as e:
        print(e)


document_list = [
    "Delhi is the capital of India",
    "London is the capital of UK",
    "New York is the capital of US",
    "Colombo is the capital of Sri Lanka",
]
generate_embeddings_docs(document_list)
