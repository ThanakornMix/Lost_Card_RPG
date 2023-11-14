import pygame
from .Character import Character
from src.constants import *
from src.Dependencies import *
from src.world.DamageText import DamageText
from pygame.sprite import Group
import random
import math

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class KingOfClub(Character):
    def __init__(self, x = WIDTH / 2 - 96 + 350, y = HEIGHT - HEIGHT / 3 - 20):
        super().__init__(name = gRangerBattle_image_list, max_hp = 500, strength = 16)
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.enemy_type = "Boss"
        self.is_skill2_use = False

    def update(self):
        super().update()

    def idle(self):
        super().idle()

    def death(self):
        super().death()

    def hurt(self, damage):
        super().hurt(damage)
    
    def skill_1(self, target):
        self.rect.center = (self.x, self.y)
        # deal damage to enemy
        self.strength += 2
        damage = int(math.ceil(self.strength)*1.3)
        # run enemy hurt animation
        target.hurt(damage)
        #set variables to attack animation
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        self.damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), (255, 0, 0))
        self.damage_text_group.add(self.damage_text)
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def skill_2(self, target):
        self.rect.center = (self.x, self.y-40)
        # deal damage to enemy
        damage = int(math.ceil(self.strength)*1.3)
        # run enemy hurt animation
        target.hurt(damage)
        #set variables to attack animation
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        self.damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), (255, 0, 0))
        self.damage_text_group.add(self.damage_text)
        self.hp += 50
        self.strength += 2
        self.evade = True
        self.action = 6
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        

    def reset(self):
        self.alive = True
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, True, False), self.rect)


