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
rect1=pygame.Rect(100,100,150,100)
l5=pygame.draw.line(screen,(255,255,255),(300,100),(400,100),2)
l6=pygame.draw.rect(screen,(123,56,0),l5,2)
a,b,c=150,150,150
speed=2
speed2=2
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.fill(bg)
    pos=pygame.mouse.get_pos()

    key=pygame.key.get_pressed()

    if rect1.right>=w or rect1.left<=0:
        speed=-speed
    if rect1.top<=0 or rect1.bottom>=w:
        speed2=-speed2

    if key[pygame.K_RIGHT]==1:
        rect1=pygame.Rect.move(rect1,speed,0)
        print("Right")
    if key[pygame.K_LEFT]==1:
        rect1=pygame.Rect.move(rect1,-speed,0)
        print("left")
    if key[pygame.K_UP]==1:
        rect1=pygame.Rect.move(rect1,0,-speed2)
        print("up")
    if key[pygame.K_DOWN]==1:
        rect1=pygame.Rect.move(rect1,0,speed2)
        print("down")





    if action!=True:
        if rect1.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                isclicked=1
                pygame.draw.rect(screen,(0,100,0),rect1)
            else:
                if isclicked==1:
                    a=random.randint(0,255)
                    b=random.randint(0,255)
                    c=random.randint(0,255)
                    isclicked=False
                    action=True
                    count+=1
                    
                    print(count)
                    pygame.draw.rect(screen,(0,0,100),
                    rect1)
                    rect1= pygame.Rect.move(rect1,5,0)
                    l6=pygame.Rect.move(l6,5,0)
                else:
                    
                    pygame.draw.rect(screen,(0,0,250),rect1)
        else:
            pygame.draw.rect(screen,(a,b,c),rect1)
    else:

        pygame.draw.rect(screen,(200,100,0),rect1)
        action=False
    l1=pygame.draw.line(screen,(255,255,255),(rect1.left,rect1.top),(rect1.right,rect1.top),2)
    l2=pygame.draw.line(screen,(255,255,255),(100+count*5,100),(100+count*5,200),2)
    pygame.draw.line(screen,(0,0,0),(100+count*5,200),(250+count*5,200),2)
    pygame.draw.line(screen,(0,0,0),(250+count*5,200),(250+count*5,100),2)
    pygame.draw.rect(screen,(0,0,0),l6,2)    
    
    pygame.display.update()
pygame.quit()
