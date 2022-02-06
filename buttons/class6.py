import random
import pygame

width=400
height=600

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((width,height))

fps=60
class mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([20,20])
        self.rect=self.image.get_rect()

    def update(self):
        self.rect.center=pygame.mouse.get_pos()

class tile(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.x=random.randint(0,3)*width//4
        self.y=-height//5
        self.b=(width//4)-2
        self.h=height//5
        self.image=pygame.Surface([self.b,self.h])
        self.rect=self.image.get_rect()
        self.rect.bottom=0
        self.clicked=False
    def update(self):
        self.rect.bottom+=speed
        if self.clicked:
            pygame.draw.rect(screen,(0,0,0),[self.x,self.y,self.b,self.h])
        else:
            pygame.draw.rect(screen,(180,180,180),[self.x,self.y,self.b,self.h])
    # def collide(self,mouse):
    #     print(self.x,self.b,mouse[0],mouse[1])
    #     if self.x<mouse[0] and self.x+self.b>mouse[0]:
    #         if self.y<mouse[1] and self.y+self.h>mouse[1]:
    #             return True
run=True
speed=2
mousesprite=pygame.sprite.Group()
mouseobject=mouse()
mousesprite.add(mouseobject)

tilegroup=pygame.sprite.Group()
tilegroup.add(tile())


while run:
    pygame.time.delay(50)
    screen.fill((200,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type== pygame.MOUSEBUTTONDOWN:
            if pygame.sprite.spritecollide(mouseobject,tilegroup,False):
                for i in pygame.sprite.spritecollide(mouseobject,tilegroup,False):
                    i.clicked=False
     
    tilegroup.draw(screen)  
    tilegroup.update()
    pygame.draw
    
    
            
        
    pygame.display.update()


