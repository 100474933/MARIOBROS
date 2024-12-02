"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
import pyxel
from point import Point
from cangrejo import Cangrejo 
from mosca import Mosca
from tortuga import Tortuga

class Pow:
    """Clase para crear un objeto pow."""
    def __init__(self):
        #asignamos su posicion
        self.__point= Point(pyxel.width/2-5.5, pyxel.height-63)

        #definimos su estado inicial
        self.__lives=3
        self.__is_alive=True
        self.__chocado=False

        #asignamos ancho y alto
        self.__width=17
        self.__height=17

    @property
    def is_alive(self):
        return self.__is_alive
    
    @is_alive.setter  
    def is_alive(self, value):
        self.__is_alive = value
        
    @property
    def x (self):
        return self.__point.x

    @x.setter 
    def x(self, value):
        self.__point.x=value

    @property
    def y (self):
        return self.__point.y   

    @y.setter 
    def y(self, value):
        self.__point.y=value

    @property 
    def w(self):
        return self.__width
    
    @w.setter
    def w(self, value):
        self.__width = value

    @property
    def h(self):
        return self.__height
    
    @h.setter
    def h(self, value):
        self.__height = value

    @property
    def lives (self):
        return self.__lives

    @lives.setter 
    def lives(self, value):
        self.__lives=value

    @property
    def chocado (self):
        return self.__chocado   

    @chocado.setter 
    def chocado(self, value):
        self.__chocado=value

    def __paint_pow(self):
        #pintamos la forma del pow dependiendo de si ha sido chocado o no
        if not self.__chocado and self.__is_alive:
            pyxel.blt(self.__point.x, self.__point.y, 2,67,81,17,17,0)
        elif self.__chocado and self.__is_alive:
            pyxel.blt(self.__point.x, self.__point.y, 2, 84, 83, 17, 14,0)
    
    def __disappear(self):
        #si las vidas del pow son 0, este desaparece
        if self.__lives==0:
            self.__is_alive=False
    
    def hit_pow(self, enemigos, mario_x, mario_y):
        #comprobamos si Mario ha saltado justo debajo del pow para voltear a los enemigos
        #y restar una vida a Mario
        if (mario_y>self.__point.y + self.__height and mario_y<160) and (mario_x>self.__point.x-10 and mario_x<self.__point.x+13) and self.__is_alive:
            self.__chocado=True 
            self.__lives-=1
            for enemigo in enemigos:
                if enemigo.ground and (enemigo.type==0 or enemigo.type==2):
                    enemigo.volteado=True
                if enemigo.ground and enemigo.type==1:
                    enemigo.onehit=False
                    enemigo.volteado=True

    def update (self):
        #reiniciamos el estado del pow en caso de haber sido chocado
        if self.__chocado:
            self.__chocado=False

        self.__disappear()

    def draw(self):
        self.__paint_pow()