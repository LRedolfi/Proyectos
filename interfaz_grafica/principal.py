import pygame,sys #Importo librerías
from constantes import * #Importo las constantes
from jugador import Jugador #Importo la clase jugador

pygame.init() # Inicio pygame

ventana = pygame.display.set_mode((ancho_ventana,alto_ventana)) #Creo la ventana
pygame.display.set_caption("Ventana") #Titulo de la ventana

jugador_1=Jugador(ancho_ventana//2-ancho_jugador//2,alto_ventana//2-alto_jugador//2) #Creo el jugador

reloj=pygame.time.Clock() #Modifico el tiempo de refresco de pantalla

while True: #Ciclo infinito para que no se cierre la ventana
    reloj.tick(60) #Seteo el tiempo de refresco de pantalla

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

    #Chequeo que el jugador no salga de los limites de la ventana
    if jugador_1.rectángulo.x<0: 
        jugador_1.rectángulo.x=0
    if jugador_1.rectángulo.x>ancho_ventana-ancho_jugador:
        jugador_1.rectángulo.x=ancho_ventana-ancho_jugador
    if jugador_1.rectángulo.y<0:
        jugador_1.rectángulo.y=0
    if jugador_1.rectángulo.y>alto_ventana-alto_jugador:
        jugador_1.rectángulo.y=alto_ventana-alto_jugador

#Si se presiona el botón cerrar de la ventana, salgo de la misma
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ventana.fill(color_fondo) #Coloreo la ventana
    jugador_1.dibujar(ventana) #El jugador se dibuja

    pygame.display.update() #Actualizo la pantalla