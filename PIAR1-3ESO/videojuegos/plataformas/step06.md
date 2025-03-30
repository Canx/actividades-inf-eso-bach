## Paso 6 - Reiniciar

En muchos juegos es necesario reiniciar el nivel cuando el jugador se cae del mapa o se activa alguna condición específica. En este paso implementaremos un mecanismo para restablecer la posición del jugador.

### Definir la Posición Inicial

Primero, define las coordenadas iniciales del jugador, que usaremos para restablecer su posición:

```python
self.player_start_x = 100
self.player_start_y = 150
```

### Reiniciar la Posición del Jugador

Cada vez que el jugador se desplace por debajo de un umbral determinado (por ejemplo, se caiga del mapa), reinicia su posición a los valores iniciales definidos:

```python
if self.player_sprite.center_y < 0:
    self.player_sprite.center_x = self.player_start_x
    self.player_sprite.center_y = self.player_start_y
```

### Consideraciones Adicionales

- Es posible que también necesites reiniciar otros elementos del nivel, como la posición de enemigos o la puntuación.
- Asegúrate de incluir esta lógica en el método `update()` o en el bucle principal del juego, para que se verifique de forma continua la posición del jugador.

Con esta implementación, cada vez que el jugador caiga por debajo del límite establecido, se restablecerá su posición, permitiendo que el juego continúe sin interrupciones.
