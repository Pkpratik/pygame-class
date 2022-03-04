import pygame
import random
pygame.init()
w=600
h=600
bg=((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
screen=pygame.display.set_mode((w,h))
fps=60
run=True
clock=pygame.time.Clock()

class rects(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([25,25])
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.center=pygame.mouse.get_pos()
        pygame.draw.rect(screen,(0,255,0),self.rect)
    def clicked(self):
        pygame.sprite.spritecollide(mouseshape,arr,True)

class otherrectangles(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface([100,100])
        self.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
rectamounts=50
mouseshape=rects()
arr=pygame.sprite.Group()
o1=otherrectangles(0,0)
arr.add(o1)

while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouseshape.clicked()
    if rectamounts:
        arr.add(otherrectangles(random.randint(0,w-100,),random.randint(0,h-100)))       
        rectamounts-=1
    screen.fill(bg)
    arr.draw(screen)
    mouseshape.update()
    pygame.display.update()
pygame.quit()