import pygame

pygame.init()

screen = pygame.display.set_mode([600,600])
rect1=pygame.Rect(300-50,200,140,32)
base_font=pygame.font.Font(None,32)
text=""



active=True
while active:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            text+=event.unicode


    screen.fill((0,0,0))


    
    pygame.draw.rect(screen,(200,0,0),rect1,4)


    surface=base_font.render(text,True,(0,200,0))
    rect1.w = max(100,surface.get_width()//2)
    screen.blit(surface,(300-surface.get_width()//2,rect1.y))

    rect1.x=300-rect1.w//2

    pygame.display.update()
pygame.quit()