import pygame #Importo librería
from constantes import * #Importo las constantes

class Enemigo(pygame.sprite.Sprite): #Defino la clase, hija de Sprite
    def __init__(self,posición_x,posición_y): #Defino el constructor con las coordenadas de creación
        pygame.sprite.Sprite.__init__(self) #Heredo el constructor

        self.imagen=pygame.Surface(tamaño_enemigo) #Creo la imagen del enemigo
        self.imagen.fill(color_enemigo) #Coloreo el enemigo
        self.rectángulo=self.imagen.get_rect() #Obtengo el rectángulo del enemigo
        self.rectángulo.x=posición_x #Seteo las posiciones iniciales del enemigo
        self.rectángulo.y=posición_y

        self.velocidad=2 #Defino la velocidad de movimiento del enemigo

    def dibujar(self, superficie): #Defino el método dibujar, que recibe donde se dibuja
        superficie.blit(self.imagen,self.rectángulo) #Dibujo el enemigo

    def abajo(self):
        self.rectángulo.y+=self.velocidad