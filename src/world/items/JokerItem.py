import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gItemJoker_image_list

class JokerItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gItemJoker_image_list, "The Joker",
                         "Demons do not know of it existence. Hold the power of fate",
                         "Use it to realize fate")
        self.player = player
        self.X = x
        self.Y = y
        self.rect.center = (self.X, self.Y)

    def update(self):
        super().update()

    def idle(self):
        # set variables to idle animation
        super().idle()
        self.rect.center = (self.X, self.Y)

    def draw(self):
        super().draw()

    def action(self):
        #change
        self.player.max_hp += 30
        self.player.acquired_joker = True
        pass