import pygame
import random
from src.constants import *
from src.Dependencies import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class BaseDemonHunter():
    def __init__(self, name, dialogue, question, choice1, choice2, dialogue2, dialogue3, background):
        self.name = name
        #background render
        self.background = background
        self.bg_image = pygame.transform.scale(
            self.background, (WIDTH + 5, HEIGHT + 5))
        self.dialogue = dialogue
        self.dialogue2 = dialogue2
        self.dialogue3 = dialogue3
        self.question = question
        self.choice1 = choice1
        self.choice2 = choice2
        self.animation_list = name
        self.frame_index = 0
        self.image = self.animation_list[self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = self.image.get_rect()
        self.current_choice = 0
        self.selected_choice = 0
        self.decision_complete = False

        #dialogue
        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
        self.t_enter = self.small_font.render(self.dialogue, False, (255, 255, 255))
        self.rect_dialogue = self.t_enter.get_rect(center=(WIDTH / 2, HEIGHT / 3 - 50))
        #question
        self.t_enter2 = self.small_font.render(self.question, False, (255, 255, 255))
        self.rect_question = self.t_enter2.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        #choice1
        self.t_enter3 = self.small_font.render(self.choice1, False, (255,255,0))
        self.rect_choice1 = self.t_enter3.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 50))
        #choice2
        self.t_enter4 = self.small_font.render(self.choice2, False, (255,255,0))
        self.rect_choice2 = self.t_enter4.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 50))
        #dialogue2
        self.t_enter5 = self.small_font.render(self.dialogue2, False, (255, 255, 255))
        self.rect_dialogue2 = self.t_enter5.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        #dialogue3
        self.t_enter6 = self.small_font.render(self.dialogue3, False, (255, 255, 255))
        self.rect_dialogue3 = self.t_enter6.get_rect(center=(WIDTH / 2, HEIGHT / 3))

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
        screen.blit(self.bg_image, (0, 0))
        if self.decision_complete is False:
            screen.blit(self.t_enter, self.rect_dialogue)
            screen.blit(self.t_enter2, self.rect_question)
            if self.current_choice == 0:
                screen.blit(self.t_enter3, self.rect_choice1)
            elif self.current_choice == 1:
                screen.blit(self.t_enter4, self.rect_choice2)
        elif self.decision_complete is True:
            if self.selected_choice == 0:
                screen.blit(self.t_enter5, self.rect_dialogue2)
            elif self.selected_choice == 1:
                screen.blit(self.t_enter6, self.rect_dialogue3)

        screen.blit(self.image, self.rect)

    def action(self):
        pass

    def action2(self):
        pass