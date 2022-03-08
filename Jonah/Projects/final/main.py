import pygame, random
from tilehit import tilehitrun
from brickbreaker import brickbreaker
from variables import *
pygame.init()
pygame.mixer.init()



pygame.display.set_caption("Profielwerkstuk")


while run:
    #Standard while-loop beginning
    screen.fill(menu_bg)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if th_button.collidepoint(event.pos):
                tilehitrun()
            if bb_button.collidepoint(event.pos):
                brickbreaker()
    
    #Displaying the buttons
    pygame.draw.rect(screen,(0,0,0),th_button)#Can these 2 be images of the game?
    screen.blit(th_img,(72,150))
    pygame.draw.rect(screen,(0,0,0),bb_button)#And titles above it?
    screen.blit(bb_img,(322,150))

    #Title
    title=title_font.render("Profielwerkstuk",True,(0,0,0))
    screen.blit(title,(50,50))
    pygame.display.update()
pygame.quit()