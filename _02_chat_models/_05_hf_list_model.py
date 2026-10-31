import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
    base_url="https://router.huggingface.co/v1",
)

models = client.models.list()

print(f"Available models: {len(models.data)}")

for model in models.data:
    print(model.id)
