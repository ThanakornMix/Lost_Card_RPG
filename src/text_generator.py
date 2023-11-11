import pygame
import sys
import time
from src.constants import *
from src.Dependencies import *

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Function to display text character by character
class TextGenerator:
    def __init__(self, text, font, x, y, delay=0.1, color=(255, 255, 255)):
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.delay = delay
        self.color = color
        self.text_index = 0
        self.fully_displayed = False
        self.typing_sound = gSounds['Retro_Single_v6']
        self.skipped = False

    def text_generation(self):
        while self.text_index <= len(self.text) and not self.skipped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.skipped = True

            if self.skipped:
                break

            time.sleep(self.delay)
            self.typing_sound.play()
            partial_text = self.text[:self.text_index]
            text_surface = self.font.render(partial_text, True, self.color)
            screen.blit(text_surface, (self.x, self.y))
            pygame.display.update()

            self.text_index += 1

        if self.text_index > len(self.text):
            self.fully_displayed = True
            time.sleep(1)  

        return self.fully_displayed

    def text_generation_reset(self):
        self.fully_displayed = False
        self.text_index = 0
        self.skipped = False