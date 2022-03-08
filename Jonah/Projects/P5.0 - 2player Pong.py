import pygame
import time
pygame.init()

#Colors
white=(255,255,255)
black=(0,0,0)

#Formatting
w=600
h=600
bg = (black)
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption('Brick Breaker')
base_font=pygame.font.Font(None,40)
other_font=pygame.font.Font(None,32)
starting_font=pygame.font.Font(None,64)

barspeed=8

#Buttons
starting_button=pygame.Rect(225,200,156,75)

#player1 info
player_name1="Voer naam1 in"
input_rect1=pygame.Rect(70,55,150,32)
input_active1=False
deactive_color=(255,0,0)
active_color=(0,255,0)
input_color1=deactive_color

#player2 info
player_name2="Voer naam2 in"
input_rect2=pygame.Rect(70,130,150,32)
input_active2=False
input_color2=deactive_color

#sounds
barhit=pygame.mixer.Sound('Jonah/Projects/final/pictures&sounds/2pp_barsound.wav')

#Scores
scoreup=5
scoredown=5

#Bar1 (Up)
line1=pygame.draw.line(screen,white,(250,500),(350,500),2)
bar1=pygame.draw.rect(screen,white,line1,2)

#Bar (Down)
line2=pygame.draw.line(screen,white,(250,100),(350,100),2)
bar2=pygame.draw.rect(screen,white,line2,2)

class ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([25,25])
        self.image.fill((3,255,74))
        #Bar1
        self.rect=self.image.get_rect()
        self.speedincrementation=0
        self.teamscore=0
        self.ths=0
        self.forward_speed=2
        self.downward_speed=2
        self.cooldown=0
        self.setup=False
        self.setdown=False
        self.space_pressed=False
    def update(self):
        pygame.draw.rect(screen,white,self.rect,0,25)
        #(GOING TO BE UPDATED) Whichever has the ball, should be able to press space to let the ball loose
        if self.setdown==False and self.setup==False:
            if self.space_pressed==False:
                self.rect.center=(300,300)
            else:
                self.rect.x+=self.forward_speed
                self.rect.y-=self.downward_speed
                # if self.rect.bottom>=h or self.rect.top<=0:
                #     self.downward_speed=-self.downward_speed
                if self.rect.left<=0 or self.rect.right>=w:
                    self.forward_speed=-self.forward_speed
                #Bar1
                if self.cooldown>0:
                    self.cooldown-=1
                if self.rect.colliderect(bar1):
                    if self.cooldown==0:
                        self.speedincrementation+=1
                        self.teamscore+=1
                        self.cooldown=5
                    pygame.mixer.Sound.play(barhit)
                    if self.downward_speed<0:
                        self.downward_speed=-self.downward_speed
                #Bar2
                if self.rect.colliderect(bar2):
                    if self.cooldown==0:
                        self.speedincrementation+=1
                        self.teamscore+=1
                        self.cooldown=5
                    pygame.mixer.Sound.play(barhit)
                    if self.downward_speed>0:
                        self.downward_speed=-self.downward_speed
        else:
            if self.setdown==True:
                self.rect.centerx=bar2.centerx
                self.rect.top=bar2.centery+1
            if self.setup==True:
                self.rect.centerx=bar1.centerx
                self.rect.bottom=bar1.centery-1
        
        #Speed incrementation
        if (self.speedincrementation+1)%6==0:
            self.speedincrementation=0
            if self.forward_speed>0:
                self.forward_speed+=1
            else:
                self.forward_speed-=1
            if self.downward_speed>0:
                self.downward_speed+=1
            else:
                self.downward_speed-=1
    
ball1=ball()

run=True
    #Openingsscreen
