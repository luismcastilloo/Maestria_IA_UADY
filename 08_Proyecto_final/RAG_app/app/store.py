import chromadb

class VectorStore:
    def __init__(self, persist_directory="./chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(name="rag_documents")

    def reset_db(self):
        """Limpia la colección existente."""
        try:
            existing_ids = self.collection.get()["ids"]
            if existing_ids:
                self.collection.delete(ids=existing_ids)
        except Exception:
            pass

    def count(self) -> int:
        """Devuelve el número total de chunks almacenados."""
        return self.collection.count()

    def add_documents(self, chunks: list, embeddings: list[list[float]], metadatas: list[dict] = None):
        if not chunks:
            return

        if isinstance(chunks[0], dict):
            text_documents = [item.get("text", "") for item in chunks]
            extracted_ids = [item.get("id", f"chunk_{i}") for i, item in enumerate(chunks)]
            if metadatas is None:
                metadatas = [
                    item.get("metadata", {"source": item.get("id", "").split("_chunk_")[0]})
                    for item in chunks
                ]
        else:
            text_documents = chunks
            existing_count = self.collection.count()
            extracted_ids = [f"chunk_{existing_count + i}" for i in range(len(chunks))]
            if metadatas is None:
                metadatas = [{}] * len(chunks)

        self.collection.add(
            documents=text_documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=extracted_ids
        )

    def add_chunks(self, chunks: list, embeddings: list[list[float]], metadatas: list[dict] = None):
        return self.add_documents(chunks, embeddings, metadatas)

    def query(self, query_vector: list[float], top_k: int = 3) -> list[dict]:
        if self.collection.count() == 0:
            return []

        results = self.collection.query(
            query_embeddings=[query_vector],
            n_results=top_k
        )
        
        output = []
        if results and results['documents']:
            documents = results['documents'][0]
            metadatas = results['metadatas'][0] if results['metadatas'] else [{}] * len(documents)
            distances = results['distances'][0] if results['distances'] else [0.0] * len(documents)

            for doc, meta, dist in zip(documents, metadatas, distances):
                similarity_score = max(0.0, 1.0 - dist)
                output.append({
                    "text": doc,
                    "metadata": meta,
                    "score": similarity_score
                })
        return output

    def search(self, query_vector: list[float], top_k: int = 3) -> list[dict]:
        return self.query(query_vector, top_k=top_k)