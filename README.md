# LangChain 101

Small, runnable examples for learning LangChain with OpenAI, Anthropic, Google Gemini and Hugging Face.

## Project layout

| Folder | What it covers |
|---|---|
| `_01_llms/` | Plain text-completion LLM basics (OpenAI) |
| `_02_chat_models/` | Chat models: OpenAI, Anthropic, Gemini, Hugging Face, and listing Hugging Face models |
| `_03_embedded_models/` | Embeddings with OpenAI and Hugging Face, for single queries and document lists |
| `_04_poc/` | Proof of concept: embed documents from `data/source.txt` and compare them with cosine similarity |
| `main.py` | Prints the installed LangChain version (quick sanity check) |

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- API keys for the providers you want to try

## Setup

```bash
# with uv
uv sync

# or with pip
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root. It is Git-ignored, so your keys are never committed.

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
HUGGINGFACEHUB_API_TOKEN=

OPENAI_CHAT_MODEL_NAME=
ANTHROPIC_CHAT_MODEL_NAME=
GEMINI_CHAT_MODEL=
HUGGINGFACE_REPO_ID=
HUGGINGFACE_TASK_ID=
```

You only need the keys and model names for the examples you run.

## Running the examples

Run each script from the project root:

```bash
python main.py
python _01_llms/_01_llm_basics.py
python _02_chat_models/_01_chat_model_openai.py
python _03_embedded_models/_01_embeddings_openai.py
```

The proof of concept reads `data/source.txt` by relative path, so run it from its own folder:

```bash
cd _04_poc
python _01_poc_application.py
```

## Security

- Never commit `.env` or any API key. The `.gitignore` already excludes it.
- Run `/chk-cred` (Claude Code) before committing to scan for leaked credentials.
