"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
import pyxel

class Intro:
    """Clase para los atirbutos y métodos necesarios para la pantalla de la intro."""
    def __init__(self):
        #sirve para detectar que estamos en la introducción
        self.__intro= 0
        
    @property 
    def get_scene(self):
        return self.__intro

    def update(self):
        #comprobamos si seguimos en la intro o si hemos pulsado enter para ir al nivel
        if self.__intro==0:
            if pyxel.btn(pyxel.KEY_RETURN) or pyxel.frame_count>2000:
                self.__intro=1
    
    def draw(self):
        #dibujamos lo necesario para la pantalla de la introducción 
        pyxel.blt(22,25,0,19,10,208,120,0) 
        pyxel.text(65,165," -PRESS ENTER TO START PLAYING- ", 8)