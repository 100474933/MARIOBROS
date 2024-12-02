"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
import pyxel

class Gameover:
    """Clase para los atirbutos y métodos necesarios para la pantalla de Game Over."""
    def __init__(self):
        #indica que estamos en la pantalla de Game Over
        self.__gameover= 2
    
    @property 
    def get_scene(self):
        return self.__gameover

    def draw(self):
        #dibujamos lo necesario en esta pantalla
        pyxel.blt(89, 80, 0, 67, 150, 72, 8, 0)
        pyxel.text(80,110," -PRESS Q TO QUIT GAME- ", 8)
        