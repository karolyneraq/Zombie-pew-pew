import pygame
from pygame.locals import *
from config import *
from poison import Poison
from element import Element


class Hall1:
    def __init__(self):
        self.scenario = pygame.sprite.Group()
        self.collide_sprites = pygame.sprite.Group()
        self.stage_hazard = pygame.sprite.Group()

        self.surface = pygame.display.get_surface()

        # Walls
        self.wall_top = pygame.image.load("assets/wall/wall_top.png")
        self.wall_corner_top1 = pygame.image.load("assets/wall/tall_corner1.png")
        self.wall_corner_top2 = pygame.image.load("assets/wall/tall_corner2.png")
        self.wall_door_top1 = pygame.image.load("assets/wall/wall_doortop1.png")
        self.wall_door_top2 = pygame.image.load("assets/wall/wall_doortop2.png")
        self.wall_corner_real = pygame.image.load("assets/wall/wall_cornerreal.png")
        self.wall_window_1 = pygame.image.load("assets/decour/wall/wall_window.png")
        self.wall_window = pygame.image.load("assets/decour/wall/wall_window.png")

        # Pipes
        self.pipe_top_left_end = pygame.image.load("assets/pipe/pipe_safe/pipe_topleftend.png")
        self.pipe_top = pygame.image.load("assets/pipe/pipe_broken/pipe_top.png")
        self.pipe_top_right_end = pygame.image.load("assets/pipe/pipe_safe/pipe_toprightend.png")

        # Stretchers
        self.stretcher_horizontal1 = pygame.image.load("assets/stretcher/stretcher_horizontal1.png")

        # Floor
        self.floor = pygame.image.load("assets/decour/floor/floor_asset.png")
        self.floor_bloody1 = pygame.image.load("assets/decour/floor/floor_bloody.png")
        self.floor_bloody2 = pygame.image.load("assets/decour/floor/floor_bloody2.png")
        self.floor_broken = pygame.image.load("assets/decour/floor/floor_broken.png")

        # Poison
        self.poison = Poison(550, 150, "top")
        self.add_elements()

    def draw_scenario(self):
        self.scenario.draw(self.surface)
        # Poison
        self.poison.animate()
        self.poison.update()

    def get_group(self):
        return self.collide_sprites

    def get_stage_hazard(self):
        return self.stage_hazard

    def add_elements(self):
        # Walls
        # Upper Walls
        wall_top_inverted = pygame.transform.rotate(self.wall_top, 180)

        # Window
        wall_window_1_rotated = pygame.transform.flip(self.wall_window_1, True, False)

        for x in range(250, 851, 75):
            if x == 775:
                Element((775, 0), [self.scenario], self.wall_window_1)
            elif x == 700:
                Element((700, 0), [self.scenario], wall_window_1_rotated)
            else:
                Element((x, 0), [self.scenario, self.collide_sprites], wall_top_inverted)

        for x in range(250, 851, 75):
            if x <= 400 or x >= 700:
                Element((x, 75), [self.scenario, self.collide_sprites], self.wall_top)

        Element((175, 0), [self.scenario, self.collide_sprites], self.wall_corner_top2)
        Element((175, 75), [self.scenario, self.collide_sprites], self.wall_corner_top1)

        # Left Walls
        wall_top_rotated = pygame.transform.rotate(self.wall_top, 90)
        Element((175, 150), [self.scenario, self.collide_sprites], wall_top_rotated)

        wall_door_top1_rotated = pygame.transform.rotate(self.wall_door_top1, 90)
        wall_door_top2_rotated = pygame.transform.rotate(self.wall_door_top2, 90)

        # Door
        Element((175, 300), [self.scenario, self.collide_sprites], wall_door_top1_rotated)
        Element((175, 225), [self.scenario, self.collide_sprites], wall_door_top2_rotated)

        # Lower Walls
        Element((175, 375), [self.scenario, self.collide_sprites], wall_top_rotated)

        wall_corner_real_rotated = pygame.transform.rotate(self.wall_corner_real, 90)
        Element((175, 450), [self.scenario, self.collide_sprites], wall_corner_real_rotated)

        for x in range(250, 851, 75):
            Element((x, 450), [self.scenario, self.collide_sprites], wall_top_inverted)

        for x in range(175, 851, 75):
            Element((x, 525), [self.scenario, self.collide_sprites], self.wall_top)

        # Pipe
        Element((475, 75), [self.scenario, self.collide_sprites], self.pipe_top_left_end)

        Element((550, 75), [self.scenario, self.collide_sprites], self.pipe_top)

        Element((625, 75), [self.scenario, self.collide_sprites], self.pipe_top_right_end)

        # Floor
        for x in range(250, 851, 75):
            for y in range(150, 376, 75):
                if x == 550 and y == 375:
                    Element((x, y), [self.scenario], self.floor_bloody2)
                elif x == 325 and y == 150:
                    Element((x, y), [self.scenario], self.floor_broken)
                else:
                    Element((x, y), [self.scenario], self.floor)

        # Stretchers
        Element((550, 375), [self.scenario, self.collide_sprites], self.stretcher_horizontal1)

        # Poison
        self.scenario.add(self.poison)
        self.stage_hazard.add(self.poison)

