import pygame
from .Character import Character
from src.constants import *
from src.Dependencies import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class JackOfClub(Character):
    def __init__(self, x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 + 40):
        super().__init__(name = gKnightBattle_image_list, max_hp = 50, strength = 2)
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.enemy_type = "Mini_Boss"

    def update(self):
        super().update()

    def idle(self):
        super().idle()

    def death(self):
        super().death()

    def hurt(self, damage):
        super().hurt(damage)
        self.hp -= damage

    def reset(self):
        self.alive = True
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, True, False), self.rect)


