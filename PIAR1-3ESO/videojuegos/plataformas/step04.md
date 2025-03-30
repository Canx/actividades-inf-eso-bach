## Paso 4 - Agregar Control de Usuario

Ahora tenemos un personaje y un mundo en el que habitar, pero ¿de qué sirve un juego si no puedes controlar al personaje y moverte por él? En este capítulo exploraremos cómo agregar la entrada del teclado en Arcade.

### Definir la Velocidad de Movimiento

Primero, al inicio de nuestro programa, definiremos una constante que controle cuántos píxeles se moverá nuestro personaje en cada actualización:

```python
PLAYER_MOVEMENT_SPEED = 5
```

### Manejo de la Entrada del Teclado

Para manejar la entrada del teclado, debemos agregar dos nuevas funciones a nuestra clase `Window`: `on_key_press` y `on_key_release`. Estas funciones se llamarán automáticamente cada vez que se presione o se suelte una tecla. Dentro de ellas, según la tecla que se haya presionado o soltado, moveremos a nuestro personaje.

```python
def on_key_press(self, key, modifiers):
    """Se llama cada vez que se presiona una tecla."""
    
    if key == arcade.key.UP or key == arcade.key.W:
        self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.DOWN or key == arcade.key.S:
        self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.LEFT or key == arcade.key.A:
        self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.RIGHT or key == arcade.key.D:
        self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

def on_key_release(self, key, modifiers):
    """Se llama cada vez que se suelta una tecla."""
    # Aquí se puede agregar la lógica para detener el movimiento o ajustar la velocidad cuando se suelta la tecla.
```

> **Nota:**  
> En este ejemplo, cuando se suelta una tecla se detendría el movimiento del personaje, aunque en el código mostrado aún deberás agregar la lógica necesaria para ello.
