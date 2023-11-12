import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gLwPistol_image_list

class PistolItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gLwPistol_image_list, "Pistol",
                         "Foreign object that should not exist in this land",
                         "Said to tremendously increase wielder strength")
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
        self.player.strength += 15
        pass