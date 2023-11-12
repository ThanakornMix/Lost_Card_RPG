import pygame
from src.world.demonhunter.BaseDemonHunter import BaseDemonHunter
from src.Dependencies import gDhunter_image_list


class SixthDemonHunter(BaseDemonHunter):
    def __init__(self, x, y, player):
        super().__init__(gDhunter_image_list, "The grave...is an empty husk. Someone has dug up a corpse and stolen it",
                         "...but why...why did such a thing... (press DOWN to confirm)",
                         "I am sorry for your lost",
                         "...",
                         "...Thank for you concern",
                         "...",
                         pygame.image.load("./graphics/backgroundFlower.png"))
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
        self.player.strength += 2
        self.player.hp += 10
        pass

    def action2(self):
        pass