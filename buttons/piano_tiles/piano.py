import random
import pygame
from objects import Tile
pygame.init()

height=512
width=288
tile_width = width//4
tile_height = 130
screen = pygame.display.set_mode((width,height))

white=(255,255,255)
scrolling=0
num_tile=0
score=0


tile_group=pygame.sprite.Group()

fps=30
speed=2
run=True
clock=pygame.time.Clock()
while run:
    
    screen.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    tile_group.update(speed)
    if scrolling>=(num_tile*tile_height):
        x=random.randint(0,3)
        t=Tile(x*tile_width,-tile_height,screen)
        tile_group.add(t)
        num_tile+=1
        tile_group.draw(screen)
        score+=1
        speed+=0.3

    scrolling+=speed

    pygame.display.update()
    clock.tick(fps)
pygame.quit()

