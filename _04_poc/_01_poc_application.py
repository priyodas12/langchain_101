from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import time
import os
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

def load_document():
    start=time.perf_counter()
    with open("data/source.txt", "r") as f:
        results = f.read().splitlines()
        end = time.perf_counter()
        print(f"document loaded in {end - start} seconds")
        return results


def load_openai():
    start = time.perf_counter()
    llm = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)
    print(f"loaded openai model in {time.perf_counter() - start} seconds")
    return llm

def get_embeddings(documents: list[str]):
    start = time.perf_counter()
    llm = load_openai()
    result = llm.embed_documents(documents)
    print(f"loaded openai model in {time.perf_counter() - start} seconds")
    return result

def check_answers(query:str):
    start = time.perf_counter()
    documents = load_document()
    embeddings_model = load_openai()

    document_embeddings = embeddings_model.embed_documents(documents)

    # embed_query returns one vector, so wrap it in a list for scikit-learn
    query_embedding = [embeddings_model.embed_query(query)]

    similarity_scores = cosine_similarity(
        query_embedding,
        document_embeddings,
    )[0]

    ranked_results = sorted(
        zip(documents, similarity_scores),
        key=lambda item: item[1],
        reverse=True,
    )

    for document, score in ranked_results[:3]:
        print(f"Score: {score:.6f} | {document}")
    end = time.perf_counter()
    print(f"query time: {end - start} seconds")

check_answers("what is heap memory?")

