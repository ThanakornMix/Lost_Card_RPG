import pygame
from .Character import Character
from src.constants import *
from src.Dependencies import *
from src.world.DamageText import DamageText
from pygame.sprite import Group
import random
import math

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Cthulu(Character):
    def __init__(self, x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 - 20):
        super().__init__(name = gCthuluBattle_image_list, max_hp = 2000, strength = 25)
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.enemy_type = "Boss"
        self.is_skill2_use = False
        self.b_name = "Cthulu"
        self.regen = False
        self.dam_receive = 0

    def update(self):
        super().update()

    def idle(self):
        if self.hp > 0.6*self.max_hp:
            self.action = 0
        else:
            self.action = 6
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        super().death()

    def hurt(self, damage):
        super().hurt(damage)
        self.dam_receive += 1
        if self.dam_receive == 3 and self.strength < 40:
            self.strength += 2
            self.dam_receive = 0
        if self.hp < self.max_hp*0.2 and self.regen == False:
            self.hp += 300
            self.regen = True

    def skill_1(self, target):
        self.rect.center = (self.x, self.y)
        # deal damage to enemy
        damage = int(math.ceil(self.strength)*1.3)
        if self.double_damage == True:
            damage = int(damage*2)
            self.double_damage = False
        # run enemy hurt animation
        target.hurt(damage)
        #set variables to attack animation
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        self.damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), (255, 0, 0))
        self.damage_text_group.add(self.damage_text)
        self.hp += int(0.05*(self.max_hp - self.hp))
        rand = random.randint(2, 3)
        if rand == 2:
            self.block = True
        elif rand == 3:
            self.double_damage = True
        if self.strength >= 40 and self.strength <= 50:
            self.strength += 2
        self.hp += 30
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def skill_2(self, target):
        self.rect.center = (self.x, self.y)
        # deal damage to enemy
        damage = int(math.ceil(self.strength)*1.3)
        if self.double_damage == True:
            damage = int(damage*2)
            self.double_damage = False
        # run enemy hurt animation
        target.hurt(damage)
        #set variables to attack animation
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        self.damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), (255, 0, 0))
        self.damage_text_group.add(self.damage_text)
        self.hp += int(0.05*(self.max_hp - self.hp))
        rand = random.randint(1, 4)
        if rand == 1:
            self.evade = True
        elif rand == 2:
            self.block = True
        elif rand == 3:
            self.double_damage = True
        self.strength += 2
        self.action = 5
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


