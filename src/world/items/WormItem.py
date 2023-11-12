import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gItemWorm_image_list

class WormItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gItemWorm_image_list, "Shadow parasite",
                         "A parasite resides in Demonic host",
                         "Said to increase slightly wielder strength but consumed wielder health tremendously")
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
        if self.player.max_hp >= 41 and self.player.hp >= 41:
            self.player.max_hp -= 40
            self.player.hp -= 40
        elif self.player.max_hp >= 41 > self.player.hp:
            self.player.max_hp -= 40
            self.player.hp = 1
        else:
            self.player.max_hp = 1
            self.player.hp = 1
        pass