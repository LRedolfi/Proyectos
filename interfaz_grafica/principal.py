import pygame,sys #Importo librerías
from constantes import *
from jugador import Jugador

pygame.init() # Inicio pygame

ventana=pygame.display.set_mode((ancho_ventana,alto_ventana)) #Creo la ventana
pygame.display.set_caption("Ventana") #Titulo de la ventana

ventana.fill(color_fondo) #Coloreo la ventana

jugador_1=Jugador

while True: #Ciclo infinito para que no se cierre la ventana

    tecla=pygame.key.get_pressed() #Capturo el evento tecla presionada

    #Según la tecla presionada muevo el jugador
    if tecla[pygame.K_a] or tecla[pygame.K_LEFT]:
        jugador_1.izquierda()
    if tecla[pygame.K_d] or tecla[pygame.K_RIGHT]:
        jugador_1.derecha()
    if tecla[pygame.K_s] or tecla[pygame.K_DOWN]:
        jugador_1.abajo()
    if tecla[pygame.K_w] or tecla[pygame.K_UP]:
        jugador_1.arriba()

#Si se presiona el botón cerrar de la ventana, salgo de la misma
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()