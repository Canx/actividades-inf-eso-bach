## Paso 8 - Recoger Monedas

En este paso aprenderás cómo implementar la recolección de monedas en tu juego. Se explicará cómo detectar colisiones entre el jugador y las monedas, actualizar la puntuación y eliminar las monedas recogidas del juego.

### Crear y Configurar las Monedas

Primero, debes crear una lista de sprites para las monedas y poblarla con instancias de monedas. Usaremos imágenes de recursos incluidos en Arcade.

```python
# Crear una lista de monedas
self.coin_list = arcade.SpriteList()

# Crear varias monedas y agregarlas a la lista
for i in range(10):
    coin = arcade.Sprite(":resources:images/items/coinGold.png", scale=0.5)
    coin.center_x = 150 + i * 50
    coin.center_y = 300
    self.coin_list.append(coin)
```

### Detectar Colisiones y Actualizar la Puntuación

Dentro del método `update()`, verifica las colisiones entre el jugador y las monedas utilizando `arcade.check_for_collision_with_list()`. Cuando se detecta una colisión, elimina la moneda del juego y aumenta la puntuación:

```python
def update(self, delta_time):
    self.player_list.update()
    
    # Verificar colisiones entre el jugador y las monedas
    coins_hit = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
    for coin in coins_hit:
        coin.remove_from_sprite_lists()
        self.score += 1
```

### Ejemplo Completo

A continuación, se muestra un ejemplo completo que integra la recolección de monedas en el juego:

```python
import arcade

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ejemplo: Recoger Monedas"

PLAYER_MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AZURE_MIST)

        # Crear el sprite del jugador y su lista
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 150

        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Crear la lista de monedas y poblarla
        self.coin_list = arcade.SpriteList()
        for i in range(10):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", scale=0.5)
            coin.center_x = 150 + i * 50
            coin.center_y = 300
            self.coin_list.append(coin)

        # Puntuación inicial
        self.score = 0

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.coin_list.draw()
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
        # Al soltar una tecla, detenemos el movimiento en esa dirección
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

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

En este ejemplo, el jugador puede moverse usando las teclas de dirección o las teclas WASD. Cada vez que el jugador toca una moneda, ésta se elimina del juego y la puntuación aumenta en uno.
