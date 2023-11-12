import pygame
from .Character import Character
from src.Dependencies import gWarriorBattle_image_list
from src.world.DamageText import DamageText
from pygame.sprite import Group
import random
import math

class Warrior(Character):
    def __init__(self, x, y):
        super().__init__(gWarriorBattle_image_list, max_hp = 100, strength = 10)
        self.X = x
        self.Y = y+15
        self.Class = "Warrior"
        self.action_list = ["W (Attack)", "Q (Skill 1)", "E (Skill 2)"]
        self.evade = False
        self.rect.center = (self.X, self.Y)
        self.action_count = 3
        self.skill_cooldown_1 = 0
        self.skill_cooldown_2 = 0
        self.acquired_joker = False
        self.turn_pass = 0

    def update(self):
        super().update()


    def idle(self):
        super().idle()
        self.rect.center = (self.X, self.Y)

    def attack(self, target):
        self.rect.center = (self.X, self.Y+120)
        super().attack(target)

    
    def skill_1(self, target):
        self.rect.center = (self.X, self.Y)
        # deal damage to enemy
        damage = math.ceil(self.strength)
        for enemy in target:
            # run enemy hurt animation
            enemy.hurt(damage)
            #set variables to attack animation
            if enemy.hp < 1:
                enemy.hp = 0
                enemy.alive = False
                enemy.death()
            self.damage_text = DamageText(enemy.rect.centerx, enemy.rect.y, str(damage), (255, 255, 255))
            self.damage_text_group.add(self.damage_text)
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        if self.block == False:
            self.block = True
            self.skill_cooldown_1 = 3
        else:
            pass
    
    def skill_2(self, target):
        if self.skill_cooldown_2 == 0:
            self.rect.center = (self.X, self.Y)
            # deal damage to enemy
            self.damage = math.ceil(self.strength * 1.2)
            # run enemy hurt animation
            target.hurt(self.damage)
            #set variables to attack animation
            if target.hp < 1:
                target.hp = 0
                target.alive = False
                target.death()
            self.damage_text = DamageText(target.rect.centerx, target.rect.y, str(self.damage), (255, 255, 255))
            self.damage_text_group.add(self.damage_text)
            self.action = 6
            heal_point = self.hp + 0.1*self.max_hp
            if heal_point > self.max_hp:
                self.hp = self.max_hp
            else:
                self.hp = heal_point
            self.frame_index = 0
            self.skill_cooldown_2 = 4
            self.update_time = pygame.time.get_ticks()
    

    def hurt(self, damage):
        super().hurt(damage)

    
    def death(self):
        super().death()

    def reset(self):
        super().reset()
        self.action_count = 3
    
    def draw(self):
        super().draw()
    