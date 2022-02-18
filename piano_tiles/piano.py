import random
import pygame
from objects import Tile,mousep
pygame.init()

#game window size
height=512
width=288
screen = pygame.display.set_mode((width,height))

#tile size
tile_width = width//4
tile_height = 130

white=(255,255,255)
scrolling=0
num_tile=1
score=0

#mouse sprite
mouseobj=mousep()

# 1st tile sprite creation  
tile_group=pygame.sprite.Group()
x=random.randint(0,3)
t=Tile(x*tile_width,-tile_height,screen)
tile_group.add(t)

#tile speed
speed=2

#game clock speed
clock=pygame.time.Clock()
fps=30

#player name input
player_name=""
base_font=pygame.font.Font(None,32)
input_active=False
input_rect= pygame.Rect(200,200,140,32)
color_active=(40,40,150)
color_passive=(100,100,100)
color=color_passive

#player name input 
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                input_active=True
                color=color_active
            else:
                input_active=False
                color=color_passive
        
        if input_active==True:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    user_text=user_text[:-1]
                else:
                    user_text+=event.unicode

    screen.fill((0,0,0))
    

    pygame.draw.rect(screen,color,input_rect,4)
    text_surface = base_font.render(player_name,True,(255,255,255))
    screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))
    input_rect.w = max(text_surface.get_width()+10,140)

    break

#actual game
run=True
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
    
    #another way of checking collision
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

    
    
       
    # mouse and tile collision and game end on tile reaching bottom
    tile_group.update(speed)
    if len(tile_group)>0:
        # when there are other tiles
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
        # when there are no tiles
        x=random.randint(0,3)
        y=-tile_height+t.rect.top
        t=Tile(x*tile_width,y,screen)
        tile_group.add(t)
        num_tile+=1
        tile_group.draw(screen)       
    # tile speed increment
    if scrolling%600==0:
        speed+=1


    
    scrolling+=speed
    mouseobj.update()
    pygame.display.update()
    clock.tick(fps)
pygame.quit()

