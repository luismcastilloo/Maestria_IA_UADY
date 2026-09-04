# Ejercicio 2 — Descripción PEAS de agentes inteligentes

## Objetivo

Para cada una de las **8 aplicaciones** listadas abajo, redacta una descripción
PEAS completa y coherente. Debes pensar como diseñador del agente: qué optimiza,
dónde actúa, con qué puede mover o modificar el mundo, y qué puede observar.

## Aplicación 1: **Asistente virtual de voz**

- **Performance:**\
Interpretar correctamente comandos de voz, minimizar errores de reconocimiento y proporcionar respuestas útiles con tiempos de respuesta bajos.
- **Environment:**\
Diferentes escenarios; lugares al aire libre, con ruido externo, lugares en silencio, con cercanía de voz o con lejanía.\

Estocástico porque los comandos pueden ser distintos, dinámico porque puede estar en movimiento o no y multiagente porque actúa con humanos y servicios.
- **Actuators:**\
Respuesta simpultánea a través de bocina, búsqueda de información en internet, gestión de aplicaciones (abrirlas y ejecutar comandos en ellas), activación de funciones programadas como alarmas, juegos verbales internos, envío de recordatorios.
- **Sensors:**\
Micrófono integrado, historial de conversaciones, acceso a recursos y aplicaciones, bases de datos, servicios web.


## Aplicación 2: **Robot Aspirador Doméstico**

- **Performance:**\
Maximizar el área limpiada, minimizar el tiempo de limpieza, evitar colisiones y optimizar el consumo de batería.
- **Environment:**\
Habitaciones de diferentes dimensiones, obstaculos, pisos con diferentes texturas, presencia de personas, diferente cantidad de basura, iluminación variada del entorno.
- **Actuators:**\
Sistema de aspiración y cepillos, moverse en diferentes direcciones, esquivar obstáculos, emitir avisos de voz, motores de desplazamiento,.
- **Sensors:**\
Sensor de movimiento, sensores de presencia, sensores de temperatura, acelerometros, micrófonos, sensor infrarrojo, sensor de proximidad.

## Aplicación 3: **Sistema de recomendación de streaming**

- **Performance:**\
Maximizar el tiempo de visualización, la satisfacción del usuario y la precisión de las recomendaciones.
- **Environment:**\
Base de datos de contenidos, perfiles de usuarios, historial de consumo y preferencias.
- **Actuators:**\
Reproduce el contenido seleccionado, ofrece el menú de opciones y hace recomendaciones basadas en el tipo de consumo, generar listas personalizadas, enviar notificaciones.
- **Sensors:**\
Historial de reproducción, calificaciones del usuario, búsquedas, tiempo de visualización, interacciones.


## Aplicación 4: **Vehículo autónomo en ciudad**

- **Performance:**\
Conducir de forma autónoma sin chocar, evitando accidentes y manteniendo seguro al pasajero.
- **Environment:**\
Entorno urbano o rural, con diferencia en caminos, presencia de obstáculos, peatones, diferencias de reglamentos viales, exposición a diferentes tipos de clima y presencia en el interior de diferente cantidad de pasajeros.
- **Actuators:**\
Control del volante, manejo de limpiaparabrisas, gestión del acelerador, freno y seguros del auto, luces, claxon.
- **Sensors:**\
Cámaras integradas, sensores de movimiento, radar, acelerometros, sensores de temperatura, GPS, conexión a internet, mapas HD.

## Aplicación 5: **Agente de trading algorítmico en bolsa**

- **Performance:**\
Maximizar el rendimiento ajustado al riesgo, minimizar pérdidas y ejecutar operaciones de compra y venta de manera eficiente.
- **Environment:**\
Diferentes sitios de internet, la bolsa de valores, casas de cambio, reportes financieros, noticias, indicadores macroeconómicos.\

Estocático por mercado variable, secuencial de acuerdo las tendencias y multiagente porque interactúa con miles de variables del mercado.
- **Actuators:**\
Ejectar ordenes de compra y venta, rebalancear portafolios, enviar alertas.
- **Sensors:**\
Precio de acciones, volumen de mercado, noticias financieras, indicadores económicos, APIs.


## Aplicación 6: **Sistema de diagnóstico médico asistido por IA**

- **Performance:**\
Realizar el diagnóstico más preciso al paciente basado en su historial médico, ofreciendo el mejor tratamiento a una enfermedad.
- **Environment:**\
Hospitales, clínicas, consultorios médicos, expedientes clínicos electrónicos, laboratorios de análisis clínicos y centros de imagenología.\

Parcialmente observable porque es una parte o un sistema de todo el cuerpo, estocástico por la variedad de casos que pueden haber y dinámico porque se mantiene en movimiento constante.
- **Actuators:**\
Generar diagnóstico probable, presentar nivel de confianza, recomendar estudios complementarios, sugerir tratamientos, emitir alertas.
- **Sensors:**\
Imágenes médicas, expedientes clínicos, resultados de laboratorio, síntomas reportados, dispositivos médicos conectados.

## Aplicación 7: **Dron de inspección de infraestructura**

- **Performance:**\
Maximizar la cobertura de inspección, detectar anomalías con precisión y minimizar riesgos de colisión..
- **Environment:**\
Exteriores, interacción del viento, cambios de temperatura, obstáculos estáticos y en movimiento, exposición a diferentes alturas y diferentes tipos de suelo de aterrizaje.\

Entorno dinámico por el movimiento constante del dron, parcialmente observable por las zonas de la estructura y estocástico por los factores externos.
- **Actuators:**\
Activación de las hélices y motor, sobrevolar de manera efectiva, mantener la conexión con el control, hacer tomas de vídeo o fotografía, transmisión de datos, aterrizaje.
- **Sensors:**\
Sensores de temperatura, de movimiento, sensores de luz, cámaras, conexión internet o bluetooth, sensor de altitud, giroscopio, GPS. 

## Aplicación 8: **Agente jugador de ajedrez**

- **Performance:**\
Maximizar la probabilidad de victoria o empate minimizando errores.
- **Environment:**\
Tablero de ajedrez, piezas propias y del oponente, reglas del juego y reloj de competencia. 
- **Actuators:**\
Realizar movimientos legales en el juego,mostrar jugada en la pantalla, emitir sonidos o gráficos que mantengan el interés del juego, abandonar la partida.
- **Sensors:**\
Estado actual del tablero, posición de las piezas, movimientos del oponente, tiempo restante.