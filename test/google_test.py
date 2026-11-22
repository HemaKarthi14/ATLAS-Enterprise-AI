import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# 1. Generate Embeddings
embed_res = client.models.embed_content(
    model="gemini-embedding-001",
    contents="Your document chunk goes here.",
    config=types.EmbedContentConfig(
        task_type="RETRIEVAL_DOCUMENT",
        output_dimensionality=768
    )
)
vector = embed_res.embeddings[0].values
print(f"Embedding length: {len(vector)}")

# 2. Generate RAG Answer
chat_res = client.models.generate_content(
    model="gemini-3.8-flash-lite",
    contents="Context: [retrieved text]\n\nQuestion: Summarize the context."
)
print(chat_res.text)
