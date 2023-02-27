import pygame
import sys


class Poison(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, direction):
        super().__init__()
        self.poison_smoke = []
        self.is_animating = False

        self.poison_sound = pygame.mixer.Sound("assets/sounds/gas_2.wav")

        self.current_x = pos_x
        self.current_y = pos_y

        self.direction(direction)

        self.current_sprites = 0
        self.image = self.poison_smoke[self.current_sprites]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        self.animation_speed = 0.1
        self.back_or_forth = 'forth'

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.animation_speed > 0:
            if self.current_sprites >= len(self.poison_smoke) - 1:
                self.animation_speed *= -1

            else:
                self.current_sprites += self.animation_speed
                self.image = self.poison_smoke[int(self.current_sprites)]

        else:
            if self.current_sprites <= 0:
                self.animation_speed *= -1
            else:
                self.current_sprites += self.animation_speed
                self.image = self.poison_smoke[int(self.current_sprites)]

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.current_x, self.current_y)

    def direction(self, direction):
        if direction == "left":
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage0/left/poison_stage0.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage0/left/poison_stage1.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage0/left/poison_stage2.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage0/left/poison_stage3.png"))

            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage1/left/start/poison_stage1.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage1/left/start/poison_stage2.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage1/left/start/poison_stage3.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage1/left/start/poison_stage4.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage1/left/start/poison_stage5.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage1/left/start/poison_stage6.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage1/left/static/poison_stage1static1.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage1/left/static/poison_stage1static2.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage1/left/static/poison_stage1static3.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage1/left/static/poison_stage1static4.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage1/left/end/poison_stage1end1.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage1/left/end/poison_stage1end2.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage1/left/end/poison_stage1end3.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage1/left/end/poison_stage1end4.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage1/left/end/poison_stage1end5.png"))

            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage2/left/start/poison_stage2start1.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage2/left/start/poison_stage2start2.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage2/left/start/poison_stage2start3.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage2/left/start/poison_stage2start4.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage2/left/start/poison_stage2start5.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage2/left/start/poison_stage2start6.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage2/left/static/poison_stage2static1.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage2/left/static/poison_stage2static2.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage2/left/static/poison_stage2static3.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage2/left/static/poison_stage2static4.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage2/left/end/poison_stage2end1.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage2/left/end/poison_stage2end2.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage2/left/end/poison_stage2end3.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage2/left/end/poison_stage2end4.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage2/left/end/poison_stage2end5.png"))

            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/start/poison_stage3start1.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/start/poison_stage3start2.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/start/poison_stage3start3.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/start/poison_stage3start4.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/start/poison_stage3start5.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/start/poison_stage3start6.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/static/poison_stage3static1.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/static/poison_stage3static2.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/static/poison_stage3static3.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/static/poison_stage3static4.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/end/poison_stage3end1.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/end/poison_stage3end2.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/end/poison_stage3end3.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/end/poison_stage3end4.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/left/end/poison_stage3end5.png"))

        elif direction == "top":
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage0/top/poison_stage0.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage0/top/poison_stage1.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage0/top/poison_stage2.png"))
            self.poison_smoke.append(pygame.image.load("assets/poison_smoke/poison_stage0/top/poison_stage3.png"))
            self.poison_smoke.append(
                pygame.image.load("assets/poison_smoke/poison_stage1/top/start/poison_stage1start1.png"))
            self.poison_smoke.append(
                pygame.image.load("assets/poison_smoke/poison_stage1/top/start/poison_stage1start2.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/top/start/poison_stage3start1.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/top/start/poison_stage3start2.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/top/start/poison_stage3start3.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/top/start/poison_stage3start4.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/top/start/poison_stage3start5.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/top/start/poison_stage3start6.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/top/static/poison_stage3static1.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/top/static/poison_stage3static2.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/top/static/poison_stage3static3.png"))
            self.poison_smoke.append(pygame.image.load(
                "assets/poison_smoke/poison_stage3/top/static/poison_stage3static4.png"))
