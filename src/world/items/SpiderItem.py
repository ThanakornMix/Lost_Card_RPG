import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gItemSpider_image_list

class SpiderItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gItemSpider_image_list, "Skull spider",
                         "A friendly demonic creature that commonly found in spirit realm",
                         "Said to slightly increase wielder strength")
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
        pass