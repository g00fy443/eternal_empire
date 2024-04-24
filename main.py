import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("ETERNAL EMPIRE")

running = True

screen.fill((255, 0, 0))


while running:
    screen.fill((140, 140, 140))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.quit()
            running = False
