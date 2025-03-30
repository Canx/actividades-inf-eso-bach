## Paso 11 - Usar una Escena

Hasta ahora, en nuestro juego hemos tenido tres SpriteLists: uno para el jugador, otro para las paredes (suelo y cajas) y otro para las monedas. Esto aún es manejable, pero ¿qué pasará cuando nuestro juego crezca? Probablemente te imagines que un juego podría terminar utilizando cientos de SpriteLists. Con el enfoque actual, tendríamos que gestionar una variable para cada uno y asegurarnos de dibujarlas en el orden correcto.

Arcade nos ofrece una forma mejor de manejar esto mediante la clase `arcade.Scene`. Esta clase se encargará de almacenar todas nuestras SpriteLists, permitiéndonos crear nuevas, cambiar el orden en el que se dibujan y mucho más. En capítulos posteriores utilizaremos una función especial para cargar un mapa desde una herramienta de edición y crear automáticamente una Scene basada en dicho mapa.

Al final de este capítulo, obtendrás el mismo resultado que antes, pero el código será algo diferente al utilizar el objeto Scene.

### Reemplazar las SpriteLists por una Scene

Primero, podemos eliminar todas las variables de tipo SpriteList de nuestro método `__init__` y reemplazarlas por una variable que contenga el objeto Scene:

```python
self.scene = None
```

Luego, al comienzo de nuestro método `setup`, inicializamos la escena de la siguiente forma:

```python
self.scene = arcade.Scene()
```

A continuación, eliminamos la línea en `setup` que inicializaba el SpriteList del jugador. Esa línea lucía así:

```python
self.player_list = arcade.SpriteList()
```

Luego, en lugar de agregar el jugador al SpriteList del jugador, lo agregaremos a la Scene. Por ejemplo, si anteriormente hacíamos:

```python
self.player_list.append(self.player_sprite)
```

Ahora lo haremos de la siguiente forma:

```python
self.scene.add_sprite("Player", self.player_sprite)
```

De esta manera, la Scene se encargará de gestionar y organizar todos los SpriteLists (o grupos de sprites) para nosotros, facilitando la administración a medida que el juego se vuelve más complejo.
