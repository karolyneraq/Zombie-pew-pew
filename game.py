import pygame
from player import Player
from pygame.locals import *
from config import *

pygame.init()
pygame.joystick.init()
Joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
print(Joysticks)

# clock
clock = pygame.time.Clock()

# screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Zombie Pew Pew")

# font
font = pygame.font.Font('assets/PressStart2P.ttf', 45)

# players
cow1 = Player("assets/Character_1/", 250, 300)
player_group = pygame.sprite.Group()
player_group.add(cow1)

# background
background1 = pygame.image.load("assets/background1.png")
background2 = pygame.image.load("assets/background2.png")
background3 = pygame.image.load("assets/background3.png")

loop = True

while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        # setting the hat commands

        if event.type == JOYBUTTONDOWN:
            print(event)
    cow1.set_movement()
    cow1.move()

    pygame.display.flip()
    screen.blit(background3, (175, 0))
    player_group.draw(screen)
    player_group.update()
    clock.tick(60)
