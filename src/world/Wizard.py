import pygame
from .Character import Character
from src.Dependencies import gWizardBattle_image_list
from src.world.DamageText import DamageText
from pygame.sprite import Group
import random
import math


class Wizard(Character):
    def __init__(self, x, y):
        super().__init__(gWizardBattle_image_list, max_hp = 90, strength = 15)
        self.X = x
        self.Y = y+20
        self.Class = "Wizard"
        self.action_list = ["Q(Attack)", "W(Blast)", "E(Devour)"]
        self.evade = False
        self.rect.center = (self.X, self.Y)
        self.action_count = 3
        self.skill_cooldown_1 = 0
        self.skill_cooldown_2 = 0
        self.acquired_joker = False
        self.is_use_skill2 = False

    def update(self):
        super().update()


    def idle(self):
        super().idle()
        self.rect.center = (self.X, self.Y)

    def attack(self, target):
        self.rect.center = (self.X, self.Y - 120)
        # deal damage to enemy
        damage = int(math.ceil(self.strength * 0.9) + ((self.max_hp - self.hp)*self.strength/100)*0.25)
        for enemy in target:
            # run enemy hurt animation
            enemy.hurt(damage)
            #set variables to attack animation
            if enemy.hp < 1:
                enemy.hp = 0
                enemy.alive = False
                enemy.death()
            self.damage_text = DamageText(enemy.rect.centerx, enemy.rect.y, str(damage), (255, 0, 0))
            self.damage_text_group.add(self.damage_text)
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    
    def skill_1(self, target):
        self.rect.center = (self.X, self.Y - 120)
        # deal damage to enemy
        damage = int(math.ceil(self.strength * 1.7))
        for enemy in target:
            # run enemy hurt animation
            enemy.hurt(damage)
            #set variables to attack animation
            if enemy.hp < 1 and enemy.alive is True:
                enemy.hp = 0
                enemy.alive = False
                enemy.death()
            self.damage_text = DamageText(enemy.rect.centerx, enemy.rect.y, str(damage), (255, 0, 0))
            self.damage_text_group.add(self.damage_text)
        self.skill_cooldown_1 = 3    
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def skill_2(self): 
        self.rect.center = (self.X, self.Y - 120)
        if self.skill_cooldown_2 == 0:
            self.is_use_skill2 = True
            self.original_str = self.strength
            self.strength = int(math.ceil(self.strength * 1.5))
            hp_down = int(math.ceil(0.1*self.max_hp))
            if self.hp < hp_down:
                self.hp = 1
            else:
                self.hp -= hp_down
            self.evade = True
            self.double_damage = True
            self.skill_cooldown_2 = 4
            self.action = 1
            self.frame_index = 6
            self.update_time = pygame.time.get_ticks()
            

    def hurt(self, damage):
        self.rect.center = (self.X, self.Y - 120)
        super().hurt(damage)
        damage_text = DamageText(self.rect.centerx, self.rect.y, str(damage), (255, 255,255))
        self.damage_text_group.add(damage_text)
    
    def death(self):
        super().death()

    def reset(self):
        super().reset()
        self.action_count = 3
    
    def draw(self):
        super().draw()
    