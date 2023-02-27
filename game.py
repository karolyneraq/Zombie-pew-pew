import pygame
from player import Player
from config import *
from zombie import Zombie
from hall1 import Hall1
from room1 import Room1
from hall2 import Hall2
from ui import UI
from element import Element

pygame.init()
pygame.joystick.init()
Joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
print(Joysticks)

# clock
clock = pygame.time.Clock()

# Playback
music = pygame.mixer.Sound("assets/sounds/theme_song.mp3")
music.set_volume(0.25)
music.play()
time_music = pygame.time.get_ticks()

# screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Zombie Pew Pew")

# players
cow1 = Player("assets/char_1red/", (325, 250))
cow2 = Player("assets/char2_blue/", (325, 350))
player_group = pygame.sprite.Group()
player_group.add(cow1)
player_group.add(cow2)

# Zombie
zombie = Zombie("assets/zombie/", (650, 150), True, False, False, False, True)
zombie_group = pygame.sprite.Group()
zombie_group.add(zombie)

zombie_list = []
for y in range(75, 451, 75):
    print(y)
    zombie_list.append(Zombie("assets/zombie/", (850, y), True, False, False, False, False))

zombie_list_group = pygame.sprite.Group()

for zombie in zombie_list:
    zombie_list_group.add(zombie)

horde_wave = 1
zombie_horde = []
for y in range(75, 451, 75):
    print(y)
    zombie_horde.append(Zombie("assets/zombie/", (850, y), True, False, False, False, True))


# scenarios
scenario1 = Room1()
door_open = False
scenario2 = Hall1()
hall_end = False
scenario3 = Hall2()
chest_open = False

# Victory and Game Over Screen
victory_pic = pygame.image.load("assets/Victory_screen.png")
victory_sound = pygame.mixer.Sound("assets/sounds/you_won.wav")
lost_pic = pygame.image.load("assets/Lose_screen.png")
lost_group = pygame.sprite.Group()
Element((0, 0), lost_group, lost_pic)
lost_sound = pygame.mixer.Sound("assets/sounds/you_lose.wav")
played_sound = 0

# collision
obstacles1 = scenario1.get_group()
obstacles2 = scenario2.get_group()
obstacles3 = scenario3.get_obstacle()

# interaction sprites
interaction_sprites = scenario1.get_interactions_sprites()

# background
background1 = pygame.image.load("assets/background1.png")
background2 = pygame.image.load("assets/background2.png")
background3 = pygame.image.load("assets/background3.png")

# User interface
ui = UI()

# victory condition
victory = False

loop = True

