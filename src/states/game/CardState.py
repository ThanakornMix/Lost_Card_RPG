from src.states.BaseState import BaseState
import pygame, sys
from src.constants import *
from src.Dependencies import *
from src.states.game.RollDiceState import *
# make change
#card
import random

class CardState(BaseState):
    current_step = 0
    current_card = 0
    level = 1
    level1 = [2,3,15,16,13,14]
    level2 = [4,5,17,18,39,40]
    level3 = [5,6,19,20,26,27]
    level4 = [7,8,21,22,0,1]
    heart = [28,29,30,31,32,33,34,35]
    diamond = [41,42,43,44,45,46,47,48]
    random.shuffle(heart)
    random.shuffle(diamond)
    current_list = level1
    for i in range(2):
        x = heart.pop()
        y = diamond.pop()
        level1.append(x)
        level1.append(y)
    for i in range(2):
        x = heart.pop()
        y = diamond.pop()
        level2.append(x)
        level2.append(y)
    for i in range(2):
        x = heart.pop()
        y = diamond.pop()
        level3.append(x)
        level3.append(y)
    for i in range(2):
        x = heart.pop()
        y = diamond.pop()
        level4.append(x)
        level4.append(y)
    random.shuffle(level1)
    random.shuffle(level2)
    random.shuffle(level3)
    random.shuffle(level4)
    level1.extend(range(23,26))
    level2.extend(range(49,52))
    level3.extend(range(36,39))
    level4.extend(range(10,13))
    level1.insert(0,0)
    level2.insert(0,0)
    level3.insert(0,0)
    level4.insert(0,0)
    heart = [28,29,30,31,32,33,34,35]
    diamond = [41,42,43,44,45,46,47,48]

    def __init__(self, state_machine):
        super(CardState, self).__init__(state_machine)
        self.bg_image = pygame.image.load("./graphics/backgroundCozyTable.png")
        self.bg_image = pygame.transform.scale(
            self.bg_image, (WIDTH + 5, HEIGHT + 5))
        self.current_sprite_flame = 0
        self.flameList = flame_image_list
        self.A2_list=[0,1,13,14,26,27,39,40]
        self.first_call = True

        self.current_stage = 0
        #current step
        self.player_X = WIDTH / 2 - 96
        self.player_Y = HEIGHT - HEIGHT / 3 + 70
        #card
        self.flameCurrentFace = 0
        self.cardList = gCard_image_list
        #random.shuffle(self.cardList)
        self.frame_index_flame = 0
        self.current_sprite_card = 0
        self.card_stop = False
        #sound
        self.confirm_sound = gSounds['burning_card']
        self.confirm_sound2 = gSounds['confirm']
        #text above witch
        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)

    def get_current_step(self):
        if self.first_call:
            CardState.current_step += RollDiceState.GetDice(RollDiceState)
            if CardState.current_step >= 12:
                CardState.current_step = 12
                self.first_call = False  # Update flag for subsequent calls
            return CardState.current_step
        else:
            CardState.current_step += RollDiceState.GetDice(RollDiceState)
            if CardState.current_step >= len(self.level1)-1:
                CardState.current_step = 13
                self.first_call = True # Update flag for subsequent calls
            return CardState.current_step

    def Enter(self, params):
        self.player = params['chosen']
        if self.player.Class == "Rogue":
            self.player.X = self.player_X
            self.player.Y = self.player_Y
        elif self.player.Class == "Warrior":
            self.player.X = self.player_X
            self.player.Y = self.player_Y
        elif self.player.Class == "Wizard":
            self.player.X = self.player_X
            self.player.Y = self.player_Y - 60


        if CardState.current_step==len(self.level1)-1:
            CardState.level += 1
            CardState.current_step = 0
            if CardState.level > 4:
                CardState.level = 1
            if CardState.level == 2:
                CardState.current_list = CardState.level2
            elif CardState.level == 3:
                CardState.current_list = CardState.level3
            elif CardState.level == 4:
                CardState.current_list = CardState.level4
            elif CardState.level == 1:
                CardState.current_list = CardState.level1
        
        self.current_stage+=RollDiceState.GetDice(RollDiceState)
        if self.current_stage >= 13 and self.level == 1:
            self.current_stage = 13
        elif self.current_stage >= 26 and self.level == 2:
            self.current_stage = 26
        elif self.current_stage >= 39 and self.level == 3:
            self.current_stage = 39
        elif self.current_stage >= 52 and self.level == 4:
            self.current_stage = 52

        pass

    def reset(self):
        self.current_step = 0
        self.current_card = 0
        self.current_stage = 0
        self.level = 1
        self.level1 = [2,3,15,16,13,14]
        self.level2 = [4,5,17,18,39,40]
        self.level3 = [5,6,19,20,26,27]
        self.level4 = [7,8,21,22,0,1]
        self.heart = [28,29,30,31,32,33,34,35]
        self.diamond = [41,42,43,44,45,46,47,48]
        random.shuffle(self.heart)
        random.shuffle(self.diamond)
        self.current_list = self.level1
        for i in range(2):
            x = self.heart.pop()
            y = self.diamond.pop()
            self.level1.append(x)
            self.level1.append(y)
        for i in range(2):
            x = self.heart.pop()
            y = self.diamond.pop()
            self.level2.append(x)
            self.level2.append(y)
        for i in range(2):
            x = self.heart.pop()
            y = self.diamond.pop()
            self.level3.append(x)
            self.level3.append(y)
        for i in range(2):
            x = self.heart.pop()
            y = self.diamond.pop()
            self.level4.append(x)
            self.level4.append(y)
        random.shuffle(self.level1)
        random.shuffle(self.level2)
        random.shuffle(self.level3)
        random.shuffle(self.level4)
        self.level1.extend(range(23,26))
        self.level2.extend(range(49,52))
        self.level3.extend(range(36,39))
        self.level4.extend(range(10,13))
        self.level1.insert(0,0)
        self.level2.insert(0,0)
        self.level3.insert(0,0)
        self.level4.insert(0,0)
        self.heart = [28,29,30,31,32,33,34,35]
        self.diamond = [41,42,43,44,45,46,47,48]

    def get_current_card(self):
        return(self.current_card)

    def get_level(self):
        return(self.level)

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #press to down stop card
                if event.key == pygame.K_DOWN and not self.card_stop:
                    CardState.current_step = self.get_current_step()
                    self.player.step_count = CardState.current_step
                    CardState.current_card = self.current_list[CardState.current_step]

                    self.confirm_sound.play()
                    gSounds['burning_continue'].stop()
                    self.card_stop = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN and self.card_stop:
                    # self.state_machine.Change('play')
                    self.card_stop = False
                    #music
                    self.confirm_sound2.play()
                    # shuffle
                    if self.current_list[CardState.current_step] in self.heart:
                        self.state_machine.Change('healing', {
                        'chosen': self.player
                        })
                    elif self.current_list[CardState.current_step] in self.diamond:
                        self.state_machine.Change('looting', {
                        'chosen': self.player
                        })
                    elif self.current_list[CardState.current_step] in self.A2_list:
                        self.state_machine.Change('meeting', {
                        'chosen': self.player
                        })
                    else:
                        self.state_machine.Change('battle', {
                            'chosen': self.player
                        })

    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        card_x1 = 0
        card_x2 = 0
        card_x3 = 0
        card_x4 = 0
        card_x5 = 0
        card_xOpen =0
        flame_x = 0

        if RollDiceState.GetDice(RollDiceState) == 1:
            card_x1 = 289
            card_x2 = 434
            card_x3 = 579
            card_x4 = 724
            card_x5 = 869
            card_xOpen = 144
            flame_x = 90
        elif RollDiceState.GetDice(RollDiceState) == 2:
            card_x1 = 144
            card_x2 = 434
            card_x3 = 579
            card_x4 = 724
            card_x5 = 869
            card_xOpen = 289
            flame_x = 235
        elif RollDiceState.GetDice(RollDiceState) == 3:
            card_x1 = 144
            card_x2 = 289
            card_x3 = 579
            card_x4 = 724
            card_x5 = 869
            card_xOpen = 434
            flame_x = 380
        elif RollDiceState.GetDice(RollDiceState) == 4:
            card_x1 = 144
            card_x2 = 289
            card_x3 = 434
            card_x4 = 724
            card_x5 = 869
            card_xOpen = 579
            flame_x = 525
        elif RollDiceState.GetDice(RollDiceState) == 5:
            card_x1 = 144
            card_x2 = 289
            card_x3 = 434
            card_x4 = 579
            card_x5 = 869
            card_xOpen = 724
            flame_x = 670
        elif RollDiceState.GetDice(RollDiceState) == 6:
            card_x1 = 144
            card_x2 = 289
            card_x3 = 434
            card_x4 = 579
            card_x5 = 724
            card_xOpen = 869
            flame_x = 815

        screen.blit(gCardBack_image_list[0],(card_x1,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(card_x2,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(card_x3,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(card_x4,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(card_x5,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(card_xOpen,HEIGHT-HEIGHT/2-200))

        if self.card_stop:
            screen.blit(self.cardList[self.current_list[CardState.current_step]], (card_xOpen, HEIGHT - HEIGHT / 2 - 200))
            t_enter = self.small_font.render("%d challenges to conquer thy fate (press 'Enter' to continue)" %(53-self.current_stage), False, (255, 255, 255))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 - 10))
            screen.blit(t_enter, rect)
        else:
            # text above witch
            if self.current_sprite_flame >= len(self.flameList):
                self.current_sprite_flame = 0

            if self.frame_index_flame % 8 == 0:  # Change 5 to control animation speed
                self.current_sprite_flame += 1  # Update frame index
                if self.current_sprite_flame >= len(self.flameList):
                    self.current_sprite_flame = 0  # Reset frame index when it reaches the end
            flame_img = pygame.transform.scale(self.flameList[self.current_sprite_flame], (300,300))
            self.frame_index_flame += 1
        # Display the current frame of the character image
        #flame_img = pygame.transform.scale(self.flameList[self.current_sprite_flame], (100, 100))
            screen.blit(flame_img, (flame_x, HEIGHT - HEIGHT / 2 - 300))
            t_enter = self.small_font.render("Press 'down' to burn the card of thy fate", False, (255, 255, 255))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 - 10))
            screen.blit(t_enter, rect)



        #card
    def Exit(self):
        pass