## Paso 7 - Agregar una Cámara

Ahora que nuestro personaje se mueve por el nivel, es importante agregar una cámara para seguirlo cuando se desplaza, especialmente si el nivel es más grande que la ventana de visualización.

### Crear la Cámara

Podemos crear una instancia de `arcade.Camera` en el método `__init__` (o en un método `setup`) de nuestro juego. Por ejemplo:

```python
self.camera = arcade.Camera(self.width, self.height)
```

### Usar la Cámara en el Dibujo

Para aplicar la cámara a todo lo que se dibuja, debemos llamar a `self.camera.use()` al inicio del método `on_draw`, antes de iniciar el renderizado:

```python
def on_draw(self):
    self.camera.use()
    arcade.start_render()
    self.player_list.draw()
    self.platform_list.draw()
```

### Actualizar la Cámara

En el método `update` es necesario mover la cámara para que siga al jugador. Para ello, calculamos una posición que centre al jugador en la ventana y actualizamos la cámara de la siguiente forma:

```python
def update(self, delta_time):
    # Actualiza la posición del jugador
    self.player_list.update()

    # Calcula la posición de la cámara para centrarla en el jugador
    position = (self.player_sprite.center_x - self.width / 2,
                self.player_sprite.center_y - self.height / 2)
    # Mueve la cámara hacia la posición deseada con un factor de suavizado
    self.camera.move_to(position, 0.1)
```

El segundo parámetro en `move_to` es el factor de suavizado, que ajusta la velocidad a la que la cámara se mueve para seguir al jugador. Puedes modificarlo según las necesidades de tu juego.

Con estas modificaciones, la cámara seguirá al jugador mientras se desplaza, permitiendo explorar niveles más amplios de forma dinámica.
