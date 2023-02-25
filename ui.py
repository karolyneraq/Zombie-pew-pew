import pygame
from config import *


class UI:
    def __init__(self):

        # General
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # Inventory
        self.health_rect = pygame.image.load('assets/UI/heart_full.png').get_rect()

        self.bullet_rect = pygame.image.load('assets/UI/gun.png').get_rect()
        
        self.medic_kit_rect = pygame.image.load('assets/UI/medics_kit.png').get_rect()
        
        self.key_rect = pygame.image.load('assets/UI/key.png').get_rect()



    def draw_inventary(self, current, max_amount, bg_rect):
        # pygame.draw.rect(self.display_surface, '#285457', bg_rect)
        screen.blit(self.health_rect, (HEALTH_WIDTH, HEALTH_HEIGHT))

    # def show_bar(self,current,max_amount,bg_rect,color):
		# draw bg 
        #pygame.draw.rect(self.display_surface, '#285457', bg_rect)

    def display(self, player):
        screen.blit(self.health_rect, (HEALTH_WIDTH, HEALTH_HEIGHT))
        #self.show_health(player.health, player.stats['health'], self.health_rect)
        #self.show_bar(player.health,player.stats['health'],self.health_bar_rect,(213, 123, 95))
        #self.show_bar(player.bullet,player.stats['bullet'],self.energy_bar_rect,(123, 4, 57))