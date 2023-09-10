---
marp: true
---

# Interacción con Bases de Datos (Parte 1)
### Sesión 6

---

## Objetivos de la Sesión
- Comprender qué es una base de datos y cómo interactuar con ella desde Python.
- Introducción al SQL.

---

## ¿Qué es una Base de Datos?
- Una base de datos es una colección organizada de datos, generalmente almacenada y accesible electrónicamente desde un sistema informático.

---

## Bases de Datos Relacionales
- Una base de datos relacional almacena datos en tablas.
- Cada tabla tiene filas (registros) y columnas (campos).

---

## SQL: Lenguaje de Consulta Estructurado
- SQL es el lenguaje utilizado para interactuar con bases de datos relacionales.

---

## Tipos de Consultas SQL
- SELECT: Consulta de datos
- INSERT: Inserción de nuevos registros

---

## Ejemplo de una Tabla
- Imagina una tabla de 'Productos' con los campos 'ID', 'Nombre' y 'Precio'.

---

## Consulta SELECT
- Ejemplo: `SELECT * FROM Productos WHERE Precio > 10;`

---

## Consulta INSERT
- Ejemplo: `INSERT INTO Productos (ID, Nombre, Precio) VALUES (1, 'Manzana', 12);`

---

## Python y SQL
- Se puede utilizar la biblioteca `sqlite3` para interactuar con bases de datos SQLite en Python.

---

## Ejercicio Guiado: Sistema de Inventario (Parte 1)
- Crear la base de datos y la tabla de 'Productos'.

---

## Preguntas y Respuestas
- ¿Hay alguna pregunta o algo que no esté claro?
- Este es un buen momento para hacer preguntas.
