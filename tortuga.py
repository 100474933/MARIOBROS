"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
import pyxel
from enemigo import Enemigo

class Tortuga (Enemigo):
    """Clase para asinar los atributos y métodos del enemigo de tipo tortuga que no son comunes al resto."""
    def __init__(self):
        super().__init__()
        
        #definimos el tipo de enemigo
        self.__type = 0
        
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type= value

    def __paint(self):
        #si está andando hacia la izquierda
        if self._is_alive and not self._right and not self._volteado and not self._angry:
            if pyxel.frame_count%6:
                pyxel.blt(self._point.x, self._point.y, 2, 13, 26, 12, 17, 0)
            else:
                pyxel.blt(self._point.x, self._point.y, 2, 40, 26, 13, 17, 0)
                
        #si está andando hacia la derecha 
        if self._is_alive and self._right and not self._volteado and not self._angry:
            if pyxel.frame_count%6==0:
                pyxel.blt(self._point.x, self._point.y, 1,77,74,12,17,0)
            else:
                pyxel.blt(self._point.x, self._point.y, 1,90,75,13,17,0)
            
        #si está volteada
        if self._is_alive and self._volteado and not self._angry:
            pyxel.blt(self._point.x, self._point.y, 2,53,26,12,17,0)
            
        #si está andando hacia la izquierda enfadado
        if self._is_alive and not self._right and not self._volteado and self._angry:
            if pyxel.frame_count%6:
                pyxel.blt(self._point.x, self._point.y, 2, 13, 106, 12, 17, 0)
            else:
                pyxel.blt(self._point.x, self._point.y, 2, 32, 106, 14, 17, 0)
                
        #si está andando hacia la derecha enfadado
        if self._is_alive and self._right and not self._volteado and self._angry:
            if pyxel.frame_count%6==0:
                pyxel.blt(self._point.x, self._point.y, 2,54,106,12,17,0)
            else:
                pyxel.blt(self._point.x, self._point.y, 2,74,106,13,17,0)
        
        #si está volteada enfadada
        if self._is_alive and self._volteado and self._angry:
            pyxel.blt(self._point.x, self._point.y, 2,65,26,12,17,0)

    def draw(self):
        self.__paint()