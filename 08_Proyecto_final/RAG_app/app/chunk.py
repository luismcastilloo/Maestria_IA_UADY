from typing import List, Dict, Any
import re 

def chunk_text(text: str, source_name: str, chunk_size: int = 300, chunk_overlap: int = 50) -> List[Dict[str, Any]]:
    """
    Divide un texto en chunks por palabras con solape (overlap).
    """
    words = text.split()
    chunks = []
    
    if not words:
        return chunks

    start = 0
    chunk_idx = 0
    
    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk_str = " ".join(chunk_words)
        
        chunks.append({
            "id": f"{source_name}_chunk_{chunk_idx}",
            "text": chunk_str,
            "metadata": {
                "source": source_name,
                "chunk_index": chunk_idx
            }
        })
        
        chunk_idx += 1
        start += (chunk_size - chunk_overlap)
        
    return chunks