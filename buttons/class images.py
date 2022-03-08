import pygame
from pygame.locals import *

pygame.init()

width=600
height=600

bg = (204, 102, 0)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Button Demo')


button_image=pygame.image.load("buttons\icon2.png")
row = pygame.transform.scale(button_image, (100,100))
run=True
while run:
    screen.fill(bg)
    pos=pygame.mouse.get_pos()
    img=Rect(75,200,100,100)
    #pygame.draw.rect(screen,(255,0,0),Rect(75,200,100,100))
    screen.blit(row,img)



    # if Rect(75,200,100,100).collidepoint(pos):
    #     pygame.draw.rect(screen,(75,225,255),Rect(75,200,100,100))
    # pygame.draw.line(screen, (0,0,0),(75,300),(175,300),2)
    # pygame.draw.line(screen, (0,0,0),(175,200),(175,300),2)
    # pygame.draw.line(screen, (255,255,255),(75,200),(175,200),2)
    # pygame.draw.line(screen, (255,255,255),(75,200),(75,300),2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            if img.collidepoint(pygame.mouse.get_pos()):
                print("fiwkurh")
    pygame.display.update()
pygame.quit()
