import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gItemThunder_image_list

class ThunderItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gItemThunder_image_list, "Spirit bird",
                         "Thunder faith manifests in spirit realm as a bird",
                         "Said to tremendously increase wielder health and fully restore it")
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
        self.player.hp = self.player.max_hp
        pass