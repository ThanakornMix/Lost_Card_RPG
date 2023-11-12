import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gItemWater_image_list

class WaterItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gItemWater_image_list, "Ethereal river drop",
                         "Drop of the river from flowing from spirit realm",
                         "Said to fully restore wielder health")
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
        self.player.hp = self.player.max_hp
        pass