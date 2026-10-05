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

El backend expone una API RESTful que gestiona la ingesta de documentos, la vectorización y la recuperación/generación de respuestas, mientras el Frontend permite proporcionar un panel interactivo que permite arrastrar y subir los documentos directamente así como ingresar las preguntas de interés, ajustar el parámetro de chunks $top k$ y visualizar la respuesta generada por el sistema. 

#### Panel Frontend RAG

| Panel Frontend RAG |
| :---: |
| ![Imagen Frontend RAG](Imagenes/Frontend_RAG.png) |

### Reporte de prueba
Para la prueba del RAG utilizando el panel mostrado previamente, se cargaron 5 documentos de temas variados y diferentes, 3 de ellos son de nutrición deportiva para deportes de alta resistencia, el otro es un reporte de grado de la aerodinámica de alerones en monoplazas de F1 y el último una antología poética de Jaime Sabines. Se añaden las evidencias de las preguntas realizadas 

| Evidencia 1 RAG | Evidencia 2 RAG |
| :---: | :---: |
| ![Evidencia 1 RAG](Imagenes/Evidencia1_RAG.png) | ![Evidencia 2 RAG](Imagenes/Evidencia2_RAG.png) |
| Evidencia 3 RAG | Evidencia 4 RAG|
| ![Evidencia 3 RAG](Imagenes/Evidencia3_RAG.png) | ![Evidencia 4 RAG](Imagenes/Evidencia5_RAG.png) |


