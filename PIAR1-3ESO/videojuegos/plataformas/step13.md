## Paso 13 - Más Tipos de Capas

En este paso aprenderás a trabajar con diferentes tipos de capas que pueden estar presentes en un mapa creado con un editor como Tiled. Además de las capas básicas de plataformas o suelos, existen otros tipos de capas que permiten agregar detalles visuales, definir áreas de colisión, colocar objetos interactivos y mucho más.

### Tipos de Capas Comunes

- **Capas de Fondo:**  
  Se utilizan para dibujar imágenes o patrones que conforman el fondo del nivel. Estas capas aportan a la ambientación visual del juego sin afectar la jugabilidad.

- **Capas de Objetos:**  
  Contienen objetos o entidades que pueden ser interactivos, como puntos de inicio, zonas de activación o elementos decorativos. Suelen incluir información adicional (como propiedades personalizadas) para definir comportamientos específicos.

- **Capas de Colisión:**  
  Definen áreas en las que se deben detectar colisiones. Estas capas permiten establecer barreras o límites que impiden que el jugador u otros objetos atraviesen determinadas zonas.

### Integración de Capas en Arcade

Cuando cargas un mapa desde Tiled usando Arcade, cada capa se convierte en un grupo dentro de la Scene. Esto te permite acceder a ellas y manipularlas de forma individual, lo que facilita la organización y el control del orden en que se dibujan.

Por ejemplo, si tu mapa tiene una capa llamada `"Ground"`, puedes acceder a ella de la siguiente manera:

```python
# Acceder a la capa de suelo
ground_layer = self.scene["Ground"]
```

Y de igual forma para otras capas, por ejemplo, la de objetos:

```python
# Acceder a la capa de objetos
object_layer = self.scene["Objects"]
```

### Ejemplo Completo

A continuación se muestra un ejemplo que integra la carga de un mapa con múltiples tipos de capas en una Scene:

```python
import arcade
from arcade.experimental import tiled

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ejemplo: Más Tipos de Capas"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        
        # Cargar el mapa creado en Tiled
        self.tile_map = tiled.read_tmx("resources/maps/mi_mapa.tmx")
        # Crear la Scene a partir del mapa
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

    def on_draw(self):
        arcade.start_render()
        # Dibuja todos los grupos de sprites según el orden definido en la Scene
        self.scene.draw()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

> **Nota:**  
> La estructura y los nombres de las capas dependen de cómo configures tu mapa en Tiled. Revisa las propiedades de cada capa y asegúrate de que los nombres que usas en el código coincidan con los definidos en el editor.
