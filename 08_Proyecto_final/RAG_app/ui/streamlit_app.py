import streamlit as st
import httpx

API_URL = "http://localhost:8000"

st.set_page_config(page_title="RAG App - Gemini + Chroma", layout="wide")

st.title("📚 Sistema RAG con Gemini y FastAPI")

# Sidebar para Ingestión de Documentos
with st.sidebar:
    st.header("1. Ingestar Documentos")
    uploaded_files = st.file_uploader(
        "Sube tus archivos (PDF, TXT, MD)", 
        accept_multiple_files=True,
        type=["pdf", "txt", "md"]
    )
    
    if st.button("Procesar e Indexar"):
        if uploaded_files:
            files_payload = [
                ("files", (f.name, f.getvalue(), f.type or "text/plain")) 
                for f in uploaded_files
            ]
            with st.spinner("Indexando en ChromaDB con Google AI..."):
                try:
                    res = httpx.post(f"{API_URL}/ingest", files=files_payload, timeout=60.0)
                    if res.status_code == 200:
                        st.success(f"¡Éxito! Chunks creados: {res.json()['chunks_created']}")
                    else:
                        st.error(f"Error: {res.text}")
                except Exception as e:
                    st.error(f"No se pudo conectar a FastAPI: {e}")
        else:
            st.warning("Selecciona al menos un archivo.")

    st.divider()
    # Estado de la API
    if st.button("Verificar estado API"):
        try:
            res = httpx.get(f"{API_URL}/health")
            st.json(res.json())
        except Exception as e:
            st.error("API no disponible")

# Panel Principal de Consultas
st.header("2. Realizar Consultas")

question = st.text_input("Escribe tu pregunta sobre el corpus:")
top_k = st.slider("Número de chunks a recuperar (top_k)", min_value=1, max_value=10, value=3)

if st.button("Preguntar", type="primary"):
    if question.strip():
        with st.spinner("Buscando evidencias y generando respuesta..."):
            try:
                res = httpx.post(
                    f"{API_URL}/query", 
                    json={"question": question, "top_k": top_k},
                    timeout=30.0
                )
                if res.status_code == 200:
                    data = res.json()
                    
                    if data["abstained"]:
                        st.warning(data["answer"])
                    else:
                        st.markdown("### Respuesta:")
                        st.write(data["answer"])
                    
                    st.divider()
                    st.markdown("### Evidencias / Chunks Recuperados:")
                    for idx, cite in enumerate(data["citations"], 1):
                        with st.expander(f"[{idx}] Fuente: {cite['source']} (Score: {cite['score']})"):
                            st.write(cite["text"])
                else:
                    st.error(f"Error en el servidor: {res.text}")
            except Exception as e:
                st.error(f"Error al conectar con la API: {e}")
    else:
        st.warning("Escribe una pregunta válida.")

        