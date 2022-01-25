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
l5=pygame.draw.line(screen,(100,0,0),(100,300),(250,300),2)
l6=pygame.draw.rect(screen,(110,0,0),l5,2)
rect1=pygame.Rect(100,100,150,100)
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
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
                    print(count)
                    pygame.draw.rect(screen,(0,0,100),rect1)
                    l6=pygame.Rect.move(l6,5,0)
                    pygame.draw.rect(screen,(0,0,0),l6,2)

                    
                else:
                    
                    pygame.draw.rect(screen,(0,0,250),rect1)
        else:
            pygame.draw.rect(screen,(a,b,c),rect1)
            
    else:

        pygame.draw.rect(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),rect1)
        action=False
    l1=pygame.draw.line(screen,(255,255,255),(100+5*count,100),(250+5*count,100),2)
    l2=pygame.draw.line(screen,(255,255,255),(100+5*count,100),(100+5*count,200),2)
    l3=pygame.draw.line(screen,(0,0,0),(100+5*count,200),(250+5*count,200),2)
    l4=pygame.draw.line(screen,(0,0,0),(250+5*count,200),(250+5*count,100),2)
    pygame.draw.rect(screen,(187,255,200),l6,2)
    
    pygame.display.update()
pygame.quit()
