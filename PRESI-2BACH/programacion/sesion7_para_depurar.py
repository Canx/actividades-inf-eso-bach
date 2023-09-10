# Programa con errores para ejercicio de depuración

# Función para calcular el cuadrado de un número
def square(num):
    return num * num

# Función para calcular el cubo de un número
def cube(n):
    return n * n * n

# Función para sumar dos números
def add(a, b):
    return a + b

# Lista de números
numbers = [1, 2, '3', 4, 5]

# Calcular y mostrar el cuadrado de cada número
for num in numbers:
    print(f"El cuadrado de {num} es {square(num)}")

# Calcular y mostrar el cubo de cada número
for n in numbers:
    print(f"El cubo de {n} es {cube(n)}")

# Calcular y mostrar la suma de dos números
a = 10
b = '20'
print(f"La suma de {a} y {b} es {add(a, b)}")
