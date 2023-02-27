import pygame
from config import *
from element import Element


class UI:
    def __init__(self):
        # General
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.inventory = pygame.sprite.Group()

        self.life_p1_0 = pygame.sprite.Group()
        self.life_p1_1 = pygame.sprite.Group()
        self.life_p1_2 = pygame.sprite.Group()
        self.life_p1_3 = pygame.sprite.Group()

        self.life_p2_0 = pygame.sprite.Group()
        self.life_p2_1 = pygame.sprite.Group()
        self.life_p2_2 = pygame.sprite.Group()
        self.life_p2_3 = pygame.sprite.Group()

        # Inventory
        self.hud_fill = pygame.image.load('assets/UI/hud_fill.png')

        self.heart_empty = pygame.image.load('assets/UI/heart_empty.png')

        self.player_1_icon = pygame.image.load('assets/UI/red_icon.png')

        self.bullet_1_icon = pygame.image.load('assets/UI/gun.png')
        self.key_1_icon = pygame.image.load('assets/UI/key.png')

        self.player_2_icon = pygame.image.load('assets/UI/blue_icon.png')
        self.bullet_2_icon = pygame.image.load('assets/UI/gun.png')
        self.key_2_icon = pygame.image.load('assets/UI/key.png')

        self.health_icon = []

        for i in range(0, 4):
            self.health_icon.append(pygame.image.load('assets/UI/health_{}.png'.format(i)))

        self.add_inventory()

        self.health_1 = 3
        self.bullet_1 = 12
        self.medic_kit_1 = 1
        self.key_1 = 2

        self.health_2 = 3
        self.bullet_2 = 12
        self.medic_kit_2 = 1
        self.key_2 = 2

    def draw_inventory(self):
        self.display_surface.blit(self.hud_fill, (0, 0))
        self.inventory.draw(self.display_surface)

    def get_group(self):
        return self.inventory

    def set_health_player1(self, health):
        self.health_1 = health

    def set_health_player2(self, health):
        self.health_2 = health

    def add_inventory(self):
        # Fill
        Element((0, 0), [self.inventory], self.hud_fill)
        Element((925, 0), [self.inventory], self.hud_fill)

        # Player 1
        Element((ICON_WIDTH, ICON_HEIGHT), [self.inventory], pygame.transform.scale(self.player_1_icon, (75, 75)))
        Element((BULLET_WIDTH, BULLET_HEIGHT), [self.inventory], self.bullet_1_icon)

        Element((HEALTH_WIDTH, HEALTH_HEIGHT), [self.life_p1_0], self.health_icon[0])
        Element((HEALTH_WIDTH, HEALTH_HEIGHT), [self.life_p1_1], self.health_icon[1])
        Element((HEALTH_WIDTH, HEALTH_HEIGHT), [self.life_p1_2], self.health_icon[2])
        Element((HEALTH_WIDTH, HEALTH_HEIGHT), [self.life_p1_3], self.health_icon[3])

        # Player 2
        Element((HEALTH_WIDTH + 925, HEALTH_HEIGHT), [self.life_p2_0], self.health_icon[0])
        Element((HEALTH_WIDTH + 925, HEALTH_HEIGHT), [self.life_p2_1], self.health_icon[1])
        Element((HEALTH_WIDTH + 925, HEALTH_HEIGHT), [self.life_p2_2], self.health_icon[2])
        Element((HEALTH_WIDTH + 925, HEALTH_HEIGHT), [self.life_p2_3], self.health_icon[3])

        Element((ICON_WIDTH + 925, ICON_HEIGHT), [self.inventory], pygame.transform.scale(self.player_2_icon, (75, 75)))
        Element((BULLET_WIDTH + 925, BULLET_HEIGHT), [self.inventory], self.bullet_2_icon)

    def inventory_data(self):
        if self.health_1 == 0:
            self.life_p1_0.draw(self.display_surface)
        elif self.health_1 == 1:
            self.life_p1_1.draw(self.display_surface)
        elif self.health_1 == 2:
            self.life_p1_2.draw(self.display_surface)
        elif self.health_1 == 3:
            self.life_p1_3.draw(self.display_surface)

        if self.health_2 == 0:
            self.life_p2_0.draw(self.display_surface)
        elif self.health_2 == 1:
            self.life_p2_1.draw(self.display_surface)
        elif self.health_2 == 2:
            self.life_p2_2.draw(self.display_surface)
        elif self.health_1 == 3:
            self.life_p2_3.draw(self.display_surface)

        # Player 1
        health_text_1 = self.font.render(f'[{self.health_1}]', True, WHITE, GREY)
        health_text_rect_1 = health_text_1.get_rect()
        health_text_rect_1.center = HEALTH_TEXT_POS_1
        self.display_surface.blit(health_text_1, health_text_rect_1)

        # Player 2
        health_text_2 = self.font.render(f'[{self.health_2}]', True, WHITE, GREY)
        health_text_rect_2 = health_text_2.get_rect()
        health_text_rect_2.center = HEALTH_TEXT_POS_2
        self.display_surface.blit(health_text_2, health_text_rect_2)
