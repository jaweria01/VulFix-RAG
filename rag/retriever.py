


# import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# KNOWLEDGE_MAP = {
#     "CWE-89": os.path.join(BASE_DIR, "knowledge_base", "cwe89_sql_injection.txt"),
#     "CWE-78": os.path.join(BASE_DIR, "knowledge_base", "cwe78_command_injection.txt"),
#     "CWE-798": os.path.join(BASE_DIR, "knowledge_base", "cwe798_hardcoded_credentials.txt")
# }

# def retrieve_knowledge(cwe_id):

#     filepath = KNOWLEDGE_MAP.get(cwe_id)

#     if not filepath:
#         return "Knowledge not found."

#     with open(filepath, "r", encoding="utf-8") as f:
#         return f.read()


# if __name__ == "__main__":

#     cwe = "CWE-89"

#     knowledge = retrieve_knowledge(cwe)

#     print(knowledge)
import chromadb
from sentence_transformers import SentenceTransformer


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="security_knowledge"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_knowledge(query_text):

    query_embedding = model.encode(
        query_text
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    return results["documents"][0][0]


if __name__ == "__main__":

    query = "SQL Injection vulnerability"

    knowledge = retrieve_knowledge(query)

    print(knowledge)