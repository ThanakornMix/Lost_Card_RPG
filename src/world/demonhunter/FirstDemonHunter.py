import pygame
from src.world.demonhunter.BaseDemonHunter import BaseDemonHunter
from src.Dependencies import gDhunter_image_list


class FirstDemonHunter(BaseDemonHunter):
    def __init__(self, x, y, player):
        super().__init__(gDhunter_image_list, "I am Colin, the last hunter of Demonhunter brotherhood",
                         "Are you also looking for demon? (press DOWN to confirm)",
                         "Yes, I am",
                         "No, I am not",
                         "Very well. Take this blessing, it might help you. Let us meet again, brother",
                         "I see. If the fate permits, we shall meet again",
                         pygame.image.load("./graphics/backgroundRedCa.png"))
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
        self.player.strength -= 2
        if self.player.hp >= 11:
            self.player.hp -= 10
        else:
            self.player.hp = 1
        pass
