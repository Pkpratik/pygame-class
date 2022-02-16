import pygame

width = 288 
height = 512

tile_width = width//4
tile_height = 130

class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,screen):
        super(Tile,self).__init__()
        self.screen = screen
        self.x=x
        self.y=y
        self.color = (0,0,0)
        self.image = pygame.Surface((tile_width,tile_height),pygame.SRCALPHA )
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y = y
        self.alive=True
    def update(self,speed):
        self.rect.y+=speed
        if self.rect.y>=height:
            self.kill()
        if self.alive==False:
            self.color=(0,0,0,90)
        pygame.draw.rect(self.image,self.color,(0,0,tile_width,tile_height))
        self.screen.blit(self.image,self.rect)
        