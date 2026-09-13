# Ejercicio 1 — Comparar BFS, UCS, DFS, DLS e IDS en el mapa de Rumania

## Objetivo

Elegir una ruta distinta de Arad → Bucharest, correr BFS, UCS, DFS, DLS e IDS,
y analizar diferencias de camino, costo, profundidad y nodos expandidos.

### Diagrama de nueva ruta

![Diagrama de ruta](Imagenes/Grafo_OrigenDestino.png)

### Resultados de algoritmos de busqueda

| BFS | UCS |
| :---: | :---: |
| ![Breadth First Search](Imagenes/BFS_Results.png) | ![Uniform Cost Search](Imagenes/UCS_Results.png) |
| DFS| DLS|
| ![Depth First Search](Imagenes/DFS_Results.png) | ![Depth Limited Search](Imagenes/DLS_Results_L2.png) |
| DLS| IDS|
| ![Depth Limited Search](Imagenes/DLS_Results_L4.png) | ![Iterative Deepening Search](Imagenes/IDS_Results.png) |


### Reporte de prueba

Después de correr todos los algoritmos de búsqueda, se idnetifica que BFS, con su búsqueda por anchura, sí logró encontrar el camino con menor número de carreteras; 4 en este caso. Esto favorecido por su metodología de explorar el grafo nivel a nivel sin dar algún paso adicional que no garantice primero poder hallar la solución con menor cantidad de pasos.\

No obstante, entre los resultados de BFS se reporta un mayor costo de distancia con respecto UCS que intenta optimizar la distancia, a pesar de generar un paso adicional. UCS toma una ruta de 5 carreeras hacia Urziceni, encontrando el camino con menor distancia con 514 km, reduciendo 32 km vs BFS.\

Caso contrario para lo que se observa con DFS que reporta la ruta con mayor costo de 1,109 km abordando 10 carreteras. El algoritmo no garantiza la solución de menor profundidad. Al utilizar una estructura LIFO  elige una rama arbitraria y la explora hacia abajo en profundidad tanto como sea posible antes de hacer el backtracking.Como DFS termina tan pronto encuentra cualquier camino al objetivo, devolvió esa ruta de 10 carreteras y 1109 km sin comprobar que existían alternativas mucho más directas.

