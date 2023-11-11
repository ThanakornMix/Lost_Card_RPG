import pygame
from .Character import Character
from src.Dependencies import gRogueBattle_image_list

class Rogue(Character):
    def __init__(self, x, y):
        super().__init__(gRogueBattle_image_list, max_hp = 100, strength = 3)
        self.X = x
        self.Y = y+15
        self.Class = "Rogue"
        self.action_list = ["W (Attack)", "Q (Evade)", "E (Slash)"]
        self.evade = False
        self.rect.center = (self.X, self.Y)

    def update(self):
        super().update()


    def idle(self):
        super().idle()
        self.rect.center = (self.X, self.Y)

    def attack(self, target):
        self.rect.center = (self.X, self.Y)
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
    