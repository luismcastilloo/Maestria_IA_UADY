# Ejercicio 1 — Comparar Greedy y A* en el mapa de Rumania

## Contexto

En el proyecto `Búsqueda informada/project` (AIMA cap. 3–4, Figuras 3.2 y 3.22)
se resuelve el problema de **encontrar una ruta** entre dos ciudades del mapa
carretero de Rumania. Dos algoritmos de búsqueda **informada** comparten el
mismo grafo, el mismo `RouteFindingProblem` y la misma heurística `h(n)`:

## Objetivo

Elegir una ruta distinta de Arad → Bucharest, inspeccionar `h(n)`, correr
Greedy y A*, y analizar diferencias de camino, costo, profundidad y nodos
expandidos a la luz de `g`, `h` y `f`.

### Diagrama de nueva ruta

![Diagrama de ruta](Imagenes/Grafo_OrigenDestino.png)

### Resultados de algoritmos de busqueda

| GBF | A* |
| :---: | :---: |
| ![Greedy Best First Search](Imagenes/GBF_Results.png) | ![A Star Search](Imagenes/ASTAR_Results.png) |


### Tabla Comparativa de rendimiento
| Algoritmo | Path | Depth | Cost | Expanded | Heuristica Usada |
| :--- | ---: | ---: | ---: |---:| ---:|
| Greedy Best-First (GBF) | Oradea $\rightarrow$ Sibiu $\rightarrow$ Fagaras $\rightarrow$ Bucharest $\rightarrow$ Urziceni  | 4 carreteras | 546 km | 4 nodos | Distancia Euclidiana a Urziceni| 
| A*Search | Oradea $\rightarrow$ Sibiu $\rightarrow$ Rimnicu Vilcea $\rightarrow$ Pitesti $\rightarrow$ Bucharest $\rightarrow$ Urziceni | 5 carreteras | 514 km | 7 nodos | Distancia Euclidiana a Urziceni |

### Reporte de prueba

Después de correr los dos algoritmos de búsqueda informada, se identiica que A* encontró la ruta óptima en distancia con un costo de 514 km, aunque en comparación el algoritmo de Greedy se desvió en la ruta, decidió optar por uba ruta menos óptima de 546 km, cerca de 32 km más costosa, aunque determinó la ruta a través de 4 carreteras únicamente, a diferencia de A* que terminó ejecutando pasos en 5 carreteras.

La razón por la que Greedy puede devolver un camino más caro aunque la "h" sea adminisble, debido evalúa los nodos utilizando $f(n) = h(n)$ ignorando completamente el costo ya acumulado. Greedy comparó a Fagaras contra Rimnicu Vilcea guiandose únicamente por la distancia directa más corta a la meta. No consideró que el tramo acumulado para llegar a la meta a través de Fagaras terminaría sumando un costo real mayor. 

Por último, respecto al comportamiento observado de $f$, sí se mantiene una consistencia en el algoritmo de A*, no se observan decrecimientos. Los valores de $f(n) = g(n) + h(n)$ a lo largo de cualquier camino nunca disminuyen, de manera que esto asegura que la primera vez que A* expande un nodo nuevo como objetivo, se tiene la garantía absoluta de haber encontrado la ruta de menor costo hacia él, sin necesidad de reevaluar nodos ya visitados.

