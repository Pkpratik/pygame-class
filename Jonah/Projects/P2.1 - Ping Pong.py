import pygame
import random
pygame.init()
w=600
h=600
white=(255,255,255)
black=(0,0,0)
bg = (black)
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption('Brick Breaker')
run=True
#ball=pygame.Rect(0,0,25,25)
forward_speed=1
downward_speed=1
barspeed=5
count=0 #Later, if you hit 10 you won.
line=pygame.draw.line(screen,(white),(100,500),(200,500),2)
bar1=pygame.draw.rect(screen,(white),line,2)
class bricks(pygame.sprite.Sprite):
    def __init__(self,x,y,s):
        super().__init__()
        self.image=pygame.Surface([90,50])
        self.image.fill((0,40,160))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.strenght=s
    def hit(self):
        self.strenght-=1
        if self.strenght<=0:
            self.kill()

class ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([25,25])
        self.image.fill((3,255,74))
        self.rect=self.image.get_rect()
        self.rect.centerx=bar1.centerx
        self.rect.bottom=bar1.centery
        self.forward_speed=2
        self.downward_speed=3
        
        self.space_pressed=False
    def update(self):
        pygame.draw.rect(screen,(white),self.rect,0,25)
        if self.space_pressed==False:
            self.rect.centerx=bar1.centerx
            self.rect.bottom=bar1.centery
        else:
            self.rect.x+=self.forward_speed
            self.rect.y-=self.downward_speed
            if self.rect.bottom>=h or self.rect.top<=0:
                self.downward_speed=-self.downward_speed
            if self.rect.left<=0 or self.rect.right>=h:
                self.forward_speed=-self.forward_speed
            if self.rect.colliderect(bar1):
                if self.rect.centerx>bar1.x and self.rect.centerx<bar1.x+bar1.width//6:
                    if self.forward_speed>0:
                        self.forward_speed=-self.forward_speed
                elif self.rect.centerx>bar1.x+bar1.width*(5//6) and self.rect.centerx<bar1.width+bar1.x:
                    if self.forward_speed<0:
                        self.forward_speed=-self.forward_speed
                self.downward_speed=-self.downward_speed
                if self.downward_speed<=0:
                    self.downward_speed=-self.downward_speed

    def hit(self):
        self.downward_speed=-self.downward_speed
ball1=ball()
brick1=bricks(50,50,2)
arr=pygame.sprite.Group()
arr.add(brick1)
arr.add(bricks(150,50,2))
arr.add(bricks(250,50,2))
arr.add(bricks(350,50,2))
arr.add(bricks(450,50,2))

arr.add(bricks(50,110,2))
arr.add(bricks(150,110,2))
arr.add(bricks(250,110,2))
arr.add(bricks(350,110,2))
arr.add(bricks(450,110,2))
#Gameloop
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    #Makes it stay inside the screen
    #Code is missing, couldnt get it working.
    screen.fill(bg)
    ball1.update()
    arr.draw(screen)
    temp=pygame.sprite.spritecollide(ball1,arr,False)
    for i in temp:
        i.hit()
    if len(temp)>0:
        ball1.hit()

    
    key=pygame.key.get_pressed()
    
    #Pongbar
    if key[pygame.K_RIGHT]==1 and bar1.right<=w:
        bar1=pygame.Rect.move(bar1,barspeed,0)
    if key[pygame.K_LEFT]==1 and bar1.left>=0:
        bar1=pygame.Rect.move(bar1,-barspeed,0)
    if key[pygame.K_SPACE]==1:
        ball1.space_pressed=True
    pygame.draw.rect(screen,(white),bar1)
    pygame.display.update()
pygame.quit()