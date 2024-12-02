"""
-------Juego Mario Bros-------
Olivia Grima y María robledano
"""
import pyxel
import random
from mario import Mario
from pow import Pow
from plataformas import Plataformas
from tortuga import Tortuga
from cangrejo import Cangrejo
from mosca import Mosca
from enemigo import Enemigo
from monedas import Monedas

class Level:
    """Clase para crear el nivel."""
    color:int
    def __init__(self, enem_pantalla_max, enem_max, color):
        #creamos objetos
        self.__mario= Mario()
        self.__enem=Enemigo()
        self.__pow=Pow()
        self.__plataformas=Plataformas(0,50)

        #creamos listas para rellenar luego
        self.__enemigos=[]
        self.__monedas=[]
        self.__platforms_ind=[]

        #introducimos atributos necesarios de las monedas y enemigos
        self.__enem_max=enem_max
        self.__enem_pantalla_max= enem_pantalla_max
        self.__enem_mostrados=0
        self.__mostrados_max=enem_max
        self.__monedas_max=20
        self.__monedas_mostradas=0
        self.__monedas_recogidas=0

        #temporizador que utilizaremos para que las monedas y enemigoa salgan progresivamente
        self.__temporizador=0

        #indica que estamos en el nivel
        self.__level= 1

        #asignamos el color
        self.color=color
    
    @property 
    def get_scene(self):
        return self.__level

    def __monedas_pantalla(self):
        #asignamos un numero maximo de monedas en la pantalla
        monedas_pantalla_max=2

        #si la lista de monedas es mayor que 0 podemos eliminar las monedas que hayan 
        #desaparecido o haya cogido Mario
        if len(self.__monedas)>0:
            i = 0
            while i < len(self.__monedas):
                if not self.__monedas[i].is_alive:
                    del(self.__monedas[i]) #borramos la moneda "muerta"
                else:
                    i +=1
        
        #hacemos que solo aparezcan monedas si el resto del contador entre 45 da 0
        if self.__temporizador%45==0:
            #se añaden monedas a la lista de monedas mientras haya espacio en la pantalla y no se hayan mostrado todas
            if len(self.__monedas) < monedas_pantalla_max and self.__monedas_mostradas<self.__monedas_max:
                m=Monedas()
                self.__monedas.append(m)
                self.__monedas_mostradas+=1 #si se crea una moneda sumamos uno a las monedas mostradas
        self.__temporizador+=1
        
        for e in self.__monedas:
            e.update()

    def __enemigos_pantalla(self):
        #si la lista de enemigos es mayor que 0 podemos eliminar los enemigos que hayan 
        #desaparecido o haya matado Mario
        if len(self.__enemigos)>0:
            i = 0
            while i < len(self.__enemigos):
                if not self.__enemigos[i].is_alive and self.__enem_max>0:
                    del(self.__enemigos[i]) #borramos enemigo muerto
                    self.__enem_max-=1 #restamos uno al numero total de enemigos por nivel
                else:
                    i +=1

        #hacemos que solo aparezcan enemigos si el resto del contador entre 43 da 0
        if self.__temporizador%43==0:
            #se añaden enemigos a la lista de enemigos mientras haya espacio en la pantalla y no se hayan mostrado todos
            if len(self.__enemigos) < self.__enem_pantalla_max and self.__enem_max>0 and self.__enem_mostrados<self.__mostrados_max:
                #se escoge aleatoriamente el tipo de enemigo
                enemigo_aleatorio=random.randint(1,3)
                if enemigo_aleatorio==1:
                    e=Tortuga()
                elif enemigo_aleatorio==2:
                    e=Cangrejo()
                else:
                    e=Mosca() 
                self.__enemigos.append(e)
                self.__enem_mostrados+=1 #si se crea uno, sumamos uno a los enemigos mostrados
        self.__temporizador+=1
        
        for e in self.__enemigos:
            e.update()
    
    def __hit_pow(self):
        #llamamos al método hit pow de la clase Pow
        self.__pow.hit_pow(self.__enemigos, self.__mario.x, self.__mario.y)
    
    def __angry(self):
        #llamamos al método angry pow de la clase Enemigo
        self.__enem.angry(self.__enemigos)

    def __voltear_enemigos(self):
        #llamamos al método voltear de la clase Mario
        self.__mario.voltear_enemigos(self.__enemigos, self.__plataformas)

    """
    def __desvoltear_enemigos(self):
        #llamamos al método desvoltear de la clase Mario
        self.__mario.desvoltear_enemigos(self.__enemigos, self.__plataformas)
    """
    
    def __matar_enemigos(self):
        #llamamos al método matar enemigos de la clase Mario
        self.__mario.matar_enemigos(self.__enemigos)

    def __morir_mario(self):
        #llamamos al método morir de la clase Mario
        self.__mario.morir(self.__enemigos)
    
    def __coger_moneda(self):
        #llamamos al método coger moneda de la clase Mario y sumamos al contador de monedas las que haya cogido
        mr= self.__mario.coger_moneda(self.__monedas)
        self.__monedas_recogidas+=mr
    
    def __ganar(self):
        #llamamos al método ganar de la clase Mario
        self.__mario.ganar(self.__enem_max)
    
    def __paint_background(self):
        pyxel.blt(0,17,1,0,3,48,29,0) #tuberia 1
        pyxel.blt(203,17,1,73,4,48,29,0) #tuberia 2
        pyxel.blt(0,165,1,168,45,34,20,0) #tuberia 3
        pyxel.blt(218,165,1,168,69,34,19,0) #tuberia 4
        pyxel.blt(24,5,1,2,104,8,8,0) #I
        pyxel.blt(85,5,1,64,104,26,8,0) #TOP
        pyxel.blt(160, 3, 1, 63, 17, 9, 12, 0)
        monedas= str(self.__monedas_recogidas)
        pyxel.text (173, 7, monedas, 7)

        cont_x=-10
        cont_y=187
        alternar=0
        for i in range(2):
            cont_x+=alternar
            for j in range (28):
                pyxel.blt(cont_x,cont_y,1,160,104,10,8,0) #suelo
                cont_x+=10
            cont_x=-10
            cont_y+=8
            alternar+=5

    def __paint_platforms(self):
        #plataforma arriba izquierda
        ini_x=0
        ini_y=50

        for bloque in range (16):
            pyxel.blt(ini_x,ini_y,1,3,92,7,8,0)
            self.__platforms_ind.append(Plataformas(ini_x, ini_y))
            ini_x+=7

        #plataforma arriba derecha
        ini_x=145
        for bloque in range (16):
            pyxel.blt(ini_x,ini_y,1,3,92,7,8,0)
            self.__platforms_ind.append(Plataformas(ini_x, ini_y))
            ini_x+=7

        #plataforma en medio izquierda
        ini_x=0
        ini_y=100
        for bloque in range (7):
            pyxel.blt(ini_x,ini_y,1,3,92,7,8,0)
            self.__platforms_ind.append(Plataformas(ini_x, ini_y))
            ini_x+=7

        #plataforma en medio derecha
        ini_x=201
        for bloque in range (7):
            pyxel.blt(ini_x,ini_y,1,3,92,7,8,0)
            self.__platforms_ind.append(Plataformas(ini_x, ini_y))
            ini_x+=7

        #plataforma central
        ini_x= 77
        ini_y=95
        for bloque in range (14):
            pyxel.blt(ini_x,ini_y,1,3,92,7,8,0)
            self.__platforms_ind.append(Plataformas(ini_x, ini_y))
            ini_x+=7
        
        #plataforma abajo izquierda
        ini_x=0
        ini_y=142
        for bloque in range (13):
            pyxel.blt(ini_x, ini_y,1,3,92,7,8,0)
            self.__platforms_ind.append(Plataformas(ini_x, ini_y))
            ini_x+=7

        #plataforma abajo derecha
        ini_x=166  
        for bloque in range (12):
            pyxel.blt(ini_x, ini_y,1,3,92,7,8,0)
            self.__platforms_ind.append(Plataformas(ini_x, ini_y))
            ini_x+=7
            
    def __paint_monedas(self):
        for moneda in self.__monedas:
            moneda.draw()

    def __paint_enemigo(self):
        for enemigo in self.__enemigos:
            enemigo.draw()

    def update(self):
        self.__mario.update(self.__pow)
        self.__pow.update()
        self.__enemigos_pantalla()
        self.__monedas_pantalla()
        self.__hit_pow()
        self.__angry()
        self.__voltear_enemigos()
        #self.__desvoltear_enemigos()
        self.__matar_enemigos()
        self.__morir_mario()
        self.__coger_moneda()
        self.__ganar()

        #comprobamos si seguimos en la pantalla del nivel o si hemos cambiado a otra pantalla
        if self.__level==1:
            if self.__mario.lives==0:
                self.__level= 2
            if self.__mario.win:
                self.__level= 3
        
    def draw(self):
        self.__paint_background()
        self.__mario.draw()
        self.__pow.draw()
        self.__paint_platforms()
        self.__paint_enemigo()
        self.__paint_monedas()
        
