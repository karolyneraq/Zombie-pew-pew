import pygame
from pygame.locals import *
from config import *
from element import Element
from chest import Chest


class Room1:
    def __init__(self):
        self.scenario = pygame.sprite.Group()
        self.collide_sprites = pygame.sprite.Group()

        self.surface = pygame.display.get_surface()

        # Floor
        self.floor = pygame.image.load("assets/decour/floor/floor_asset.png")
        self.floor_broken = pygame.image.load("assets/decour/floor/floor_broken.png")

        # Walls
        self.wall_window_1 = pygame.image.load("assets/decour/wall/wall_window.png")
        self.wall_window_2 = pygame.image.load("assets/decour/wall/wall_window2.png")
        self.wall_painting_1 = pygame.image.load("assets/decour/wall/wall_painting1.png")
        self.wall_painting_2 = pygame.image.load("assets/decour/wall/wall_painting2.png")
        self.wall_painting_3 = pygame.image.load("assets/decour/wall/wall_painting3.png")
        self.wall_top = pygame.image.load("assets/wall/wall_top.png")
        self.door_top2 = pygame.image.load("assets/door/door_top2.png")
        self.wall_corner_real = pygame.image.load("assets/wall/wall_cornerreal.png")

        # Stretchers
        self.stretcher_horizontal1 = pygame.image.load("assets/stretcher/stretcher_horizontal1.png")
        self.stretcher_vertical1 = pygame.image.load("assets/stretcher/stretcher_vertical1.png")
        self.stretcher_vertical2 = pygame.image.load("assets/stretcher/stretcher_vertical2.png")

        # Chests
        self.chest_player1 = Chest(450, 150, False)
        self.chest_player2 = Chest(450, 375, False)

        self.add_elements()

    def draw_scenario(self):
        self.scenario.draw(self.surface)

        # Chest
        self.chest_player1.animate()
        self.chest_player2.animate()
        self.chest_player1.update()
        self.chest_player2.update()

    def get_group(self):
        return self.collide_sprites

    def add_elements(self):
        # Floor
        for x in range(175, 851, 75):
            for y in range(75, 451, 75):
                Element((x, y), [self.scenario], self.floor)

        Element((775, 300), [self.scenario], self.floor_broken)

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

        # Decour
        wall_window1 = pygame.transform.rotate(self.wall_window_1, 90)
        wall_window1_flip = pygame.transform.flip(wall_window1, False, True)
        
        Element((175, 225), [self.scenario], wall_window1)
        Element((175, 300), [self.scenario], wall_window1_flip)

        wall_window2 = pygame.transform.rotate(self.wall_window_2, 180)
        
        Element((325, 0), [self.scenario], wall_window2)
        Element((700, 0), [self.scenario], wall_window2)

        wall_painting2 = pygame.transform.flip(self.wall_painting_2, True, False)

        Element((550, 0), [self.scenario], self.wall_painting_3)
        Element((475, 0), [self.scenario], wall_painting2)

        # Door
        door_top2_rotated = pygame.transform.rotate(self.door_top2, 270)
        Element((850, 300), [self.scenario, self.collide_sprites], door_top2_rotated)

        # Stretchers
        Element((250, 225), [self.scenario, self.collide_sprites], self.stretcher_horizontal1)
        Element((250, 300), [self.scenario, self.collide_sprites], self.stretcher_horizontal1)
        Element((625, 150), [self.scenario, self.collide_sprites], self.stretcher_vertical1)
        Element((625, 375), [self.scenario, self.collide_sprites], self.stretcher_vertical2)

        # Chest
        self.scenario.add(self.chest_player1)
        self.scenario.add(self.chest_player2)
        self.collide_sprites.add(self.chest_player1)
        self.collide_sprites.add(self.chest_player2)