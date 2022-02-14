import pygame
from sys import exit
from random import randint

pygame.init()

clock = pygame.time.Clock()

screen_width = 1000
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))

# Treasure
treasure = pygame.Surface([10,10])
treasure_surf = pygame.transform.scale(treasure, (10, 10))
treasure_surf.fill((100,200,150))
treasure_rect = treasure_surf.get_rect(center = (500, 330))

# Zombie
zombie_vel = 1
zombie = pygame.Surface([100,100])
zombie_surf = pygame.transform.scale(zombie, (100, 100))
zombie_surf.fill((200,100,150))
zombie_rect = zombie_surf.get_rect(center = (randint(0, 1000), randint(0, 600)))

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if zombie_rect.centerx < 500:
        zombie_rect.centerx += zombie_vel

    if zombie_rect.centerx > 500:
        zombie_rect.centerx -= zombie_vel

    if zombie_rect.centery < 330:
        zombie_rect.centery += zombie_vel

    if zombie_rect.centery > 330:
        zombie_rect.centery -= zombie_vel

    if zombie_rect.colliderect(treasure_rect):
        zombie_rect.centerx = randint(0, 1000)
        zombie_rect.centery = randint(0, 600)


    screen.fill('DarkGreen')
    screen.blit(treasure_surf, treasure_rect)
    screen.blit(zombie_surf, zombie_rect)
        

    pygame.display.update()
    clock.tick(60)