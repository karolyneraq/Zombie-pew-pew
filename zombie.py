from math import sin

import pygame
from config import *


class Zombie(pygame.sprite.Sprite):
    def __init__(self, path, spawn, up, right, left, down, walking):
        super().__init__()
        self.sprites_down_w = []
        self.sprites_up_w = []
        self.sprites_right_w = []
        self.sprites_left_w = []
        self.sprites_down_w.append(
            pygame.transform.scale(pygame.image.load(path + "front/zombie_frontWalk1.png"), (60, 60)))
        self.sprites_down_w.append(
            pygame.transform.scale(pygame.image.load(path + "front/zombie_frontWalk2.png"), (60, 60)))
        self.sprites_down_w.append(
            pygame.transform.scale(pygame.image.load(path + "front/zombie_frontWalk3.png"), (60, 60)))
        self.sprites_down_w.append(
            pygame.transform.scale(pygame.image.load(path + "front/zombie_frontWalk4.png"), (60, 60)))
        self.sprites_down_w.append(
            pygame.transform.scale(pygame.image.load(path + "front/zombie_frontWalk5.png"), (60, 60)))
        self.sprites_up_w.append(
            pygame.transform.scale(pygame.image.load(path + "back/zombie_backWalk1.png"), (60, 60)))
        self.sprites_up_w.append(
            pygame.transform.scale(pygame.image.load(path + "back/zombie_backWalk2.png"), (60, 60)))
        self.sprites_up_w.append(
            pygame.transform.scale(pygame.image.load(path + "back/zombie_backWalk3.png"), (60, 60)))
        self.sprites_up_w.append(
            pygame.transform.scale(pygame.image.load(path + "back/zombie_backWalk4.png"), (60, 60)))
        self.sprites_up_w.append(
            pygame.transform.scale(pygame.image.load(path + "back/zombie_backWalk5.png"), (60, 60)))
        self.sprites_right_w.append(
            pygame.transform.scale(pygame.image.load(path + "right/zombie_walkright1.png"), (60, 60)))
        self.sprites_right_w.append(
            pygame.transform.scale(pygame.image.load(path + "right/zombie_walkright2.png"), (60, 60)))
        self.sprites_right_w.append(
            pygame.transform.scale(pygame.image.load(path + "right/zombie_walkright3.png"), (60, 60)))
        self.sprites_right_w.append(
            pygame.transform.scale(pygame.image.load(path + "right/zombie_walkright4.png"), (60, 60)))
        self.sprites_right_w.append(
            pygame.transform.scale(pygame.image.load(path + "right/zombie_walkright5.png"), (60, 60)))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[0], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[1], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[2], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[3], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[4], True, False))

        self.current_sprite = 0
        self.sprite_state = 3
        self.image = self.sprites_right_w[self.current_sprite]
        self.spawn_x = spawn[0]
        self.spawn_y = spawn[1]
        self.rect = self.image.get_rect(topleft=spawn)
        self.up = up
        self.right = right
        self.left = left
        self.down = down
        self.speed_x = 1
        self.speed_y = 1
        self.fire = False
        self.reloading = False
        self.reload_time = 0
        self.vulnerable = True
        self.vulnerable_time = 0
        self.vulnerable_cooldown = 700
        self.projectiles = []
        self.health = 2
        self.obstacles = None
        self.walking = walking

    def get_image(self):
        return self.image

    def get_spawn_x(self):
        return self.spawn_x

    def get_spawn_y(self):
        return self.spawn_y

    def get_up(self):
        return self.up

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_down(self):
        return self.down

    def get_fire(self):
        return self.fire

    def get_reloading(self):
        return self.reloading

    def get_reload_time(self):
        return self.reload_time

    def get_projectiles(self):
        return self.projectiles

    def get_health(self):
        return self.health

    def get_rect(self):
        return self.rect

    def set_image(self, asset):
        self.image = asset

    def set_spawn_x(self, spawn_x):
        self.spawn_x = spawn_x

    def set_spawn_y(self, spawn_y):
        self.spawn_y = spawn_y

    def set_up(self, up):
        self.up = up

    def set_right(self, right):
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_down(self, down):
        self.down = down

    def reset_speed(self):
        self.speed_x = zombie_speed_x
        self.speed_y = zombie_speed_y

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
        self.health = lives

    def set_rect(self, rect):
        self.rect = rect

    def set_rect_topleft(self, x, y):
        self.rect.topleft = (x, y)

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles

    def damaged(self):
        self.vulnerable = False
        self.vulnerable_time = pygame.time.get_ticks()
        self.health -= 1

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0

    def update(self):
        if self.walking:
            self.move()
        self.current_sprite += 0.1
        self.check_death()
        if not self.vulnerable and pygame.time.get_ticks() - self.vulnerable_time >= self.vulnerable_cooldown:
            self.vulnerable = True
        if self.current_sprite >= 4:
            self.current_sprite = 0
        if self.sprite_state == 1:
            self.image = self.sprites_up_w[int(self.current_sprite)]
        elif self.sprite_state == 2:
            self.image = self.sprites_right_w[int(self.current_sprite)]
        elif self.sprite_state == 3:
            self.image = self.sprites_left_w[int(self.current_sprite)]
        elif self.sprite_state == 4:
            self.image = self.sprites_down_w[int(self.current_sprite)]

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def collision(self):
        collision_tolerance = 10
        for sprite in self.obstacles:
            if sprite.rect.colliderect(self.rect):
                if abs(self.rect.top - sprite.rect.bottom) < collision_tolerance and self.speed_y < 0:  #
                    self.sprite_state = 4
                    self.speed_y *= -1
                if abs(self.rect.bottom - sprite.rect.top) < collision_tolerance and self.speed_y > 0:  #
                    self.sprite_state = 1
                    self.speed_y *= -1
                if abs(self.rect.right - sprite.rect.left) < collision_tolerance and self.speed_x > 0:  #
                    self.sprite_state = 3
                    self.speed_x *= -1
                if abs(self.rect.left - sprite.rect.right) < collision_tolerance and self.speed_x < 0:  #
                    self.sprite_state = 2
                    self.speed_x *= -1
        if self.rect.x >= 850 and self.speed_x > 0:
            self.sprite_state = 3
            self.speed_x *= -1
        elif self.rect.x <= 0 and self.speed_x < 0:
            self.sprite_state = 2
            self.speed_x *= -1
        if self.rect.y >= 600 and self.speed_y > 0:
            self.sprite_state = 1
            self.speed_y *= -1
        elif self.rect.y <= 0 and self.speed_y < 0:
            self.sprite_state = 4
            self.speed_y *= -1

    def move(self):
        self.rect.x = self.rect.x + self.speed_x
        self.collision()
        self.rect.y = self.rect.y + self.speed_y
        self.collision()

    def check_death(self):
        if self.health <= 0:
            self.kill()
