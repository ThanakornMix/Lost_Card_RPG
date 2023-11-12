import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gItemScorpion_image_list

class ScorpionItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gItemScorpion_image_list, "Kin of The Sand Demon",
                         "A unborn fetus ripped from the great demon",
                         "Said to tremendously increase wielder health but consume wielder strength")
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
        self.player.max_hp += 50
        if self.player.strength >= 11:
            self.player.strength -= 10
        else:
            self.player.strength = 1
        pass