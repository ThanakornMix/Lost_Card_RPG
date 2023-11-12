from src.states.BaseState import BaseState
import pygame, sys

from src.constants import *
from src.Dependencies import *

# make change
from src.text_generator import TextGenerator
#chosen character
from src.world.Rogue import Rogue
from src.world.Warrior import Warrior
from src.world.Wizard import Wizard
#dice
import random

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class RollDiceState(BaseState):
    diceCurrentFace = 0
    def __init__(self, state_machine):
        super(RollDiceState, self).__init__(state_machine)
        self.bg_image = pygame.image.load("./graphics/backgroundCozy.png")
        self.bg_image = pygame.transform.scale(
            self.bg_image, (WIDTH + 5, HEIGHT + 5))

        #make change
        font = pygame.font.Font(None, 36)
        text = "Oh...Great being... Please roll the dice to accept the guidance of fate"
        self.generator = TextGenerator(text, font, 50, HEIGHT / 2 + 200)
        self.frame_index_witch = 0
        self.current_sprite_witch = 0
        #dice
        self.diceList = gDice_image_list
        self.diceCurrentFace = 0
        self.frame_index_dice = 0
        self.current_sprite_dice = 0
        self.dice_stop = False
        #sound
        self.confirm_sound = gSounds['confirm']
        #text above witch
        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)

        #loading BG
        self.loading = 0
        self.loading_bg_img = pygame.image.load("./graphics/loading_3.png")
        self.loading_bg_img = pygame.transform.scale(self.loading_bg_img, (WIDTH + 5, HEIGHT + 5))

    def Enter(self, params):
        #make change
        self.player = params['chosen']
        #sounds
        gSounds['late-hours'].play(-1)
        gSounds['campfire_fireplace'].play(-1)
        pass

    def GetDice(self):
        return (self.diceCurrentFace)

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #press to down stop dice
                if event.key == pygame.K_DOWN and not self.dice_stop:
                    
                    self.confirm_sound.play()
                    self.dice_stop = True
                    self.render(screen)
                    print("DiceCurrentFace is")
                    RollDiceState.diceCurrentFace = self.current_sprite_dice+1
                    print(RollDiceState.diceCurrentFace)
                    print("dice stop == true")
                    print("current dice")
                    print(self.current_sprite_dice)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if self.dice_stop:
                    # self.state_machine.Change('play')
                    self.dice_stop = False

                    self.generator.text_generation_reset()
                    #music
                    self.confirm_sound.play()
                    gSounds['campfire_fireplace'].stop()
                    gSounds['late-hours'].stop()
                    gSounds['burning_continue'].play(-1)
                    #gSounds['music'].play(-1)
                    # shuffle
                    pygame.time.delay(1000)
                    self.loading = 0
                    self.state_machine.Change('card', {
                        'chosen': self.player
                    })

    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        
        # witch
        if self.dice_stop:
            if self.current_sprite_witch >= len(gWitch2_image_list):
                self.current_sprite_witch = 0

            if self.frame_index_witch % 10 == 0:  # Change 5 to control animation speed
                self.current_sprite_witch += 1  # Update frame index
                if self.current_sprite_witch >= len(gWitch2_image_list):
                    self.current_sprite_witch = 0  # Reset frame index when it reaches the end

            # Display the current frame of the character image
            character_img = gWitch2_image_list[self.current_sprite_witch]
            screen.blit(character_img, (WIDTH / 2 - 96 + 16, HEIGHT - HEIGHT / 2 + 15))

            self.frame_index_witch += 1
        else:
            if self.current_sprite_witch >= len(gWitch_image_list):
                self.current_sprite_witch = 0

            if self.frame_index_witch % 5 == 0:  # Change 5 to control animation speed
                self.current_sprite_witch += 1  # Update frame index
                if self.current_sprite_witch >= len(gWitch_image_list):
                    self.current_sprite_witch = 0  # Reset frame index when it reaches the end

            # Display the current frame of the character image
            character_img = gWitch_image_list[self.current_sprite_witch]
            screen.blit(character_img, (WIDTH / 2 - 96, HEIGHT - HEIGHT / 2 + 15))

            self.frame_index_witch += 1

        # #text generation
        # if not self.generator.fully_displayed:
        #     self.generator.text_generation()
        #     #fully_displayed = self.generator.text_generation()
        # # chosen character
        # self.player.draw()
        # self.player.update()

        #text generation
        if not self.generator.fully_displayed:
            self.generator.text_generation()
            #fully_displayed = self.generator.text_generation()
        # chosen character
        self.player.draw()
        self.player.update()

        #dice
        if self.dice_stop:
            dice_img = pygame.transform.scale(self.diceList[self.diceCurrentFace], (100, 100))
            screen.blit(dice_img, (WIDTH / 2 - 100, HEIGHT - HEIGHT / 2 - 60))
            print(self.diceCurrentFace)
            
        else:
            # text above witch
            t_enter = self.small_font.render("Press 'down' to stop the dice", False, (255, 255, 255))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 - 10))
            screen.blit(t_enter, rect)

            if self.current_sprite_dice >= len(self.diceList):
                self.current_sprite_dice = 0

            if self.frame_index_dice % 5 == 0:  # Change 5 to control animation speed
                self.current_sprite_dice += 1  # Update frame index
                if self.current_sprite_dice >= len(self.diceList):
                    self.current_sprite_dice = 0  # Reset frame index when it reaches the end
                    print(self.current_sprite_dice)
            dice_img = pygame.transform.scale(self.diceList[self.current_sprite_dice], (100, 100))
            self.frame_index_dice += 1
        # Display the current frame of the character image
        #dice_img = pygame.transform.scale(self.diceList[self.current_sprite_dice], (100, 100))
            screen.blit(dice_img, (WIDTH / 2 - 80, HEIGHT - HEIGHT / 2 - 60))
        #self.frame_index_dice += 1

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

    def Exit(self):
        pass