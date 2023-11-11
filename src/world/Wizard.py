import pygame
from .Character import Character
from src.Dependencies import gWizardBattle_image_list


class Wizard(Character):
    def __init__(self, x, y):
        super().__init__(gWizardBattle_image_list, max_hp = 100, strength = 10)
        self.X = x
        self.Y = y+15
        self.Class = "Wizard"
        self.action_list = ["W (Attack)", "Q (______)", "E (_______)"]
        self.evade = False
        self.rect.center = (self.X, self.Y)

    def update(self):
        super().update()


    def idle(self):
        super().idle()
        self.rect.center = (self.X, self.Y)

    def attack(self, target):
        self.rect.center = (self.X, self.Y-120)
        super().attack(target)

    
    def skill(self):
        self.rect.center = (self.X, self.Y)
        super().skill()
        if self.evade == False:
            self.evade = True
        else:
            pass

    def hurt(self, damage):
        super().hurt(damage)
    
    def death(self):
        super().death()

    def reset(self):
        super().reset()
    
    def draw(self):
        super().draw()
    