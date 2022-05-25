from operator import le
from random import randint
import pygame,sys #Importo librerías
from constantes import * #Importo las constantes
from jugador import Jugador #Importo la clase jugador
from enemigo import Enemigo

pygame.init() # Inicio pygame

ventana = pygame.display.set_mode((ancho_ventana,alto_ventana)) #Creo la ventana
pygame.display.set_caption("Ventana") #Titulo de la ventana

jugador=Jugador(ancho_ventana//2-ancho_jugador//2,alto_ventana//2-alto_jugador//2) #Creo el jugador
enemigos=pygame.sprite.Group()

reloj=pygame.time.Clock() #Modifico el tiempo de refresco de pantalla

nivel=1

while True: #Ciclo infinito para que no se cierre la ventana
    reloj.tick(60) #Seteo el tiempo de refresco de pantalla

    tecla=pygame.key.get_pressed() #Capturo el evento tecla presionada

    #Según la tecla presionada muevo el jugador
    if tecla[pygame.K_a] or tecla[pygame.K_LEFT]:
        jugador.izquierda()
    if tecla[pygame.K_d] or tecla[pygame.K_RIGHT]:
        jugador.derecha()
    if tecla[pygame.K_s] or tecla[pygame.K_DOWN]:
        jugador.abajo()
    if tecla[pygame.K_w] or tecla[pygame.K_UP]:
        jugador.arriba()

    #Chequeo que el jugador no salga de los limites de la ventana
    if jugador.rect.x<0: 
        jugador.rect.x=0
    if jugador.rect.x>ancho_ventana-ancho_jugador:
        jugador.rect.x=ancho_ventana-ancho_jugador
    if jugador.rect.y<0:
        jugador.rect.y=0
    if jugador.rect.y>alto_ventana-alto_jugador:
        jugador.rect.y=alto_ventana-alto_jugador

    #Si se presiona el botón cerrar de la ventana, salgo de la misma
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ventana.fill(color_fondo) #Coloreo la ventana

    if len(enemigos)==0:
        for número in range(5*nivel):
            posición_x=randint(0,ancho_ventana)
            posición_y=randint(-500,-100)

            enemigo=Enemigo(posición_x,posición_y,nivel)
            enemigos.add(enemigo)

    for enemigo in enemigos:
        enemigo.abajo()
        enemigo.dibujar(ventana)

        if enemigo.rect.y>alto_ventana:
            enemigos.remove(enemigo)

    if len(enemigos)==0:
        nivel +=1

    if pygame.sprite.spritecollideany(jugador,enemigos):
        print("El jugador perdió")

    jugador.dibujar(ventana) #El jugador se dibuja
    

    pygame.display.update() #Actualizo la pantalla