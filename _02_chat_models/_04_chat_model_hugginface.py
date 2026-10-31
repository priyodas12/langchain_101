from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import time
import os
from dotenv import load_dotenv

load_dotenv()

hf_repo = os.getenv("HUGGINGFACE_REPO_ID")
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
hf_task_id = os.getenv("HUGGINGFACE_TASK_ID")

start = time.time()
try:
    # get huggingface llm via client
    llm = HuggingFaceEndpoint(
        repo_id=hf_repo,
        task=hf_task_id,
    )

    # create chat model
    chat_model = ChatHuggingFace(
        llm=llm,
    )

    # interact with chat model
    response = chat_model.invoke("what is the popular dish in italy?")

    print(response.content)
except Exception as e:
    print(e)
finally:
    end = time.time()
    print(f"execution time: {end - start}")
