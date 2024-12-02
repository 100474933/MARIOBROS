"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
import pyxel
from intro import  Intro
from level import Level
from gameover import Gameover
from win import Win

class Game:
    """Clase para jugar, es el main con el que ejecutar el juego."""
    __num_nivel:int

    def __init__(self):
        pyxel.init(250, 200, title= "Mario Bros")

        #importamos los assets necesarios
        pyxel.load("marioassets.pyxres") 

        #musica en bucle durante todo el juego
        pyxel.play(0,0,loop=True)

        #creamos objetos de intro, level, gameover y win
        self.__intro= Intro()
        self.__gameover= Gameover()
        self.__win=Win()
        self.__num_nivel=0

        #indicamos la escena en la que nos encontramos
        self.__scene= 0
        pyxel.run(self.update, self.draw)

    def __check_scene(self):
        #comprobamos en qué escena estamos
        if self.__scene==0:
            self.__intro.update()
            if self.__intro.get_scene==1:
                self.__scene= 1
                self.__level= Level(2,3,15)
                self.__num_nivel=1

        elif self.__scene==1:
            self.__level.update()
            if self.__level.get_scene==2:
                self.__scene= 2

            elif self.__level.get_scene==3 and self.__num_nivel==1:
                self.__num_nivel=2
                self.__level=Level(2,6,10)

            elif self.__level.get_scene==3 and self.__num_nivel==2:
                self.__num_nivel=3
                self.__level=Level(3,9,1)

            elif self.__level.get_scene==3 and self.__num_nivel==3:
                self.__num_nivel=4
                self.__level=Level(4,12,0)

            elif self.__level.get_scene==3 and self.__num_nivel==4:
                self.__scene= 3
            
    def __draw_scene(self):
        #pintamos la escena en la que estamos
        if self.__scene==0:
            self.__intro.draw()
        elif self.__scene==1:
            self.__level.draw()
        elif self.__scene==2:
            self.__gameover.draw()
        elif self.__scene==3:
            self.__win.draw()

    def update(self):
        #comprobamos si se pulsa la tecla Q para salir del juego
        if pyxel.btnp(pyxel.KEY_Q): 
            pyxel.quit()		
        
        #actualizamos la escena
        self.__check_scene()
	
    def draw(self):
        #dibujamos el fondo y la escena correspondiente
        if self.__num_nivel>=1:
            pyxel.cls(self.__level.color)
        else:
            pyxel.cls(0)
        self.__draw_scene()
		
Game()