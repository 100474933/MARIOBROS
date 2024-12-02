"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
from point import Point

class Plataformas:
    """Clase para los atributos necesarios para crear un objeto plataforma."""
    def __init__(self, x, y):
        #comprobamos la x e y de cada bloque
        self.__point= Point(x,y)

        #asignamos su ancho y alto
        self.__width= 7
        self.__height= 8
        
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

    

