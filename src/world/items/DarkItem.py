import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gItemDark_image_list

class DarkItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gItemDark_image_list, "Deceased Soul of Demon",
                         "Legacy of the deceased high rank demon",
                         "Said to increase wielder strength")
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
        self.player.strength += 10
        pass