import pygame
from projectile import Projectile
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, path, spawn_x_pos, spawn_y_pos):
        super().__init__()
        self.sprites_down_s = []
        self.sprites_down_w = []
        self.sprites_up_s = []
        self.sprites_up_w = []
        self.sprites_right_s = []
        self.sprites_right_w = []
        self.sprites_left_s = []
        self.sprites_left_w = []
        self.sprites_down_s.append(pygame.image.load(path + "FRONT_STATIC/front_static1.png"))
        self.sprites_down_s.append(pygame.image.load(path + "FRONT_STATIC/front_static2.png"))
        self.sprites_down_s.append(pygame.image.load(path + "FRONT_STATIC/front_static3.png"))
        self.sprites_down_s.append(pygame.image.load(path + "FRONT_STATIC/front_static4.png"))
        self.sprites_down_s.append(pygame.image.load(path + "FRONT_STATIC/front_static5.png"))
        self.sprites_down_w.append(pygame.image.load(path + "FRONT_WALKING/front_walking1.png"))
        self.sprites_down_w.append(pygame.image.load(path + "FRONT_WALKING/front_walking2.png"))
        self.sprites_down_w.append(pygame.image.load(path + "FRONT_WALKING/front_walking3.png"))
        self.sprites_down_w.append(pygame.image.load(path + "FRONT_WALKING/front_walking4.png"))
        self.sprites_up_s.append(pygame.image.load(path + "BACK_STATIC/back_static1.png"))
        self.sprites_up_s.append(pygame.image.load(path + "BACK_STATIC/back_static2.png"))
        self.sprites_up_s.append(pygame.image.load(path + "BACK_STATIC/back_static3.png"))
        self.sprites_up_s.append(pygame.image.load(path + "BACK_STATIC/back_static4.png"))
        self.sprites_up_s.append(pygame.image.load(path + "BACK_STATIC/back_static5.png"))
        self.sprites_up_w.append(pygame.image.load(path + "BACK_WALKING/back_walking1.png"))
        self.sprites_up_w.append(pygame.image.load(path + "BACK_WALKING/back_walking2.png"))
        self.sprites_up_w.append(pygame.image.load(path + "BACK_WALKING/back_walking3.png"))
        self.sprites_up_w.append(pygame.image.load(path + "BACK_WALKING/back_walking4.png"))
        self.sprites_right_s.append(pygame.image.load(path + "SIDE_STATIC/side_static1.png"))
        self.sprites_right_s.append(pygame.image.load(path + "SIDE_STATIC/side_static2.png"))
        self.sprites_right_s.append(pygame.image.load(path + "SIDE_STATIC/side_static3.png"))
        self.sprites_right_s.append(pygame.image.load(path + "SIDE_STATIC/side_static4.png"))
        self.sprites_right_s.append(pygame.image.load(path + "SIDE_STATIC/side_static5.png"))
        self.sprites_right_w.append(pygame.image.load(path + "SIDE_WALKING/side_walking1.png"))
        self.sprites_right_w.append(pygame.image.load(path + "SIDE_WALKING/side_walking2.png"))
        self.sprites_right_w.append(pygame.image.load(path + "SIDE_WALKING/side_walking3.png"))
        self.sprites_right_w.append(pygame.image.load(path + "SIDE_WALKING/side_walking4.png"))
        self.sprites_left_s.append(pygame.transform.flip(self.sprites_right_s[0], True, False))
        self.sprites_left_s.append(pygame.transform.flip(self.sprites_right_s[1], True, False))
        self.sprites_left_s.append(pygame.transform.flip(self.sprites_right_s[2], True, False))
        self.sprites_left_s.append(pygame.transform.flip(self.sprites_right_s[3], True, False))
        self.sprites_left_s.append(pygame.transform.flip(self.sprites_right_s[4], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[0], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[1], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[2], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[3], True, False))
        self.current_sprite = 0
        self.sprite_state = 2
        self.image = self.sprites_right_s[self.current_sprite]
        self.spawn_x = spawn_x_pos
        self.spawn_y = spawn_y_pos
        self.current_x = spawn_x_pos
        self.current_y = spawn_y_pos
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.current_x, self.current_y)
        self.up = False
        self.right = False
        self.left = False
        self.down = False
        self.speed = pygame.math.Vector2((player_speed_x, player_speed_y))
        self.fire = False
        self.reloading = False
        self.reload_cooldown = 500
        self.reload_time = 0
        self.bullets = pygame.sprite.Group()
        self.lives = 3

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

    def get_bullets(self):
        return self.bullets

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

    def set_reloading(self, reloading):
        self.reloading = reloading

    def set_reload_time(self, reload_time):
        self.reload_time = reload_time

    def add_bullet(self, projectile):
        self.bullets.add(projectile)

    def remove_bullet(self, projectile):
        self.bullets.remove(projectile)

    def set_lives(self, lives):
        self.lives = lives

    def set_rect(self, rect):
        self.rect = rect

    def set_rect_topleft(self, x, y):
        self.rect.topleft = (x, y)

    def update(self):
        self.current_sprite += 0.1
        if self.up or self.down or self.right or self.left:
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

        else:
            if self.current_sprite >= 5:
                self.current_sprite = 0
            if self.sprite_state == 1:
                self.image = self.sprites_up_s[int(self.current_sprite)]
            elif self.sprite_state == 2:
                self.image = self.sprites_right_s[int(self.current_sprite)]
            elif self.sprite_state == 3:
                self.image = self.sprites_left_s[int(self.current_sprite)]
            elif self.sprite_state == 4:
                self.image = self.sprites_down_s[int(self.current_sprite)]

    def set_movement(self, joy):
        if joy.get_hat(0) == (0, 1):
            self.set_up(True)
            self.set_down(False)
            self.set_right(False)
            self.set_left(False)
            self.sprite_state = 1
        elif joy.get_hat(0) == (1, 1):
            self.set_up(True)
            self.set_right(True)
            self.set_down(False)
            self.set_left(False)
            self.sprite_state = 2
        elif joy.get_hat(0) == (-1, 1):
            self.set_up(True)
            self.set_left(True)
            self.set_down(False)
            self.set_right(False)
            self.sprite_state = 3
        elif joy.get_hat(0) == (0, -1):
            self.set_down(True)
            self.set_up(False)
            self.set_right(False)
            self.set_left(False)
            self.sprite_state = 4
        elif joy.get_hat(0) == (1, -1):
            self.set_down(True)
            self.set_right(True)
            self.set_up(False)
            self.set_left(False)
            self.sprite_state = 2
        elif joy.get_hat(0) == (-1, -1):
            self.set_down(True)
            self.set_left(True)
            self.set_right(False)
            self.set_up(False)
            self.sprite_state = 3
        elif joy.get_hat(0) == (1, 0):
            self.set_right(True)
            self.set_up(False)
            self.set_down(False)
            self.set_left(False)
            self.sprite_state = 2
        elif joy.get_hat(0) == (-1, 0):
            self.set_left(True)
            self.set_up(False)
            self.set_down(False)
            self.set_right(False)
            self.sprite_state = 3
        elif joy.get_hat(0) == (0, 0):
            self.set_up(False)
            self.set_down(False)
            self.set_right(False)
            self.set_left(False)

    def move(self):
        if self.up:
            if self.speed[1] > 0:
                self.speed[1] *= -1
            self.current_y = self.current_y + self.speed[1]

        if self.down:
            if self.speed[1] < 0:
                self.speed[1] *= -1
            self.current_y = self.current_y + self.speed[1]

        if self.right:
            if self.speed[0] < 0:
                self.speed[0] *= -1
            self.current_x = self.current_x + self.speed[0]

        if self.left:
            if self.speed[0] > 0:
                self.speed[0] *= -1
            self.current_x = self.current_x + self.speed[0]

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.current_x, self.current_y)

    def shoot(self, direction):
        if self.sprite_state == 2:
            if direction == (0, 0):
                direction = (1, 0)
            bullet = Projectile("assets/bullet.png", direction, self.rect.midright[0], self.rect.midright[1])
            self.bullets.add(bullet)
        elif self.sprite_state == 1:
            if direction == (0, 0):
                direction = (0, 1)
            bullet = Projectile("assets/bullet.png", direction, self.rect.midtop[0], self.rect.midtop[1])
            self.bullets.add(bullet)
        elif self.sprite_state == 3:
            if direction == (0, 0):
                direction = (-1, 0)
            bullet = Projectile("assets/bullet.png", direction, self.rect.midleft[0], self.rect.midleft[1])
            self.bullets.add(bullet)
        elif self.sprite_state == 4:
            if direction == (0, 0):
                direction = (0, -1)
            bullet = Projectile("assets/bullet.png", direction, self.rect.midbottom[0], self.rect.midbottom[1])
            self.bullets.add(bullet)

    def set_fire(self, joy):
        if joy.get_button(1) == 1 and not self.reloading:
            self.shoot(joy.get_hat(0))
            self.reloading = True
            self.reload_time = pygame.time.get_ticks()
        elif self.reloading:
            if pygame.time.get_ticks() - self.reload_time >= self.reload_cooldown:
                self.reloading = False