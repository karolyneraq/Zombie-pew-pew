import pygame
from player import Player
from config import *
from zombie import Zombie
from ui import UI
from hall1 import Hall1
import random



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
font = pygame.font.Font('assets/font/PressStart2P.ttf', 45)

# players
cow1 = Player("assets/Character_1/", 250, 300)
player_group = pygame.sprite.Group()
player_group.add(cow1)

# Zombie
zombie = Zombie(325, 150, True, False, False, False)
zombie_group = pygame.sprite.Group()
zombie_group.add(zombie)

# scenario 2
scenario = Hall1()

# background
background1 = pygame.image.load("assets/background1.png")
background2 = pygame.image.load("assets/background2.png")
background3 = pygame.image.load("assets/background3.png")

# User interface
ui = UI()
# ui_group = pygame.sprite.Group()
# ui_group.add(ui)

loop = True

while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # Movement Keys
    #cow1.set_movement(pygame.joystick.Joystick(0))
    cow1.set_fire(pygame.joystick.Joystick(0))

    # Moving the objects
    cow1.move()
    zombie.move()
    for bullet in cow1.get_bullets():
        bullet.move()

    # Showing everything
    pygame.display.flip()
    screen.blit(background3, (175, 0))
    scenario.draw_scenario()
    ui.draw_inventory()
    ui.inventory_data()

    zombie_group.draw(screen)
    player_group.draw(screen)
    cow1.get_bullets().draw(screen)
    zombie_group.update()
    player_group.update()

    clock.tick(60)
