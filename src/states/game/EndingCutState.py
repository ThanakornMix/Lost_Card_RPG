from src.states.BaseState import BaseState
import pygame, sys
from src.constants import *
from src.Dependencies import *
from src.states.game.CardState import *
# text generator
from src.text_generator import TextGenerator
# make change
import random
from src.states.game.MeetingState import MeetingState
from src.states.game.LootingState import LootingState


class EndingCutState(BaseState):
    def __init__(self, state_machine):
        super(EndingCutState, self).__init__(state_machine)
        # chosen character for rogue
        self.player_X = WIDTH / 2 - 150
        self.player_Y = HEIGHT - HEIGHT / 3 + 130
        # for wizard and warrior
        self.playerW_X = WIDTH / 2 - 200
        self.playerW_Y = HEIGHT - HEIGHT / 3 + 120
        # for reset position
        # chosen character for rogue and warrior
        self.playerResetR_X = WIDTH / 2 - 150
        self.playerResetR_Y = HEIGHT - HEIGHT / 3 - 20
        # for wizard
        self.playerResetRW_X = WIDTH / 2 - 200
        self.playerResetRW_Y = HEIGHT - HEIGHT / 3 - 30

        # sound
        self.unavailable_sound = gSounds['no-select']
        self.available_sound = gSounds['select']
        self.confirm_sound = gSounds['confirm']
        # text
        # text generator
        #
        font = pygame.font.Font('./fonts/font.ttf', 25)
        text = " I am for the promise... Thankyou for keeping it..."
        self.generator = TextGenerator(text, font, 50, HEIGHT / 2 - 100, 0.1, (255, 255, 255))
        text1 = " However, you must perish here..."
        self.generator1 = TextGenerator(text1, font, 50, HEIGHT / 2 - 50, 0.1, (255, 0, 0))
        text2 = " Foolish one"
        self.generator2 = TextGenerator(text2, font, 50, HEIGHT / 2, 0.1, (255, 255, 255))

        text3 = " Foolish one!! I, the Fate Demon, I curse thee!!"
        self.generator3 = TextGenerator(text3, font, 50, HEIGHT / 2 - 100, 0.1, (255, 255, 255))
        text4 = " Let there be blood and death upon thy path!!..."
        self.generator4 = TextGenerator(text4, font, 50, HEIGHT / 2 - 50, 0.1, (255, 255, 255))
        text5 = " Let there be blood and death upon thy path..."
        self.generator5 = TextGenerator(text5, font, 50, HEIGHT / 2 - 50, 0.1, (255, 0, 0))

        self.generator.skip_able = False
        self.generator1.skip_able = False
        self.generator2.skip_able = False
        self.generator3.skip_able = False
        self.generator4.skip_able = False
        self.generator5.skip_able = False


        # loading BG
        self.loading = 0
        self.loading_bg_img = pygame.image.load("./graphics/loading_5.png")
        self.loading_bg_img = pygame.transform.scale(self.loading_bg_img, (WIDTH + 5, HEIGHT + 5))

    def Enter(self, params):
        self.player = params['chosen']
        if self.player.Class == "Rogue":
            self.player.X = self.player_X
            self.player.Y = self.player_Y
        elif self.player.Class == "Warrior":
            self.player.X = self.playerW_X
            self.player.Y = self.playerW_Y
        elif self.player.Class == "Wizard":
            self.player.X = self.playerW_X
            self.player.Y = self.playerW_Y
        pass

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # select item
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_DOWN:
                    pass

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    # reset position

                    # reset text
                    # self.generator.text_generation_reset()
                    # shuffle
                    self.loading = 0
                    CardState.reset(CardState)
                    MeetingState.reset(MeetingState)
                    LootingState.reset(LootingState)
                    self.state_machine.Change('start', {
                    'chosen': self.player
                    })

    def render(self, screen):
        # text generator
        if self.player.acquired_joker is False:
            if not self.generator.fully_displayed:
                self.generator.text_generation()
            if not self.generator1.fully_displayed:
                self.generator1.text_generation()
            if not self.generator2.fully_displayed:
                self.generator2.text_generation()
        elif self.player.acquired_joker is True:
            if not self.generator3.fully_displayed:
                self.generator3.text_generation()
            if not self.generator4.fully_displayed:
                self.generator4.text_generation()
            if not self.generator5.fully_displayed:
                self.generator5.text_generation()

        # loading
        if self.loading > 70:
            self.player.reset_pos = False
        elif self.loading > 70 and self.player.reset_pos == False:
            pass
        else:
            font = pygame.font.Font('./fonts/font.ttf', 28)
            text = font.render('Loading...', True, (255, 255, 255))
            screen.blit(self.loading_bg_img, (0, 0))
            screen.blit(text, (WIDTH - 170, HEIGHT - 70))
            self.loading += 1

    def Exit(self):
        pass