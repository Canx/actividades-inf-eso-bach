## Paso 12 - Cargar un Mapa desde un Editor de Mapas

En este capítulo aprenderás a cargar un mapa creado con un editor (como Tiled) en tu juego de Arcade. Gracias a las funciones que Arcade ofrece, podrás importar el mapa y convertir las capas definidas en listas de sprites, facilitando la gestión de colisiones, fondos y otros elementos.

### Exportar el Mapa desde Tiled

1. **Crear el Mapa:**  
   Utiliza el Tiled Map Editor para diseñar tu nivel, configurando las capas necesarias (por ejemplo, plataformas, objetos, fondos, etc.).

2. **Exportar el Mapa:**  
   Al finalizar, exporta el mapa en un formato compatible, como TMX.

### Cargar el Mapa en Arcade

Arcade dispone de funciones para cargar un mapa en formato TMX. Por ejemplo, puedes usar el módulo experimental `arcade.experimental.tiled`:

```python
import arcade
from arcade.experimental import tiled

# Lee el archivo TMX y crea una representación del mapa
tile_map = tiled.read_tmx("resources/maps/mi_mapa.tmx")
```

### Crear la Escena a partir del Mapa

Una vez cargado el mapa, puedes convertirlo en una escena. Cada capa del mapa se transformará en un grupo dentro de la escena:

```python
# Crea la escena a partir del mapa
scene = arcade.Scene.from_tilemap(tile_map)
```

### Ejemplo Completo

A continuación, se muestra un ejemplo completo que integra la carga del mapa en un juego sencillo:

```python
import arcade
from arcade.experimental import tiled

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ejemplo: Cargar Mapa desde un Editor de Mapas"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        
        # Carga el mapa creado en Tiled
        self.tile_map = tiled.read_tmx("resources/maps/mi_mapa.tmx")
        # Crea la escena a partir del mapa
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

    def on_draw(self):
        arcade.start_render()
        self.scene.draw()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

> **Nota:**  
> Asegúrate de que el archivo `"resources/maps/mi_mapa.tmx"` exista y esté correctamente configurado. Puedes ajustar la ruta y el nombre del archivo según tu proyecto.
