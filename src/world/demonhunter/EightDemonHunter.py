import pygame
from src.world.demonhunter.BaseDemonHunter import BaseDemonHunter
from src.Dependencies import gItemJoker_image_list


class EightDemonHunter(BaseDemonHunter):
    def __init__(self, x, y, player):
        super().__init__(gItemJoker_image_list, "The Joker, left behind of Colin.",
                         "(press DOWN to confirm)",
                         "Take it",
                         "Leave it",
                         "...",
                         "...",
                         pygame.image.load("./graphics/backgroundCA3.png"))
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
        self.player.acquired_joker = True
        pass

    def action2(self):
        pass