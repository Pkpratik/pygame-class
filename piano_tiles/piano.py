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
num_tile=1
score=0


tile_group=pygame.sprite.Group()
x=random.randint(0,3)
t=Tile(x*tile_width,-tile_height,screen)
tile_group.add(t)
fps=30
speed=2
run=True
clock=pygame.time.Clock()
while run:
    pos=None
    screen.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=event.pos
    #tile_group.update(speed)
    for tile in tile_group:
        tile.update(speed)
        if pos:
            if tile.rect.collidepoint(pos):
                score+=1
                tile.alive=False
                print(score)
        if tile.rect.bottom>=height and tile.alive:
            run=False
    if len(tile_group)>0:
        t=tile_group.sprites()[-1]
        if t.rect.top+speed>=0:
            x=random.randint(0,3)
            y=-tile_height+t.rect.top
            t=Tile(x*tile_width,y,screen)
            tile_group.add(t)
            num_tile+=1
            tile_group.draw(screen)
    else:
        x=random.randint(0,3)
        y=-tile_height+t.rect.top
        t=Tile(x*tile_width,y,screen)
        tile_group.add(t)
        num_tile+=1
        tile_group.draw(screen)       
    if scrolling%600==0:
        speed+=1

    scrolling+=speed

    pygame.display.update()
    clock.tick(fps)
pygame.quit()

