import pygame

pygame.init()

w=600
h=600
bg = (204, 102, 0)
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Button')

#Game loop
run=True
while run:
    screen.fill(bg)
    rect1=pygame.draw.Rect(100,100,400,400)





    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.draw.rect(screen,(255,0,0),(100,100,400,400))    
    #Outlines of the button
    pygame.draw.line(screen,(255,255,255),(100,100),(100,500),2)
    pygame.draw.line(screen,(255,255,255),(100,100),(500,100),2)
    pygame.draw.line(screen,(0,0,0),(500,500),(100,500),2)
    pygame.draw.line(screen,(0,0,0),(500,500),(500,100),2)
    

    pygame.display.update()



#Should always stay last.
pygame.quit()