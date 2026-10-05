import io
import pypdf
from typing import List
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel

from app.embed import Embedder
from app.store import VectorStore  # Si tu archivo se llama store.py
from app.generate import Generator

app = FastAPI(title="RAG System API")

embedder = Embedder()
vector_store = VectorStore()
generator = Generator()

class QueryRequest(BaseModel):
    question: str
    top_k: int = 3
    min_score: float = 0.3

@app.get("/")
def read_root():
    return {"status": "API is running"}

@app.post("/ingest")
async def ingest(files: List[UploadFile] = File(...)):
    try:
        # 1. Limpiar base de datos
        vector_store.reset_db()
        
        total_chunks = 0
        processed_files = 0

        for file in files:
            content = await file.read()
            text = ""

            if file.filename.lower().endswith(".pdf"):
                try:
                    # strict=False evita que se cuelgue con PDFs que tienen objetos corruptos
                    pdf_reader = pypdf.PdfReader(io.BytesIO(content), strict=False)
                    for page in pdf_reader.pages:
                        try:
                            extracted = page.extract_text()
                            if extracted:
                                text += extracted + "\n"
                        except Exception:
                            continue
                except Exception as e:
                    print(f"Error leyendo {file.filename}: {e}")
                    continue
            else:
                text = content.decode("utf-8", errors="ignore")

            if not text.strip():
                continue

            # 2. Chunking simple por párrafos/bloques
            raw_chunks = [c.strip() for c in text.split("\n\n") if len(c.strip()) > 50]
            
            # Si no hay párrafos grandes, fragmentar cada 500 caracteres
            if not raw_chunks:
                chunk_size = 500
                raw_chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

            if not raw_chunks:
                continue

            # Formatear metadatos e IDs
            chunks_data = []
            for idx, chunk_text in enumerate(raw_chunks):
                chunks_data.append({
                    "id": f"{file.filename}_chunk_{idx}",
                    "text": chunk_text,
                    "metadata": {"source": file.filename}
                })

            # 3. Generar embeddings e indexar
            texts_to_embed = [item["text"] for item in chunks_data]
            embeddings = embedder.get_embeddings_batch(texts_to_embed)
            
            vector_store.add_chunks(chunks_data, embeddings)
            
            total_chunks += len(chunks_data)
            processed_files += 1

        return {
            "status": "success",
            "processed_files": processed_files,
            "chunks_created": total_chunks,
            "total_index_size": vector_store.count()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
def query_rag(request: QueryRequest):
    try:
        query_vector = embedder.get_embedding(request.question)
        results = vector_store.query(query_vector, top_k=request.top_k)
        
        answer, abstained = generator.generate_response(
            question=request.question,
            retrieved_chunks=results,
            min_score=request.min_score
        )
        
        return {
            "question": request.question,
            "answer": answer,
            "abstained": abstained,
            "retrieved_chunks": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))