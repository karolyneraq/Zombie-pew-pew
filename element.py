import pygame.sprite
import pygame


class Element(pygame.sprite.Sprite):
    def __init__(self, pos, group, image):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
