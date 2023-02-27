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

        self.player_1_icon = pygame.image.load('assets/UI/red_icon.png')
        self.health_1 = pygame.image.load('assets/UI/heart_full.png')
        self.bullet_1 = pygame.image.load('assets/UI/gun.png')
        self.medic_kit_1 = pygame.image.load('assets/UI/medics_kit.png')
        self.key_1 = pygame.image.load('assets/UI/key.png')

        self.player_2_icon = pygame.image.load('assets/UI/blue_icon.png')
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

        # Player 1
        Element((ICON_WIDTH, ICON_HEIGHT), [self.inventory], pygame.transform.scale(self.player_1_icon, (75, 75)))
        Element((HEALTH_WIDTH, HEALTH_HEIGHT), [self.inventory], self.health_1)
        Element((KEY_WIDTH, KEY_HEIGHT), [self.inventory], self.key_1)

        # Player 2
        Element((ICON_WIDTH + 925, ICON_HEIGHT), [self.inventory], pygame.transform.scale(self.player_2_icon, (75, 75)))
        Element((HEALTH_WIDTH + 925, HEALTH_HEIGHT ), [self.inventory], self.health_2)
        Element((KEY_WIDTH + 925, KEY_HEIGHT), [self.inventory], self.key_2)

    def set_health_player1(self, health):
        self.health_1 = health

    def set_health_player2(self, health):
        self.health_2 = health
    
    def set_key_player1(self, key):
        self.key_1 = health
    
    def set_key_player2(self, key):
        self.key_2 = health

    def get_health_player1(self, health):
        return self.health_1

    def get_health_player2(self, health):
        return self.health_2
    
    def get_key_player1(self, key):
        return self.key_1
    
    def get_key_player2(self, key):
        return self.key_2

    def inventory_data(self):
        # Player 1
        self.health_1 = 3
        self.key_1 = 2

        # Player 2
        self.health_2 = 3
        self.key_2 = 2

        # Player 1
        health_text_1 = self.font.render(f'[{self.health_1}]', True, WHITE, GREY)
        health_text_rect_1 = health_text_1.get_rect()
        health_text_rect_1.center = HEALTH_TEXT_POS_1
        self.display_surface.blit(health_text_1, health_text_rect_1)

        key_text_1 = self.font.render(f'[{self.key_1}]', True, WHITE, GREY)
        key_text_rect_1 = key_text_1.get_rect()
        key_text_rect_1.center = KEY_TEXT_POS_1
        self.display_surface.blit(key_text_1, key_text_rect_1)

        # Player 2
        health_text_2 = self.font.render(f'[{self.health_2}]', True, WHITE, GREY)
        health_text_rect_2 = health_text_2.get_rect()
        health_text_rect_2.center = HEALTH_TEXT_POS_2
        self.display_surface.blit(health_text_2, health_text_rect_2)

        key_text_2 = self.font.render(f'[{self.key_2}]', True, WHITE, GREY)
        key_text_rect_2 = key_text_2.get_rect()
        key_text_rect_2.center = KEY_TEXT_POS_2
        self.display_surface.blit(key_text_2, key_text_rect_2)
