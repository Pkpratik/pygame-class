#Basic frameworking
import pygame, random
pygame.init()
pygame.display.set_caption("Piano Hit")
bg=(255,255,255)

#Important Data
screen_width=288
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()
started=False
starting_button=pygame.Rect(screen_width//4,150,156,75)
starting_font=pygame.font.Font(None,64)
base_font=pygame.font.Font(None,32)

#Colors
white=(255,255,255)
gray=(128,128,128)
black=(0,0,0)

#Tiles Data
speed=2
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
            if i.alive==True:
                self.score+=1
                i.alive=False
        
        
#Class object in variables
clicker=mouse()
tiles=pygame.sprite.Group()
run=True
while run:
    #Standard while-loop beginning
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if starting_button.collidepoint(event.pos):
                pygame.draw.rect(screen,(85,176,85),starting_button)
                run=False
    pygame.draw.rect(screen,(4,126,4),starting_button)
    someothervariable2=starting_font.render("START",True,black)
    screen.blit(someothervariable2,(80,170))
    game_explanation=base_font.render("Game info(tbc)",True,black)
    screen.blit(game_explanation,(80,380))
    pygame.display.update()
    
#
tiles.add(Tiles(random.randint(0,3),-tile_height))

#Actual Game
fps=30
run=True
while run:
    #Standard while-loop beginning
    clock.tick(fps)
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            clicker.clicked()
    
    #Before hitting the Start button
    mouse_pos=pygame.mouse.get_pos()

    #After hitting the Start button  
    scrolling+=speed
    if scrolling%600==0:
        speed+=1

    #Tile creation
    if len(tiles)>0:
        t=tiles.sprites()[-1]
        print(t.rect.top,t)
        y=-tile_height+t.rect.top
        if t.rect.top+speed>=0:
            tiles.add(Tiles(random.randint(0,3),y))
    else:
        t=tiles.sprites()[-1]
        y=-tile_height+t.rect.top
        tiles.add(Tiles(random.randint(0,3),-y))


    if tiles.sprites()[0].rect.bottom>=screen_height:
        if tiles.sprites()[0].alive==True:
            pygame.time.wait(4000)
            
    
    tiles.update(speed)
    someothervariable1=base_font.render("Score - "+str(clicker.score),True,(255,0,0))
    screen.blit(someothervariable1,(screen_width//3,40))
    clicker.update()
    #Standard while-loop End
    pygame.display.update()
pygame.quit()
