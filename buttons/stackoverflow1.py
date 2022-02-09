import pygame
from random import randint
from sys import exit

pygame.init()
game_active = True #start the game on the Welcome Screen
clock = pygame.time.Clock() #an object to track time, for fps


def display_surface():
    """function to create the main window"""
    disp_surface = pygame.display.set_mode(size = (610, 700)) #creates a main display window
    pygame.display.set_caption("Snake")
    return disp_surface
disp_surface = display_surface() #MUST return this immediately so it can be pushed to pygame.display.update()

class snake(pygame.sprite.Sprite):
    def __init__(self, x_pos = 300, y_pos = 300):
        #Access the super class of Sprite
        super().__init__()
        image1 = pygame.Surface([25,25])
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.image = image1
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(x = x_pos, y = y_pos)

    def update(self, left, right, up, down):
        """defines the movement of the snake using arrow keys"""
        if left:
            self.rect.left -= 1
        if right:
            self.rect.right += 1
        if up:
            self.rect.top -= 1
        if down:
            self.rect.bottom += 1

snakegroup = pygame.sprite.Group()
original_snake = snake()
snakegroup.add(original_snake)

class food(pygame.sprite.Sprite):
    """class to control food action"""
    def __init__(self):
        super().__init__() #access the Sprite super class methods
        food1 = pygame.Surface([25,25])
        x_pos = randint(50,600)
        y_pos = randint(50,650)
        self.image = food1
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect(x = x_pos,y = y_pos)

foods = pygame.sprite.GroupSingle()
foods.add(food())

multiplier_x_pos = 1
while True:
    """EVENT LOOP CODE"""
    for eachevent in pygame.event.get():
        if eachevent.type == pygame.QUIT:
            pygame.quit()
            exit()

        game_active = True
        if pygame.sprite.spritecollideany(foods.sprite, snakegroup):
            foods.empty()
            foods.add(food())
            foods.draw(disp_surface)

            snakegroup.add(snake(original_snake.rect.x-(25*multiplier_x_pos),original_snake.rect.y))
            multiplier_x_pos += 1
            snakegroup.update(left, right, up, down)
            
        
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        
        left = keys[pygame.K_LEFT]
        right = keys[pygame.K_RIGHT]
        up = keys[pygame.K_UP]
        down = keys[pygame.K_DOWN]
     
        snakegroup.update(left,right,up,down)

    """PYGAME EVENT CODE"""
    if game_active:
        disp_surface = display_surface()

        snakegroup.draw(disp_surface)
        foods.draw(disp_surface)

    else:
        disp_surface.fill((64,64,64))

    pygame.display.update() #update all the surfaces on each frame
    clock.tick(120)