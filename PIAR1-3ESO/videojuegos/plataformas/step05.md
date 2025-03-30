## Paso 5 - Agregar Gravedad

Ahora que tenemos el control del personaje, es el momento de simular la gravedad para darle un comportamiento más realista.

Para lograr esto, debemos aplicar una fuerza gravitatoria que haga que nuestro personaje caiga cuando no esté apoyado en una plataforma. Esto se logra modificando la velocidad vertical del personaje en cada actualización del juego.

### Definir la Gravedad

Primero, define una constante para la gravedad:

```python
GRAVITY = 1
```

### Aplicar la Gravedad en la Actualización

Dentro del método `update()` de tu clase, resta la gravedad al cambio en la posición vertical del sprite del jugador:

```python
def update(self, delta_time):
    # Aplica la gravedad
    self.player_sprite.change_y -= GRAVITY

    # Actualiza la posición del jugador
    self.player_list.update()

    # Aquí se puede incluir la detección de colisiones para detener la caída del jugador
```

### Ejemplo Completo

A continuación, se muestra un ejemplo completo que ilustra cómo implementar la gravedad en tu juego:

```python
import arcade

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ejemplo: Agregar Gravedad"

GRAVITY = 1
PLAYER_MOVEMENT_SPEED = 5
PLAYER_JUMP_SPEED = 20

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        # Crea el sprite del jugador
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
        self.player_sprite.center_x = width // 2
        self.player_sprite.center_y = height // 2

        # Crea listas de sprites para el jugador y las plataformas
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        self.platform_list = arcade.SpriteList()
        # Aquí se podría agregar una plataforma que actúe como suelo

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.platform_list.draw()

    def update(self, delta_time):
        # Aplica la gravedad
        self.player_sprite.change_y -= GRAVITY

        # Actualiza la posición del jugador
        self.player_list.update()

        # Aquí se puede agregar la lógica de colisión para detener la caída del jugador

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

En este ejemplo, en cada actualización se resta la constante `GRAVITY` a la velocidad vertical del sprite del jugador, haciendo que se acelere hacia abajo. Ajusta la constante según sea necesario para obtener el comportamiento deseado. Además, en una implementación completa deberás incluir la lógica de colisión para que el jugador se detenga al chocar con el suelo o con plataformas.
