from src.states.BaseState import BaseState
import pygame, sys
from src.constants import *
from src.Dependencies import *
from src.states.game.CardState import *
# text generator
from src.text_generator import TextGenerator
# make change
from src.world.demonhunter.FirstDemonHunter import FirstDemonHunter
from src.world.demonhunter.SecondDemonHunter import SecondDemonHunter
from src.world.demonhunter.ThirdDemonHunter import ThirdDemonHunter
from src.world.demonhunter.FourthDemonHunter import FourthDemonHunter
from src.world.demonhunter.FifthDemonHunter import FifthDemonHunter
from src.world.demonhunter.SixthDemonHunter import SixthDemonHunter
from src.world.demonhunter.SeventhDemonHunter import SeventhDemonHunter
from src.world.demonhunter.EightDemonHunter import EightDemonHunter
import random


class MeetingState(BaseState):
    def __init__(self, state_machine):
        super(MeetingState, self).__init__(state_machine)
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
        self.small_font = pygame.font.Font('./fonts/font.ttf', 20)
        # text generator
        font = pygame.font.Font('./fonts/font.ttf', 24)
        # first meet
        text = " What is your business with me, stranger?"
        # second meet
        text2 = " Fate is intriguing, is not it?"
        text3 = " What a surprise to meet you here, brother"
        # third meet
        text4 = " We keep running in to each other, stranger"
        text5 = " Brother. This place is beautiful, is not it?"
        # fourth meet
        text6 = " I wonder what fate stores for us, stranger"
        text7 = " The moon shines red likes the first time we met, brother"
        # fifth meet
        text8 = " You have found your way here eventually, stranger"
        text9 = " It seems you are stronger then last time we met, brother"
        # sixth meet
        text10 = " What do you want..., stranger"
        text11 = " Why is fate so cruel, brother..."
        # seventh meet
        text12 = " This might be the last time we meet, stranger"
        text13 = " Today is a good day to die, brother"
        # seventh meet
        text14 = "..."
        self.generator = TextGenerator(text, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator2 = TextGenerator(text2, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator3 = TextGenerator(text3, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator4 = TextGenerator(text4, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator5 = TextGenerator(text5, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator6 = TextGenerator(text6, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator7 = TextGenerator(text7, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator8 = TextGenerator(text8, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator9 = TextGenerator(text9, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator10 = TextGenerator(text10, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator11 = TextGenerator(text11, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator12 = TextGenerator(text12, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator13 = TextGenerator(text13, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        self.generator14 = TextGenerator(text14, font, 50, HEIGHT / 2, 0.1, (204, 204, 0))
        # demon hunter position
        self.item_X = WIDTH / 2 + 150
        self.item_Y = HEIGHT - HEIGHT / 3 + 100
        self.current_meeting = 0
        self.demonhunter_favor = 0

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

        # demon hunter call
        self.demonhunter_list = [FirstDemonHunter(self.item_X, self.item_Y, self.player),
                                 SecondDemonHunter(self.item_X, self.item_Y, self.player),
                                 ThirdDemonHunter(self.item_X, self.item_Y, self.player),
                                 FourthDemonHunter(self.item_X, self.item_Y, self.player),
                                 FifthDemonHunter(self.item_X, self.item_Y, self.player),
                                 SixthDemonHunter(self.item_X, self.item_Y, self.player),
                                 SeventhDemonHunter(self.item_X, self.item_Y, self.player),
                                 EightDemonHunter(self.item_X, self.item_Y, self.player)]
        self.demonhunter = self.demonhunter_list[self.current_meeting]
        # music
        if self.current_meeting == 0:
            gSounds['epic-orchestra'].play(-1)
        else:
            gSounds['sad-violin'].play(-1)

        pass

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # select item
                if event.key == pygame.K_LEFT and self.demonhunter.decision_complete is False:
                    if self.demonhunter.current_choice == 0:
                        self.unavailable_sound.play()
                    else:
                        self.available_sound.play()
                        self.demonhunter.current_choice -= 1
                elif event.key == pygame.K_RIGHT and self.demonhunter.decision_complete is False:
                    if self.demonhunter.current_choice == 1:
                        self.unavailable_sound.play()
                    else:
                        self.demonhunter.current_choice += 1
                        self.available_sound.play()

                if event.key == pygame.K_DOWN:
                    gSounds['confirm'].play()
                    self.demonhunter.decision_complete = True
                    self.demonhunter.selected_choice = self.demonhunter.current_choice

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN and self.demonhunter.decision_complete is True:
                    # reset position
                    if self.player.Class == "Rogue":
                        self.player.X = self.playerResetR_X
                        self.player.Y = self.playerResetR_X
                    elif self.player.Class == "Warrior":
                        self.player.X = self.playerResetR_X
                        self.player.Y = self.playerResetR_Y
                    elif self.player.Class == "Wizard":
                        self.player.X = self.playerResetRW_X
                        self.player.Y = self.playerResetRW_Y

                    self.player.reset()
                    self.player.draw()

                    # music
                    if self.current_meeting == 0:
                        gSounds['epic-orchestra'].stop()
                    else:
                        gSounds['sad-violin'].play(-1)

                    # demon hunter blessing
                    if self.demonhunter.selected_choice == 0:
                        self.demonhunter.action()
                        if self.current_meeting == 0 or self.current_meeting == 2:
                            self.demonhunter_favor += 1
                    if self.demonhunter.selected_choice == 1:
                        self.demonhunter.action2()
                    self.current_meeting += 1
                    self.demonhunter.decision_complete = False
                    if self.current_meeting == 8:
                        self.current_meeting = 7
                    # reset text
                    # self.generator.text_generation_reset()
                    # shuffle
                    self.loading = 0
                    self.state_machine.Change('roll', {
                        'chosen': self.player
                    })

    def render(self, screen):
        # text generation
        if self.current_meeting == 0:
            if not self.generator.fully_displayed:
                self.generator.text_generation()
                # fully_displayed = self.generator.text_generation()
        elif self.current_meeting == 1:
            if self.demonhunter_favor == 0:
                if not self.generator2.fully_displayed:
                    self.generator2.text_generation()
            elif self.demonhunter_favor > 0:
                if not self.generator3.fully_displayed:
                    self.generator3.text_generation()
        elif self.current_meeting == 2:
            if self.demonhunter_favor == 0:
                if not self.generator4.fully_displayed:
                    self.generator4.text_generation()
            elif self.demonhunter_favor > 0:
                if not self.generator5.fully_displayed:
                    self.generator5.text_generation()
        elif self.current_meeting == 3:
            if self.demonhunter_favor == 0:
                if not self.generator6.fully_displayed:
                    self.generator6.text_generation()
            elif self.demonhunter_favor > 0:
                if not self.generator7.fully_displayed:
                    self.generator7.text_generation()
        elif self.current_meeting == 4:
            if self.demonhunter_favor == 0:
                if not self.generator8.fully_displayed:
                    self.generator8.text_generation()
            elif self.demonhunter_favor > 0:
                if not self.generator9.fully_displayed:
                    self.generator9.text_generation()
        elif self.current_meeting == 5:
            if self.demonhunter_favor == 0:
                if not self.generator10.fully_displayed:
                    self.generator10.text_generation()
            elif self.demonhunter_favor > 0:
                if not self.generator11.fully_displayed:
                    self.generator11.text_generation()
        elif self.current_meeting == 6:
            if self.demonhunter_favor == 0:
                if not self.generator12.fully_displayed:
                    self.generator12.text_generation()
            elif self.demonhunter_favor > 0:
                if not self.generator13.fully_displayed:
                    self.generator13.text_generation()
        elif self.current_meeting == 7:
            if not self.generator14.fully_displayed:
                self.generator14.text_generation()

        # demonhunter draw
        self.demonhunter.draw()
        self.demonhunter.update()

        # chosen character
        self.player.draw()
        self.player.update()

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
