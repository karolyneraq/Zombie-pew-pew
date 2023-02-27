import pygame
from pygame.locals import *
from config import *
from poison import Poison
from element import Element


class Hall2:
    def __init__(self):
        self.scenario = pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.stage_hazard = pygame.sprite.Group()

        self.decour = pygame.sprite.Group()
        self.surface = pygame.display.get_surface()
        # Floor
        self.floor = pygame.image.load("assets/decour/floor/floor_asset.png")
        self.floor_bloody_1 = pygame.image.load("assets/decour/floor/floor_bloody.png")
        self.floor_bloody_2 = pygame.image.load("assets/decour/floor/floor_bloody2.png")
        self.floor_broken = pygame.image.load("assets/decour/floor/floor_broken.png")
        self.floor_slime_1 = pygame.image.load("assets/decour/floor/floor_slime.png")
        self.floor_slime_2 = pygame.image.load("assets/decour/floor/floor_slime2.png")
        # Walls
        self.wall_painting_1 = pygame.image.load("assets/decour/wall/wall_painting1.png")
        self.wall_window_1 = pygame.image.load("assets/decour/wall/wall_window.png")
        self.wall_top = pygame.image.load("assets/wall/wall_top.png")
        self.wall_top_side = pygame.image.load("assets/wall/wall_top_side.png")
        self.wall_door_top1 = pygame.image.load("assets/wall/wall_doortop1.png")
        self.wall_corner_real = pygame.image.load("assets/wall/wall_cornerreal.png")
        # Door
        self.door_top = pygame.image.load("assets/door/door_top1.png")
        # Pipes
        self.pipe_top_left_end = pygame.image.load("assets/pipe/pipe_safe/pipe_topleftend.png")
        self.pipe_top = pygame.image.load("assets/pipe/pipe_broken/pipe_top.png")
        self.pipe_top_right_end = pygame.image.load("assets/pipe/pipe_safe/pipe_toprightend.png")
        # Stretchers
        self.stretcher_horizontal2 = pygame.image.load("assets/stretcher/stretcher_horizontal2.png")
        self.stretcher_vertical1 = pygame.image.load("assets/stretcher/stretcher_vertical1.png")
        self.stretcher_diagonal1 = pygame.image.load("assets/stretcher/stretcher_diagonal1.png")

        # Poison
        self.poison = Poison(400, 75, "top")

        self.add_elements()

    def draw_scenario(self):
        self.scenario.draw(self.surface)
        self.decour.draw(self.surface)
        # Poison
        self.poison.animate()
        self.poison.update()

    def get_group_decour(self):
        return self.decour

    def get_group_scenario(self):
        return self.scenario

    def get_obstacle(self):
        return self.obstacle

    def get_stage_hazard(self):
        return self.stage_hazard

    def add_elements(self):

        # Floor
        for x in range(175, 851, 75):
            for y in range(75, 451, 75):
                Element((x, y), [self.scenario], self.floor)

        Element((625, 75), [self.scenario], pygame.transform.rotate(self.floor_broken, 180))
        Element((250, 150), [self.scenario], pygame.transform.rotate(self.floor_broken, 90))
        Element((850, 450), [self.scenario], self.floor_broken)

        Element((850, 225), [self.scenario], self.floor_slime_1)
        Element((325, 450), [self.scenario], pygame.transform.rotate(self.floor_slime_1, 90))
        Element((400, 75), [self.scenario], self.floor_slime_2)
        Element((175, 375), [self.scenario], pygame.transform.rotate(self.floor_slime_1, 270))

        Element((400, 375), [self.scenario], pygame.transform.rotate(self.floor_bloody_1, 270))
        Element((475, 375), [self.scenario], self.floor_bloody_1)
        Element((550, 75), [self.scenario], self.floor_bloody_2)

        # Walls
        # Upper Walls
        for x in range(250, 851, 75):
            Element((x, 0), [self.scenario, self.obstacle], self.wall_top)

        Element((175, 0), [self.scenario, self.obstacle], self.wall_corner_real)

        # Left Walls
        wall_top_side_rotated = pygame.transform.rotate(self.wall_top_side, 90)
        Element((175, 75), [self.scenario, self.obstacle], self.wall_top_side)
        Element((175, 450), [self.scenario, self.obstacle], wall_top_side_rotated)

        # Transparent Walls
        rect_wall = pygame.Surface((75, 75))
        for y in range(150, 375):
            Element((100, y), [self.obstacle], rect_wall)
        for y in range(75, 451, 75):
            Element((925, y), [self.obstacle], rect_wall)

        # Lower Walls
        wall_corner_real_rotated_lower = pygame.transform.rotate(self.wall_corner_real, 90)
        Element((175, 525), [self.scenario, self.obstacle], wall_corner_real_rotated_lower)

        wall_top_inverted = pygame.transform.rotate(self.wall_top, 180)
        for x in range(250, 851, 75):
            Element((x, 525), [self.scenario, self.obstacle], wall_top_inverted)

        wall_door_top1_rotated = pygame.transform.rotate(self.wall_door_top1, 180)
        wall_door_top1_flip = pygame.transform.flip(wall_door_top1_rotated, True, False)
        Element((325, 525), [self.scenario, self.obstacle], wall_door_top1_flip)
        Element((700, 525), [self.scenario, self.obstacle], wall_door_top1_rotated)

        # Door
        door_top_rotated = pygame.transform.rotate(self.door_top, 180)
        door_top_flip = pygame.transform.flip(door_top_rotated, True, False)
        Element((325, 525), [self.decour], door_top_flip)
        Element((700, 525), [self.decour], door_top_rotated)

        # Window
        wall_window_1_rotated = pygame.transform.flip(self.wall_window_1, True, False)
        Element((700, 0), [self.decour], self.wall_window_1)
        Element((625, 0), [self.decour], wall_window_1_rotated)

        # Painting
        wall_painting_1_rotated = pygame.transform.rotate(self.wall_painting_1, 180)
        Element((512.5, 525), [self.decour], wall_painting_1_rotated)

        # Pipe
        Element((325, 0), [self.decour], self.pipe_top_left_end)
        Element((400, 0), [self.decour], self.pipe_top)
        Element((475, 0), [self.decour], self.pipe_top_right_end)

        # Stretchers
        Element((400, 375), [self.scenario, self.obstacle], self.stretcher_vertical1)
        Element((475, 375), [self.scenario, self.obstacle], self.stretcher_diagonal1)
        Element((550, 75), [self.scenario, self.obstacle], self.stretcher_horizontal2)

        # Poison
        self.scenario.add(self.poison)
        self.stage_hazard.add(self.poison)
