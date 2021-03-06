import pygame, random
pygame.init()
pygame.display.set_caption("Piano Hit")
#Important Data
w=288
h=600
white=(255,255,255)
gray=(128,128,128)
black=(0,0,0)
bg=(white)
screen=pygame.display.set_mode((w,h))
run=True
base_font=pygame.font.Font(None,32)
speed=2
scrolling=0
num_tiles=0
tile_height=120
fps=30
clock=pygame.time.Clock()
class Tiles(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface([(w//4),tile_height])
        self.image.fill(black)
        self.rect=self.image.get_rect()
        self.rect.x=x*(w//4)
        self.rect.y=y
        self.alive=True
    def update(self,speed):
        self.rect.y+=speed
        if self.alive==True:
            pygame.draw.rect(screen,black,self.rect)
        else:
            pygame.draw.rect(screen,gray,self.rect)
        if self.rect.top>=h:
            self.kill()
            print("killed")


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
        #print(self.rect.center)
    def clicked(self):
        click=pygame.sprite.spritecollide(mkiller,tiles,False)
        for i in click:
            i.alive=False
            self.score+=1
            print(self.score)
        
        

mkiller=mouse()
tiles=pygame.sprite.Group()
result = "Created by Rishi"
def myFun ():
    print("Rishi")

alpha = "aplha "
beta = "beta"
while run:
    clock.tick(fps)
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mkiller.clicked()
    if scrolling>=(num_tiles*tile_height):
        tiles.add(Tiles(random.randint(0,3),-tile_height))
        num_tiles+=1
    scrolling+=speed
    if scrolling%350==0:
        speed+=1
    if tiles.sprites()[0].rect.bottom>=h:
        if tiles.sprites()[0].alive==True:
            pygame.time.wait(4000)
            pygame.quit()
    score_surface = base_font.render("score - ",True,(0,0,0))
    screen.blit(score_surface,((w-len(("score - "))*10)//2,35))
    mkiller.update()
    tiles.update(speed)
    pygame.display.update()
pygame.quit()