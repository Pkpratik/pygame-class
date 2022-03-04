import pygame
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

#dif. speeds
forward_speed=1
downward_speed=1
barspeed=8

#sounds
barhit=pygame.mixer.Sound('Projects/2pp_barsound.wav')

#Bar1 (Up)
line1=pygame.draw.line(screen,white,(250,500),(350,500),2)
bar1=pygame.draw.rect(screen,white,line1,2)
scoreup=0

#Bar (Down)
line2=pygame.draw.line(screen,white,(250,100),(350,100),2)
bar2=pygame.draw.rect(screen,white,line2,2)
scoredown=0

class ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([25,25])
        self.image.fill((3,255,74))
        #Bar1
        self.rect=self.image.get_rect()
        
        self.forward_speed=2
        self.downward_speed=2
        
        self.space_pressed=False
    def update(self):
        pygame.draw.rect(screen,white,self.rect,0,25)
        #(GOING TO BE UPDATED) Whichever has the ball, should be able to press space to let the ball loose
        if self.space_pressed==False:
            self.rect.center=(300,300)
        else:
            self.rect.x+=self.forward_speed
            self.rect.y-=self.downward_speed
            if self.rect.bottom>=h or self.rect.top<=0:
                self.downward_speed=-self.downward_speed
            if self.rect.left<=0 or self.rect.right>=h:
                self.forward_speed=-self.forward_speed
            #Bar1
            if self.rect.colliderect(bar1):
                pygame.mixer.Sound.play(barhit)
                self.forward_speed=-self.forward_speed
                self.forward_speed=-self.forward_speed
                self.downward_speed=-self.downward_speed
            #Bar2
            if self.rect.colliderect(bar2):
                pygame.mixer.Sound.play(barhit)
                self.forward_speed=-self.forward_speed
                self.forward_speed=-self.forward_speed
                self.downward_speed=-self.downward_speed
    def turnup(self):
        if self.space_pressed==False:
            self.rect.centerx=bar1.centerx
            self.rect.bottom=bar1.centery
        else:
            self.rect.x+=self.forward_speed
            self.rect.y-=self.downward_speed
    def turndown(self):
        if self.space_pressed==False:   
            self.rect.centerx=bar2.centerx
            self.rect.bottom=bar2.centery
        else:
            self.rect.x-=self.forward_speed
            self.rect.y+=self.downward_speed
    
ball1=ball()

#Gameloop
run=True
while run:
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
        ball1.space_pressed=True

    #Pongbar2
    if key[pygame.K_d]==1 and bar2.right<=w:
        bar2=pygame.Rect.move(bar2,barspeed,0)
    if key[pygame.K_a]==1 and bar2.left>=0:
        bar2=pygame.Rect.move(bar2,-barspeed,0)

    if ball1.rect.bottom>=h:
        scoreup+=1
        ball1.turnup()
    if ball1.rect.top<=0:
        scoredown+=1
        ball1.turndown()



    # Speed incrementation
    # f+=forward_speed
    # d+=downward_speed
    # if f%500==0 or d%500==0:
    #     ball1.forward_speed+=1
    #     ball1.downward_speed+=1
    #     barspeed+=1
    #     print("increased")
    
    #Showing scores
    sup=base_font.render(str(scoreup),True,white)
    screen.blit(sup,(25,250))
    sdown=base_font.render(str(scoredown),True,white)
    screen.blit(sdown,(25,350))

    #Overall drawing/displaying
    pygame.draw.rect(screen,white,bar1)
    pygame.draw.rect(screen,white,bar2)
    pygame.draw.line(screen,white,(0,300),(600,300))
    
    #Standard While-loop ending
    pygame.display.update()
pygame.quit()