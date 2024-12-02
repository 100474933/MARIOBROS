"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
from enemigo import Enemigo
import pyxel

class Cangrejo(Enemigo):
    """Clase para asignar los atributos y métodos del enemigo de tipo cangrejo que no son comunes al resto."""
    def __init__(self):
        #heredamos de la clase enemigo el init
        super().__init__()

        #asignamos su estado inicial
        self.__onehit= False

        #definimos el tipo de enemigo
        self.__type = 1
 
    @property
    def onehit (self):
        return self.__onehit
    
    @onehit.setter
    def onehit(self, value):
        self.__onehit=value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type= value
   
    def __paint(self):
        #si está andando hacia la izquierda con 0 hits
        if self._is_alive and not self._right and not self._volteado and not self._angry  and not self.__onehit:
            pyxel.blt(self._point.x, self._point.y, 2, 34, 45, 17, 17,0)
        
        #si está andando hacia la izquierda con 1 hit
        if self._is_alive and not self._right and not self._volteado and not self._angry and self.__onehit:
            pyxel.blt(self._point.x, self._point.y, 2, 92, 45, 16, 17,0)   

        #si está andando hacia la derecha con 0 hits
        if self._is_alive and self._right and not self._volteado and not self._angry  and not self.__onehit:
            pyxel.blt(self._point.x, self._point.y, 2, 34, 45, 17, 17,0)
        
        #si está andando hacia la derecha con 1 hit
        if self._is_alive and self._right and not self._volteado and not self._angry and self.__onehit:
            pyxel.blt(self._point.x, self._point.y, 2, 92, 45, 16, 17, 0)

        #si está volteada
        if self._is_alive and self._volteado and not self._angry and not self.__onehit:
            pyxel.blt(self._point.x, self._point.y, 2, 143, 44, 17, 17,0)

        #si está andando hacia la izquierda enfadada con 0 hits
        if self._is_alive and not self._right and not self._volteado and self._angry and not self.__onehit:
            pyxel.blt(self._point.x, self._point.y, 2, 17, 45,  17, 16,0)
        
        #si está andando hacia la izquierda enfadada con 1 hit
        if self._is_alive and not self._right and not self._volteado and self._angry and self.__onehit:
            pyxel.blt(self._point.x, self._point.y, 2, 109, 45, 17, 17,0)  

        #si está andando hacia la derecha enfadada con 0 hits
        if self._is_alive and self._right and not self._volteado and self._angry and not self.__onehit:
            pyxel.blt(self._point.x, self._point.y, 2, 17, 45, 17, 16,0)
        
        #si está andando hacia la derecha enfadada con 1 hit
        if self._is_alive and self._right and not self._volteado and self._angry and self.__onehit:
            pyxel.blt(self._point.x, self._point.y, 2, 109, 45, 17, 17,0)   

        #si está volteada angry
        if self._is_alive and self._volteado and self._angry and not self.__onehit:
            pyxel.blt(self._point.x, self._point.y, 2, 160, 47, 17, 14,0) 

    def draw(self):
        self.__paint()