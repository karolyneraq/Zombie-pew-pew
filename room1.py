import pygame
from pygame.locals import *
from config import *
from element import Element
from chest import Chest


class Room1:
    def __init__(self):
        self.scenario = pygame.sprite.Group()
        self.collide_sprites = pygame.sprite.Group()
        self.interactions_sprites = pygame.sprite.Group()

        self.surface = pygame.display.get_surface()

        # Walls
        self.wall_top = pygame.image.load("assets/wall/wall_top.png")
        self.door_top2 = pygame.image.load("assets/door/door_top2.png")
        self.wall_corner_real = pygame.image.load("assets/wall/wall_cornerreal.png")

        # Stretchers
        self.stretcher_horizontal1 = pygame.image.load("assets/stretcher/stretcher_horizontal1.png")

        self.add_elements()

    def draw_scenario(self):
        self.scenario.draw(self.surface)

    def get_group(self):
        return self.collide_sprites

    def get_interactions_sprites(self):
        return self.interactions_sprites

    def add_elements(self):
        # Walls
        # Upper Walls
        wall_top_inverted = pygame.transform.rotate(self.wall_top, 180)

        for x in range(175, 851, 75):
            Element((x, 0), [self.scenario, self.collide_sprites], wall_top_inverted)

        for x in range(250, 850, 75):
            Element((x, 75), [self.scenario, self.collide_sprites], self.wall_top)

        # Corners
        Element((175, 75), [self.scenario, self.collide_sprites], self.wall_corner_real)

        wall_corner_real_rotated_rt = pygame.transform.rotate(self.wall_corner_real, 270)
        Element((850, 75), [self.scenario, self.collide_sprites], wall_corner_real_rotated_rt)

        wall_corner_real_rotated = pygame.transform.rotate(self.wall_corner_real, 90)
        Element((175, 450), [self.scenario, self.collide_sprites], wall_corner_real_rotated)

        wall_corner_real_rotated_lf = pygame.transform.rotate(self.wall_corner_real, 360)
        Element((850, 450), [self.scenario, self.collide_sprites], wall_corner_real_rotated_lf)

        # Lower Walls
        for x in range(250, 850, 75):
            Element((x, 450), [self.scenario, self.collide_sprites], wall_top_inverted)

        for x in range(175, 851, 75):
            Element((x, 525), [self.scenario, self.collide_sprites], self.wall_top)

        # Left Walls
        wall_top_rotated_left = pygame.transform.rotate(self.wall_top, 90)
        for y in range(150, 376, 75):
            Element((175, y), [self.scenario, self.collide_sprites], wall_top_rotated_left)

        # Right Walls
        wall_top_rotated_right = pygame.transform.rotate(self.wall_top, 270)
        for y in range(150, 376, 75):
            Element((850, y), [self.scenario, self.collide_sprites], wall_top_rotated_right)

        # Door
        door_top2_rotated = pygame.transform.rotate(self.door_top2, 270)
        Element((850, 300), [self.scenario, self.collide_sprites, self.interactions_sprites], door_top2_rotated)

        # Stretchers
        Element((250, 225), [self.scenario, self.collide_sprites], self.stretcher_horizontal1)
        Element((250, 300), [self.scenario, self.collide_sprites], self.stretcher_horizontal1)
