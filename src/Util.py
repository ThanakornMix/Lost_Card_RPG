import pygame
import json

def GenerateTiles(file_name, tile_width, tile_height, scale=3, colorkey=None):
    image = pygame.image.load(file_name)

    (img_width, img_height) = image.get_size()

    sheet_width = img_width//tile_width
    sheet_height = img_height//tile_height

    sheet_counter = 1
    tile_sheet = []

    for y in range(sheet_height):
        for x in range(sheet_width):
            tile = pygame.Surface((tile_width, tile_height))

            # surface, location, area of surface
            tile.blit(image, (0, 0), (x*tile_width, y*tile_height, tile_width, tile_height))

            # transparency
            if colorkey is not None:
                tile.set_colorkey(colorkey, pygame.RLEACCEL)

            tile = pygame.transform.scale(
                tile, (tile_width * scale, tile_height * scale)
            )

            tile_sheet.append(tile)

            sheet_counter += 1

    return tile_sheet

class Animation:
    def __init__(self, images, idleSprite=None, looping=True, interval_time=0.15):
        self.images = images
        self.timer = 0
        self.index = 0
        if idleSprite is None:
            self.image = self.images[self.index]
        else:
            self.image = idleSprite
        self.idleSprite = idleSprite

        self.interval_time = interval_time

        self.looping = looping #default loop

        self.times_played = 0

    def Refresh(self):
        self.timer=0
        self.index = 0
        self.times_played=0

    def update(self, dt):
        # one time animation check (attacking)
        if self.looping is False and self.times_played>0:
            return

        self.timer = self.timer + dt

        if self.timer > self.interval_time:
            self.timer = self.timer % self.interval_time

            self.index = (self.index+1) % len(self.images)
            #print(self.index)

            if self.index == 0:
                self.times_played += 1

        self.image = self.images[self.index]

    def Idle(self):
        self.image = self.idleSprite


class Sprite:
    def __init__(self, image, animation=None):
        self.image = image
        self.animation = animation

    def drawSprite(self, x, y, screen):
        dimensions = (x * 32, y * 32)
        if self.animation is None:
            screen.blit(self.image, dimensions)
        else:
            self.animation.update()
            screen.blit(self.animation.image, dimensions)


