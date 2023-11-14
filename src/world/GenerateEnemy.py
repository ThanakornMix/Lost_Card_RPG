import time
import pygame
from src.constants import *
from src.world.Knight1 import Knight1
from src.world.Huntress import Huntress
from src.world.HealthBar import HealthBar
from src.world.KingOfDiamond import KingOfDiamond
from src.world.KingOfClub import KingOfClub
from src.world.KingOfHeart import KingOfHeart
from src.world.KingOfSpade import KingOfSpade
from src.world.QueenOfDiamond import QueenOfDiamond
from src.world.QueenOfHeart import QueenOfHeart
from src.world.QueenOfSpade import QueenOfSpade
from src.world.QueenOfClub import QueenOfClub
from src.world.Jack import Jack
from src.world.HeroKnight import HeroKnight
from src.world.Skeleton import Skeleton
from src.world.Cthulu import Cthulu
from src.world.Witch import Witch

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Enemy():
    def __init__(self, map_number):
        self.selected_enemy_index = 0
        self.map_number = map_number
        self.generate_enemy()

    def generate_enemy(self):
        self.enemy_list = []
        self.enemy_health_list = []
        if self.map_number == 1:
            #Level 1 monster number 1
            self.enemy_list.append(Huntress(x = WIDTH / 2 - 96 + 300))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 300, HEIGHT - HEIGHT / 3 - 30, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            #Level 1 monster number 2
            self.enemy_list.append(Huntress(x = WIDTH / 2 - 96 + 500))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 500, HEIGHT - HEIGHT / 3 - 30, self.enemy_list[1].hp, self.enemy_list[1].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1

        elif self.map_number == 2:
            #Level 2 monster number 1
            self.enemy_list.append(Skeleton(x = WIDTH / 2 - 96 + 300))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 300, HEIGHT - HEIGHT / 3 - 30, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            #Level 2 monster number 2
            self.enemy_list.append(Skeleton(x = WIDTH / 2 - 96 + 500))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 500, HEIGHT - HEIGHT / 3 - 30, self.enemy_list[1].hp, self.enemy_list[1].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1

        elif self.map_number == 3:
            #Level 3 monster number 1
            self.enemy_list.append(Knight1(x = WIDTH / 2 - 96 + 300))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 300, HEIGHT - HEIGHT / 3 - 30, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            #Level 3 monster number 2
            self.enemy_list.append(Knight1(x = WIDTH / 2 - 96 + 500))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 500, HEIGHT - HEIGHT / 3 - 30, self.enemy_list[1].hp, self.enemy_list[1].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1

        elif self.map_number == 4:
            #Level 4 monster number 1
            self.enemy_list.append(HeroKnight(x = WIDTH / 2 - 96 + 300))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 300, HEIGHT - HEIGHT / 3 - 30, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            #Level 4 monster number 2
            self.enemy_list.append(HeroKnight(x = WIDTH / 2 - 96 + 500))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 500, HEIGHT - HEIGHT / 3 - 30, self.enemy_list[1].hp, self.enemy_list[1].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1
        
        elif self.map_number == 25:
            #King of Club
            self.enemy_list.append(KingOfClub(x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 - 35))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 45, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1
        
        elif self.map_number == 51:
            #King of Diamond
            self.enemy_list.append(KingOfDiamond(x = WIDTH / 2 - 96 + 400))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 30, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1

        elif self.map_number == 38:
            # King of Heart
            self.enemy_list.append(KingOfHeart(x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 - 35))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 30, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1
        
        elif self.map_number == 12:
            # King of Spade
            self.enemy_list.append(KingOfSpade(x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 + 10))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 45, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1

        #Queen
        elif self.map_number == 24:
            #Queen of Club
            self.enemy_list.append(QueenOfClub(x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 - 35))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 45, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1
        
        elif self.map_number == 50:
            #Queen of Diamond
            self.enemy_list.append(QueenOfDiamond(x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 - 35))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 45, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1

        elif self.map_number == 37:
            #Queen of Heart
            self.enemy_list.append(QueenOfHeart(x = WIDTH / 2 - 96 + 300, y = HEIGHT - HEIGHT / 3 + 20))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 290, HEIGHT - HEIGHT / 3 - 45, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1
        
        elif self.map_number == 11:
            #Queen of Spade
            self.enemy_list.append(QueenOfSpade(x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 - 35))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 45, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1
        #Jack
        elif self.map_number == 23:
            #Jack of Club
            self.enemy_list.append(Jack(hp = 200, strength = 7, x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 + 10))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 50, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1
        
        elif self.map_number == 49:
            #Jack of Diamond
            self.enemy_list.append(Jack(hp = 400, strength = 12, x = WIDTH / 2 - 96 + 400 + 10, y = HEIGHT - HEIGHT / 3 + 10))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 50 , self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1

        elif self.map_number == 36:
            #Jack of Heart
            self.enemy_list.append(Jack(hp = 600, strength = 15, x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 + 10))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 50, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1
        
        elif self.map_number == 10:
            #Jack of Spade
            self.enemy_list.append(Jack(hp = 800, strength = 17, x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 + 10))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 50, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1
        
        elif self.map_number == 98:
            #Cthulu
            self.enemy_list.append(Cthulu(x = WIDTH / 2 - 96 + 350, y = HEIGHT - HEIGHT / 3 + 50))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 350, HEIGHT - HEIGHT / 3 - 90, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1
        
        elif self.map_number == 99:
            #Witch
            self.enemy_list.append(Witch(x = WIDTH / 2 - 96 + 300, y = HEIGHT - HEIGHT / 3 + 70))
            self.enemy_health_list.append(HealthBar(WIDTH / 2 - 96 - 50 + 300, HEIGHT - HEIGHT / 3 - 40, self.enemy_list[0].hp, self.enemy_list[0].max_hp))
            self.selected_enemy_index = len(self.enemy_list) - 1
            
            
                
    def render_enemy(self):
        for enemy in self.enemy_list:
            enemy.update()
            enemy.draw()
                    
        for i in range(0, len(self.enemy_health_list), 1):
            self.enemy_health_list[i].draw(self.enemy_list[i].hp)

    def draw_pointer_enemy(self):
        if len(self.enemy_list) > 1:
            if self.selected_enemy_index > 0:
                if self.selected_enemy_index == 1:
                    self.arrow_x = self.enemy_list[0].x
                    self.arrow_y = self.enemy_list[0].y - 100
                    pygame.draw.polygon(screen, (255, 0, 0), [(self.arrow_x, self.arrow_y), (self.arrow_x + 10, self.arrow_y - 20), (self.arrow_x - 10, self.arrow_y - 20)])
                elif self.selected_enemy_index == 2:
                    self.arrow_x = self.enemy_list[1].x
                    self.arrow_y = self.enemy_list[1].y - 100
                    pygame.draw.polygon(screen, (255, 0, 0), [(self.arrow_x, self.arrow_y), (self.arrow_x + 10, self.arrow_y - 20), (self.arrow_x - 10, self.arrow_y - 20)])
        else:
            # self.arrow_x = self.enemy_list[0].x
            # self.arrow_y = self.enemy_list[0].y - 50
            # pygame.draw.polygon(screen, (255, 0, 0), [(self.arrow_x, self.arrow_y), (self.arrow_x + 10, self.arrow_y - 20), (self.arrow_x - 10, self.arrow_y - 20)])
            pass
            

