import pygame
from pygame import JOYHATMOTION

from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, path, spawn_x_pos, spawn_y_pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.spawn_x = spawn_x_pos
        self.spawn_y = spawn_y_pos
        self.current_x = spawn_x_pos
        self.current_y = spawn_y_pos
        self.up = False
        self.right = False
        self.left = False
        self.down = False
        self.speed = pygame.math.Vector2((player_speed_x, player_speed_y))
        self.fire = False
        self.reloading = False
        self.reload_time = 0
        self.projectiles = []
        self.lives = 3
        self.rect.center = (self.current_x, self.current_y)

    def get_image(self):
        return self.image

    def get_spawn_x(self):
        return self.spawn_x

    def get_spawn_y(self):
        return self.spawn_y

    def get_current_x(self):
        return self.current_x

    def get_current_y(self):
        return self.current_y

    def get_up(self):
        return self.up

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_down(self):
        return self.down

    def get_speed(self):
        return self.speed

    def get_fire(self):
        return self.fire

    def get_reloading(self):
        return self.reloading

    def get_reload_time(self):
        return self.reload_time

    def get_projectiles(self):
        return self.projectiles

    def get_lives(self):
        return self.lives

    def get_rect(self):
        return self.rect

    def set_image(self, asset):
        self.image = asset

    def set_spawn_x(self, spawn_x):
        self.spawn_x = spawn_x

    def set_spawn_y(self, spawn_y):
        self.spawn_y = spawn_y

    def set_current_x(self, current_x):
        self.current_x = current_x

    def set_current_y(self, current_y):
        self.current_y = current_y

    def set_up(self, up):
        self.up = up

    def set_right(self, right):
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_down(self, down):
        self.down = down

    def set_speed(self, speed):
        self.speed = speed

    def reset_speed(self):
        self.speed = pygame.math.Vector2((player_speed_x, player_speed_y))

    def set_fire(self, fire):
        self.fire = fire

    def set_reloading(self, reloading):
        self.reloading = reloading

    def set_reload_time(self, reload_time):
        self.reload_time = reload_time

    def add_projectile(self, projectile):
        self.projectiles.append(projectile)

    def remove_projectile(self, projectile):
        self.projectiles.remove(projectile)

    def set_lives(self, lives):
        self.lives = lives

    def set_rect(self, rect):
        self.rect = rect

    def set_rect_center(self, x, y):
        self.rect.center = (x, y)

    def set_movement(self, event):

        if event == (0, 1):
            self.set_up(True)
            self.set_down(False)
            self.set_right(False)
            self.set_left(False)
        elif event == (1, 1):
            self.set_up(True)
            self.set_right(True)
            self.set_down(False)
            self.set_left(False)
        elif event == (-1, 1):
            self.set_up(True)
            self.set_left(True)
            self.set_down(False)
            self.set_right(False)
        elif event == (0, -1):
            self.set_down(True)
            self.set_up(False)
            self.set_right(False)
            self.set_left(False)
        elif event == (1, -1):
            self.set_down(True)
            self.set_right(True)
            self.set_up(False)
            self.set_left(False)
        elif event == (-1, -1):
            self.set_down(True)
            self.set_left(True)
            self.set_right(False)
            self.set_up(False)
        elif event == (1, 0):
            self.set_right(True)
            self.set_up(False)
            self.set_down(False)
            self.set_left(False)
        elif event == (-1, 0):
            self.set_left(True)
            self.set_up(False)
            self.set_down(False)
            self.set_right(False)
        elif event == (0, 0):
            self.set_up(False)
            self.set_down(False)
            self.set_right(False)
            self.set_left(False)

    def move(self):
        if self.get_up():
            self.set_current_y(self.get_current_y() + self.get_speed()[1])

        if self.get_down():
            self.set_current_y(self.get_current_y() - self.get_speed()[1])

        if self.get_right():
            self.set_current_x(self.get_current_x() - self.get_speed()[0])

        if self.get_left():
            self.set_current_x(self.get_current_x() + self.get_speed()[0])

        self.set_rect(self.get_image().get_rect())
        self.set_rect_center(self.get_current_x(), self.get_current_y())
