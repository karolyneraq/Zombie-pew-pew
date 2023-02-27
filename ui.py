import pygame
from config import *
from element import Element


class UI:
    def __init__(self):
        # General
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.inventory = pygame.sprite.Group()

        # Inventory
        self.hud_fill = pygame.image.load('assets/UI/hud_fill.png')

        self.heart_empty = pygame.image.load('assets/UI/heart_empty.png')

        self.player_1_icon = pygame.image.load('assets/UI/character_1_icon.png')
        self.health_1 = pygame.image.load('assets/UI/heart_full.png')
        self.bullet_1 = pygame.image.load('assets/UI/gun.png')
        self.medic_kit_1 = pygame.image.load('assets/UI/medics_kit.png')
        self.key_1 = pygame.image.load('assets/UI/key.png')

        self.player_2_icon = pygame.image.load('assets/UI/character_2_icon.png')
        self.health_2 = pygame.image.load('assets/UI/heart_full.png')
        self.bullet_2 = pygame.image.load('assets/UI/gun.png')
        self.medic_kit_2 = pygame.image.load('assets/UI/medics_kit.png')
        self.key_2 = pygame.image.load('assets/UI/key.png')

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

    def add_inventory(self):
        # Fill
        Element((0, 0), [self.inventory], self.hud_fill)
        Element((925, 0), [self.inventory], self.hud_fill)

        # Element(())

        # Player 1
        Element((ICON_WIDTH, ICON_HEIGHT), [self.inventory], self.player_1_icon)
        Element((HEALTH_WIDTH, HEALTH_HEIGHT), [self.inventory], self.health_1)
        Element((BULLET_WIDTH, BULLET_HEIGHT), [self.inventory], self.bullet_1)
        Element((MEDIC_KIT_WIDTH, MEDIC_KIT_HEIGHT), [self.inventory], self.medic_kit_1)
        Element((KEY_WIDTH, KEY_HEIGHT), [self.inventory], self.key_1)

        # Player 2
        Element((ICON_WIDTH + 925, ICON_HEIGHT), [self.inventory], self.player_2_icon)
        Element((HEALTH_WIDTH + 925, HEALTH_HEIGHT), [self.inventory], self.health_2)
        Element((BULLET_WIDTH + 925, BULLET_HEIGHT), [self.inventory], self.bullet_2)
        Element((MEDIC_KIT_WIDTH + 925, MEDIC_KIT_HEIGHT), [self.inventory], self.medic_kit_2)
        Element((KEY_WIDTH + 925, KEY_HEIGHT), [self.inventory], self.key_2)

    def inventory_data(self):
        # Player 1
        health_1 = 3
        bullet_1 = 12
        medic_kit_1 = 1
        key_1 = 2

        # Player 2
        health_2 = 3
        bullet_2 = 12
        medic_kit_2 = 1
        key_2 = 2

        # Player 1
        health_text_1 = self.font.render(f'[{health_1}]', True, WHITE, BLACK)
        health_text_rect_1 = health_text_1.get_rect()
        health_text_rect_1.center = HEALTH_TEXT_POS_1
        self.display_surface.blit(health_text_1, health_text_rect_1)

        bullet_text_1 = self.font.render(f'[{bullet_1}]', True, WHITE, BLACK)
        bullet_text_rect_1 = bullet_text_1.get_rect()
        bullet_text_rect_1.center = BULLET_TEXT_POS_1
        self.display_surface.blit(bullet_text_1, bullet_text_rect_1)

        medic_kit_text_1 = self.font.render(f'[{medic_kit_1}]', True, WHITE, BLACK)
        medic_kit_text_rect_1 = medic_kit_text_1.get_rect()
        medic_kit_text_rect_1.center = MEDIC_KIT_TEXT_POS_1
        self.display_surface.blit(medic_kit_text_1, medic_kit_text_rect_1)

        key_text_1 = self.font.render(f'[{key_1}]', True, WHITE, BLACK)
        key_text_rect_1 = key_text_1.get_rect()
        key_text_rect_1.center = KEY_TEXT_POS_1
        self.display_surface.blit(key_text_1, key_text_rect_1)

        # Player 2
        health_text_2 = self.font.render(f'[{health_2}]', True, WHITE, BLACK)
        health_text_rect_2 = health_text_2.get_rect()
        health_text_rect_2.center = HEALTH_TEXT_POS_2
        self.display_surface.blit(health_text_2, health_text_rect_2)

        bullet_text_2 = self.font.render(f'[{bullet_2}]', True, WHITE, BLACK)
        bullet_text_rect_2 = bullet_text_2.get_rect()
        bullet_text_rect_2.center = BULLET_TEXT_POS_2
        self.display_surface.blit(bullet_text_2, bullet_text_rect_2)

        medic_kit_text_2 = self.font.render(f'[{medic_kit_2}]', True, WHITE, BLACK)
        medic_kit_text_rect_2 = medic_kit_text_2.get_rect()
        medic_kit_text_rect_2.center = MEDIC_KIT_TEXT_POS_2
        self.display_surface.blit(medic_kit_text_2, medic_kit_text_rect_2)

        key_text_2 = self.font.render(f'[{key_2}]', True, WHITE, BLACK)
        key_text_rect_2 = key_text_2.get_rect()
        key_text_rect_2.center = KEY_TEXT_POS_2
        self.display_surface.blit(key_text_2, key_text_rect_2)

    # def display(self, player):
    # screen.blit(self.health_rect, (HEALTH_WIDTH, HEALTH_HEIGHT))
    # self.show_health(player.health, player.stats['health'], self.health_rect)
    # self.show_bar(player.health,player.stats['health'],self.health_bar_rect,(213, 123, 95))
    # self.show_bar(player.bullet,player.stats['bullet'],self.energy_bar_rect,(123, 4, 57))