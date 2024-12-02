"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
from enemigo import Enemigo
import pyxel
import random

class Mosca(Enemigo):
    """Clase para asinar los atributos y métodos del enemigo de tipo mosca que no son comunes al resto."""
    def __init__(self):
        super().__init__()
        
        #definimos el tipo de enemigo
        self.__type = 2
        
        #asignamos velocidades de la y
        self.__speed_y=1
        self.__speed_y_angry=1.5

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type= value

    def __fly(self):
        #hacemos que la mosca vuele, para ello comprobamos si esta tocando el suelo
        if self._ground: 
            #comprobamos si esta enfadada o no para dibujarla correctamente
            if self._angry:
                cont=0
                #hacemos un frame count para que se quede en el suelo durante un tiempo y 
                #un contados para determinar su altura máxima
                while cont<20 and pyxel.frame_count%20==0:
                    #restamos "y" para que suba
                    self._point.y-=self.__speed_y_angry
                    self._ground=False
                    #hacemos que se desplace a la izquierda o derecha solo si noestá tocando el suelo
                    if not self._ground:
                        if self._right:
                            self._turn_right()
                        else:
                            self._turn_left()
                    cont+=1

            #hacemos lo mismo que antes pero para cuando no está enfadada
            else:
                cont=0
                while cont<20 and pyxel.frame_count%25==0:
                    self._point.y-=self.__speed_y
                    self._ground=False
                    if not self._ground:
                        if self._right:
                            self._turn_right()
                        else:
                            self._turn_left()
                    cont+=1
            

    def _move (self):
        #como el movimiento es distinto a los otros dos enemigos lo especificamos aquí
        #comprobamos que no esté dada la vuelta
        if not self._volteado:
            #hacemos que vaya hacia un lado u otro aleatoriamente
            a=random.randint(1,1000)
            if self._right:
                #si esta mirando a la derecha y el random da menor que 10 cambia de lado, 
                #si no sigue yendo hacia la derecha
                if a<10:
                    self.__fly()
                    self._right=False

                else:
                    self.__fly()
                    self._right=True

            else:
                #si esta mirando a la izquierda y el random da menor que 10 cambia de lado, 
                #si no sigue yendo hacia la derecha
                if a<10:
                    self.__fly()
                    self._right=True

                else:
                    self.__fly()
                    self._right=False
            
    def __paint(self):
        #si está yendo hacia la izquierda 
        if self._is_alive and not self._right and not self._volteado and not self._angry:
            pyxel.blt(self._point.x, self._point.y, 1, 142, 57, 16, 14,0)

        #si está yendo hacia la derecha 
        if self._is_alive and self._right and not self._volteado and not self._angry:
            pyxel.blt(self._point.x, self._point.y, 1, 142, 57, 16, 14,0)
        
        #si está volteada
        if self._is_alive and self._volteado and not self._angry:
            pyxel.blt(self._point.x, self._point.y, 1, 146, 77, 17, 13,0)

        #si está yendo hacia la izquierda enfadada
        if self._is_alive and not self._right and not self._volteado and self._angry:
            pyxel.blt(self._point.x, self._point.y, 2, 206, 25, 16, 14, 0)
        
        #si está yendo hacia la derecha enfadada
        if self._is_alive and self._right and not self._volteado and self._angry:
            pyxel.blt(self._point.x, self._point.y, 2, 206, 25, 16, 14, 0)

        #si está volteada angry
        if self._is_alive and self._volteado and self._angry:
            pyxel.blt(self._point.x, self._point.y, 2, 147, 30, 17, 13, 0) 

    def update(self):
        self._move()
        self._change_side()
        self._gravedad()
        self._disappear()
 
    def draw(self):
        self.__paint()