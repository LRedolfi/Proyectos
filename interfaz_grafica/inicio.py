import pygame,sys #Importo librerías

pygame.init() # Inicio pygame

ancho_ventana=500 #Dimensiones de ventana   
alto_ventana=400 
alto_rectángulo=20 #Dimensiones de rectángulo
ancho_rectángulo=130

ventana=pygame.display.set_mode((ancho_ventana,alto_ventana)) #Creo la ventana
pygame.display.set_caption("Ventana") #Titulo de la ventana
rectángulo = pygame.Rect(80, 100, ancho_rectángulo, alto_rectángulo) #Creo el rectángulo

while True: #Ciclo infinito para que no se cierre la ventana
    ventana.fill((51,123,255)) #Coloreo la ventana
    pygame.draw.rect(ventana,(141,51,255),rectángulo) #Dibujo el rectángulo
    pygame.display.update() #Actualizo la pantalla
    tecla=pygame.key.get_pressed() #Capturo el evento tecla presionada
#Chequeo que el rectángulo no salga de los limites de la ventana
    if rectángulo.x<0: 
        rectángulo.x=0
    if rectángulo.x>ancho_ventana-ancho_rectángulo:
        rectángulo.x=ancho_ventana-ancho_rectángulo
    if rectángulo.y<0:
        rectángulo.y=0
    if rectángulo.y>alto_ventana-alto_rectángulo:
        rectángulo.y=alto_ventana-alto_rectángulo
#Según la tecla presionada muevo el rectángulo
    if tecla[pygame.K_a] or tecla[pygame.K_LEFT]:
        rectángulo.x=rectángulo.x-1
    if tecla[pygame.K_d] or tecla[pygame.K_RIGHT]:
        rectángulo.x=rectángulo.x+1
    if tecla[pygame.K_s] or tecla[pygame.K_DOWN]:
        rectángulo.y=rectángulo.y+1
    if tecla[pygame.K_w] or tecla[pygame.K_UP]:
        rectángulo.y=rectángulo.y-1
#Si se presiona el botón cerrar de la ventana, salgo de la misma
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit()
            sys.exit()