while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    if pygame.time.get_ticks() - time_music <= 0:
        music.play()
        time_music = pygame.time.get_ticks()

    # Movement Keys
    cow1.set_movement(pygame.joystick.Joystick(0))
    cow1.set_fire(pygame.joystick.Joystick(0))
    cow2.set_movement(pygame.joystick.Joystick(0))
    cow2.set_fire(pygame.joystick.Joystick(0))

    if not victory and len(player_group) != 0:
        # Moving the objects
        for bullet in cow1.get_bullets():
            bullet.move()
        for bullet in cow2.get_bullets():
            bullet.move()

        # Showing everything
        pygame.display.flip()
        screen.blit(background3, (175, 0))

        if not door_open:
            ui.set_health_player1(cow1.get_health())
            ui.set_health_player2(cow2.get_health())
            scenario1.draw_scenario()
            cow1.set_obstacles(obstacles1)
            cow1.set_zombies(zombie_group)
            cow2.set_obstacles(obstacles1)
            cow2.set_zombies(zombie_group)

            for monstro in zombie_group:
                monstro.set_obstacles(obstacles1)

            zombie_group.draw(screen)

            if cow1.get_rect().x == 790 and 250 <= cow1.get_rect().y <= 300 or cow2.get_rect().x == 790 and \
                    250 <= cow2.get_rect().y <= 300:
                door_open = True
                screen.blit(background3, (175, 0))
                cow1.set_rect_topleft(325, 275)
                cow2.set_rect_topleft(325, 350)

        elif not hall_end:
            ui.set_health_player1(cow1.get_health())
            ui.set_health_player2(cow2.get_health())
            scenario2.draw_scenario()
            cow1.set_obstacles(obstacles2)
            cow1.set_zombies(zombie_group)
            cow1.set_hazards(scenario2.get_stage_hazard())
            cow2.set_obstacles(obstacles2)
            cow2.set_zombies(zombie_group)
            cow2.set_hazards(scenario2.get_stage_hazard())

            for monstro in zombie_group:
                monstro.set_obstacles(obstacles2)

            zombie_group.draw(screen)

            if cow1.get_rect().x >= 860 or cow2.get_rect().x >= 860:
                hall_end = True
                screen.blit(background3, (175, 0))
                cow1.set_rect_topleft(250, 275)
                cow2.set_rect_topleft(325, 350)
        else:
            if horde_wave == 1:
                if len(zombie_group) == 0:
                    for zombie in zombie_horde:
                        zombie_group.add(zombie)
                    for monstro in zombie_group:
                        monstro.set_obstacles(obstacles3)
                    horde_wave = 2
            if horde_wave == 2:
                if len(zombie_group) == 0:
                    wait1 = pygame.time.get_ticks()
                    for x in range(775, 851, 75):
                        for y in range(75, 451, 75):
                            zombie_horde.append(Zombie("assets/zombie/", (x, y), True, False, False, False, True))
                    for zombie in zombie_horde:
                        zombie_group.add(zombie)
                    for monstro in zombie_group:
                        monstro.set_obstacles(obstacles3)
                    horde_wave = 3
            if horde_wave == 3:
                if len(zombie_group) == 0:
                    wait1 = pygame.time.get_ticks()
                    for x in range(700, 851, 75):
                        for y in range(75, 451, 75):
                            zombie_horde.append(Zombie("assets/zombie/", (x, y), True, False, False, False, True))
                    for zombie in zombie_horde:
                        zombie_group.add(zombie)
                    for monstro in zombie_group:
                        monstro.set_obstacles(obstacles3)
                    horde_wave = 4
            if horde_wave == 4:
                if len(zombie_group) == 0:
                    wait1 = pygame.time.get_ticks()
                    for x in range(625, 851, 75):
                        for y in range(75, 451, 75):
                            zombie_horde.append(Zombie("assets/zombie/", (x, y), True, False, False, False, True))
                    for zombie in zombie_horde:
                        zombie_group.add(zombie)
                    for monstro in zombie_group:
                        monstro.set_obstacles(obstacles3)
                    horde_wave = 5
            if horde_wave == 5 and len(zombie_group) == 0:
                for zombie in zombie_list_group:
                    zombie.kill()
                victory = True
            scenario3.draw_scenario()
            ui.set_health_player1(cow1.get_health())
            ui.set_health_player2(cow2.get_health())
            zombie_list_group.draw(screen)
            cow1.set_obstacles(obstacles3)
            cow1.set_zombies(zombie_group)
            cow1.set_hazards(scenario3.get_stage_hazard())
            cow2.set_obstacles(obstacles3)
            cow2.set_zombies(zombie_group)
            cow2.set_hazards(scenario3.get_stage_hazard())
            zombie_group.draw(screen)
            zombie_list_group.update()

        ui.draw_inventory()
        ui.inventory_data()

        player_group.draw(screen)
        cow1.get_bullets().draw(screen)
        cow2.get_bullets().draw(screen)

        zombie_group.update()
        player_group.update()

    elif victory and len(player_group) != 0:
        pygame.display.flip()
        screen.blit(victory_pic, (0, 0))
        music.fadeout(1000)
        if played_sound == 0:
            victory_sound.play()
            played_sound = 1
        pygame.display.flip()

    elif len(player_group) == 0:
        if played_sound == 0:
            lost_sound.play()
            played_sound = 1
        screen.blit(lost_pic, (0, 0))
        music.fadeout(1000)
        pygame.display.flip()

    clock.tick(60)
