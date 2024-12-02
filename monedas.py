"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
import pyxel
import random
from point import Point

class Monedas: 
    """Clase para crear las monedas."""
    def __init__(self):
        #asignamos estado inicial
        self.__is_alive = True
        self.__ground=False

        #hacemos que aparezcan aleatoriamente de cada uno de los tubos
        tubo_aleatorio= random.randint(1,2)
        if tubo_aleatorio==1:
            self.__point= Point(47, 20)
            self.__right=True
        else:
            self.__point= Point(190, 20)
            self.__right=False

        #definimos ancho y alto
        self.__width = 14
        self.__height = 17

        #asignamos velocidad
        self.__speed_x = 1
    
    @property
    def is_alive(self):
        return self.__is_alive
    
    @is_alive.setter  
    def is_alive(self, value):
        self.__is_alive = value
    
    @property
    def x(self):
        return self.__point.x 

    @x.setter  
    def x(self, value):
        self.__point.x = value

    @property
    def y(self):
        return self.__point.y
    
    @y.setter  
    def y(self, value):
        self.__point.y = value

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

    def __turn_right(self):
        #sumamos "x" para que se desplace a la derecha
        self.__point.x+=self.__speed_x

    def __turn_left(self):
        #sumamos "x" para que se desplace a la derecha
        self.__point.x-=self.__speed_x

    def __touching_ground(self):
        #comprobamos si la moneda está sobre el suelo o plataforma

        #suelo 
        if self.__point.y==160:
            self.__ground= True

        #plataforma arriba izquierda
        elif self.__point.x<113-self.__width/3 and self.__point.y==40-self.__height:
            self.__ground= True

        #plataforma arriba derecha
        elif self.__point.x>145-self.__width and self.__point.y==40-self.__height:
            self.__ground= True

        #plataforma en medio izquierda
        elif self.__point.x<50-self.__width/3 and self.__point.y==80-self.__height:
            self.__ground= True

        #plataforma en medio derecha
        elif self.__point.x>201-self.__width*0.75 and self.__point.y==80-self.__height:
            self.__ground= True

        #plataforma central
        elif self.__point.x>77-self.__width*0.75 and self.__point.x<175-self.__width/3 and self.__point.y==83-self.__height:
            self.__ground= True

        #plataforma abajo izquierda
        elif self.__point.x<92-self.__width/3 and self.__point.y==132-self.__height:
            self.__ground= True

        #plataforma abajo derecha
        elif self.__point.x>166-self.__width*0.75 and self.__point.y==132-self.__height:
            self.__ground= True

        else:
            self.__ground=False

        return self.__ground

    def __change_side(self):
        #si la moneda sobrepasa la pantalla por la derecha aparece por la izquierda
        if self.__point.x>255:
            self.__point.x=-10
        
        #si la moneda sobrepasa la pantalla por la izquierda aparece por la derecha
        if self.__point.x<-20:
            self.__point.x=255

    def __move (self):
        #llamamos a las funciones que hacen que la moneda se desplace dependiendo 
        #del tubo por el que haya salido
        if self.__right:
            self.__turn_right()

        else:
            self.__turn_left() 

    def __paint_moneda(self):
        #pintamos la moneda según el frame count para que parezca que gira
        if self.__is_alive and pyxel.frame_count%10>5:
            pyxel.blt(self.__point.x, self.__point.y,  1, 63, 17, 9, 12, 0)

        elif self.__is_alive and pyxel.frame_count%10>2:
            pyxel.blt(self.__point.x, self.__point.y,  0, 159, 137, 5, 12, 0)

        else:
            pyxel.blt(self.__point.x, self.__point.y,  1, 53, 11, 5, 12, 0)
    
    def __gravedad(self):
        #asignamos la gravedad
        cont=0
        while not self.__touching_ground() and cont<5:
            self.__point.y+=1
            cont+=1

    def __disappear(self):
        #si las monedas alcanzan la parte inferior de la pantalla y sobrepasan los tubos desaparecen
        if (self.__point.x<32 and self.__point.y==160) or (self.__point.x>207 and self.__point.y==160):
            self.__is_alive=False

    def update(self):
        self.__move()
        self.__change_side()
        self.__gravedad()
        self.__disappear()

    def draw(self):
        self.__paint_moneda()