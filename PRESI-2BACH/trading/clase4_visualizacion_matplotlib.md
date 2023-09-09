---
marp: true
theme: default
---

# Curso de Python y Trading Algorítmico
## Día 4: Visualización de Datos con Matplotlib

---

# Agenda

- Repaso del Día 3
- Introducción a Matplotlib
  - Instalación y configuración
  - Tipos de gráficos
- Crear gráficos básicos

---

# Repaso del Día 3

- Introducción a Pandas
  - DataFrames y Series
  - Lectura de archivos
- Análisis básico de datos

---

# ¿Qué es Matplotlib?

- Biblioteca de Python para la creación de gráficos estáticos, interactivos y animados.
- Útil para la visualización de datos y análisis exploratorio.

---

# Instalación de Matplotlib

- Instalación mediante pip o conda

```bash
pip install matplotlib
```

o

```bash
conda install matplotlib
```

---

# Tipos de Gráficos

- Gráficos de línea
- Gráficos de barras
- Histogramas
- Diagramas de dispersión (scatter plots)

---

# Crear un Gráfico de Línea Simple

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.show()
```

---

# Crear un Gráfico de Barras

```python
nombres = ['Alice', 'Bob', 'Charlie']
edades = [28, 34, 45]

plt.bar(nombres, edades)
plt.show()
```

---

# Ejercicio en Clase

- Utilizar un DataFrame de Pandas para visualizar datos
- Crear diferentes tipos de gráficos

```python
import pandas as pd

df = pd.read_csv('data.csv')
df['Edad'].plot(kind='hist')
plt.show()
```

---

# Preguntas

¿Alguna pregunta o duda?

---

# Tarea
- Experimentar con diferentes tipos de gráficos
- Utilizar Matplotlib para visualizar un conjunto de datos de tu elección