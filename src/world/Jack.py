import pygame
from .Character import Character
from src.constants import *
from src.Dependencies import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Jack(Character):
    def __init__(self, hp, strength, x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3):
        super().__init__(name = gNightBorneBattle_image_list, max_hp = hp, strength = strength)
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.enemy_type = "Miniboss"
        self.dam_count = 0

    def update(self):
        super().update()

    def idle(self):
        super().idle()

    def death(self):
        super().death()

    def hurt(self, damage):
        self.dam_count += 1
        if self.dam_count == 2:
            self.strength += 1
            self.dam_count = 0
        super().hurt(damage)

    def reset(self):
        self.alive = True
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)


