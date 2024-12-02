"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
import pyxel

class Win:
    """Clase para los atirbutos y métodos necesarios para la pantalla de Win."""
    def __init__(self):
        #indica que estamos en la pantalla de Win
        self.__win= 3
    
    @property 
    def get_scene(self):
        return self.__win

    def draw(self):
        pyxel.blt(75, 60, 1, 4, 71, 17, 21, 0) #mario
        pyxel.blt(100, 66, 0, 157, 157, 67, 11, 0) #YOU WON
        
        pyxel.text(80,140," -PRESS Q TO QUIT GAME- ", 8)
        pyxel.text(30,165," -JUEGO HECHO POR OLIVIA GRIMA Y MARÍA ROBLEDANO- ", 7)

