import pygame
from src.world.demonhunter.BaseDemonHunter import BaseDemonHunter
from src.Dependencies import gDhunter_image_list


class SeventhDemonHunter(BaseDemonHunter):
    def __init__(self, x, y, player):
        super().__init__(gDhunter_image_list, "Now, I knew where the great demon is. It possessed my wife body",
                         "Acting as a green witch. I will go settling my score (press DOWN to confirm)",
                         "I hope to see you again",
                         "I see",
                         "We will surely meet again",
                         "I have been talking too much. I will take my leave",
                         pygame.image.load("./graphics/backgroundLake.png"))
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