while run:
    #Standard while-loop beginning
    screen=pygame.display.set_mode((600,600))
    screen.fill((184,255,184))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if starting_button.collidepoint(event.pos):
                pygame.draw.rect(screen,(85,176,85),starting_button)
                run=False
            if input_rect1.collidepoint(event.pos):
                input_active2=False
                input_active1=True
                input_color1=active_color
                if player_name1=="Voer naam1 in":
                    player_name1=""
            else:
                input_color=deactive_color
            if input_rect2.collidepoint(event.pos):
                input_active1=False
                input_active2=True
                input_color2=active_color
                if player_name2=="Voer naam2 in":
                    player_name2=""
            else:
                input_color=deactive_color
        

        if event.type==pygame.KEYDOWN:
            if input_active1==True:
                if event.key==pygame.K_BACKSPACE:
                    player_name1=player_name1[:-1]
                else:
                    player_name1+=event.unicode
            if input_active2==True:
                if event.key==pygame.K_BACKSPACE:
                    player_name2=player_name2[:-1]
                else:
                    player_name2+=event.unicode
            
    pygame.draw.rect(screen,(4,126,4),starting_button)
    pygame.draw.rect(screen,input_color1,input_rect1,4)
    pygame.draw.rect(screen,input_color2,input_rect2,4)
    name_surface1=base_font.render(player_name1,True,black)
    name_surface2=base_font.render(player_name2,True,black)
    input_rect1.w = max(name_surface1.get_width()+10,140)
    input_rect1.x=w//2-input_rect1.w//2
    input_rect2.w = max(name_surface2.get_width()+10,140)
    input_rect2.x=w//2-input_rect2.w//2
    screen.blit(name_surface1,(input_rect1.x+5,input_rect1.y+5))
    screen.blit(name_surface2,(input_rect2.x+5,input_rect2.y+5))
    
    #Other
    someothervariable2=starting_font.render("START",True,black)
    screen.blit(someothervariable2,(starting_button.x+5,starting_button.y+17))
    pygame.display.update()

#Gameloop
run=True
run2=True
while run:
    if run2==False:
        pygame.time.delay(1500)
        run=False
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.fill(bg)
    ball1.update()

    #Keybinding for pongbars
    key=pygame.key.get_pressed()
    #Pongbar1
    if key[pygame.K_RIGHT]==1 and bar1.right<=w:
        bar1=pygame.Rect.move(bar1,barspeed,0)
    if key[pygame.K_LEFT]==1 and bar1.left>=0:
        bar1=pygame.Rect.move(bar1,-barspeed,0)
    if key[pygame.K_SPACE]==1:
        if ball1.setdown==True:
            ball1.teamscore=-1
            ball1.forward_speed=2
            ball1.downward_speed=2
        if ball1.setup==True:
            ball1.teamscore=0 
            ball1.forward_speed=2
            ball1.downward_speed=2
        ball1.space_pressed=True
        ball1.setdown=False
        ball1.setup=False
        
        

    #Pongbar2
    if key[pygame.K_d]==1 and bar2.right<=w:
        bar2=pygame.Rect.move(bar2,barspeed,0)
    if key[pygame.K_a]==1 and bar2.left>=0:
        bar2=pygame.Rect.move(bar2,-barspeed,0)

    if ball1.rect.bottom>=h:
        scoreup+=1
        ball1.setup=True
        if ball1.teamscore>=ball1.ths:
            ball1.ths=ball1.teamscore
    if ball1.rect.top<=0:
        scoredown+=1
        ball1.setdown=True
        if ball1.teamscore>=ball1.ths:
            ball1.ths=ball1.teamscore
    
    if scoreup==7:
        winnerup=other_font.render(str(player_name1)+" Won!",True,white)
        screen.blit(winnerup,(150,150))
        run2=False
    if scoredown==7:
        winnerdown=other_font.render(str(player_name2)+" Won!",True,white)
        screen.blit(winnerdown,(150,450))
        run2=False
    #Showing score
    sup=base_font.render(str(scoreup),True,white)
    screen.blit(sup,(25,250))
    sdown=base_font.render(str(scoredown),True,white)
    screen.blit(sdown,(25,350))
    if ball1.setup==True or ball1.setdown==True:
        steam=other_font.render("Teamscore - "+str(ball1.teamscore),True,white)
        screen.blit(steam,(425,40))
        hsteam=other_font.render("Team Highscore - "+str(ball1.ths),True,white)
        screen.blit(hsteam,(371,10))
    n1=other_font.render(str(player_name1),True,white)
    screen.blit(n1,(10,10))
    n2=other_font.render(str(player_name2),True,white)
    screen.blit(n2,(10,h-32))

    #Overall drawing/displaying
    pygame.draw.rect(screen,white,bar1)
    pygame.draw.rect(screen,white,bar2)
    
    #Standard While-loop ending
    pygame.display.update()
pygame.quit()