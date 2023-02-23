import pygame
import sys


class Poison(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.poison_smoke = []
        self.is_animating = False
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage0/left/poison_stage0.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage0/left/poison_stage1.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage0/left/poison_stage2.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage0/left/poison_stage3.png"))

        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/start/poison_stage1.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/start/poison_stage2.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/start/poison_stage3.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/start/poison_stage4.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/start/poison_stage5.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/start/poison_stage6.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/static/poison_stage1static1.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/static/poison_stage1static2.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/static/poison_stage1static3.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/static/poison_stage1static4.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/end/poison_stage1end1.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/end/poison_stage1end2.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/end/poison_stage1end3.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/end/poison_stage1end4.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage1/left/end/poison_stage1end5.png"))

        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/start/poison_stage2start1.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/start/poison_stage2start2.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/start/poison_stage2start3.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/start/poison_stage2start4.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/start/poison_stage2start5.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/start/poison_stage2start6.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/static/poison_stage2static1.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/static/poison_stage2static2.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/static/poison_stage2static3.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/static/poison_stage2static4.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/end/poison_stage2end1.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/end/poison_stage2end2.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/end/poison_stage2end3.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/end/poison_stage2end4.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage2/left/end/poison_stage2end5.png"))

        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/start/poison_stage3start1.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/start/poison_stage3start2.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/start/poison_stage3start3.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/start/poison_stage3start4.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/start/poison_stage3start5.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/start/poison_stage3start6.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/static/poison_stage3static1.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/static/poison_stage3static2.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/static/poison_stage3static3.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/static/poison_stage3static4.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/end/poison_stage3end1.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/end/poison_stage3end2.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/end/poison_stage3end3.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/end/poison_stage3end4.png"))
        self.poison_smoke.append(pygame.image.load("poison_smoke/poison_stage3/left/end/poison_stage3end5.png"))

        self.current_sprites = 0
        self.image = self.poison_smoke[self.current_sprites]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating:
            self.current_sprites += speed

            if self.current_sprites >= len(self.poison_smoke):
                self.current_sprites = 0
                self.is_animating = False

            self.image = self.poison_smoke[int(self.current_sprites)]


