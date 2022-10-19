# Simulador robot de limpieza

Modifica el código fuente del simulador para programar al robot de limpieza y que limpie cada habitación de suciedad antes de que se te acabe la batería! Accede al simulador con el siguiente enlace:

[Roomba jungle](https://scratch.mit.edu/projects/746278041/)

Debes pulsar en "Ver dentro", y añadir tu código en el objeto "Roomba", modificando los eventos "Empezar_nivel" y "Choque".

Es imprescindible que uses los bloques de usuario "avanzar", "girar_derecha" y "girar_izquierda" para controlar el robot.

Puedes utilizar las variables "sensor_izquierda", "sensor_derecha" y "sensor_frontal" para saber si hay cerca una pared en cada dirección.


# Ejercicios roomba

## Ejercicio 1: robot aleatorio que choca

Programa el robot para que avance siempre y que cuando detecte un choque cambie la dirección a una aleatoria.

## Ejercicio 2: robot aleatorio que no choca

Modifica el programa del ejercicio 1 para que se utilice la variable "sensor_frontal" para evitar el choque frontal con las paredes.

## Ejercicio 3: limpieza en espiral cuadrada creciente.

Programa el robot para que limpie en espiral cuadrada creciente. Cuando choque con una pared debe cambiar el sentido de la espiral. Cuando la espiral sea demasiado grande debe volver a hacerla desde 0.

## Ejercicio 5: limpieza en espiral con curva creciente.

Programa el robot para que limpie en espiral con curva creciente. Cuando choque con una pared debe cambiar el sentido de la espiral. Cuando la espiral sea demasiado grande debe volver a hacerla desde 0.

## Ejercicio 6: limpieza de bordes

Programa el robot para que limpie los bordes. Primero debe avanzar hasta encontrar una pared. Después deberás girar 90 grados y avanzar utilizando los sensores para comprobar continuamente si estas cerca de la pared o no, y saber si debes de avanzar o girar. El programa debe parar cuando se vuelva a la posición original donde se encontró la pared.

## Ejercicio 7: limpieza en serpiente

Programa el robot para que limpie haciendo "eses". Cuando detecte una pared frontalmente debe girar avanzando un poco y luego hacer la pasada contraria. Cuando no pueda avanzar más debe pararse el programa.

# Ejercicio 8: limpieza de bordes + serpiente

Combina la limpieza de bordes y la de serpiente. Deberás previamente haberlas encapsulado en una función.
## Ejercicio 7: Funciones con tiempo

Crea bloques de funciones que tengan el nombre de cada algoritmo de limpieza, y que tengan como parámetro el tiempo que durará la función de limpieza.

Deberás comprobar dentro de cada función si has llegado al tiempo límite y abandonar.

## Ejercicio 9
## Ejercicio 8: Limpieza con algoritmos variable

Crea un programa de limpieza que cada cierto tiempo aleatorio cambie el algoritmo de limpieza a uno diferente.
