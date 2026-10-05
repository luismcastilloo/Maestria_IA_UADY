import os
from pathlib import Path
from fastembed import TextEmbedding
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Embedder:
    def __init__(self):
        # Modelo multilenguaje ligero de alto rendimiento (soporta español perfectamente)
        print("Cargando modelo de embeddings local...")
        self.model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

    def get_embedding(self, text: str) -> list[float]:
        if not text or not text.strip():
            return [0.0] * 384
        
        embeddings = list(self.model.embed([text]))
        return embeddings[0].tolist()

    def get_embeddings_batch(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        
        # Filtramos o reemplazamos textos vacíos
        cleaned_texts = [t if t and t.strip() else " " for t in texts]
        embeddings = list(self.model.embed(cleaned_texts))
        return [e.tolist() for e in embeddings]
    