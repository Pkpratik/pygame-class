import pygame

pygame.init()
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
                
                # if self.rect.centerx>= bar1.x+bar1.width*(1//3) and self.rect.centerx<= bar1.x+bar1.width*2//3:
                #     self.forward_speed*=-1
                # left side bar hit 
                if self.rect.centerx>= bar1.x and self.rect.centerx<= bar1.x+bar1.width//3:
                    if self.forward_speed>0:
                        self.forward_speed*=-1
                #right side bar hit
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
    def side_hit(self):
        self.forward_speed*=-1
    

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
# arr.add(brick(20,100,2,brickcolor))
# arr.add(brick(130,100,2,brickcolor))
# arr.add(brick(240,100,2,brickcolor))
# arr.add(brick(350,100,2,brickcolor))
# arr.add(brick(460,100,2,brickcolor))
# arr.add(brick(20,130,2,brickcolor))
# arr.add(brick(130,130,2,brickcolor))
# #arr.add(brick(240,130,2,brickcolor))
# arr.add(brick(350,130,2,brickcolor))
arr.add(brick(460,130,2,brickcolor))
arr.add(brick(240,130,1000000,(100,100,100)))
arr.add(brick(240,230,1000000,(100,100,100)))
arr.add(brick(240,330,1000000,(100,100,100)))

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
        # ball hits left side of brick



        if ball.rect.right<=temp[0].rect.left+3:
            ball.side_hit()
        # ball hits right side of brick
        elif ball.rect.left>=temp[0].rect.right-3:
            ball.side_hit()
        else:
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
pygame.quit()