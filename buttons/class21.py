import pygame
import random
pygame.init()
count=0
w=600
h=600
bg = (204, 102, 0)
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Button Demo')
action=False
run=True
isclicked=0
a,b,c=150,150,150

rect1=pygame.Rect(100,100,150,100)
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
    screen.fill(bg)
    pos=pygame.mouse.get_pos()

    if action!=True:
        if rect1.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                isclicked=1
                pygame.draw.rect(screen,(0,100,0),rect1)
            else:
                if isclicked==1:
                    a=random.randint(0,256)
                    b=random.randint(0,256)
                    c=random.randint(0,256)
                    isclicked=False
                    action=True
                    count+=1
                    rect1=pygame.Rect.move(rect1,5,0)
                    l2=pygame.Rect.move_ip(l2,5,0)
                    print(count)
                    pygame.draw.rect(screen,(0,0,100),rect1)
                else:
                    
                    pygame.draw.rect(screen,(0,0,250),rect1)
        else:
            pygame.draw.rect(screen,(a,b,c),rect1)
    else:

        pygame.draw.rect(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),rect1)
        action=False
    l1=pygame.draw.line(screen,(255,255,255),(100+5*count,100),(250+5*count,100),2)
    l2=pygame.draw.line(screen,(255,255,255),(100,100),(100,200),2)
    pygame.draw.line(screen,(0,0,0),(100,200),(250,200),2)
    pygame.draw.line(screen,(0,0,0),(250,200),(250,100),2)
    
    
pygame.quit()
