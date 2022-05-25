import pygame #Importo librería
from constantes import * #Importo las constantes

class Enemigo(pygame.sprite.Sprite): #Defino la clase, hija de Sprite
    def __init__(self,posición_x,posición_y,velocidad): #Defino el constructor con las coordenadas de creación
        pygame.sprite.Sprite.__init__(self) #Heredo el constructor

        self.imagen=pygame.Surface(tamaño_enemigo) #Creo la imagen del enemigo
        self.imagen.fill(color_enemigo) #Coloreo el enemigo
        self.rect=self.imagen.get_rect() #Obtengo el rectángulo del enemigo
        self.rect.x=posición_x #Seteo las posiciones iniciales del enemigo
        self.rect.y=posición_y

        self.velocidad=velocidad #Defino la velocidad de movimiento del enemigo

    def dibujar(self, superficie): #Defino el método dibujar, que recibe donde se dibuja
        superficie.blit(self.imagen,self.rect) #Dibujo el enemigo

    def abajo(self):
        self.rect.y+=self.velocidad