import pygame

pygame.init()

w=600
h=600
bg = (204, 102, 0)
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Button Demo')

run=True
while run:
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
