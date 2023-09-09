---
marp: true
theme: default
---

# Curso de Python y Trading Algorítmico
## Día 2: Profundizando en Python

---

# Agenda

- Repaso del Día 1
- Control de flujo
  - Condicionales
  - Bucles
- Funciones y bibliotecas

---

# Repaso del Día 1

- Presentación del curso y expectativas
- ¿Por qué Python?
- Conceptos básicos de Python
  - Variables
  - Operadores
  - Tipos de datos

---

# Control de flujo: Condicionales

- Sentencias `if`, `else` y `elif`

  ```python
  x = 10
  if x > 5:
      print("x es mayor que 5")
  elif x == 5:
      print("x es igual a 5")
  else:
      print("x es menor que 5")

---

# Control de flujo: Bucles

- for y while

  ```
  for i in range(5):
      print(i)
      
  x = 0
  while x < 5:
      print(x)
      x += 1
  ```

---

# Funciones y bibliotecas

- ¿Qué es una función?

- Crear una función simple

def saludo(nombre):
    return "Hola, " + nombre

---

# Importando bibliotecas

- Utilizando bibliotecas externas

  ```
  import math
  print(math.sqrt(16))
  ```

---

# Ejercicio en clase

- Crear una función que calcule el área de un círculo dado su radio.

- Utilizar la biblioteca math para acceder a la constante π.

  ```
  import math
  
  def area_circulo(radio):
      return math.pi * radio ** 2
  ```

---

# Preguntas

- ¿Alguna duda o pregunta?

---

# Tarea

- Practicar con condicionales y bucles.
- Escribir funciones para cálculos simples.
- Experimentar con algunas bibliotecas estándar de Python.
