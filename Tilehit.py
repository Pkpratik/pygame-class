#Basic frameworking
import pygame, random
pygame.init()
pygame.display.set_caption("Piano Hit")
base_font=pygame.font.Font(None,32)

#Important Data
screen_width=288
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()
started=False
starting_button=pygame.Rect(screen_width//4,150,156,40)

#Colors
white=(255,255,255)
gray=(128,128,128)
black=(0,0,0)

#Tiles Data
speed=0
scrolling=0
num_tiles=0
tile_height=120

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
            i.alive=False
            self.score+=1
            print(self.score)
        
        
#Class object in variables
clicker=mouse()
tiles=pygame.sprite.Group()

#Actual Game
fps=30
run=True
while run:
    #Standard while-loop beginning
    clock.tick(fps)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            clicker.clicked()
    
    #Before hitting the Start button
    mouse_pos=pygame.mouse.get_pos()
    if started==False:
        if starting_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen,(85,176,85),starting_button)
            if pygame.mouse.get_pressed()[0]==1:
                started=True
        else:
            pygame.draw.rect(screen,(4,126,4),starting_button)
        

    if scrolling>=(num_tiles*tile_height):
        tiles.add(Tiles(random.randint(0,3),-tile_height))
        num_tiles+=1
    
    if started==True:
        scrolling+=speed
        if scrolling%250==0:
            speed+=1
    
    if tiles.sprites()[0].rect.bottom>=screen_height:
        if tiles.sprites()[0].alive==True:
            pygame.time.wait(4000)
            pygame.quit()
    
    tiles.update(speed)
    if started==True:
        someothervariable=base_font.render("Score - "+str(clicker.score),True,(255,0,0))
        screen.blit(someothervariable,(screen_width//3,40))
    clicker.update()
    #Standard while-loop End
    pygame.display.update()
pygame.quit()
