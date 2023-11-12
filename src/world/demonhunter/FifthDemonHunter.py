import pygame
from src.world.demonhunter.BaseDemonHunter import BaseDemonHunter
from src.Dependencies import gDhunter_image_list


class FifthDemonHunter(BaseDemonHunter):
    def __init__(self, x, y, player):
        super().__init__(gDhunter_image_list, "This place was plentifully. However, a great demon ruined it",
                         "The one who took my other half. This is a good starting place (press DOWN to confirm)",
                         "If I found a clue, I will tell you",
                         "I see",
                         "Thankyou. May the fate favor you",
                         "let us meet again, if fate permits",
                         pygame.image.load("./graphics/backgroundRuinedDesert.png"))
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
