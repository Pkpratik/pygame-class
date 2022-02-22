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

#game progress trachers
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
player_name="Enter your name"
base_font=pygame.font.Font(None,32)
input_active=False
input_rect= pygame.Rect(70,170,140,32)
color_active=(40,40,150)
color_passive=(120,200,50)
color=color_passive
white=(255,255,255)

# game start button
start_rect= pygame.Rect(75,220,140,52)



#player name input 
run=True
while run:
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
            if start_rect.collidepoint(pygame.mouse.get_pos()):
                run=False
        
        if input_active==True:
            if player_name=="Enter your name":
                player_name=""
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    player_name=player_name[:-1]
                else:
                    player_name+=event.unicode

    screen.fill((100,100,80))
    
    # player name box display
    pygame.draw.rect(screen,color,input_rect,4)
    name_surface = base_font.render(player_name,True,(255,255,255))
    screen.blit(name_surface,(input_rect.x+5,input_rect.y+5))
    input_rect.w = max(name_surface.get_width()+10,140)
    input_rect.x=width//2-input_rect.w//2


    #start button display
    pygame.draw.rect(screen,(100,150,100),start_rect)
    start_surface = base_font.render("START",True,(255,255,255))
    screen.blit(start_surface,(start_rect.x+33,start_rect.y+15))

    pygame.display.update()
    

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
                if i.alive==True:
                    score+=1
                    i.alive=False
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

    
    
       
    # new tile creation and game end on tile reaching bottom
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


    # score bar
    score_surface = base_font.render("score - "+str(score),True,(0,0,0))
    screen.blit(score_surface,((width-len(("score - "+str(score)))*10)//2,35))


    scrolling+=speed
    mouseobj.update()
    pygame.display.update()
    clock.tick(fps)
pygame.time.wait(3000)
hsdict={}

with open("piano_tiles/score.txt","r+") as file:
    for line in file:
        hsname,hsscore=line.split()
        hsdict[hsname]=hsscore

hsdict.setdefault(player_name,score)
hsdict[player_name]=max(int(hsdict[player_name]),score)


with open("piano_tiles/score.txt","w") as file:
    for i in hsdict.items():
        file.write(i[0]+" "+str(i[1])+"\n")
pygame.quit()

