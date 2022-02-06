import random
import pygame
import sys

def terminate():
    pygame.quit()
    sys.exit()

pygame.init()

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
fps=30

screen_height = 520
screen_width = 650
screen = pygame.display.set_mode((screen_width,screen_height))

class Rect1(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color,value):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.value = value
    def update(self):
        self.rect.x+=2
        
class mousep(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center=pygame.mouse.get_pos()
    def update(self):
        self.rect.center=pygame.mouse.get_pos()
        pygame.draw.rect(screen,(0,0,0),self.rect)
    def clicked(self):
        pygame.sprite.spritecollide(mousep,rects,True)

rects = pygame.sprite.Group()
mousep=mousep()
rect = Rect1(50,50,100,100,black,0)
rects.add(rect)
m=50
while True:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousep.clicked()
    if m>0:
        rects.add(Rect1(random.randint(0,screen_width-100),random.randint(0,screen_height-100),100,100,(random.randint(0,255),0,0),0))
    screen.fill(white)
    
    pygame.sprite.spritecollide(mousep,rects,False)
    

    rects.draw(screen)
    m-=1

    rects.update()
    mousep.update()
    pygame.display.update()

    clock.tick(fps)