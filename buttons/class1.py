import pygame
from pygame.locals import *

pygame.init()

width=600
height=600

bg = (204, 102, 0)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Button Demo')

run=True
while run:
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
