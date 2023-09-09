---
marp: true
theme: default
---

# Curso de Python y Trading Algorítmico
## Día 6: Introducción al Trading Algorítmico

---

# Agenda

- Repaso del Día 5
- ¿Qué es el Trading Algorítmico?
- Ventajas y Desventajas
- Herramientas en Python para Trading Algorítmico

---

# Repaso del Día 5

- Introducción a los mercados financieros
  - Tipos de mercados
  - Instrumentos financieros
- Introducción al Trading

---

# ¿Qué es el Trading Algorítmico?

- Uso de algoritmos para hacer trading de forma automática
- Basado en un conjunto definido de criterios
- Ejemplo básico en Python

```python
  if precio_actual > media_móvil:
      comprar()
  else:
      vender()
```

---
# Ventajas del Trading Algorítmico

- Rapidez y eficiencia
- Eliminación del error humano
- Posibilidad de backtesting

---

# Desventajas del Trading Algorítmico

- Riesgo de fallos técnicos
- Requiere un conocimiento sólido tanto en finanzas como en programación
- Riesgo de sobreajuste en el backtesting

---

# Herramientas en Python para Trading Algorítmico

- Pandas para el manejo de datos
- Matplotlib para la visualización
- QuantConnect y Backtrader para el backtesting

---



# Ejercicio en Clase

Diseñar un algoritmo de trading muy simple

Discutir cómo podríamos implementarlo en Python

```python
def estrategia_simple(precio_actual, media_móvil):
    if precio_actual > media_móvil:
        return "Comprar"
    else:
        return "Vender"
```

---

# Preguntas

¿Alguna pregunta o duda?

---

# Tarea

- Investigar más sobre trading algorítmico
- Pensar en un proyecto de trading algorítmico para desarrollar en las próximas clases