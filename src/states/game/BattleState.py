from src.states.BaseState import BaseState
import pygame, sys

from src.constants import *
from src.Dependencies import *

#make change
from src.world.Character import *
from src.world.Knight1 import Knight1
from src.world.HealthBar import HealthBar
from src.world.Rogue import Rogue
from src.world.BattleMenu import BattleMenu
from src.world.GenerateEnemy import Enemy
from src.states.game.CardState import *

class BattleState(BaseState):
    def __init__(self, state_machine):
        super(BattleState, self).__init__(state_machine)

        #map image
        self.map = 0
        self.bg_image1 = pygame.image.load("./graphics/Battleground3.png")
        self.bg_image1 = pygame.transform.scale(
            self.bg_image1, (WIDTH + 5, HEIGHT + 5))
        self.bg_image2 = pygame.image.load("./graphics/Battleground1.png")
        self.bg_image2 = pygame.transform.scale(
            self.bg_image2, (WIDTH + 5, HEIGHT + 5))
            
        self.bg_image = pygame.image.load("./graphics/background.png")
        self.bg_image = pygame.transform.scale(
            self.bg_image, (WIDTH + 5, HEIGHT + 5))

        #loading BG
        self.loading_bg_img = pygame.image.load("./graphics/loading_1.png")
        self.loading_bg_img = pygame.transform.scale(self.loading_bg_img, (WIDTH + 5, HEIGHT + 5))
        
        self.unavailable_sound = gSounds['no-select']
        self.available_sound = gSounds['select']
        self.confirm_sound = gSounds['confirm']
        self.return_to_main_sound = gSounds['wall_hit']

        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
        self.medium_font = pygame.font.Font('./fonts/font.ttf', 48)
        #position reset for next stage
        # chosen character for rogue and warrior
        self.playerResetR_X = WIDTH / 2 - 150
        self.playerResetR_Y = HEIGHT - HEIGHT / 3 - 20
        # for wizard
        self.playerResetW_X = WIDTH / 2 - 200
        self.playerResetW_Y = HEIGHT - HEIGHT / 3 - 30

    def Enter(self, params):
        #make change
        self.player = params['chosen']
        if self.player.Class == "Rogue":
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 50, HEIGHT - HEIGHT / 3 - 30,
                                          self.player.hp, self.player.max_hp)
        elif self.player.Class == "Warrior":
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 50, HEIGHT - HEIGHT / 3 - 30,
                                          self.player.hp, self.player.max_hp)
        elif self.player.Class == "Wizard":
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 50, HEIGHT - HEIGHT / 3 - 30,
                                          self.player.hp, self.player.max_hp)
        self.battle_menu = BattleMenu(self.player.action_list)
        #make change later fighter
        self.total_step = self.player.step_count
        
        if self.total_step > 6:
            print(f"Total sttep = '{self.total_step}")  
            self.map = 1
            self.enemy = Enemy(self.map)
        else:
            self.enemy = Enemy(self.map)
            print(f"Total sttep = '{self.total_step}")   
        
        #game variable
        self.current_fighter = 1
        self.total_fighter = 1 + len(self.enemy.enemy_list)
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.battle_over = 0
        self.action_count = 3
        self.enemy_alive = len(self.enemy.enemy_list)
        self.loading = 0
        pass

    def update(self, dt, events):
        #make change

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #select enemies to hit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.enemy.selected_enemy_index == 2:
                        self.enemy.selected_enemy_index = 1
                    else:
                        pass
                elif event.key == pygame.K_RIGHT:
                    if self.enemy.selected_enemy_index == 1:
                        self.enemy.selected_enemy_index = 2
                    else:
                        pass
                        
                #test attack key(w)
                if event.key == pygame.K_w:
                    self.attack = True
                    if self.player.alive == True:
                        if self.current_fighter == 1:
                            self.action_cooldown += 1
                            print(self.action_cooldown)
                            if self.attack == True and self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive:
                                if self.action_count > 1:
                                    self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                    self.action_count -= 1
                                    self.action_cooldown = 0
                                else:
                                    self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                    self.action_count -= 1
                                    self.current_fighter += 1
                                    self.action_cooldown = 0
                            else:
                                pass


                    # self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                    else:
                        self.battle_over = -1
           

                # test skill key(e)
                if event.key == pygame.K_e:
                    self.player.skill()

                if event.key == pygame.K_RETURN:
                    # update player position
                    if self.player.Class == "Rogue":
                        self.player.X = self.playerResetR_X
                        self.player.Y = self.playerResetR_X
                    elif self.player.Class == "Warrior":
                        self.player.X = self.playerResetR_X
                        self.player.Y = self.playerResetR_Y
                    elif self.player.Class == "Wizard":
                        self.player.X = self.playerResetW_X
                        self.player.Y = self.playerResetW_Y

                    #sound
                    #reset if want player to have full hp
                    for e in self.enemy.enemy_list:
                        e.reset()
                    
                    self.confirm_sound.play()
                    gSounds['music'].stop()
                    gSounds['late-hours'].play(-1)
                    gSounds['campfire_fireplace'].play(-1)
                    self.loading = 0
                    self.player.reset_pos = True

                    self.state_machine.Change('roll', {
                        'chosen': self.player
                    })

        for index, enemy in enumerate(self.enemy.enemy_list):
            if self.current_fighter == 2 + index:
                if enemy.alive == True:
                    self.action_cooldown += 1
                    if self.action_cooldown >= self.action_wait_time:
                        enemy.attack(self.player)
                        self.current_fighter += 1
                        self.action_cooldown = 0
                else:
                    self.current_fighter += 1
            else:
                if self.current_fighter > self.total_fighter:
                    self.current_fighter = 1 
                    self.action_count = 3           
    

    def is_enemy_alive(self):
        for enemy in self.enemy.enemy_list:
            if enemy.alive == True:
                self.enemy_alive -= 1
        if self.enemy_alive == 0:
            self.game_over = 1

    def render(self, screen):
        #make change
        if self.map == 0:
            screen.blit(self.bg_image1, (0, 0))
        elif self.map == 1:
            screen.blit(self.bg_image2, (0, 0))
        #fighter & health
        self.player.draw()
        self.playerHealth.draw(self.player.hp)
        self.player.update()

        self.enemy.render_enemy()
        self.enemy.draw_pointer_enemy()

        #display battle menus
        self.battle_menu.display_fighting_menu()

        #loading
        if self.loading > 70:
            self.player.reset_pos = False
        elif self.loading > 70 and self.player.reset_pos == False:
            pass
        else:
            font  = pygame.font.Font('./fonts/font.ttf', 28)
            text = font.render('Loading...', True, (255, 255, 255))
            screen.blit(self.loading_bg_img, (0, 0))
            screen.blit(text, (WIDTH - 170, HEIGHT - 70))
            self.loading += 1

        #make change later
        # Update frame index for animation (for instance, every 5 frames)


    def Exit(self):
        pass
