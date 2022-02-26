from operator import le
import random
import pygame
from objects import Tile,mousep
pygame.init()

#game window size
height=512
width=300
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
leaderbord_rect= pygame.Rect(75,320,140,52)

def show_hs():
    back_rect= pygame.Rect(5,5,50,50)
    namearr=[]
    scorearr=[]
    with open("piano_tiles/score.txt","r+") as file:
        for line in file:
            hsname,hsscore=line[:line.rindex(" ")],line[line.rindex(" ")+1:]
            namearr.append(hsname)
            scorearr.append(hsscore[:-1])

    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    run=False
        screen.fill((100,100,100))
        pygame.draw.rect(screen,(150,0,0),back_rect)
        
        hsn0 = base_font.render(namearr[0],True,(255,255,255))
        hsn1 = base_font.render(namearr[1],True,(255,255,255))
        hsn2 = base_font.render(namearr[2],True,(255,255,255))
        hsn3 = base_font.render(namearr[3],True,(255,255,255))
        hsn4 = base_font.render(namearr[4],True,(255,255,255))
        hsn5 = base_font.render(namearr[5],True,(255,255,255))
        hsn6 = base_font.render(namearr[6],True,(255,255,255))
        hsn7 = base_font.render(namearr[7],True,(255,255,255))
        hsn8 = base_font.render(namearr[8],True,(255,255,255))
        hsn9 = base_font.render(namearr[9],True,(255,255,255))
        
        hss0 = base_font.render(scorearr[0],True,(255,255,255))
        hss1 = base_font.render(scorearr[1],True,(255,255,255))
        hss2 = base_font.render(scorearr[2],True,(255,255,255))
        hss3 = base_font.render(scorearr[3],True,(255,255,255))
        hss4 = base_font.render(scorearr[4],True,(255,255,255))
        hss5 = base_font.render(scorearr[5],True,(255,255,255))
        hss6 = base_font.render(scorearr[6],True,(255,255,255))
        hss7 = base_font.render(scorearr[7],True,(255,255,255))
        hss8 = base_font.render(scorearr[8],True,(255,255,255))
        hss9 = base_font.render(scorearr[9],True,(255,255,255))

        higher_font= pygame.font.Font(None,50)
        leaderboardtext = higher_font.render("High Scores",True,(255,255,255))
        screen.blit(leaderboardtext,(60,40))

        screen.blit(hsn0,(25,100))
        screen.blit(hsn1,(25,130))
        screen.blit(hsn2,(25,160))
        screen.blit(hsn3,(25,190))
        screen.blit(hsn4,(25,220))
        screen.blit(hsn5,(25,250))
        screen.blit(hsn6,(25,280))
        screen.blit(hsn7,(25,310))
        screen.blit(hsn8,(25,340))
        screen.blit(hsn9,(25,370))

        screen.blit(hss0,(250,100))
        screen.blit(hss1,(250,130))
        screen.blit(hss2,(250,160))
        screen.blit(hss3,(250,190))
        screen.blit(hss4,(250,220))
        screen.blit(hss5,(250,250))
        screen.blit(hss6,(250,280))
        screen.blit(hss7,(250,310))
        screen.blit(hss8,(250,340))
        screen.blit(hss9,(250,370))



        pygame.display.update()



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
            if leaderbord_rect.collidepoint(event.pos):
                show_hs()


        if input_active==True:
            if player_name=="Enter your name":
                player_name=""
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    player_name=player_name[:-1]
                else:
                    player_name+=event.unicode
                    if len(player_name)>20:
                        player_name=player_name[:-1]
    screen.fill((100,100,80))
    
    # player name box display
    pygame.draw.rect(screen,color,input_rect,4)
    name_surface = base_font.render(player_name,True,(255,255,255))
    screen.blit(name_surface,(input_rect.x+5,input_rect.y+5))
    input_rect.w = max(name_surface.get_width()+10,140)
    input_rect.x=width//2-input_rect.w//2
    start_rect.x=width//2-start_rect.w//2
    leaderbord_rect.x=width//2-leaderbord_rect.w//2

    #start button display
    pygame.draw.rect(screen,(100,150,100),start_rect)
    pygame.draw.rect(screen,(100,150,100),leaderbord_rect)
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
pygame.time.wait(1000)
hsdict={}

with open("piano_tiles/score.txt","r+") as file:
    for line in file:
        line[line.rindex(" "):]
        hsname,hsscore=line[:line.rindex(" ")],int(line[line.rindex(" ")+1:])
        hsdict[hsname]=hsscore

hsdict.setdefault(player_name,score)
hsdict[player_name]=max(int(hsdict[player_name]),score)


with open("piano_tiles/score.txt","w") as file:
    lim=10
    for i in sorted(hsdict.items(),key= lambda item:item[1],reverse=True):
        
        file.write(i[0]+" "+str(i[1])+'\n')
        lim-=1
        if lim==0:
            break
pygame.quit()

