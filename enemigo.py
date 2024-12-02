"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
import pyxel
import random
from point import Point

class Enemigo:
    """Superclase para asignar los atributos y métodos comunes de los enemigos."""
    def __init__ (self):
        #asignamos estados iniciales
        self._is_alive = True
        self._volteado= False
        self._angry=False
        self._ground=False

        #hacemos que aparezcan aleatoriamente de cada uno de los tubos
        tubo_aleatorio= random.randint(1,2)
        if tubo_aleatorio==1:
            self._point= Point(47, 20)
            self._right=True
        else:
            self._point= Point(190, 20)
            self._right=False

        #asignamos ancho y alto porque todos los enemigos son iguales
        self._width = 14
        self._height = 17

        #asignamos velocidades
        self._speed_x = 0.8
        self._speed_x_angry=1.5

    @property
    def is_alive(self):
        return self._is_alive
    
    @is_alive.setter  
    def is_alive(self, value):
        self._is_alive = value
    
    @property
    def x(self):
        return self._point.x 
    
    @x.setter
    def x(self, value):
        self._point.x = value

    @property
    def y(self):
        return self._point.y 

    @y.setter
    def y(self, value):
        self._point.y = value

    @property 
    def w(self):
        return self._width
    
    @w.setter
    def w(self, value):
        self._width = value

    @property
    def h(self):
        return self._height
    
    @h.setter
    def h(self, value):
        self._height = value

    @property
    def volteado (self):
        return self._volteado
    
    @volteado.setter
    def volteado(self, value):
        self._volteado=value

    @property
    def angry (self):
        return self._angry
    
    @angry.setter
    def angry(self, value):
        self._angry=value

    @property
    def ground (self):
        return self._ground
    
    @ground.setter
    def ground(self, value):
        self._ground=value

    def _turn_right(self):
        #comprobamos si está enfadado o no para poder dibujarlo luego y 
        #sumamos "x" para que se desplace a la derecha 
        if not self._angry:
            self._point.x+=self._speed_x
        else:
            self._point.x+=self._speed_x_angry

    def _turn_left(self):
        #comprobamos si está enfadado o no para poder dibujarlo luego y 
        #restamos "x" para que se desplace a la izquierda
        if not self._angry:
            self._point.x-=self._speed_x
        else:
            self._point.x-=self._speed_x_angry

    def _change_side(self):
        #si el enemigo sobrepasa la pantalla por la derecha aparece por la izquierda
        if self._point.x>255:
            self._point.x=-10
        #si el enemigo sobrepasa la pantalla por la izquierda aparece por la derecha
        if self._point.x<-20:
            self._point.x=255

    def _touching_ground(self):
        #comprobamos si el enemigo está sobre el suelo o plataforma

        #suelo 
        if self._point.y==170:
            self._ground= True

        #plataforma arriba izquierda
        elif self._point.x<113-self._width/3 and self._point.y==51-self._height:
            self._ground= True

        #plataforma arriba derecha
        elif self._point.x>145-self._width and self._point.y==51-self._height:
            self._ground= True

        #plataforma central
        elif self._point.x>77-self._width*0.75 and self._point.x<175-self._width/3 and self._point.y==96-self._height:
            self._ground= True

        #plataforma abajo izquierda
        elif self._point.x<92-self._width/3 and self._point.y==142-self._height:
            self._ground= True

        #plataforma abajo derecha
        elif self._point.x>166-self._width*0.75 and self._point.y==142-self._height:
            self._ground= True

        else:
            self._ground=False

        return self._ground

    def _move (self):
        #comprobamos is el enemigo no está dado la vuelta para hacer que ande
        if not self._volteado:
            #con el random hacemos que cambie de lado aleatoriamente
            a=random.randint(1,1000)
            #si esta mirando a la derecha y el random da menor que 10 cambia de lado, 
            #si no sigue yendo hacia la derecha
            if self._right:
                if a<10:
                    self._turn_left()
                    self._right=False

                else:
                    self._turn_right()
                    self._right=True
            
            #si esta mirando a la izquierda y el random da menor que 10 cambia de lado,
            #si no sigue yendo hacia la izquierda
            else:
                if a<10:
                    self._turn_right()
                    self._right=True

                else:
                    self._turn_left()
                    self._right=False   
    
    def angry(self, enemigos):
        #comprobamos si el enemigo esta volteado y si el pyxel.frame_count es divisible entre 300
        #el enemigo entra en estado angry (hacemos esto para que se queden un rato dados la vuelta)
        for enemigo in enemigos:
            if enemigo._volteado and pyxel.frame_count%300==0:
                    enemigo._volteado=False
                    enemigo._angry=True


    def _disappear(self):
        #si los enemigos alcanzan la parte inferior de la pantalla y sobrepasan los tubos desaparecen
        if (self._point.x<32 and self._point.y==170) or (self._point.x>207 and self._point.y==170):
            self._is_alive=False
    
    def _gravedad(self):
        #asignamos la gravedad a los enemigos
        cont=0
        while not self._touching_ground() and cont<5:
            self._point.y+=1
            cont+=1

    def update(self):
        self._move()
        self._change_side()
        self._gravedad()
        self._disappear()
 
    