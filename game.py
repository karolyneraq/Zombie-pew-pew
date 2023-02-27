import pygame
from player import Player
from config import *
from zombie import Zombie
from hall1 import Hall1
from room1 import Room1
from hall2 import Hall2
from ui import UI

pygame.init()
pygame.joystick.init()
Joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
print(Joysticks)

# clock
clock = pygame.time.Clock()

# screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Zombie Pew Pew")

# players
cow1 = Player("assets/char_1red/", (325, 300))
player_group = pygame.sprite.Group()
player_group.add(cow1)

# Zombie
zombie = Zombie("assets/zombie/", (650, 150), True, False, False, False)
zombie_group = pygame.sprite.Group()
zombie_group.add(zombie)

# scenarios
scenario1 = Room1()
door_open = False
scenario2 = Hall1()
hall_end = False
scenario3 = Hall2()
chest_open = False

# collision
obstacles1 = scenario1.get_group()
obstacles2 = scenario2.get_group()
obstacles3 = scenario3.get_obstacle()

# stage_hazard
stage_hazard = [scenario2.get_stage_hazard(), scenario3.get_stage_hazard()]

# interaction sprites
interaction_sprites = scenario1.get_interactions_sprites()

# background
background1 = pygame.image.load("assets/background1.png")
background2 = pygame.image.load("assets/background2.png")
background3 = pygame.image.load("assets/background3.png")

# User interface
ui = UI()

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

    if not door_open:
        scenario1.draw_scenario()
        cow1.set_obstacles(obstacles1)
        cow1.set_zombies(zombie_group)

        for monstro in zombie_group:
            monstro.set_obstacles(obstacles1)

        if 440 <= cow1.get_rect().x <= 480 and cow1.get_rect().y == 225:
            if not chest_open:
                scenario1.open_chest()
                chest_open = True

        if chest_open:
            scenario1.chest_opened()

        if cow1.get_rect().x == 790 and 250 <= cow1.get_rect().y <= 300:
            door_open = True
            screen.blit(background3, (175, 0))
            cow1.set_rect_topleft(250, 275)

    elif not hall_end:
        scenario2.draw_scenario()
        cow1.set_obstacles(obstacles2)
        cow1.set_zombies(zombie_group)

        for monstro in zombie_group:
            monstro.set_obstacles(obstacles2)

        if cow1.get_rect().x >= 860:
            hall_end = True
            screen.blit(background3, (175, 0))
            cow1.set_rect_topleft(250, 275)
    else:
        scenario3.draw_scenario()
        cow1.set_obstacles(obstacles3)

    ui.draw_inventory()
    ui.inventory_data()

    zombie_group.draw(screen)
    player_group.draw(screen)
    cow1.get_bullets().draw(screen)

    zombie_group.update()
    player_group.update()

    clock.tick(60)
