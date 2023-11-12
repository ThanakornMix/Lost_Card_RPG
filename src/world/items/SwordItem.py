import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gItemSword_image_list

class SwordItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gItemSword_image_list, "Grasscutter",
                         "Sword that once slain a great demon",
                         "Said to tremendously increase wielder strength but consume wielder health")
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
        self.player.strength += 20
        if self.player.hp >= 31:
            self.player.hp -= 30
            self.player.max_hp -= 30
        pass