import pygame #Importo librería
from constantes import * #Importo las constantes

class Jugador(pygame.sprite.Sprite): #Defino la clase, hija de Sprite
    def __init__(self,posición_x,posición_y): #Defino el constructor con las coordenadas de creación
        pygame.sprite.Sprite.__init__(self) #Heredo el constructor

        self.imagen=pygame.Surface(tamaño_jugador) #Creo la imagen del jugador
        self.imagen.fill(color_jugador) #Coloreo el jugador
        self.rect=self.imagen.get_rect() #Obtengo el rect del jugador
        self.rect.x=posición_x #Seteo las posiciones iniciales del jugador
        self.rect.y=posición_y

        self.velocidad=2 #Defino la velocidad de movimiento del jugador
    
    def dibujar(self, superficie): #Defino el método dibujar, que recibe donde se dibuja
        superficie.blit(self.imagen,self.rect) #Dibujo el jugador

    #Defino los métodos para mover el jugador
    def izquierda(self): 
        self.rect.x-=self.velocidad

    def derecha(self):
        self.rect.x+=self.velocidad

    def arriba(self):
        self.rect.y-=self.velocidad

    def abajo(self):
        self.rect.y+=self.velocidad