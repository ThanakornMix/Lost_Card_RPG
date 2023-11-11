from src.states.BaseState import BaseState
import pygame, sys
from src.constants import *
from src.Dependencies import *
import random

#item
from src.world.items.DarkItem import DarkItem
from src.world.items.HolyItem import HolyItem
from src.world.items.PistolItem import PistolItem
from src.world.items.GravityItem import GravityItem

#text generator
from src.text_generator import TextGenerator
# make change
import random
class LootingState(BaseState):
    def __init__(self, state_machine):
        super(LootingState, self).__init__(state_machine)
        #background
        self.bg_door_image1 = pygame.image.load("./graphics/trove_room/door1.png")
        self.bg_door_image2 = pygame.image.load("./graphics/trove_room/door2.png")
        self.bg_door_image3 = pygame.image.load("./graphics/trove_room/door3.png")
        self.bg_door_image4 = pygame.image.load("./graphics/trove_room/door4.png")
        self.bg_door_image5 = pygame.image.load("./graphics/trove_room/door5.png")
        self.bg_trove_image1 = pygame.image.load("./graphics/trove_room/treasure_room1.png")
        self.bg_trove_image2 = pygame.image.load("./graphics/trove_room/treasure_room2.png")
        self.bg_trove_image3 = pygame.image.load("./graphics/trove_room/treasure_room3.png")
        self.bg_trove_image4 = pygame.image.load("./graphics/trove_room/treasure_room4.png")

        self.bg_door_list = [self.bg_door_image1, self.bg_door_image2,
                             self.bg_door_image3, self.bg_door_image4, self.bg_door_image5]
        self.bg_trove_list = [self.bg_trove_image1, self.bg_trove_image2, self.bg_trove_image3,
                              self.bg_trove_image4]

        #for reset position
        # chosen character for rogue and warrior
        self.playerResetR_X = WIDTH / 2 - 150
        self.playerResetR_Y = HEIGHT - HEIGHT / 3 - 20
        # for wizard
        self.playerResetRW_X = WIDTH / 2 - 200
        self.playerResetRW_Y = HEIGHT - HEIGHT / 3 - 30

        #for items
        #item location
        self.item_X = WIDTH / 2
        self.item_Y = HEIGHT - HEIGHT / 3
        #item_list
        self.item_list = [DarkItem(self.item_X, self.item_Y),
                          HolyItem(self.item_X, self.item_Y),
                          PistolItem(self.item_X, self.item_Y),
                          GravityItem(self.item_X, self.item_Y)]
        #current_item
        self.current_item = 0

        #sound
        self.unavailable_sound = gSounds['no-select']
        self.available_sound = gSounds['select']
        self.confirm_sound = gSounds['confirm']
        #text
        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
        self.medium_font = pygame.font.Font('./fonts/font.ttf', 48)
        #text generator
        font = pygame.font.Font('./fonts/font.ttf', 24)
        text = " The mysterious path has been discovered. Thou shalt not be consumed by greed"
        self.generator = TextGenerator(text, font, 50, HEIGHT / 2 + 200, 0.1, (255,0,255))

    def Enter(self, params):
        self.player = params['chosen']
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

        #item
        random.shuffle(self.item_list)
        self.item_1 = self.item_list[0]
        self.item_2 = self.item_list[1]
        self.item_3 = self.item_list[2]

        #sound
        gSounds['door-creaking'].play()
        gSounds['mystery_unfold'].play(-1)
        #backgroundshuffle
        random_number1 = random.randint(0,4)
        random_number2 = random.randint(0,3)
        self.background_door = self.bg_door_list[random_number1]
        self.background_trove = self.bg_trove_list[random_number2]
        self.bg_image = pygame.transform.scale(
            self.background_door, (WIDTH + 5, HEIGHT + 5))
        self.bg_image2 = pygame.transform.scale(
            self.background_trove, (WIDTH + 5, HEIGHT + 5))

        pass

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #select item
                if event.key == pygame.K_LEFT:
                    if self.current_item == 0:
                        self.unavailable_sound.play()
                    else:
                        self.available_sound.play()
                        self.current_item -= 1
                elif event.key == pygame.K_RIGHT:
                    if self.current_item == 2:
                        self.unavailable_sound.play()
                    else:
                        self.current_item += 1
                        self.available_sound.play()

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    #reset position
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
                    #reset text
                    self.generator.text_generation_reset()
                    #music
                    self.confirm_sound = gSounds['confirm']
                    gSounds['mystery_unfold'].stop()
                    # shuffle
                    self.state_machine.Change('roll', {
                        'chosen': self.player
                    })

    def render(self, screen):

        # text generation
        if not self.generator.fully_displayed:
            screen.blit(self.bg_image, (0, 0))
            self.generator.text_generation()
            # fully_displayed = self.generator.text_generation()

        #background2
        screen.blit(self.bg_image2, (0, 0))

        #text
        t_instruct = self.medium_font.render("Choose one relic (left right)", False, (255, 255, 255))
        rect = t_instruct.get_rect(center=(WIDTH / 2, HEIGHT / 4))
        screen.blit(t_instruct, rect)

        #render item
        if self.current_item == 0:
            self.item_1.draw()
            self.item_1.update()
        elif self.current_item == 1:
            self.item_2.draw()
            self.item_2.update()
        elif self.current_item == 2:
            self.item_3.draw()
            self.item_3.update()

    def Exit(self):
        pass