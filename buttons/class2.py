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
    pos=pygame.mouse.get_pos()
    pygame.draw.rect(screen,(255,0,0),Rect(75,200,100,100))
    
    if Rect(75,200,100,100).collidepoint(pos):
        pygame.draw.rect(screen,(75,225,255),Rect(75,200,100,100))
    pygame.draw.line(screen, (0,0,0),(75,300),(175,300),2)
    pygame.draw.line(screen, (0,0,0),(175,200),(175,300),2)
    pygame.draw.line(screen, (255,255,255),(75,200),(175,200),2)
    pygame.draw.line(screen, (255,255,255),(75,200),(75,300),2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
