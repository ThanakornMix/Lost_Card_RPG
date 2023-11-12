import pygame
from src.world.demonhunter.BaseDemonHunter import BaseDemonHunter
from src.Dependencies import gDhunter_image_list


class FourthDemonHunter(BaseDemonHunter):
    def __init__(self, x, y, player):
        super().__init__(gDhunter_image_list, "Have you heard of The joker? Rumors say such a card exists",
                         "It said to have power over fate. It's worth investigating (press DOWN to confirm)",
                         "I will keep an eye",
                         "I am not interested in rumors",
                         "Very well. If you find it, keep it secret.",
                         "I see. Rumors might be just rumors after all",
                         pygame.image.load("./graphics/backgroundCA2.png"))
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