from app.config import get_settings

settings = get_settings()

print(f"pinecone_index_name: {settings.pinecone_index_name}")