## Paso 2 - Texturas y Sprites

Nuestro siguiente paso en este tutorial es dibujar algo en la pantalla. Para ello, necesitamos cubrir dos temas: **Texturas** y **Sprites**.

Al final de este capítulo, tendremos algo que se verá así. Es en gran medida lo mismo que en el capítulo anterior, pero ahora estamos dibujando un personaje en la pantalla:

![Ejemplo de pantalla con personaje](images/title_02.png)

### Texturas

Las texturas son, en esencia, un objeto que contiene datos de una imagen. Cada vez que cargas un archivo de imagen en Arcade, por ejemplo, un archivo `.png` o `.jpeg`, se crea una textura.

Para ello, internamente Arcade utiliza Pyglet para cargar los datos de la imagen, y la textura se encarga de mantener estos datos.

Podemos crear una textura con un comando sencillo, y esto se puede hacer dentro de la función `__init__`. Procede a crear una textura que utilizaremos para dibujar a un jugador:

```python
self.player_texture = arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
```

> **Nota:**  
> Es posible que te preguntes de dónde proviene este archivo de imagen y qué significa `:resources:`.  
>  
> La sección `:resources:` de la cadena es lo que Arcade denomina un *resource handle* (manejador de recursos). Puedes registrar tus propios resource handles para diferentes directorios de activos. Por ejemplo, podrías querer tener un handle `:characters:` y otro `:objects:`.  
>  
> Sin embargo, no es obligatorio usar un resource handle para cargar tus imágenes.

### Sprites

Los sprites son objetos que usan texturas para representarse visualmente en la pantalla. Un sprite contiene no solo la textura, sino también datos relacionados con su posición, escala, rotación y otros atributos visuales.

> **Nota:**  
> La funcionalidad de sprites es muy útil para animar personajes, gestionar colisiones y organizar los elementos visuales en tu juego.

A continuación, se muestra un ejemplo básico de cómo crear un sprite utilizando una textura:

```python
import arcade

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Carga la textura y crea un sprite
        self.player_texture = arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
        self.player_sprite = arcade.Sprite()
        self.player_sprite.texture = self.player_texture
        self.player_sprite.center_x = width // 2
        self.player_sprite.center_y = height // 2

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()

def main():
    window = MyGame(800, 600, "Ejemplo: Texturas y Sprites")
    arcade.run()

if __name__ == "__main__":
    main()
```

Este código carga la textura del personaje y la asigna a un sprite, que se posiciona en el centro de la ventana y se dibuja en la pantalla.
