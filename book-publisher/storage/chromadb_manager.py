import chromadb
from chromadb.config import Settings

class ChromaManager:
    def __init__(self, persist_dir="db"):
        self.client = chromadb.Client(Settings(persist_directory=persist_dir))
        self.col = self.client.create_collection("chapters", get_or_create=True)

    def add_version(self, chapter_id, text):
        self.col.add(
            documents=[text],
            ids=[f"{chapter_id}_v{self.col.count()+1}"]
        )

    def retrieve_similar(self, query, k=3):
        results = self.col.query(query_texts=[query], n_results=k)
        return results["documents"][0]
