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
forward_speed=1
downward_speed=1
while run:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.fill(bg)
    pos=pygame.mouse.get_pos()
    
    key=pygame.key.get_pressed()
    if rect1.right>=w or rect1.left<=0:
        forward_speed=-forward_speed
    if rect1.top<=0 or rect1.bottom>=h:
        downward_speed=-downward_speed

    # if rect1.right>=w or rect1.left<=0:
    #     forward_speed=-forward_speed
    
    if key[pygame.K_RIGHT]==1:
        rect1=pygame.Rect.move(rect1,forward_speed,0)
        # print("Right = ",rect1.right)
        # print("Left = ",rect1.left)
        # print("speed = ",forward_speed)
        print("Right")
    if key[pygame.K_LEFT]==1:
        rect1=pygame.Rect.move(rect1,-forward_speed,0)
        # print("Right = ",rect1.right)
        # print("Left = ",rect1.left)
        print("Left")

    if key[pygame.K_UP]==1:
        rect1=pygame.Rect.move(rect1,0,-downward_speed)
        # print("Right = ",rect1.right)
        # print("Left = ",rect1.left)
        print("up")

    if key[pygame.K_DOWN]==1:
        rect1=pygame.Rect.move(rect1,0,downward_speed)
        # print("Right = ",rect1.right)
        # print("Left = ",rect1.left)
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
                    rect1=pygame.Rect.move(rect1,forward_speed,0)
                    print(count)
                    pygame.draw.rect(screen,(0,0,100),rect1)
                    l6=pygame.Rect.move(l6,forward_speed,0)
                    pygame.draw.rect(screen,(0,0,0),l6,2)

                    print("Right = ",rect1.right)
                    print("Left = ",rect1.left)
                else:
                    
                    pygame.draw.rect(screen,(0,0,250),rect1)
        else:
            pygame.draw.rect(screen,(a,b,c),rect1)
            
    else:

        pygame.draw.rect(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),rect1)
        action=False
    l1=pygame.draw.line(screen,(255,255,255),(100+2*count,100),(250+2*count,100),2)
    l2=pygame.draw.line(screen,(255,255,255),(100+2*count,100),(100+2*count,200),2)
    l3=pygame.draw.line(screen,(0,0,0),(100+2*count,200),(250+2*count,200),2)
    l4=pygame.draw.line(screen,(0,0,0),(250+2*count,200),(250+2*count,100),2)
    pygame.draw.rect(screen,(187,255,200),l6,2)
    
    pygame.display.update()
pygame.quit()
