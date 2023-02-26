import pygame
from player import Player
from config import *
from zombie import Zombie
from hall1 import Hall1
from room1 import Room1

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
cow1 = Player("assets/char_1red/", (325, 300))
player_group = pygame.sprite.Group()
player_group.add(cow1)

# Zombie
zombie = Zombie("assets/zombie/", (650, 150), True, False, False, False)
zombie_group = pygame.sprite.Group()
zombie_group.add(zombie)

# scenarios
choice_scenario = 2
scenario1 = Room1()
scenario2 = Hall1()

# collision
obstacles1 = scenario1.get_group()
obstacles2 = scenario2.get_group()

# background
background1 = pygame.image.load("assets/background1.png")
background2 = pygame.image.load("assets/background2.png")
background3 = pygame.image.load("assets/background3.png")

loop = True

while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # Movement Keys
    cow1.set_movement(pygame.joystick.Joystick(0))
    cow1.set_fire(pygame.joystick.Joystick(0))

    # Moving the objects
    for bullet in cow1.get_bullets():
        bullet.move()

    # Showing everything
    pygame.display.flip()
    screen.blit(background3, (175, 0))

    if choice_scenario == 1:
        scenario1.draw_scenario()
        cow1.set_obstacles(obstacles1)
        cow1.set_zombies(zombie_group)
        for monstro in zombie_group:
            monstro.set_obstacles(obstacles1)
    else:
        scenario2.draw_scenario()
        cow1.set_obstacles(obstacles2)
        cow1.set_zombies(zombie_group)
        for monstro in zombie_group:
            monstro.set_obstacles(obstacles2)

    zombie_group.draw(screen)
    player_group.draw(screen)
    cow1.get_bullets().draw(screen)

    zombie_group.update()
    player_group.update()

    clock.tick(60)
