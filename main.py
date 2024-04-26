import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("ETERNAL EMPIRE")

running = True

screen.fill((255, 0, 0))
elliotspriteimage=pygame.image.load('sprites/elliotposter.png')
scaledelliotposter=pygame.transform.scale(elliotspriteimage,(32, 32))
x=0
y=0
direction=1
font=pygame.font.Font(None, 100)
text=font.render('eternal empire', True, (0, 0 ,0))
while running:
    screen.fill((140, 140, 140))
    screen.blit(text,(x , 3))
    screen.blit(scaledelliotposter,(x, y))
    x=x+.05*direction
    y=y+.05*direction
    if x > 640:
        direction=-1
    if x < 0:
        direction=1
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.quit()
            running = False

