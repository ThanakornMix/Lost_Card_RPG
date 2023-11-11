import pygame
import random
from src.constants import *
from src.Dependencies import *
from src.world.DamageText import DamageText
from pygame.sprite import Group

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Character():
    def __init__(self, name, max_hp, strength):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.step_count = 0
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # 0:idle, 1:attack, 2:hurt, 3:dead, 4:skill, 5:skill
        self.update_time = pygame.time.get_ticks()
        self.add_animation_list(self.name)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont('Times New Roman', 26)
        self.damage_text_group = Group()
        self.reset_pos = False

    def add_animation_list(self, name):
        for animation in name:
            self.animation_list.append(animation)

    def update(self):
        animation_cooldown = 100
        # handle animation
        # update image
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()
    def idle(self):
        # set variables to idle animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        # deal damage to enemy
        self.rand = random.randint(1, 5)
        self.damage = self.strength + self.rand
        # run enemy hurt animation
        target.hurt(self.damage)
        #set variables to attack animation
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        self.damage_text = DamageText(target.rect.centerx, target.rect.y, str(self.damage), (255, 255, 255))
        self.damage_text_group.add(self.damage_text)
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    #change
    def skill(self):
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self, damage):
        self.hp -= damage
        # set variables to hurt animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def reset(self):
        self.alive = True
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        if self.reset_pos == False:
            screen.blit(self.image, self.rect)
        else:
            pass
        self.damage_text_group.update()
        self.damage_text_group.draw(screen)

