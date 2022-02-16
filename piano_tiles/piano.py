import random
import pygame
from objects import Tile,mousep
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

mouseobj=mousep()
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
            col=pygame.sprite.spritecollide(mouseobj,tile_group,False)
            for i in col:
                i.alive=False
                score+=1
                print(score)
            
    #tile_group.update(speed)
    # for tile in tile_group:
    #     tile.update(speed)
    #     if pos:
    #         if tile.rect.collidepoint(pos):
    #             score+=1
    #             tile.alive=False
    #             print(score)
    #     if tile.rect.bottom>=height and tile.alive:
    #         run=False

    
    
       
    
    tile_group.update(speed)
    if len(tile_group)>0:
        t=tile_group.sprites()[-1]
        if t.rect.top+speed>=0:
            x=random.randint(0,3)
            y=-tile_height+t.rect.top
            t=Tile(x*tile_width,y,screen)
            tile_group.add(t)
            num_tile+=1
            tile_group.draw(screen)
        t=tile_group.sprites()[0]
        if t.rect.bottom>=height and t.alive==True:
            run=False
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
    mouseobj.update()
    pygame.display.update()
    clock.tick(fps)
pygame.quit()

