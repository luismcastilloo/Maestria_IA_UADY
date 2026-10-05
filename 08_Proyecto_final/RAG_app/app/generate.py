import os
from pathlib import Path
from typing import List, Dict, Any, Tuple
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Generator:
    def __init__(self):
        pass

    def generate_response(self, question: str, retrieved_chunks: List[Dict[str, Any]], min_score: float = 0.3) -> Tuple[str, bool]:
        # 1. Filtrar fragmentos por score mínimo de similitud
        # (ChromaDB devuelve score entre 0 y 1 en nuestra conversión)
        valid_chunks = [c for c in retrieved_chunks if c.get("score", 0) >= min_score]
        
        # 2. Extraer palabras clave relevantes de la pregunta (omitimos stopwords cortas)
        stopwords = {"cuándo", "cuando", "dónde", "donde", "quién", "quien", "cómo", "como", "qué", "que", "para", "está", "esta", "sobre", "nació", "nacio"}
        words = [w.lower().strip("?,.") for w in question.split()]
        keywords = [w for w in words if len(w) > 2 and w not in stopwords]

        # 3. Validar si los fragmentos recuperados contienen al menos una palabra clave de la pregunta
        has_relevant_content = False
        relevant_summary = []

        if valid_chunks:
            for idx, chunk in enumerate(valid_chunks, 1):
                text = chunk.get("text", "")
                text_lower = text.lower()
                
                # Verificar coincidencia de palabras clave
                if any(kw in text_lower for kw in keywords):
                    has_relevant_content = True
                
                source_file = chunk.get("metadata", {}).get("source", chunk.get("source", "Documento"))
                relevant_summary.append(f"[{idx}] ({source_file}): {text.strip()}")

        # 4. Regla de abstención: si no hay palabras clave en los chunks o no superan el umbral
        if not valid_chunks or not has_relevant_content:
            return "No tengo evidencia suficiente en el corpus para responder esta pregunta.", True

        # 5. Si hay evidencia relevante, formatear respuesta
        answer = (
            f"Basado en los documentos recuperados para '{question}':\n\n" +
            "\n\n".join(relevant_summary)
        )

        return answer, False