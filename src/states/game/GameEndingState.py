from src.states.BaseState import BaseState
import pygame, sys

from src.constants import *
from src.Dependencies import *

# make change
from src.world.Character import *
from src.world.Knight1 import Knight1
from src.world.HealthBar import HealthBar
from src.world.Rogue import Rogue
from src.world.BattleMenu import BattleMenu
from src.world.GenerateEnemy import Enemy
from src.states.game.MeetingState import MeetingState
from src.states.game.LootingState import LootingState

# text generator
from src.text_generator import TextGenerator

class GameEndingState(BaseState):
    def __init__(self, state_machine):
        super(GameEndingState, self).__init__(state_machine)
        # map image
        self.bg_image = pygame.image.load("./graphics/backgroundFinal.jpg")


        # loading BG
        self.loading_bg_img = pygame.image.load("./graphics/loading_5.png")
        self.loading_bg_img = pygame.transform.scale(self.loading_bg_img, (WIDTH + 5, HEIGHT + 5))

        #sound
        self.unavailable_sound = gSounds['no-select']
        self.available_sound = gSounds['select']
        self.confirm_sound = gSounds['confirm']
        self.return_to_main_sound = gSounds['wall_hit']

        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
        self.medium_font = pygame.font.Font('./fonts/font.ttf', 48)

        #text generator
        self.opening_font = gFonts['zelda']
        self.opening_text = " ignorant"
        self.opening_text2 = " should"
        self.opening_text3 = " remain"
        self.generator = TextGenerator(self.opening_text, self.opening_font, 100, HEIGHT / 2 - 200, 0.1, (220,20,60))
        self.generator2 = TextGenerator(self.opening_text2, self.opening_font, 100, HEIGHT / 2 - 100, 0.1, (220, 20, 60))
        self.generator3 = TextGenerator(self.opening_text3, self.opening_font, 100, HEIGHT / 2, 0.1, (220, 20, 60))
        self.generator4 = TextGenerator(self.opening_text, self.opening_font, 100, HEIGHT / 2 + 100, 0.1, (220, 20, 60))

        self.generator.skip_able = False
        self.generator2.skip_able = False
        self.generator3.skip_able = False
        self.generator4.skip_able = False

        # final boss map
        self.map = 99

    def Enter(self, params):
        # sounds
        self.music_selected = gSounds['battle5']
        self.music_selected.play(-1)
        # make change
        self.player = params['chosen']
        if self.player.Class == "Rogue":
            self.player.Y += 50
            self.player.X -= 20
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 100, HEIGHT - HEIGHT / 3 - 40,
                                          self.player.hp, self.player.max_hp)
        elif self.player.Class == "Warrior":
            self.player.Y += 30
            self.player.X -= 30
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 100, HEIGHT - HEIGHT / 3 - 40,
                                          self.player.hp, self.player.max_hp)
        elif self.player.Class == "Wizard":
            self.player.Y += 90
            self.player.X += 30
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 110, HEIGHT - HEIGHT / 3 - 40,
                                          self.player.hp, self.player.max_hp)
            self.player.is_use_skill2 = False    

        self.battle_menu = BattleMenu(self.player.action_list)
        # make change later fighter
        self.total_step = self.player.step_count
        self.ATK_increase = int(math.ceil(self.player.strength * 0.05))
        self.HP_increase = int(math.ceil(self.player.max_hp * 0.05))
        self.enemy_turn = 0
        self.enemy_turn_skill_2 = False


        #call enemy
        self.enemy = Enemy(self.map)

        # game variable
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
            if self.loading > 80:
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
                            
                    #test attack key(q)
                    if event.key == pygame.K_q:
                        self.attack = True
                        if self.player.alive == True:
                            if self.current_fighter == 1:
                                self.action_cooldown += 1
                                if self.attack == True and self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive:
                                    if self.player.action_count > 1:
                                        if self.player.Class == "Wizard":
                                            self.player.attack(self.enemy.enemy_list)
                                        else:
                                            self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                        self.player.action_count -= 1
                                        self.action_cooldown = 0
                                    else:
                                        if self.player.Class == "Wizard":
                                            self.player.attack(self.enemy.enemy_list)
                                        else:
                                            self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                        self.player.action_count -= 1
                                        self.current_fighter += 1
                                        self.action_cooldown = 0
                                        if self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].b_name == "Witch" and self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive == False:
                                            self.map = 98
                                            self.enemy.map_number = self.map
                                            self.enemy.generate_enemy() 
                                else:
                                    pass
                            else:
                                pass
                        else:
                            self.battle_over = -1
            

                    # test skill key(w)
                    elif event.key == pygame.K_w:
                        self.skill_1 = True
                        if self.player.alive == True:
                            if self.current_fighter == 1:
                                self.action_cooldown += 1
                                if self.skill_1 == True and self.player.skill_cooldown_1 == 0:
                                    if self.player.action_count > 1:
                                        if self.player.Class == "Rogue":
                                            self.player.skill_1()
                                        elif self.player.Class == "Warrior" or self.player.Class == "Wizard":
                                            if self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive:
                                                self.player.skill_1(self.enemy.enemy_list)
                                        self.player.action_count -= 1
                                        self.action_cooldown = 0
                                    else:
                                        if self.player.Class == "Rogue":
                                            self.player.skill_1()
                                        elif self.player.Class == "Warrior" or self.player.Class == "Wizard":
                                            if self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive:
                                                self.player.skill_1(self.enemy.enemy_list)
                                        self.player.action_count -= 1
                                        self.current_fighter += 1
                                        self.action_cooldown = 0
                                    if self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].b_name == "Witch" and self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive == False:
                                            self.map = 98
                                            self.enemy.map_number = self.map
                                            self.enemy.generate_enemy()
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
                                if self.skill_2 == True and self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive and self.player.skill_cooldown_2 == 0:
                                    if self.player.action_count > 1:
                                        if self.player.Class == "Wizard":
                                            self.player.skill_2()
                                        else:
                                            self.player.skill_2(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                        self.player.action_count -= 1
                                        self.action_cooldown = 0
                                    else:
                                        if self.player.Class == "Wizard":
                                            self.player.skill_2()
                                        else:
                                            self.player.skill_2(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                        self.player.action_count -= 1
                                        self.current_fighter += 1
                                        self.action_cooldown = 0
                                    if self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].b_name == "Witch" and self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive == False:
                                            self.map = 98
                                            self.enemy.map_number = self.map
                                            self.enemy.generate_enemy()
                                else:
                                    pass
                            else:
                                pass
                        else:
                            self.battle_over = -1

                    elif event.key == pygame.K_RETURN and self.battle_over != 0:
                        # update player position
                        if self.player.Class == "Wizard" and self.player.is_use_skill2 == True:
                            self.player.strength = self.player.original_str
                        self.player.strength+=self.ATK_increase
                        self.player.max_hp+=self.HP_increase
                        #sound
                        #reset if want player to have full hp
                        for e in self.enemy.enemy_list:
                            if e.enemy_type == "Boss":
                                self.player.hp = self.player.max_hp
                            elif e.enemy_type == "Miniboss":
                                self.player.hp += int(self.player.max_hp*0.2)
                            e.reset()

                        self.confirm_sound.play()
                        self.loading = 0
                        self.player.reset_pos = True
                        self.player.action_count = 3
                        self.player.skill_cooldown_1 = 0
                        self.player.skill_cooldown_2 = 0
                        self.player.block = False
                        self.player.evade = False
                        self.player.double_damage = False
                        #stop music
                        self.music_selected.stop()
                        if self.battle_over == 1:
                            if self.map == 98:
                                if self.player.acquired_joker == True:
                                    self.state_machine.Change('EndingCut', {
                                    'chosen': self.player
                                    })
                        if self.battle_over == -1:
                            CardState.reset(CardState)
                            MeetingState.reset(MeetingState)
                            LootingState.reset(LootingState)
                            self.state_machine.Change('start', {
                            'chosen': self.player
                            })

        for index, enemy in enumerate(self.enemy.enemy_list):
            if self.current_fighter == 2 + index:
                if enemy.alive == True and self.player.alive == True:
                    self.action_cooldown += 1
                    if self.action_cooldown >= self.action_wait_time:
                        if enemy.enemy_type == "Normal" or enemy.enemy_type == "Miniboss":
                            enemy.attack(self.player)
                            if self.player.alive == False:
                                    self.battle_over = -1
                        elif enemy.enemy_type == "Boss":
                            if enemy.hp > int(enemy.max_hp*0.6):
                                enemy.attack(self.player)
                            else:
                                if enemy.is_skill2_use == False:
                                    enemy.skill_2(self.player)
                                    enemy.is_skill2_use = True
                                    self.enemy_turn_skill_2 = True
                                else:
                                    enemy.skill_1(self.player)
                            if self.player.alive == False:
                                    self.battle_over = -1
                        self.current_fighter += 1
                        self.action_cooldown = 0
                else:
                    self.current_fighter += 1
            else:
                if self.current_fighter > self.total_fighter:
                    if enemy.enemy_type == "Boss":
                        if enemy.is_skill2_use == True and self.enemy_turn_skill_2 == True:
                            if self.enemy_turn > 150:
                                self.enemy_turn_skill_2 = False
                                self.current_fighter = 1 
                                self.player.turn_count += 1
                                self.enemy_turn = 0
                            else:
                                self.enemy_turn += 1
                        else:
                            if self.enemy_turn > 80:
                                self.current_fighter = 1 
                                self.player.turn_count += 1
                                self.enemy_turn = 0
                            else:
                                self.enemy_turn += 1
                    else:
                        if self.enemy_turn > 80:
                            self.current_fighter = 1 
                            self.player.turn_count += 1
                            self.enemy_turn = 0
                        else:
                            self.enemy_turn += 1


        if self.player.action_count == 0:
            self.player.action_count = 3
            if self.player.skill_cooldown_1 > 0:
                self.player.skill_cooldown_1 -= 1
            if self.player.skill_cooldown_2 > 0:
                self.player.skill_cooldown_2 -= 1

        if self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].b_name == "Witch" and self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive == False:
                self.map = 98
                self.enemy.map_number = self.map
                self.enemy.generate_enemy() 
            
        if self.player.Class == "Wizard":
            if self.player.turn_count == 2 and self.player.is_use_skill2 == True:
                self.player.strength = self.player.original_str
                self.player.double_damage = False
            elif self.player.skill_cooldown_2 == 0:
                self.player.turn_count = 0

        self.is_enemy_alive()

    def is_enemy_alive(self):
        self.enemy_alive = len(self.enemy.enemy_list)
        self.action_cooldown += 1
        if self.action_cooldown >= self.action_wait_time:
            for enemy in self.enemy.enemy_list:
                if enemy.alive == False:
                    self.enemy_alive -= 1
            if self.enemy_alive == 0 and self.enemy.enemy_list[0].b_name == "Cthulu":
                self.battle_over = 1

    def render(self, screen):
        # make change
        #text generator
        if not self.generator.fully_displayed:
            self.generator.text_generation()
        if not self.generator2.fully_displayed:
            self.generator2.text_generation()
        if not self.generator3.fully_displayed:
            self.generator3.text_generation()
        if not self.generator4.fully_displayed:
            self.generator4.text_generation()

        screen.blit(self.bg_image, (0, 0))
        # fighter & health
        self.player.draw()
        self.playerHealth.draw(self.player.hp)
        self.player.update()

        self.enemy.render_enemy()
        self.enemy.draw_pointer_enemy()
        font = pygame.font.Font('./fonts/font.ttf', 30)
        # display battle menus
        self.battle_menu.display_fighting_menu()

        #display skill cooldown
        skill_1_cooldown = font.render(('CD: ('+str(self.player.skill_cooldown_1)+'turn)'), True, (255, 255, 255))
        screen.blit(skill_1_cooldown, (210, 320))

        skill_2_cooldown = font.render(('CD: ('+str(self.player.skill_cooldown_2)+'turn)'), True, (255, 255, 255))
        screen.blit(skill_2_cooldown, (210, 360))

        if self.enemy.enemy_list[0].evade == True:
            enemy_evade = self.small_font.render(('Enemy: Evade'), True, (0, 255, 0))
            screen.blit(enemy_evade, (self.enemy.enemy_list[0].x - 100, self.player.Y + 70))
        elif self.enemy.enemy_list[0].block == True:
            enemy_block = self.small_font.render(('Enemy: Block'), True, (0, 255, 0))
            screen.blit(enemy_block, (self.enemy.enemy_list[0].x - 100, self.player.Y + 70))
        elif self.enemy.enemy_list[0].double_damage == True:
            e_y = self.player.Y + 70
            if self.enemy.enemy_list[0].evade == True:
                e_y = self.player.Y + 90
            enemy_double = self.small_font.render(('Enemy: Damage x2'), True, (0, 255, 0))
            screen.blit(enemy_double, (self.enemy.enemy_list[0].x - 100, e_y))

        if self.player.evade == True:
            r_y = self.player.Y + 105
            if self.player.Class == "Rogue" and self.map == 12:
                r_y = self.player.Y + 85
            player_evade = self.small_font.render(('Player: Evade'), True, (0, 255, 0))
            screen.blit(player_evade, (self.player.X - 100, r_y))
        elif self.player.block == True:
            player_block = self.small_font.render(('Player: Block'), True, (0, 255, 0))
            screen.blit(player_block, (self.player.X - 100, self.player.Y + 70))
        if self.player.double_damage == True:
            if self.player.Class == "Wizard":
                player_double = self.small_font.render(('Player: Damage x1.5'), True, (0, 255, 0))
                screen.blit(player_double, (self.player.X - 100, self.player.Y + 85))
            if self.player.Class == "Rogue":
                d_y = self.player.Y + 85
                if self.map == 12:
                    d_y = self.player.Y + 65
                player_double = self.small_font.render(('Player: Damage x2'), True, (0, 255, 0))
                screen.blit(player_double, (self.player.X - 100, d_y))

        #display action count
        total_turn_text = font.render(('Action: '+str(self.player.action_count)), True, (255, 255, 255))
        screen.blit(total_turn_text, (50, HEIGHT - 70))

        #loading
        if self.loading > 70:
            self.player.reset_pos = False
            if self.loading > 80:
                pass
            else:
                self.loading+=1
        else:
            font  = pygame.font.Font('./fonts/font.ttf', 28)
            text = font.render('Loading...', True, (255, 255, 255))
            screen.blit(self.loading_bg_img, (0, 0))
            screen.blit(text, (WIDTH - 170, HEIGHT - 70))
            self.loading += 1

        if self.battle_over == 1:
            screen.blit(self.bg_image, (0, 0))
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

        elif self.battle_over == -1:
            screen.blit(self.bg_image, (0, 0))
            t_enter = gFonts['zelda'].render("Defeated"
                                             , False, (175, 53, 42))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 - 10))
            screen.blit(t_enter, rect)
            t_enter = self.small_font.render("You are pathetic"
                                             , False, (255, 255, 0))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 + 40))
            screen.blit(t_enter, rect)
            t_enter = self.small_font.render("Press 'Enter' to restart journey"
                                             , False, (255, 255, 0))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 + 80))
            screen.blit(t_enter, rect)

    def Exit(self):
        pass