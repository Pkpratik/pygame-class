import pygame

screen_width=600
screen_height=600
menu_bg=(185,255,185)
title_font=pygame.font.Font(None,95)
base_font=(None,32)


screen=pygame.display.set_mode((screen_width,screen_height))


th_button=pygame.draw.rect(screen,(0,0,0),(72,150,200,100))
bb_button=pygame.draw.rect(screen,(255,255,255),(322,150,200,100))

th_big=pygame.image.load('Jonah/Projects/final/pictures&sounds/tilehit.png')
th_img=pygame.transform.scale(th_big,(200,100))
bb_big=pygame.image.load('Jonah/Projects/final/pictures&sounds/brickbreaker.png')
bb_img=pygame.transform.scale(bb_big,(200,100))

#Actual hub
run=True