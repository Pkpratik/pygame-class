import pygame

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode([800,800])
base_font=pygame.font.Font(None,32)
user_text=""

input_rect= pygame.Rect(200,200,140,32)
color_active=(40,40,150)
color_passive=(100,100,100)
color=color_passive

active=False
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active=True
                color=color_active
            else:
                active=False
                color=color_passive
        
        if active==True:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    user_text=user_text[:-1]
                else:
                    user_text+=event.unicode
            
    screen.fill((0,0,0))
    pygame.draw.rect(screen,color,input_rect,4)

    text_surface = base_font.render(user_text,True,(255,255,255))
    screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))

    input_rect.w = max(text_surface.get_width()+10,140)

    pygame.display.flip()
    clock.tick(60)