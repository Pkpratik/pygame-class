import pygame, random
from tilehit import tilehitrun
from brickbreaker import brickbreaker
from variables import *
from pong_final import pong
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
            if pong_button.collidepoint(event.pos):
                pong()

        key=pygame.key.get_pressed()
        if qwerty==True:
            if key[pygame.K_1]==1 and key[pygame.K_0]==1:
                display_easteregg2=True
            if display_easteregg2==True:
                pygame.mixer.Sound.play(eeg2)
                pygame.time.wait(3000)
                qwerty=False

    #Displaying the buttons
    pygame.draw.rect(screen,(0,0,0),th_button)
    screen.blit(th_img,(75,150))
    pygame.draw.rect(screen,(0,0,0),bb_button)
    screen.blit(bb_img,(325,150))
    pygame.draw.rect(screen,(0,0,0),pong_button)
    screen.blit(pong_img,(200,300))
    #Title
    title=title_font.render("Profielwerkstuk",True,(0,0,0))
    screen.blit(title,(50,50))
    pygame.display.update()
pygame.quit()