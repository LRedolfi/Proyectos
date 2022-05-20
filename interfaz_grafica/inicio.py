import pygame,sys

pygame.init()

ventana=pygame.display.set_mode((500,400))
pygame.display.set_caption("Ventana")
rectángulo = pygame.Rect(80, 100, 120, 30)

while True:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    ventana.fill((51,123,255))
    pygame.draw.rect(ventana,(141,51,255),rectángulo)
    pygame.draw.circle(ventana,(255,255,21),(200,200),50)
    pygame.display.update()