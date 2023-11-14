import pygame
from .Character import Character
from src.constants import *
from src.Dependencies import *
from src.world.DamageText import DamageText
from pygame.sprite import Group
import random
import math

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Witch(Character):
    def __init__(self, x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 - 20):
        super().__init__(name = gWitchBattle_image_list, max_hp = 1000, strength = 30)
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.enemy_type = "Boss"
        self.is_skill2_use = False
        self.b_name = "Witch"

    def update(self):
        super().update()

    def idle(self):
        if self.hp > 60:
            self.action = 0
        else:
            self.action = 6
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        super().death()

    def hurt(self, damage):
        super().hurt(damage)

    def skill_1(self, target):
        self.rect.center = (self.x, self.y)
        # deal damage to enemy
        damage = int(1.5*self.strength)
        # run enemy hurt animation
        target.hurt(damage)
        #set variables to attack animation
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        self.damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), (255, 0, 0))
        self.damage_text_group.add(self.damage_text)
        self.action = 6
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def skill_2(self, target):
        self.rect.center = (self.x, self.y)
        self.strength += int(0.05*target.hp)
        self.action = 5
        self.hp += 100
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def reset(self):
        self.alive = True
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)


