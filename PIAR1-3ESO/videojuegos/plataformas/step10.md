## Paso 10 - Agregar una Puntuación

Nuestro juego está tomando forma, pero aún necesitamos recompensar al jugador por su esfuerzo al recoger monedas. Para ello, añadiremos una puntuación que se incrementará cada vez que se recoja una moneda y se mostrará en la pantalla.

En este capítulo se explica cómo utilizar objetos de tipo `arcade.Text` y se introduce una técnica para usar dos cámaras: una para dibujar objetos en "espacio-mundo" y otra para dibujar objetos en "espacio-pantalla".

> **Nota:**  
> ¿Qué son el espacio-mundo y el espacio-pantalla? Piensa en otros juegos que hayas jugado y compáralos con nuestro juego.  
> 
> - El **espacio-mundo** se refiere a las coordenadas en las que el jugador se mueve dentro del mundo, que puede extenderse más allá de la ventana de visualización, requiriendo una cámara que se desplace en consecuencia.
> - El **espacio-pantalla** se refiere a las coordenadas fijas de la pantalla. Un ejemplo es el indicador de puntuación, que se dibuja en la pantalla y no se mueve cuando la cámara se desplaza.  
> 
> Para lograr esto, usaremos dos cámaras diferentes: la cámara del mundo y la `gui_camera` (cámara de la interfaz gráfica), que se mantendrá fija.

### Inicializar la Puntuación y la `gui_camera`

Primero, añade una variable para la nueva cámara y la puntuación. Inicialízalas tanto en el método `__init__` como en `setup` (si existe un método `setup` en tu código):

```python
self.score = 0
self.gui_camera = arcade.Camera(self.width, self.height)
```

### Dibujar la Puntuación en la Pantalla

Para dibujar el texto en el espacio-pantalla, debemos activar la `gui_camera` al inicio del método `on_draw`. Esto asegura que el texto (la puntuación) permanezca en una posición fija en la pantalla, sin moverse cuando se desplaza la cámara del mundo.

```python
def on_draw(self):
    # Utiliza la cámara del mundo
    self.camera.use()
    arcade.start_render()
    # Dibuja todos los elementos del mundo, como el jugador y las plataformas
    self.player_list.draw()
    self.coin_list.draw()

    # Utiliza la cámara de la GUI para dibujar la puntuación en pantalla
    self.gui_camera.use()
    arcade.draw_text(f"Puntuación: {self.score}", 10, 10, arcade.color.BLACK, 14)
```

### Ejemplo Completo

A continuación, se muestra un ejemplo completo que integra la puntuación y el uso de dos cámaras:

```python
import arcade

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ejemplo: Agregar Puntuación"

PLAYER_MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AZURE_MIST)

        # Crea el sprite del jugador y su lista
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 150

        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Crea la lista de monedas y poblarla
        self.coin_list = arcade.SpriteList()
        for i in range(10):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", scale=0.5)
            coin.center_x = 150 + i * 50
            coin.center_y = 300
            self.coin_list.append(coin)

        # Cargar el sonido de la moneda (si se utiliza en otro paso)
        self.coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")

        # Puntuación inicial
        self.score = 0

        # Inicializa las cámaras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

    def on_draw(self):
        # Dibuja en el espacio-mundo
        self.camera.use()
        arcade.start_render()
        self.player_list.draw()
        self.coin_list.draw()

        # Dibuja en el espacio-pantalla (GUI)
        self.gui_camera.use()
        arcade.draw_text(f"Puntuación: {self.score}", 10, 10, arcade.color.BLACK, 14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.W, arcade.key.DOWN, arcade.key.S):
            self.player_sprite.change_y = 0
        elif key in (arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D):
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        # Actualiza la posición del jugador
        self.player_list.update()

        # Verificar colisiones entre el jugador y las monedas
        coins_hit = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

        # Aquí se actualizaría la posición de la cámara del mundo para seguir al jugador
        position = (self.player_sprite.center_x - self.width / 2,
                    self.player_sprite.center_y - self.height / 2)
        self.camera.move_to(position, 0.1)

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

En este ejemplo se utilizan dos cámaras: la `camera` para el espacio-mundo (donde se mueven el jugador, las monedas, etc.) y la `gui_camera` para el espacio-pantalla, donde se muestra la puntuación de forma fija.
