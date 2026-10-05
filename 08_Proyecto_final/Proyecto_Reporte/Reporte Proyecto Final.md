# Proyecto final — Sistema RAG (Streamlit + FastAPI + ChromaDB + Google AI)

## Objetivo

Implementar un sistema **RAG** completo, con:

| Capa | Tecnología | Rol |
|---|---|---|
| UI | **Streamlit** | Cargar documentos, preguntar y ver la respuesta con citas |
| API | **FastAPI** | Ingestar, consultar e informar el estado del índice |
| Índice | **ChromaDB** | Guardar chunks + embeddings y devolver los más similares |
| Embeddings | **Google AI** | Convertir cada chunk y cada pregunta en un vector |

La interfaz **no** habla con Chroma ni con Google AI en silencio: todo pasa
por la API. Streamlit es un cliente HTTP de FastAPI.

## Desarrollo
Previo a presentar los resultados obtenidos en la ejecución del sistema RAG, se añade una imagen de la arquitectura construida para el proyecto, de donde se genera una aplicación que utiliza un enfoque modular y desacoplado, separando la lógica del servidor API (Backend) de la interfaz de usuario (Frontend). La organización de directorios se compone de la siguiente manera:

#### Arquitectura RAG

| Arquitectura |
| :---: |
| ![Imagen Arquitectura RAG](Imagenes/Arquitectura_RAG.png) |