---
marp: true
---

# Introducción al Pensamiento Computacional

<!--
Notas para el orador:  
- Presentarse y dar una breve introducción a la clase.
- Describir los objetivos de aprendizaje y la agenda para la clase.
-->

---

# Objetivos de Aprendizaje

1. Comprender qué es el pensamiento computacional.
2. Familiarizarse con los conceptos básicos.
3. Aplicar el pensamiento computacional para resolver un problema simple.

<!--
Notas para el orador:  
- Explicar por qué es importante el pensamiento computacional.
- Detallar qué se espera que los estudiantes aprendan al final de la clase.
-->

---

# Conceptos Clave del Pensamiento Computacional

1. **Descomposición**
2. **Reconocimiento de patrones**
3. **Abstracción**
4. **Diseño de algoritmos**

<!--
Notas para el orador:  
- Explicar cada concepto brevemente.
- Indicar que a continuación se mostrarán ejemplos de cada uno.
-->

---

# Descomposición

### Definición
- Dividir un problema grande en partes más pequeñas y manejables.

---

# Descomposición

- **Montar un rompecabezas**: Dividir las piezas del rompecabezas en bordes y centro.

<!--
Notas para el orador:  
- Explicar cómo dividir un problema grande en partes más pequeñas hace que sea más fácil de manejar.
-->

---

# Reconocimiento de Patrones

### Definición
- Identificar similitudes o tendencias en un conjunto de datos o problemas.

---

# Reconocimiento de Patrones

- **Jugar al "Veoveo"**: Identificar objetos por su color o forma.

<!--
Notas para el orador:  
- Mostrar cómo reconocer patrones puede ayudar en juegos y en la vida cotidiana.
-->

---

# Abstracción

### Definición
- Simplificar problemas complejos al enfocarse en las características más importantes.

---

# Abstracción

- **Crear un Mapa del Barrio**: Dibujar solo las calles y las intersecciones importantes, ignorando casas y árboles.

<!--
Notas para el orador:  
- Explicar cómo la abstracción ayuda a enfocarse en la información relevante, haciendo la tarea más eficiente.
-->

---

# Diseño de Algoritmos

### Definición
- Crear un conjunto de pasos o reglas para resolver un problema.

---

# Diseño de Algoritmos

- **Rutina de la Mañana**: Hacer una lista de tareas para prepararse para la escuela.

<!--
Notas para el orador:  
- Hablar sobre cómo diseñar un algoritmo puede ayudar a alcanzar un objetivo específico, como prepararse para la escuela de manera eficiente.
-->

---

# Actividad: Resolviendo un Laberinto

![Laberinto para la Actividad](maze_activity.png)

<!--
Notas para el orador:  
- Distribuir hojas impresas del laberinto o mostrarlo en la pantalla.
- Guía a los estudiantes a través de la actividad, destacando cómo se aplican los conceptos clave.
- Puedes optar por usar un laberinto preimpreso o dibujar uno en el pizarrón.
-->

---

# Algoritmos Detallados para Resolver el Laberinto

1. **El Derechista**:
    - Instrucciones: Gira a la derecha en intersecciones. Si no puedes, sigue recto o gira a la izquierda.
    
2. **El Izquierdista**: 
    - Instrucciones: Gira a la izquierda en intersecciones. Si no puedes, sigue recto o gira a la derecha.
    
3. **Avanzar y Retroceder**: 
    - Instrucciones: Avanza hasta un callejón sin salida, luego retrocede a la última intersección y toma un nuevo camino.
    
4. **El Zigzag**: 
    - Instrucciones: Alterna entre girar a la izquierda y a la derecha en cada intersección.
    
5. **El Explorador**: 
    - Instrucciones: Toma caminos no explorados. Si todos están explorados, retrocede a la última intersección.
    
6. **El Método del Bucle**: 
    - Instrucciones: En intersecciones con tres o más caminos, elige el primer camino a la derecha y sigue en círculos.
    
7. **El Método del Rastreador**: 
    - Instrucciones: Mantén tu mano izquierda tocando una pared en todo momento y avanza.

<!--
Notas para el orador:  
- Explicar que estos algoritmos son guías que los estudiantes pueden seguir o adaptar para resolver el laberinto.
- Invitar a los estudiantes a escoger uno o inventar el suyo propio antes de comenzar la actividad.
-->

