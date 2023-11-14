import pygame
from src.world.demonhunter.BaseDemonHunter import BaseDemonHunter
from src.Dependencies import gDhunter_image_list


class SecondDemonHunter(BaseDemonHunter):
    def __init__(self, x, y, player):
        super().__init__(gDhunter_image_list, "This place is where I and my wife once share our loves",
                         "By the way, are you aware of the power of cards you behold (press DOWN to confirm)",
                         "Yes, I am aware",
                         "No, I am not aware",
                         "I see. Then I have nothing to worry about. Feel free to look around",
                         "I see. Just keep them close. They will ward off demons away from you",
                         pygame.image.load("./graphics/backgroundSwampHouse.png"))
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
        self.player.strength += 2
        self.player.hp += 10
        pass
