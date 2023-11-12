import pygame
from src.world.demonhunter.BaseDemonHunter import BaseDemonHunter
from src.Dependencies import gDhunter_image_list


class ThirdDemonHunter(BaseDemonHunter):
    def __init__(self, x, y, player):
        super().__init__(gDhunter_image_list, "This is my wife grave. She had a beautiful green hair. I miss her...",
                         "She were killed by a great demon. Revenge...I must have it (press DOWN to confirm)",
                         "You are a kind person",
                         "I see",
                         "... I will be on my way. You can watch the flowers if you want",
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