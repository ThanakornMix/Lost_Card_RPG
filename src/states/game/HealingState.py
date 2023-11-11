from src.states.BaseState import BaseState
import pygame, sys
from src.constants import *
from src.Dependencies import *

#text generator
from src.text_generator import TextGenerator
# make change
import random
class HealingState(BaseState):
    def __init__(self, state_machine):
        super(HealingState, self).__init__(state_machine)
        #background
        self.bg_image = pygame.image.load("./graphics/backgroundFountain1.png")
        self.bg_image2 = pygame.image.load("./graphics/backgroundFountain2.png")
        self.bg_image3 = pygame.image.load("./graphics/backgroundFountain3.png")
        self.bg_image = pygame.transform.scale(
            self.bg_image, (WIDTH + 5, HEIGHT + 5))
        self.bg_image2 = pygame.transform.scale(
            self.bg_image2, (WIDTH + 5, HEIGHT + 5))
        self.bg_image3 = pygame.transform.scale(
            self.bg_image3, (WIDTH + 5, HEIGHT + 5))
        self.background = [self.bg_image, self.bg_image2, self.bg_image3]

        # chosen character for rogue
        self.player_X = WIDTH / 2 - 150
        self.player_Y = HEIGHT - HEIGHT / 3 + 100
        # for wizard and warrior
        self.playerW_X = WIDTH / 2 - 200
        self.playerW_Y = HEIGHT - HEIGHT / 3 + 60
        #for reset position
        # chosen character for rogue and warrior
        self.playerResetR_X = WIDTH / 2 - 150
        self.playerResetR_Y = HEIGHT - HEIGHT / 3 - 20
        # for wizard
        self.playerResetRW_X = WIDTH / 2 - 200
        self.playerResetRW_Y = HEIGHT - HEIGHT / 3 - 30

        #water effect1
        self.waterList = gWaterSplash_image_list
        self.frame_index_water = 0
        self.current_sprite_water = 0
        # water effect2
        self.frame_index_water2 = 5
        self.current_sprite_water2 = 5
        # water effect3
        self.frame_index_water3 = 10
        self.current_sprite_water3 = 10

        #sound
        self.confirm_sound = gSounds['confirm']
        #text
        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
        #text generator
        font = pygame.font.Font('./fonts/font.ttf', 24)
        text = " The ethereal river has been discovered. The vitality surges within you"
        self.generator = TextGenerator(text, font, 50, HEIGHT / 2 + 200, 0.1, (204, 204, 0))

        #loading BG
        self.loading = 0
        self.loading_bg_img = pygame.image.load("./graphics/loading_4.png")
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
        #healing to full
        self.player.hp = self.player.max_hp
        #sound
        gSounds['water_droplets'].play(-1)
        gSounds['weird-mysterious'].play(-1)
        #backgroundshuffle
        random_number = random.randint(0,2)
        self.background_random = self.background[random_number]
        pass

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #press to down stop card
                if event.key == pygame.K_DOWN:
                    self.confirm_sound.play()
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
                    gSounds['water_droplets'].stop()
                    gSounds['weird-mysterious'].stop()
                    gSounds['late-hours'].play(-1)
                    gSounds['campfire_fireplace'].play(-1)
                    # shuffle
                    self.loading = 0
                    self.state_machine.Change('roll', {
                        'chosen': self.player
                    })

    def render(self, screen):
        screen.blit(self.background_random, (0, 0))

        # text generation
        if not self.generator.fully_displayed:
            self.generator.text_generation()
            # fully_displayed = self.generator.text_generation()

        #water effect1
        t_enter = self.small_font.render("Press 'Enter' to continue thy journey", False, (196, 180, 84))
        rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 - 10))
        screen.blit(t_enter, rect)

        if self.current_sprite_water >= len(self.waterList):
            self.current_sprite_water = 0

        if self.frame_index_water % 8 == 0:  # Change 5 to control animation speed
            self.current_sprite_water += 1  # Update frame index
            if self.current_sprite_water >= len(self.waterList):
                self.current_sprite_water = 0  # Reset frame index when it reaches the end

        water_img = gWaterSplash_image_list[self.current_sprite_water]
        self.frame_index_water += 1

        if self.current_sprite_water > 10:
            screen.blit(water_img, (WIDTH / 2 - 80, HEIGHT - HEIGHT / 2 - 245 + 300))
        else:
            screen.blit(water_img, (WIDTH / 2 - 80, HEIGHT - HEIGHT / 2 - 60 + 300))

        #water effect2
        if self.current_sprite_water2 >= len(self.waterList):
            self.current_sprite_water2 = 0

        if self.frame_index_water2 % 8 == 0:  # Change 5 to control animation speed
            self.current_sprite_water2 += 1  # Update frame index
            if self.current_sprite_water2 >= len(self.waterList):
                self.current_sprite_water2 = 0  # Reset frame index when it reaches the end

        water_img2 = gWaterSplash_image_list[self.current_sprite_water2]
        self.frame_index_water2 += 1

        if self.current_sprite_water2 > 10:
            screen.blit(water_img2, (WIDTH / 2 - 80 + 120, HEIGHT - HEIGHT / 2 - 245 + 250))
        else:
            screen.blit(water_img2, (WIDTH / 2 - 80 + 120, HEIGHT - HEIGHT / 2 - 60 + 250))

        #water effect3
        if self.current_sprite_water3 >= len(self.waterList):
            self.current_sprite_water3 = 0

        if self.frame_index_water3 % 8 == 0:  # Change 5 to control animation speed
            self.current_sprite_water3 += 1  # Update frame index
            if self.current_sprite_water3 >= len(self.waterList):
                self.current_sprite_water3 = 0  # Reset frame index when it reaches the end

        water_img3 = gWaterSplash_image_list[self.current_sprite_water3]
        self.frame_index_water3 += 1

        if self.current_sprite_water3 > 10:
            screen.blit(water_img3, (WIDTH / 2 - 80 - 120, HEIGHT - HEIGHT / 2 - 245 + 250))
        else:
            screen.blit(water_img3, (WIDTH / 2 - 80 - 120, HEIGHT - HEIGHT / 2 - 60 + 250))

        # chosen character
        self.player.draw()
        self.player.update()

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