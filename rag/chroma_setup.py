import chromadb
from sentence_transformers import SentenceTransformer
import os

# Create persistent ChromaDB storage

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="security_knowledge"
)

# Embedding model

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

knowledge_folder = "knowledge_base"

for filename in os.listdir(knowledge_folder):

    filepath = os.path.join(
        knowledge_folder,
        filename
    )

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    embedding = model.encode(
        content
    ).tolist()

    collection.add(
        documents=[content],
        embeddings=[embedding],
        ids=[filename]
    )

    print(f"Added: {filename}")

print("\nKnowledge Base Loaded Into ChromaDB")