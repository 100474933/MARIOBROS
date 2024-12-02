"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
import pyxel
from pow import Pow
from point import Point
from cangrejo import Cangrejo 
from mosca import Mosca
from tortuga import Tortuga

class Mario:
    """Clase para crear el personaje principal."""
    def __init__(self):       
        #definimos posicion inicial
        self.__point= Point(45, 187-22) #coordenada de x donde empieza mario y de Y donde empieza el suelo menos la altura de mario
        
        #ancho y alto de Mario
        self.__width= 17
        self.__height= 22

        #adignamos estado inicial
        self.__is_alive=True
        self.__lives= 3  
        self.__win=False
        self.__right=True
        self.__ground=True
        self.__hit=False

        #asignamos velocidades
        self.__speed_x= 2
        self.__speed_y= 1

        #asignamos puntuación inicial
        self.__score= 0
        self.__max_score= 0

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
    
    @property
    def lives (self):
        return self.__lives   

    @lives.setter
    def lives (self, value):
        self.__lives=value

    @property
    def win (self):
        return self.__win
    
    @win.setter
    def win(self, value):
        self.__win= value
        
    @property
    def score(self):
        return self.__score

    @score.setter
    def score (self,value):
        self.__score=value
    
    def __reset(self):
        #en caso de que Mario pierda una vida, vuelve a la posicion inicial con un score de 0 puntos
        self.__point = Point(45, 187-22)	
        self.__is_alive = True
        self.__score = 0
    
    def __turn_right(self):
        #sumamos "x" para que se desplace a la derecha
        self.__point.x+=self.__speed_x

    def __turn_left(self):
        #restamos "x" para que se desplace a la izquierda
        self.__point.x-=self.__speed_x

    def __jump(self, pow):
        #comprobamos si está en el suelo para poder ejecutar el salto
        if self.__ground: 
            cont=0
            #si el contador es menor que 62 o si no ha tocado una plataforma con la cabeza
            #puede seguir saltando, para lo que restamos "y"
            while cont< 62 and not self.__hit_platform(pow):
                self.__point.y-=self.__speed_y
                cont+=1
            self.__ground=False

    def __change_side(self):
        #si mario sobrepasa la pantalla por la derecha aparece por la izquierda
        if self.__point.x>265:
            self.__point.x=-10
        #si mario sobrepasa la pantalla por la izquierda aparece por la derecha
        if self.__point.x<-20:
            self.__point.x=255

    def __move (self, pow):
        #si presionamos la tecla izquierda llamamos al método que hace que se desplace a la izquierda
        if pyxel.btn(pyxel.KEY_LEFT):
            self.__turn_left()

        #si presionamos la tecla derecha llamamos al método que hace que se desplace a la derecha
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.__turn_right()
        
        #si presionamos la tecla up llamamos al método que hace que salte
        if pyxel.btn(pyxel.KEY_UP):
            self.__jump(pow)

        #si presionamos la tecla derecha y up llamamos al método que hace que se desplace a 
        #la derecha y salte a la vez
        if pyxel.btn(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_RIGHT):
            self.__jump(pow)
            self.__turn_right()

        #si presionamos la tecla izquierda y up llamamos al método que hace que se desplace a 
        #la izquierda y salte a la vez
        if pyxel.btn(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_LEFT):
            self.__jump(pow)
            self.__turn_left()

    def __paint_player(self):
        #si estamos quietos (sin pulsar teclas) mirando a la derecha
        if self.__right and not pyxel.btn(pyxel.KEY_RIGHT) and not pyxel.btn(pyxel.KEY_UP):
                pyxel.blt(self.__point.x, self.__point.y, 1, 4, 71, 17, 21, 0)
                
        #si estamos quietos (sin pulsar teclas) mirando a la izquierda
        if not self.__right and not pyxel.btn(pyxel.KEY_LEFT) and not pyxel.btn(pyxel.KEY_UP):
                pyxel.blt(self.__point.x, self.__point.y, 1, 90, 39, 17, 21, 0)
                
        #para correr a la izquierda
        if pyxel.btn(pyxel.KEY_LEFT):
            self.__right=False
            if pyxel.frame_count%4==0:
                pyxel.blt(self.__point.x, self.__point.y, 1,48,39,16,21,0)
            else:
                pyxel.blt(self.__point.x, self.__point.y, 1,48,119,15,21,0)
            
        #para correr a la derecha
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.__right=True
            if pyxel.frame_count%4==0:
                pyxel.blt(self.__point.x, self.__point.y, 1,23,71,16,21,0)
            else:
                pyxel.blt(self.__point.x, self.__point.y, 1,24,119,15,21,0)
        
        #para saltar
        if pyxel.btn(pyxel.KEY_UP):
            if self.__right and not pyxel.btn(pyxel.KEY_RIGHT):
                pyxel.blt(self.__point.x, self.__point.y, 1,2,40,16,22,0)
            if not self.__right and not pyxel.btn(pyxel.KEY_LEFT):
                pyxel.blt(self.__point.x, self.__point.y, 1,5,120,16,22,0)
    
    
    def voltear_enemigos(self, enemigos, plataformas):
        #recorremos la lista de enemigos, deoendiendo del tipo y si esta en el suelo comprobamos 
        #coordenadas para darles la vuelta
        for enemigo in enemigos:
            if enemigo.type==0 and enemigo.ground:
                if (self.__point.x>enemigo.x-5 and self.__point.x<enemigo.x+enemigo.w) and (self.__point.y>enemigo.y+enemigo.h and self.__point.y<enemigo.y+enemigo.h+plataformas.h+5):
                    enemigo.volteado=True

            if enemigo.type==1 and enemigo.ground:
                #para el cangrejo, si le damos una vez cambia de forma, si le damos dos veces se da la vuelta
                if not enemigo.onehit and not enemigo.volteado and (self.__point.x>enemigo.x-5 and self.__point.x<enemigo.x+enemigo.w) and  (self.__point.y>enemigo.y+enemigo.h and self.__point.y<enemigo.y+enemigo.h+plataformas.h+5):
                    enemigo.onehit=True
                elif enemigo.onehit and(self.__point.x>enemigo.x-5 and self.__point.x<enemigo.x+enemigo.w) and  (self.__point.y>enemigo.y+enemigo.h and self.__point.y<enemigo.y+enemigo.h+plataformas.h+1):
                    enemigo.onehit=False
                    enemigo.volteado=True

            if enemigo.type==2 and enemigo.ground:
                if (self.__point.x>enemigo.x-5 and self.__point.x<enemigo.x+enemigo.w) and  (self.__point.y>enemigo.y+enemigo.h and self.__point.y<enemigo.y+enemigo.h+plataformas.h+5):
                    enemigo.volteado=True
                    
    """
    def desvoltear_enemigos(self, enemigos, plataformas):
        #recorremos la lista de enemigos para comprobar si el enemigo está dado la vuelta, 
        #si es así y le volvemos a dar desde abajo, vuelve a andar
        for enemigo in enemigos:
            if enemigo.volteado and pyxel.frame_count%2>0.3:
                if (self.__point.x>enemigo.x-5 and self.__point.x<enemigo.x+enemigo.w) and (self.__point.y>enemigo.y+enemigo.h+plataformas.h and self.__point.y<enemigo.y+enemigo.h+plataformas.h+5):
                    enemigo.volteado=False
    """

    def matar_enemigos(self, enemigos):
        #comprobamos si el enemigo está dado la vuelta y si es así y Mario entra en contacto con ellos
        #desde los lados, les mata y gana puntos
        for enemigo in enemigos:
            if enemigo.volteado and (enemigo.type==0 or enemigo.type==2):
                if (self.__point.x>enemigo.x-self.__width and self.__point.x<enemigo.x+enemigo.w) and (self.__point.y>enemigo.y-self.__height and self.__point.y<enemigo.y+enemigo.h):
                    enemigo.is_alive=False
                    pyxel.play(1,1) #sonido al matar enemigo
                    self.__score+=800 #matar tortuga y mosca 800 puntos
                    
            if enemigo.volteado and enemigo.type==1:
                if (self.__point.x>enemigo.x-self.__width and self.__point.x<enemigo.x+enemigo.w) and (self.__point.y>enemigo.y-self.__height and self.__point.y<enemigo.y+enemigo.h):
                    enemigo.is_alive=False
                    pyxel.play(1,1) #sonido al matar enemigo
                    self.__score+=1000 #matar cangrejo 1000 puntos

    def morir(self, enemigos):  
        #si los enemigos están andando y rozan a Mario, le quitan una vida y llamamos a la funcion reset
        for enemigo in enemigos:
                if not enemigo.volteado:
                    if (self.__point.x>enemigo.x-self.__width and self.__point.x<enemigo.x+enemigo.w) and (self.__point.y>enemigo.y-self.__height and self.__point.y<enemigo.y+enemigo.h):
                        self.__lives-=1
                        pyxel.play(1,3) #sonido al perder una vida
                        self.__reset()

    def coger_moneda(self, monedas):
        #si Mario entra en contacto con una Moneda, la recoge, suma puntos e incrementa el contador de monedas
        monedas_recogidas=0
        for moneda in monedas:
            if (self.__point.x>moneda.x-self.__width and self.__point.x<moneda.x+moneda.w) and (self.__point.y>moneda.y-self.__height*0.75 and self.__point.y<moneda.y+moneda.h):
                moneda.is_alive=False
                pyxel.play(1,2) #sonido al coger moneda
                monedas_recogidas+=1
                self.__score+=100 #coger moneda 100 puntos
        return monedas_recogidas

    def ganar(self, enem_max):
        #comprobamos si Mario ha ganado la partida si ha derrotado a todos los enemigos y le quedan vidas
        if enem_max==0 and self.__lives>0:
            self.__win=True

    def __paint_lives(self):
        #pintamos las vidas que le quedan a Mario
        x=54
        for i in range (self.__lives):
            pyxel.blt(x, 17, 1,188,103,9,7,0)
            x+=11

    def __paint_score(self):
        #pintamos el score actual y el máximo conseguido en ese nivel
        score = str(self.__score)
        pyxel.text(35,7, score, 7)

        max_score=str(self.__max_score)
        if self.__score>self.__max_score:
            self.__max_score=self.__score
        pyxel.text(114,7, max_score, 7)

    def __touching_ground(self, pow):
        #comprobamos si Mario está sobre el suelo o plataforma

        #suelo 
        if self.__point.y==165:
            self.__ground= True

        #plataforma arriba izquierda
        elif self.__point.x<113-self.__width/3 and self.__point.y==51-self.__height:
            self.__ground= True

        #plataforma arriba derecha
        elif self.__point.x>145-self.__width*0.75 and self.__point.y==51-self.__height:
            self.__ground= True

        #plataforma en medio izquierda
        elif self.__point.x<50-self.__width/3 and self.__point.y==101-self.__height:
            self.__ground= True

        #plataforma en medio derecha
        elif self.__point.x>201-self.__width*0.75 and self.__point.y==101-self.__height:
            self.__ground= True

        #plataforma central
        elif self.__point.x>77-self.__width*0.90 and self.__point.x<175-self.__width/3 and self.__point.y==96-self.__height:
            self.__ground= True

        #plataforma abajo izquierda
        elif self.__point.x<92-self.__width/3 and self.__point.y==142-self.__height:
            self.__ground= True

        #plataforma abajo derecha
        elif self.__point.x>166-self.__width*0.75 and self.__point.y==142-self.__height:
            self.__ground= True
 
        #pow
        elif pow.is_alive and self.__point.x>119-self.__width*0.75 and self.__point.x<136-self.__width/3 and self.__point.y==137-self.__height:
            self.__ground= True
            
        else:
            self.__ground=False

        return self.__ground

    
    def __hit_platform(self, pow): 
        #comprobamos si Mario ha dado a una plataforma con la cabeza

        #plataforma arriba izquierda
        if self.__point.x<113-self.__width/3 and self.__point.y==52:
            self.__hit= True

        #plataforma arriba derecha
        elif self.__point.x>145-self.__width*0.75 and self.__point.y==52:
            self.__hit=True

        #plataforma en medio izquierda
        elif self.__point.x<50-self.__width/3 and self.__point.y==103:
            self.__hit=True

        #plataforma en medio derecha
        elif self.__point.x>201-self.__width*0.75 and self.__point.y==103:
            self.__hit=True

        #plataforma central
        elif self.__point.x>77-self.__width*0.75 and self.__point.x<175-self.__width/3 and self.__point.y==97:
            self.__hit=True

        #plataforma abajo izquierda
        elif self.__point.x<92-self.__width/3 and self.__point.y==145:
            self.__hit=True

        #plataforma abajo derecha
        elif self.__point.x>166-self.__width*0.75 and self.__point.y==145:
            self.__hit=True
        
        #pow
        elif pow.is_alive and self.__point.x>119-self.__width*0.75 and self.__point.x<136-self.__width/3 and self.__point.y==170-self.__height:
            self.__hit= True
        
        else:
            self.__hit=False
        
        return self.__hit

    def __gravedad(self,pow):
        #implementamos la gravedad a Mario
        cont=0
        while not self.__touching_ground(pow) and cont<4:
            self.__point.y+=1
            cont+=1

    def update(self, pow):
        self.__move(pow)
        self.__change_side()
        self.__gravedad(pow)

    def draw(self):
        self.__paint_player()
        self.__paint_lives()
        self.__paint_score()