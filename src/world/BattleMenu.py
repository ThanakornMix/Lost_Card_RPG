import pygame
from src.constants import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class BattleMenu():
    def __init__(self, action_list):
        self.action_list = action_list
        self.pointer_index = 0

    # Function to display the fighting menu
    def display_fighting_menu(self):
        menu_font = pygame.font.Font('./fonts/font.ttf', 30)
        menu_x, menu_y = 50, 280

        for index, action in enumerate(self.action_list):
            text = menu_font.render(action, True, (255, 255, 255))
            text_rect = text.get_rect(topleft=(menu_x, menu_y + index * 40))
            screen.blit(text, text_rect)
        
            # if index == self.pointer_index:
            #     pointer = menu_font.render("v", True, (255, 0, 0))  # Red pointer
            #     pointer_rect = pointer.get_rect(topleft=(menu_x - 30, menu_y + index * 40))
            #     screen.blit(pointer, pointer_rect)

