A continuación se muestra la traducción al formato Markdown para el Paso 14:

---

## Paso 14 - Múltiples Niveles

A medida que tu juego crece, es probable que necesites manejar diferentes niveles o etapas. En este paso aprenderás cómo organizar y cargar múltiples niveles en tu juego, permitiendo transiciones entre ellos y facilitando la expansión de tu proyecto.

### Conceptos Clave

- **Separar la Lógica por Nivel:**  
  Cada nivel puede tener su propio mapa, enemigos, plataformas y objetos. Lo ideal es encapsular la configuración de cada nivel en funciones o incluso archivos separados para facilitar el mantenimiento y la escalabilidad.

- **Función de Configuración del Nivel:**  
  Es recomendable crear una función, por ejemplo `setup_level()`, que reciba como parámetro el número o identificador del nivel y se encargue de configurar la escena (o *Scene*) correspondiente.

- **Transiciones entre Niveles:**  
  Puedes definir condiciones (como alcanzar cierta posición o recoger un objeto) que indiquen que el jugador ha completado el nivel. Cuando esto ocurra, incrementas el número de nivel y vuelves a llamar a la función de configuración para cargar el siguiente nivel.

### Ejemplo Completo

El siguiente ejemplo ilustra cómo implementar múltiples niveles en un juego utilizando Arcade:

```python
import arcade

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ejemplo: Múltiples Niveles"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.current_level = 1
        self.scene = None
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
        # Posición inicial del jugador
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 150
        
        # Variable para almacenar el nivel actual
        self.setup_level(self.current_level)
        
    def setup_level(self, level):
        """Configura el nivel actual cargando la escena correspondiente."""
        # En una implementación real, aquí podrías cargar un mapa TMX u otra configuración específica para cada nivel.
        self.scene = arcade.Scene()
        
        # Agrega el jugador a la escena
        self.scene.add_sprite("Player", self.player_sprite)
        
        # Configuración del nivel según el número
        if level == 1:
            # Configuración para el nivel 1
            # Ejemplo: agregar plataformas, enemigos, monedas, etc.
            platform = arcade.SpriteSolidColor(200, 20, arcade.color.DARK_BROWN)
            platform.center_x = 400
            platform.center_y = 50
            self.scene.add_sprite("Platforms", platform)
        elif level == 2:
            # Configuración para el nivel 2
            # Se podría cambiar el diseño del nivel, agregar nuevos desafíos, etc.
            platform = arcade.SpriteSolidColor(300, 20, arcade.color.DARK_BROWN)
            platform.center_x = 400
            platform.center_y = 50
            self.scene.add_sprite("Platforms", platform)
            # Puedes agregar otros elementos específicos del nivel 2 aquí.
        # Puedes seguir añadiendo configuraciones para niveles adicionales.
    
    def on_draw(self):
        arcade.start_render()
        if self.scene:
            self.scene.draw()
    
    def update(self, delta_time):
        # Actualiza la escena y el jugador
        if self.scene:
            self.scene.update()
        
        # Ejemplo de lógica para cambiar de nivel:
        # Si el jugador alcanza cierta posición en X, se carga el siguiente nivel.
        if self.player_sprite.center_x > SCREEN_WIDTH:
            self.current_level += 1
            self.setup_level(self.current_level)
            # Reinicia la posición del jugador
            self.player_sprite.center_x = 100

    def on_key_press(self, key, modifiers):
        # Permite mover al jugador usando teclas de dirección
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.UP:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5

    def on_key_release(self, key, modifiers):
        # Detiene el movimiento del jugador al soltar la tecla
        if key in (arcade.key.RIGHT, arcade.key.LEFT):
            self.player_sprite.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN):
            self.player_sprite.change_y = 0

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

### Explicación del Código

- **Configuración Inicial:**  
  En el constructor (`__init__`), se inicializa el número de nivel y se configura el primer nivel llamando a `setup_level(self.current_level)`.

- **Función `setup_level()`:**  
  Dependiendo del valor de `level`, se configura la escena. En este ejemplo se muestra una configuración básica para dos niveles, agregando una plataforma distinta en cada uno.

- **Transición de Nivel:**  
  En el método `update()`, se comprueba si el jugador ha alcanzado una posición que indique el final del nivel (por ejemplo, salir de la parte derecha de la pantalla). Si es así, se incrementa el número de nivel y se vuelve a configurar la escena.

- **Control del Jugador:**  
  Se gestionan los eventos de teclado para mover al jugador y se detiene su movimiento al soltar las teclas.

Con esta estructura, puedes extender fácilmente el juego agregando más niveles y configuraciones específicas para cada uno.

---

¿Hay algo más en lo que pueda ayudarte o continuamos con alguna otra parte del tutorial?
