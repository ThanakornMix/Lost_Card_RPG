import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gItemHoly_image_list

class HolyItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gItemHoly_image_list, "The Ever brilliant Light",
                         "Miracle blessed upon, thus faith is born",
                         "Said to slightly increase wielder strength and health")
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
        self.player.strength += 5
        self.player.max_hp += 30
        pass