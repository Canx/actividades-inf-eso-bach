---
marp: true
theme: default
---

# Curso de Python y Trading Algorítmico
## Día 3: Python para Análisis de Datos con Pandas

---

# Agenda

- Repaso del Día 2
- Introducción a Pandas
  - DataFrames y Series
  - Lectura de archivos
- Análisis básico de datos

---

# Repaso del Día 2

- Control de flujo
  - Condicionales
  - Bucles
- Funciones y bibliotecas

---

# ¿Qué es Pandas?

- Librería de Python para análisis de datos
- Estructuras de datos flexibles
- Herramientas para manipular y analizar datos

---

# Instalación de Pandas

- Instalación mediante pip o conda

```bash
pip install pandas
```

```bash
conda install pandas
```

---

# DataFrames y Series

- DataFrame: Tabla de datos con filas y columnas etiquetadas
- Series: Columna individual de un DataFrame

  ```python
  import pandas as pd
  
  data = {'Nombre': ['Alice', 'Bob'], 'Edad': [28, 34]}
  df = pd.DataFrame(data)
  ```

---

# Lectura de Archivos
Leer archivos CSV, Excel y otros formatos

```python
df = pd.read_csv('data.csv')
```

---

# Análisis Básico de Datos

- Descripción estadística

```python
df.describe()
```

- Filtrado de datos
```python
df[df['Edad'] > 30]
```

---

### Ejercicio en clase

- Leer un archivo CSV con datos de precios de acciones
- Realizar un análisis básico usando Pandas

```python
# Leer el archivo
df = pd.read_csv('precios_acciones.csv')

# Análisis básico
print(df.head())
print(df.describe())
```