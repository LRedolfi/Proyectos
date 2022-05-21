import pygame,sys

pygame.init()
ancho_ventana=500
alto_ventana=400
alto_rectángulo=20
ancho_rectángulo=130
ventana=pygame.display.set_mode((ancho_ventana,alto_ventana))
pygame.display.set_caption("Ventana")
rectángulo = pygame.Rect(80, 100, ancho_rectángulo, alto_rectángulo)

while True:
    ventana.fill((51,123,255))
    pygame.draw.rect(ventana,(141,51,255),rectángulo)
    pygame.display.update()
    tecla=pygame.key.get_pressed()

    if rectángulo.x<0:
        rectángulo.x=0
    if rectángulo.x>ancho_ventana-ancho_rectángulo:
        rectángulo.x=ancho_ventana-ancho_rectángulo
    if rectángulo.y<0:
        rectángulo.y=0
    if rectángulo.y>alto_ventana-alto_rectángulo:
        rectángulo.y=alto_ventana-alto_rectángulo

    if tecla[pygame.K_a]:
        rectángulo.x=rectángulo.x-1
    if tecla[pygame.K_d]:
        rectángulo.x=rectángulo.x+1
    if tecla[pygame.K_s]:
        rectángulo.y=rectángulo.y+1
    if tecla[pygame.K_w]:
        rectángulo.y=rectángulo.y-1

    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit()
            sys.exit()