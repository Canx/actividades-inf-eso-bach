---
marp: true
theme: default
---

# Curso de Python y Trading Algorítmico
## Día 7: Análisis Técnico y Python

---

# Agenda

- Repaso del Día 6
- Cargando Datos Financieros en Python
- Visualización con Matplotlib

---

# Repaso del Día 6

- Introducción al Trading Algorítmico
- Concepto de Estrategia de Trading

---



# Herramientas en Python para Trading Algorítmico

- Pandas para el manejo de datos
- Matplotlib para la visualización 

---

# Cargando Datos Financieros en Python

- Fuentes comunes para datos financieros:
  - APIs (Alpha Vantage, Yahoo Finance)
  - Archivos CSV descargados
  - Bases de datos

---

# Usando Pandas para cargar datos desde un CSV

```python
import pandas as pd

# Cargar datos desde un archivo CSV
df = pd.read_csv('AAPL.csv')

# Mostrar las primeras 5 filas del DataFrame
print(df.head())
```
---

# Visualización de Datos Financieros

- Importancia de visualizar los datos antes de realizar análisis
- Ayuda a entender mejor las tendencias y patrones

---

# Biblioteca Matplotlib

- Biblioteca de visualización de datos en Python
- Ideal para gráficos de líneas, barras, histogramas y más

---

# Ejemplo de Gráfico con Matplotlib

## Código en Python

```python
import matplotlib.pyplot as plt

# Crear un gráfico de líneas para el precio de cierre
plt.figure(figsize=(12,6))
plt.title('Precio de Cierre de AAPL')
plt.plot(df['Date'], df['Close'])
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre (en USD)')
plt.show()
```

---

#  Ejercicio en Clase


---
# Preguntas

¿Alguna pregunta o duda?

--- 

# Tarea

- Probar con distintos activos y visualizar sus precios