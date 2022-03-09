import pygame, random
pygame.init()
pygame.mixer.init()


#Tile Hit
def tilehitrun():
    pygame.display.set_caption("Piano Hit")
    bg=(255,255,255)

    #Important Data
    screen_width=288
    screen_height=600
    screen=pygame.display.set_mode((screen_width,screen_height))
    clock=pygame.time.Clock()
    starting_bg=(184,255,184)

    #Buttons
    starting_button=pygame.Rect(72,150,156,75)
    lb_button=pygame.Rect(72,400,156,75)
    lb_button_b=pygame.Rect(440,10,50,50)
    
    #Fonts
    base_font=pygame.font.Font(None,32)
    starting_font=pygame.font.Font(None,64)
    title_font=pygame.font.Font(None,95)
    
    #Colors
    white=(255,255,255)
    gray=(128,128,128)
    black=(0,0,0)

    #Tiles Data
    speed=6
    scrolling=0
    tile_height=120
    tile_sound=pygame.mixer.Sound('Jonah/Projects/final/pictures&sounds/piano_tiles_sound1 (1).wav')
    gg_sound=pygame.mixer.Sound('Jonah/Projects/final/pictures&sounds/pianolol.wav')
    #player info
    player_name="Voer je naam in"
    input_rect=pygame.Rect(70,80,150,32)
    input_active=False
    deactive_color=(255,0,0)
    active_color=(0,255,0)
    input_color=deactive_color

    #Leaderboard function
    def lb():
        #getting data from txt
        hsscore=[]
        hsname=[]
        with open("Jonah/Projects/final/scores/myscore.txt","r+") as file:
            for line in file:
                hsscore.append(line[line.rindex(" "):-1])
                hsname.append(line[:line.rindex(" ")])
        #showing data from array
        run=True
        while run:
            screen=pygame.display.set_mode((500,600))
            screen.fill(starting_bg)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if lb_button_b.collidepoint(event.pos):
                        run=False

            #Rendering scores
            #Scores
            hss0=base_font.render(hsscore[0],True,black)
            hss1=base_font.render(hsscore[1],True,black)
            hss2=base_font.render(hsscore[2],True,black)
            hss3=base_font.render(hsscore[3],True,black)
            hss4=base_font.render(hsscore[4],True,black)
            hss5=base_font.render(hsscore[5],True,black)
            hss6=base_font.render(hsscore[6],True,black)
            hss7=base_font.render(hsscore[7],True,black)
            hss8=base_font.render(hsscore[8],True,black)
            hss9=base_font.render(hsscore[9],True,black)
            #Names
            hsn0=base_font.render(hsname[0],True,black)
            hsn1=base_font.render(hsname[1],True,black)
            hsn2=base_font.render(hsname[2],True,black)
            hsn3=base_font.render(hsname[3],True,black)
            hsn4=base_font.render(hsname[4],True,black)
            hsn5=base_font.render(hsname[5],True,black)
            hsn6=base_font.render(hsname[6],True,black)
            hsn7=base_font.render(hsname[7],True,black)
            hsn8=base_font.render(hsname[8],True,black)
            hsn9=base_font.render(hsname[9],True,black)

            #Blitting scores
            #Scores
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
            #Names
            screen.blit(hss0,(400,100))
            screen.blit(hss1,(400,130))
            screen.blit(hss2,(400,160))
            screen.blit(hss3,(400,190))
            screen.blit(hss4,(400,220))
            screen.blit(hss5,(400,250))
            screen.blit(hss6,(400,280))
            screen.blit(hss7,(400,310))
            screen.blit(hss8,(400,340))
            screen.blit(hss9,(400,370))

            #ADD A CROSS IMG
            pygame.draw.rect(screen,(255,0,0),lb_button_b)
            lb_title=title_font.render("Leaderboard",True,black)
            screen.blit(lb_title,(25,10))

            pygame.display.update()

    #Tiles class
    class Tiles(pygame.sprite.Sprite):
        def __init__(self,x,y):
            super().__init__()
            self.image=pygame.Surface([(screen_width//4),tile_height])
            self.image.fill(black)
            self.rect=self.image.get_rect()
            self.rect.x=x*(screen_width//4)
            self.rect.y=y
            self.alive=True
        def update(self,speed):
            self.rect.y+=speed
            if self.alive==True:
                pygame.draw.rect(screen,black,self.rect)
            else:
                pygame.draw.rect(screen,gray,self.rect)
            if self.rect.top>=screen_height:
                self.kill()

    #Mouse class
    class mouse(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image=pygame.Surface([5,5])
            self.image.fill(black)
            self.rect=self.image.get_rect()
            self.rect.center=pygame.mouse.get_pos()
            self.score=0
        def update(self):
            #pygame.draw.rect(screen,black,self.rect)
            self.rect.center=pygame.mouse.get_pos()
        def clicked(self):
            click=pygame.sprite.spritecollide(clicker,tiles,False)
            for i in click:
                if i.alive==True:
                    if player_name=="goed gedaan":
                        pygame.mixer.Sound.play(gg_sound)
                    else:
                        pygame.mixer.Sound.play(tile_sound)
                    
                    self.score+=1
                    i.alive=False
            
            
    #Class object in variables
    clicker=mouse()
    tiles=pygame.sprite.Group()

    run=True
    #Openingsscreen
    while run:
        #Standard while-loop beginning
        screen=pygame.display.set_mode((288,600))
        screen.fill(starting_bg)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                #Leaderboard
                if lb_button.collidepoint(event.pos):
                    lb()
                if starting_button.collidepoint(event.pos):
                    pygame.draw.rect(screen,(85,176,85),starting_button)
                    run=False
                if input_rect.collidepoint(event.pos):
                    input_active=True
                    input_color=active_color
                    if player_name=="Voer je naam in":
                        player_name=""
                else:
                    input_color=deactive_color
            

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    player_name=player_name[:-1]
                else:
                    player_name+=event.unicode
                
        pygame.draw.rect(screen,(4,126,4),lb_button)
        pygame.draw.rect(screen,(4,126,4),starting_button)
        pygame.draw.rect(screen,input_color,input_rect,4)
        name_surface=base_font.render(player_name,True,black)
        input_rect.w = max(name_surface.get_width()+10,140)
        input_rect.x=screen_width//2-input_rect.w//2
        screen.blit(name_surface,(input_rect.x+5,input_rect.y+5))
        
        #Other
        someothervariable2=starting_font.render("START",True,black)
        screen.blit(someothervariable2,(80,170))
        game_explanation=base_font.render("Leaderboard",True,black)
        screen.blit(game_explanation,(80,380))
        pygame.display.update()
        
    #First tile
    tiles.add(Tiles(random.randint(0,3),-tile_height))

    #Actual Game
    fps=30
    run=True
    while run:
        #Standard while-loop beginning
        clock.tick(fps)
        screen.fill(bg)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                clicker.clicked()

        #After hitting the Start button  
        scrolling+=speed
        if scrolling%600==0:
            speed+=1

        #Tile creation
        if len(tiles)>0:
            t=tiles.sprites()[-1]
            y=-tile_height+t.rect.top
            if t.rect.top+speed>=0:
                tiles.add(Tiles(random.randint(0,3),y))
        else:
            t=tiles.sprites()[-1]
            y=-tile_height+t.rect.top
            tiles.add(Tiles(random.randint(0,3),-y))

        #Losing Mechanism
        if tiles.sprites()[0].rect.bottom>=screen_height:
            if tiles.sprites()[0].alive==True:
                pygame.time.wait(2000)
                screen_width=600
                screen=pygame.display.set_mode((screen_width,screen_height))
                run=False
        tiles.update(speed)
        someothervariable1=base_font.render("Score - "+str(clicker.score),True,(255,0,0))
        screen.blit(someothervariable1,(screen_width//3,40))
        clicker.update()
        
        #Standard while-loop End
        pygame.display.update()

    #reading previous hs
    hsdict={}
    with open("Jonah/Projects/final/scores/myscore.txt","r+") as file:
        for line in file:
            line[line.rindex(" "):]
            hsname,hsscore=line[:line.rindex(" ")],line[line.rindex(" ")+1:-1]
            hsdict[hsname]=int(hsscore)
    #adding current hs
    hsdict.setdefault(player_name,clicker.score)
    hsdict[player_name]=max(int(hsdict[player_name]),clicker.score)
    #storing all hs
    with open("Jonah/Projects/final/scores/myscore.txt","w") as file:
        for i in sorted(hsdict.items(),key=lambda item:item[1],reverse=True):    
        
            file.write(i[0]+" "+str(i[1])+'\n')