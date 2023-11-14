import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gItemIce_image_list

class IceItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gItemIce_image_list, "Shard of the cold one",
                         "Left behind of the something greater",
                         "Said to increase wielder strength slightly and health")
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