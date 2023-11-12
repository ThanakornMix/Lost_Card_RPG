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
from src.states.game.CardState import CardState

class BattleState(BaseState):
    def __init__(self, state_machine):
        super(BattleState, self).__init__(state_machine)
        #map image
        self.bg_image = None
        self.bg_image_list = []
        self.map = 0
        self.bg_image1 = pygame.image.load("./graphics/Battleground3.png")
        self.bg_image1 = pygame.transform.scale(
            self.bg_image1, (WIDTH + 5, HEIGHT + 5))
        self.bg_image_list.append(self.bg_image1)
        self.bg_image2 = pygame.image.load("./graphics/Battle_BG_3.png")
        self.bg_image2 = pygame.transform.scale(
            self.bg_image2, (WIDTH + 5, HEIGHT + 5))
        self.bg_image_list.append(self.bg_image2)
        self.bg_image3 = pygame.image.load("./graphics/Battle_BG_1.jpg")
        self.bg_image3 = pygame.transform.scale(
            self.bg_image3, (WIDTH + 5, HEIGHT + 5))
        self.bg_image_list.append(self.bg_image3)
        self.bg_image4 = pygame.image.load("./graphics/Battleground2.png")
        self.bg_image4 = pygame.transform.scale(
            self.bg_image4, (WIDTH + 5, HEIGHT + 5))
        self.bg_image_list.append(self.bg_image4)
        self.bg_image5 = pygame.image.load("./graphics/Battle_BG_2.png")
        self.bg_image5 = pygame.transform.scale(
            self.bg_image5, (WIDTH + 5, HEIGHT + 5))
        self.bg_image_list.append(self.bg_image5)
        self.bg_image6 = pygame.image.load("./graphics/Battle_BG_4.png")
        self.bg_image6 = pygame.transform.scale(
            self.bg_image6, (WIDTH + 5, HEIGHT + 5))
        self.bg_image_list.append(self.bg_image6)
        self.bg_image7 = pygame.image.load("./graphics/Battle_BG_5.png")
        self.bg_image7 = pygame.transform.scale(
            self.bg_image7, (WIDTH + 5, HEIGHT + 5))
        self.bg_image_list.append(self.bg_image7)
        self.bg_image8 = pygame.image.load("./graphics/Battle_BG_6.png")
        self.bg_image8 = pygame.transform.scale(
            self.bg_image8, (WIDTH + 5, HEIGHT + 5))
        self.bg_image_list.append(self.bg_image8)
        self.bg_image = None

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
        self.ATK_increase = math.ceil(self.player.strength*0.05)
        self.HP_increase = math.ceil(self.player.max_hp*0.05)

        if CardState.get_current_card(CardState) == 25:
            self.map = 25
            self.bg_image = self.bg_image_list[4]
        elif CardState.get_current_card(CardState) == 51:
            self.map = 51
            self.bg_image = self.bg_image_list[5]
        elif CardState.get_current_card(CardState) == 38:
            self.map = 38
            self.bg_image = self.bg_image_list[6]
        elif CardState.get_current_card(CardState) == 12:
            self.map = 12
            self.bg_image = self.bg_image_list[7]
        elif CardState.get_current_card(CardState) == 24:
            self.map = 12
            self.bg_image = self.bg_image_list[CardState.get_level(CardState) - 1]
        elif CardState.get_current_card(CardState) == 50:
            self.map = 12
            self.bg_image = self.bg_image_list[CardState.get_level(CardState) - 1] 
        elif CardState.get_current_card(CardState) == 37:
            self.map = 12
            self.bg_image = self.bg_image_list[CardState.get_level(CardState) - 1] 
        elif CardState.get_current_card(CardState) == 11:
            self.map = 12
            self.bg_image = self.bg_image_list[CardState.get_level(CardState) - 1]
        elif CardState.get_current_card(CardState) == 23:
            self.map = 12
            self.bg_image = self.bg_image_list[CardState.get_level(CardState) - 1] 
        elif CardState.get_current_card(CardState) == 49:
            self.map = 12
            self.bg_image = self.bg_image_list[CardState.get_level(CardState) - 1] 
        elif CardState.get_current_card(CardState) == 36:
            self.map = 12
            self.bg_image = self.bg_image_list[CardState.get_level(CardState) - 1] 
        elif CardState.get_current_card(CardState) == 10:
            self.map = 12
            self.bg_image = self.bg_image_list[CardState.get_level(CardState) - 1]       
        else:
            self.map = CardState.get_level(CardState)
            self.bg_image = self.bg_image_list[self.map - 1]
        
        self.enemy = Enemy(self.map)

        #game variable
        self.current_fighter = 1
        self.total_fighter = 1 + len(self.enemy.enemy_list)
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.skill_1 = False
        self.skill_2 = False
        self.battle_over = 0
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
                            print(f"Action cooldown = {self.action_cooldown}")
                            if self.attack == True and self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive:
                                if self.player.action_count > 1:
                                    self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                    self.player.action_count -= 1
                                    self.action_cooldown = 0
                                else:
                                    self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                    self.player.action_count -= 1
                                    self.current_fighter += 1
                                    self.action_cooldown = 0
                            else:
                                pass
                        else:
                            pass
                    else:
                        self.battle_over = -1
           

                # test skill key(q)
                elif event.key == pygame.K_q:
                    self.skill_1 = True
                    if self.player.alive == True:
                        if self.current_fighter == 1:
                            self.action_cooldown += 1
                            print(f"Action cooldown = {self.action_cooldown}")
                            if self.skill_1 == True and self.player.skill_cooldown_1 == 0:
                                if self.player.action_count > 1:
                                    if self.player.Class == "Rogue":
                                        self.player.skill_1()
                                    elif self.player.Class == "Warrior":
                                        if self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive:
                                            self.player.skill_1(self.enemy.enemy_list)
                                    self.player.action_count -= 1
                                    self.action_cooldown = 0
                                else:
                                    if self.player.Class == "Rogue":
                                        self.player.skill_1()
                                        self.player.action_count -= 1
                                        self.current_fighter += 1
                                        self.action_cooldown = 0
                            else:
                                pass
                        else:
                            pass
                    else:
                        self.battle_over = -1
                #test skill key(e)
                elif event.key == pygame.K_e:
                    self.skill_2 = True
                    if self.player.alive == True:
                        if self.current_fighter == 1:
                            self.action_cooldown += 1
                            print(f"Action cooldown = {self.action_cooldown}")
                            if self.skill_2 == True and self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive and self.player.skill_cooldown_2 == 0:
                                if self.player.action_count > 1:
                                    self.player.skill_2(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                    self.player.action_count -= 1
                                    self.action_cooldown = 0
                                else:
                                    self.player.skill_2(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                    self.player.action_count -= 1
                                    self.current_fighter += 1
                                    self.action_cooldown = 0
                            else:
                                pass
                        else:
                            pass
                    else:
                        self.battle_over = -1

                elif event.key == pygame.K_RETURN:
                    # update player position
                    self.player.strength+=self.ATK_increase
                    self.player.max_hp+=self.HP_increase
                    if self.player.Class == "Rogue":
                        self.player.X = self.playerResetR_X
                        self.player.Y = self.playerResetR_X
                    elif self.player.Class == "Warrior":
                        self.player.X = self.playerResetR_X
                        self.player.Y = self.playerResetR_Y
                    elif self.player.Class == "Wizard":
                        self.player.X = self.playerResetW_X
                        self.player.Y = self.playerResetW_Y
                    print(self.player.max_hp)
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
                    self.player.action_count = 3
                    self.player.skill_cooldown_1 = 0
                    self.player.skill_cooldown_2 = 0

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

        if self.player.action_count == 0:
            self.player.action_count = 3
            if self.player.skill_cooldown_1 > 0:
                self.player.skill_cooldown_1 -= 1
            if self.player.skill_cooldown_2 > 0:
                self.player.skill_cooldown_2 -= 1

        self.is_enemy_alive()
    

    def is_enemy_alive(self):
        self.enemy_alive = len(self.enemy.enemy_list)
        for enemy in self.enemy.enemy_list:
            if enemy.alive == False:
                self.enemy_alive -= 1
        if self.enemy_alive == 0:
            self.battle_over = 1

    def render(self, screen):
        #make change
        print(CardState.get_level(CardState))

        screen.blit(self.bg_image, (0, 0))
        #fighter & health
        self.player.draw()
        self.playerHealth.draw(self.player.hp)
        self.player.update()

        self.enemy.render_enemy()
        self.enemy.draw_pointer_enemy()
        font  = pygame.font.Font('./fonts/font.ttf', 30)
        #display battle menus
        self.battle_menu.display_fighting_menu()

        #display skill cooldown
        skill_1_cooldown = font.render(('CD: ('+str(self.player.skill_cooldown_1)+'turn)'), True, (255, 255, 255))
        screen.blit(skill_1_cooldown, (210, 320))

        skill_2_cooldown = font.render(('CD: ('+str(self.player.skill_cooldown_2)+'turn)'), True, (255, 255, 255))
        screen.blit(skill_2_cooldown, (210, 360))



        #display action count
        total_turn_text = font.render(('Action: '+str(self.player.action_count)), True, (255, 255, 255))
        screen.blit(total_turn_text, (WIDTH - 170, HEIGHT - 70))

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

        if self.battle_over == 1:
            if self.map == 0:
                screen.blit(self.bg_image1, (0, 0))
            elif self.map == 1:
                screen.blit(self.bg_image2, (0, 0))
            t_enter = gFonts['zelda'].render("Victory"
                                             , False, (175, 53, 42))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 - 10))
            screen.blit(t_enter, rect)
            t_enter = self.small_font.render("The card grant you"
                                             , False, (255, 255, 0))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 + 40))
            screen.blit(t_enter, rect)
            t_enter = self.small_font.render("%d ATK and %d HP" %(self.ATK_increase,self.HP_increase)
                                             , False, (255, 255, 0))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 + 80))
            screen.blit(t_enter, rect)
            t_enter = self.small_font.render("Press 'Enter' to continue your journey"
                                             , False, (255, 255, 0))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 + 120))
            screen.blit(t_enter, rect)

        


        #make change later
        # Update frame index for animation (for instance, every 5 frames)


    def Exit(self):
        pass