class SpriteManager:
    def __init__(self):
        self.spriteCollection = self.loadSprites(
            [
                #extra
                "./sprite/RogueAnimation.json",
                "./sprite/RogueAnimationIdle.json",
                "./sprite/WarriorAnimationIdle.json",
                "./sprite/WizardAnimationIdle.json",
                "./sprite/dice-roll-nobg.json",
                "./sprite/WitchAnimationIdle.json",
                "./sprite/WitchAnimationIdle2.json",
                #Rogue battle
                "./sprite/RogueAnimationBattleAttack.json",
                "./sprite/RogueAnimationBattleDead.json",
                "./sprite/RogueAnimationBattleIdle.json",
                "./sprite/RogueAnimationBattleSkill.json",
                "./sprite/RogueAnimationBattleHurt.json",
                "./sprite/RogueAnimationBattleSkill2.json",
                #Warrior battle
                "./sprite/WarriorAnimationBattleAttack.json",
                "./sprite/WarriorAnimationBattleIdle.json",
                "./sprite/WarriorAnimationBattleHurt.json",
                "./sprite/WarriorAnimationBattleDead.json",
                "./sprite/WarriorAnimationBattleSkill.json",
                "./sprite/WarriorAnimationBattleSkill2.json",
                #Wizard battle
                "./sprite/WizardAnimationBattleAttack.json",
                "./sprite/WizardAnimationBattleIdle.json",
                "./sprite/WizardAnimationBattleHurt.json",
                "./sprite/WizardAnimationBattleDead.json",
                "./sprite/WizardAnimationBattleSkill.json",
                #knight enemy battle
                "./sprite/KnightAnimationBattleAttack_level1.json",
                "./sprite/KnightAnimationBattleHurt1.json",
                "./sprite/KnightAnimationBattleidle.json",
                "./sprite/KnightAnimationBattleDeath1.json",
                "./sprite/KnightAnimationBattleDeathIdle1.json",
                #flame
                "./sprite/flame.json",
                #card
                "./sprite/cards.json",
                #water
                "./sprite/water_effect.json",
                "./sprite/water_effect2.json",

                #Every stage Jack
                "./sprite/NightBorneAnimationBattleIdle.json",
                "./sprite/NightBorneAnimationBattleAttack.json",
                "./sprite/NightBorneAnimationBattleDead.json",
                "./sprite/NightBorneAnimationBattleHurt.json",
                "./sprite/NightBorneAnimationBattleSkill.json",
                "./sprite/NightBorneAnimationBattleDeadIdle.json",

                #King of Spade
                "./sprite/MedKingAnimationBattleAttack.json",
                "./sprite/MedKingAnimationBattleIdle.json",
                "./sprite/MedKingAnimationBattleDeadIdle.json",
                "./sprite/MedKingAnimationBattleSkill.json",
                "./sprite/MedKingAnimationBattleDead.json",
                "./sprite/MedKingAnimationBattleHurt.json",
                "./sprite/MedKingAnimationBattleSkill2.json",

                #Club mob
                "./sprite/HuntressAnimationBattleHurt.json",
                "./sprite/HuntressAnimationBattleAttack.json",
                "./sprite/HuntressAnimationBattleIdle.json",
                "./sprite/HuntressAnimationBattleDeadIdle.json",
                "./sprite/HuntressAnimationBattleSkill.json",
                "./sprite/HuntressAnimationBattleDead.json",
                #Diamond mob
                "./sprite/UndeadAnimationBattleHurt.json",
                "./sprite/UndeadAnimationBattleAttack.json",
                "./sprite/UndeadAnimationBattleIdle.json",
                "./sprite/UndeadAnimationBattleDeadIdle.json",
                "./sprite/UndeadAnimationBattleSkill.json",
                "./sprite/UndeadAnimationBattleDead.json",
                #Spade mob
                "./sprite/HeroKnightAnimationBattleHurt.json",
                "./sprite/HeroKnightAnimationBattleAttack.json",
                "./sprite/HeroKnightAnimationBattleIdle.json",
                "./sprite/HeroKnightAnimationBattleDeadIdle.json",
                "./sprite/HeroKnightAnimationBattleSkill.json",
                "./sprite/HeroKnightAnimationBattleDead.json",

                #Queen of Club
                "./sprite/GroundMonkAnimationBattleAttack.json",
                "./sprite/GroundMonkAnimationBattleDead.json",
                "./sprite/GroundMonkAnimationBattleDeadIdle.json",
                "./sprite/GroundMonkAnimationBattleHurt.json",
                "./sprite/GroundMonkAnimationBattleIdle.json",
                "./sprite/GroundMonkAnimationBattleSkill.json",
                "./sprite/GroundMonkAnimationBattleSkill2.json",
                #Queen of Diamond
                "./sprite/BladekeeperAnimationBattleAttack.json",
                "./sprite/BladekeeperAnimationBattleDead.json",
                "./sprite/BladekeeperAnimationBattleDeadIdle.json",
                "./sprite/BladekeeperAnimationBattleHurt.json",
                "./sprite/BladekeeperAnimationBattleIdle.json",
                "./sprite/BladekeeperAnimationBattleSkill.json",
                "./sprite/BladekeeperAnimationBattleSkill2.json",
                #Queen of Heart
                "./sprite/SpearwomanAnimationBattleAttack.json",
                "./sprite/SpearwomanAnimationBattleDead.json",
                "./sprite/SpearwomanAnimationBattleDeadIdle.json",
                "./sprite/SpearwomanAnimationBattleHurt.json",
                "./sprite/SpearwomanAnimationBattleIdle.json",
                "./sprite/SpearwomanAnimationBattleSkill.json",
                "./sprite/SpearwomanAnimationBattleSkill2.json",
                #Queen of Spade
                "./sprite/WaterPriestessAnimationBattleAttack.json",
                "./sprite/WaterPriestessAnimationBattleDead.json",
                "./sprite/WaterPriestessAnimationBattleDeadIdle.json",
                "./sprite/WaterPriestessAnimationBattleHurt.json",
                "./sprite/WaterPriestessAnimationBattleIdle.json",
                "./sprite/WaterPriestessAnimationBattleSkill.json",
                "./sprite/WaterPriestessAnimationBattleSkill2.json",
                #King of Club
                "./sprite/RangerAnimationBattleAttack.json",
                "./sprite/RangerAnimationBattleDead.json",
                "./sprite/RangerAnimationBattleDeadIdle.json",
                "./sprite/RangerAnimationBattleHurt.json",
                "./sprite/RangerAnimationBattleIdle.json",
                "./sprite/RangerAnimationBattleSkill.json",
                "./sprite/RangerAnimationBattleSkill2.json",
                #King of Diamond
                "./sprite/HashashinAnimationBattleAttack.json",
                "./sprite/HashashinAnimationBattleDead.json",
                "./sprite/HashashinAnimationBattleDeadIdle.json",
                "./sprite/HashashinAnimationBattleHurt.json",
                "./sprite/HashashinAnimationBattleIdle.json",
                "./sprite/HashashinAnimationBattleSkill.json",
                "./sprite/HashashinAnimationBattleSkill2.json",
                #King of Heart
                "./sprite/FireKnightAnimationBattleAttack.json",
                "./sprite/FireKnightAnimationBattleDead.json",
                "./sprite/FireKnightAnimationBattleDeadIdle.json",
                "./sprite/FireKnightAnimationBattleHurt.json",
                "./sprite/FireKnightAnimationBattleIdle.json",
                "./sprite/FireKnightAnimationBattleSkill.json",
                "./sprite/FireKnightAnimationBattleSkill2.json",
                #undead
                "./sprite/UndeadAnimationBattleHurt.json",
                "./sprite/UndeadAnimationBattleAttack.json",
                "./sprite/UndeadAnimationBattleIdle.json",
                "./sprite/UndeadAnimationBattleDeadIdle.json",
                "./sprite/UndeadAnimationBattleSkill.json",
                "./sprite/UndeadAnimationBattleDead.json",
                #item
                "./sprite/item_sprite/Dark.json",
                "./sprite/item_sprite/Gravity.json",
                "./sprite/item_sprite/Holy.json",
                "./sprite/item_sprite/Pistol.json",
                "./sprite/item_sprite/ice.json",
                "./sprite/item_sprite/Thunder.json",
                "./sprite/item_sprite/Water.json",
                "./sprite/item_sprite/Joker.json",
                "./sprite/item_sprite/Sword.json",
                "./sprite/item_sprite/Scorpion.json",
                "./sprite/item_sprite/Worm.json",
                "./sprite/item_sprite/Spider.json",
                #demon hunter
                "./sprite/DhunterAnimationIdle.json",
                #skeleton
                "./sprite/SkeletonAnimationBattleAttack.json",
                "./sprite/SkeletonAnimationBattleDead.json",
                "./sprite/SkeletonAnimationBattleDeadIdle.json",
                "./sprite/SkeletonAnimationBattleHurt.json",
                "./sprite/SkeletonAnimationBattleIdle.json",
                "./sprite/SkeletonAnimationBattleSkill.json",
                #cthulu
                "./sprite/CthuluAnimationBattleHurt.json",
                "./sprite/CthuluAnimationBattleAttack.json",
                "./sprite/CthuluAnimationBattleIdle.json",
                "./sprite/CthuluAnimationBattleDeadIdle.json",
                "./sprite/CthuluAnimationBattleSkill.json",
                "./sprite/CthuluAnimationBattleSkill2.json",
                "./sprite/CthuluAnimationBattleDead.json",
                #witch
                "./sprite/WitchAnimationBattleHurt.json",
                "./sprite/WitchAnimationBattleAttack.json",
                "./sprite/WitchAnimationBattleIdle.json",
                "./sprite/WitchAnimationBattleDeadIdle.json",
                "./sprite/WitchAnimationBattleSkill.json",
                "./sprite/WitchAnimationBattleDead1.json",
                "./sprite/WitchAnimationBattleDead2.json"    
            ]
        )

    def loadSprites(self, urlList, shrink_scale=1):
        resDict = {}
        for url in urlList:
            with open(url) as jsonData:
                data = json.load(jsonData)
                mySpritesheet = SpriteSheet(data["spriteSheetURL"])
                dic = {}

                if data["type"] == "animation":
                    for sprite in data["sprites"]:
                        images = []
                        for image in sprite["images"]:
                            try:
                                xSize = sprite['xsize']
                                ySize = sprite['ysize']
                            except KeyError:
                                xSize, ySize = data['size']
                            images.append(
                                mySpritesheet.image_at(
                                    image["x"],
                                    image["y"],
                                    image["scale"],
                                    colorkey=-1, #sprite["colorKey"],
                                    xTileSize=xSize,
                                    yTileSize=ySize,
                                )
                            )
                        try:
                            idle_info = sprite['idle_image']
                            idle_img = mySpritesheet.image_at(
                                idle_info["x"],
                                idle_info["y"],
                                idle_info["scale"],
                                colorkey=-1,
                                xTileSize=xSize,
                                yTileSize=ySize
                            )
                        except KeyError:
                            idle_img = None
                        try:
                            loop = sprite['loop']
                        except KeyError:
                            loop = True

                        dic[sprite["name"]] = Sprite(
                            None,
                            animation=Animation(images, idleSprite=idle_img, looping=loop, interval_time=sprite["interval_time"]),
                        )

                    resDict.update(dic)
                    continue
                else:
                    for sprite in data["sprites"]:
                        try:
                            colorkey = sprite["colorKey"]
                        except KeyError:
                            colorkey = None
                        try:
                            xSize = sprite['xsize']
                            ySize = sprite['ysize']
                        except KeyError:
                            xSize, ySize = data['size']
                        dic[sprite["name"]] = Sprite(
                            mySpritesheet.image_at(
                                sprite["x"],
                                sprite["y"],
                                sprite["scalefactor"],#//shrink_scale,
                                colorkey,
                                xTileSize=xSize,
                                yTileSize=ySize,
                            ),
                        )
                    resDict.update(dic)
                    continue
        return resDict

class SpriteSheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename)
            self.sheet = pygame.image.load(filename)
            if not self.sheet.get_alpha():
                self.sheet.set_colorkey((0, 0, 0))
        except pygame.error:
            print("Unable to load spritesheet image:", filename)
            raise SystemExit

    def image_at(self, x, y, scalingfactor, colorkey=None,
                 xTileSize=16, yTileSize=16):
        rect = pygame.Rect((x, y, xTileSize, yTileSize))
        image = pygame.Surface(rect.size)
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return pygame.transform.scale(
            image, (xTileSize * scalingfactor, yTileSize * scalingfactor)
        )