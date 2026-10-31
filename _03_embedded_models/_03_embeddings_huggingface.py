from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)


def get_hf_embeddings(query):
    try:
        result = embeddings.embed_documents(query)
        print(result)
    except Exception as e:
        print(e)


get_hf_embeddings("this is just a test")

document_list = [
    "Delhi is the capital of India",
    "London is the capital of UK",
    "New York is the capital of US",
    "Colombo is the capital of Sri Lanka",
]

get_hf_embeddings(document_list)
