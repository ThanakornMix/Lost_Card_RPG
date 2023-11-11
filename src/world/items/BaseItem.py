import pygame
import random
from src.constants import *
from src.Dependencies import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class BaseItem():
    def __init__(self, name, item_name, item_description):
        self.name = name
        self.item_name = item_name
        self.item_description = item_description
        self.animation_list = name
        self.frame_index = 0
        self.image = self.animation_list[self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = self.image.get_rect()

        #Name of item
        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
        self.t_enter = self.small_font.render(self.item_name, False, (255, 255, 255))
        self.rect_name = self.t_enter.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        #Item description
        self.t_enter2 = self.small_font.render(self.item_description, False, (255, 255, 255))
        self.rect_des = self.t_enter2.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 50))

    def update(self):
        animation_cooldown = 100
        # handle animation
        # update image
        self.image = self.animation_list[self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list):
            self.idle()

    def idle(self):
        # set variables to idle animation
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.t_enter, self.rect_name)
        screen.blit(self.t_enter2, self.rect_des)
        screen.blit(self.image, self.rect)

    def action(self):
        pass