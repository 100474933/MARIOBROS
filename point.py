"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
class Point:
    """Clase para calcular coordenadas x e y de un objeto."""
    def __init__(self, x, y):
        
        #comprobamos que la x e y estén bien dadas
        if type(x) != int and type(x) != float:
            raise TypeError("x debe der un numero")
        else:
            self.__x = x
        
        if type(y) != int and type(y) != float:
            raise TypeError("x debe der un numero")
        else:
            self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value