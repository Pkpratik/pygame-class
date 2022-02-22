import random
import pygame
from objects import Tile,mousep
pygame.init()
def bb():
    
    w=580
    h=600
    bg = (0,0,0)
    screen=pygame.display.set_mode((w,h))
    pygame.display.set_caption('Pong with wall')
    run=True
    rect1=pygame.Rect(0,0,25,25)

    barspeed=5
    count=0 #Later, if you hit 10 you won.
    line=pygame.draw.line(screen,(255,255,255),(100,500),(200,500),10)
    bar1=pygame.draw.rect(screen,(255,255,255),line)

    class ball(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image=pygame.Surface([25,25])
            self.image.fill((255,255,255))
            self.rect=self.image.get_rect()
            self.rect.bottomleft=bar1.center
            self.play=1
            self.forward_speed=2
            self.downward_speed=3
            self.start=0
        def update(self):
            if self.start==1:

                if self.play:
                    self.rect.centerx+=self.forward_speed
                    self.rect.centery-=self.downward_speed
            # uncomment the bellow if statement for game over 
                if self.rect.bottom>=h:
                    self.play=0
                    
                if self.rect.right>=w:
                    if self.forward_speed>0:
                        self.forward_speed=-self.forward_speed
                        
                if self.rect.left<=0:
                    if self.forward_speed<0:
                        self.forward_speed=-self.forward_speed
                if self.rect.top<=0 or self.rect.bottom>=h:
                    self.downward_speed=-self.downward_speed
                if self.rect.colliderect(bar1):
                    

                    if self.rect.centerx>= bar1.x and self.rect.centerx<= bar1.x+bar1.width//3:
                        if self.forward_speed>0:
                            self.forward_speed*=-1
                    elif self.rect.centerx>=bar1.x+bar1.width*(2//3) and self.rect.centerx<=bar1.x+bar1.width:
                        if self.forward_speed<0:
                            self.forward_speed*=-1
                    if self.downward_speed<0:
                        self.downward_speed*=-1
                    
            else:
                self.rect.centerx=bar1.centerx
                self.rect.bottom=bar1.top
            pygame.draw.rect(screen,(255,255,255),self.rect,0,25)

        def move(self):
            self.start=1
        def hit(self):
            self.downward_speed*=-1

    class brick(pygame.sprite.Sprite):
        def __init__(self,x,y,s,color):
            super().__init__()
            self.image=pygame.Surface([100,25])
            self.image.fill(color)
            self.rect=self.image.get_rect()
            self.rect.x=x
            self.rect.y=y
            self.strength=s
        def update(self):
            self.rect.y+=1
            if self.strength<1:
                self.kill()
        def hit(self):
            self.strength-=1
            if self.strength<1:
                self.kill()
            
    #Gameloop 
    ball=ball()
    arr=pygame.sprite.Group()
    brickcolor=(100,100,25)
    arr.add(brick(20,100,2,brickcolor))
    arr.add(brick(130,100,2,brickcolor))
    arr.add(brick(240,100,2,brickcolor))
    arr.add(brick(350,100,2,brickcolor))
    arr.add(brick(460,100,2,brickcolor))
    arr.add(brick(20,130,2,brickcolor))
    arr.add(brick(130,130,2,brickcolor))
    #arr.add(brick(240,130,2,brickcolor))
    arr.add(brick(350,130,2,brickcolor))
    arr.add(brick(460,130,2,brickcolor))
    arr.add(brick(240,130,1000000,(100,100,100)))

    play=True

    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            
        #Makes it stay inside the screen
        #Code is missing, couldnt get it working.
        
        screen.fill(bg)
        #Makes the cube move
        ball.update() 
        if ball.rect.bottom>=h:
            break
        # if play:
        #     rect1=pygame.Rect.move(rect1,forward_speed,downward_speed)
        # # uncomment the bellow if statement for game over 
        # if rect1.bottom>=h:
        #     play=False
        # if rect1.right>=w or rect1.left<=0:
        #     forward_speed=-forward_speed
        # if rect1.top<=0 or rect1.bottom>=h:
        #     downward_speed=-downward_speed
        # if rect1.colliderect(bar1) and downward_speed>0:
        #     downward_speed*=-1
        #Pongbar
        temp=pygame.sprite.spritecollide(ball,arr,False)
        
        for i in temp:
            i.hit()
        if len(temp)>0:
            ball.hit()
            
        key=pygame.key.get_pressed()
        if key[pygame.K_RIGHT]==1 and bar1.right<w:
            bar1=pygame.Rect.move(bar1,barspeed,0)
        if key[pygame.K_LEFT]==1 and bar1.left>0:
            bar1=pygame.Rect.move(bar1,-barspeed,0)
        if key[pygame.K_SPACE]==1:
            ball.move()

        arr.draw(screen)
        #Losing mechanism
        # if rect1.bottom>=h:
        #     forward_speed=0
        #     downward_speed=0
        #     print("You lost.")

        #pygame.draw.rect(screen,(255,255,255),rect1)
        pygame.draw.rect(screen,(255,255,255),bar1,0,5,5,5)
        pygame.display.update()
def pt():
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
    speed=6

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


height=512
width=288
screen = pygame.display.set_mode((width,height))

#game window size

rect2= pygame.Rect(75,220,140,52)
rect3= pygame.Rect(75,420,140,52)

# main menu
run=True
while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if rect2.collidepoint(event.pos):
                bb()
            if rect3.collidepoint(event.pos):
                pt()
            
    pygame.draw.rect(screen,(100,1,1),rect2,4)
    pygame.draw.rect(screen,(100,1,1),rect3,4)

    pygame.display.update()



#player name input 
