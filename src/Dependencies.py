import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import StateMachine

sprite_collection = SpriteManager().spriteCollection

gRogue_animation_list = {"down": sprite_collection["rogue_walk_down"].animation,
                         "right": sprite_collection["rogue_walk_right"].animation,
                         "up": sprite_collection["rogue_walk_up"].animation,
                         "left": sprite_collection["rogue_walk_left"].animation
                         }


gRogue_image_list = [sprite_collection["rogue_1"].image, sprite_collection["rogue_2"].image,
                     sprite_collection["rogue_3"].image, sprite_collection["rogue_4"].image,
                     sprite_collection["rogue_5"].image, sprite_collection["rogue_6"].image,
                     sprite_collection["rogue_7"].image, sprite_collection["rogue_8"].image,
                     sprite_collection["rogue_9"].image, sprite_collection["rogue_10"].image,
                     sprite_collection["rogue_11"].image, sprite_collection["rogue_12"].image]

gWarrior_image_list = [sprite_collection["warrior_1"].image, sprite_collection["warrior_2"].image,
                    sprite_collection["warrior_3"].image, sprite_collection["warrior_4"].image,
                    sprite_collection["warrior_5"].image,sprite_collection["warrior_6"].image,
                    sprite_collection["warrior_7"].image]

gWizard_image_list = [sprite_collection["wizard_1"].image, sprite_collection["wizard_2"].image,
                    sprite_collection["wizard_3"].image, sprite_collection["wizard_4"].image,
                    sprite_collection["wizard_5"].image, sprite_collection["wizard_6"].image,
                    sprite_collection["wizard_7"].image, sprite_collection["wizard_8"].image]

gWitch_image_list = [sprite_collection["witch_charge_1"].image, sprite_collection["witch_charge_2"].image,
                    sprite_collection["witch_charge_3"].image, sprite_collection["witch_charge_4"].image,
                    sprite_collection["witch_charge_5"].image]

gWitch2_image_list = [sprite_collection["witch_idle_1"].image, sprite_collection["witch_idle_2"].image,
                    sprite_collection["witch_idle_3"].image, sprite_collection["witch_idle_4"].image,
                    sprite_collection["witch_idle_5"].image, sprite_collection["witch_idle_6"].image]

gDice_image_list = [sprite_collection["dice_face_1"].image, sprite_collection["dice_face_2"].image,
                    sprite_collection["dice_face_3"].image, sprite_collection["dice_face_4"].image,
                    sprite_collection["dice_face_5"].image,sprite_collection["dice_face_6"].image]

#warrior battle sprite
gWarriorBattleIdle_image_list = [sprite_collection["warrior_1_BI"].image, sprite_collection["warrior_2_BI"].image,
                               sprite_collection["warrior_3_BI"].image, sprite_collection["warrior_4_BI"].image,
                               sprite_collection["warrior_5_BI"].image, sprite_collection["warrior_6_BI"].image,
                               sprite_collection["warrior_7_BI"].image, sprite_collection["warrior_8_BI"].image,
                               sprite_collection["warrior_9_BI"].image, sprite_collection["warrior_10_BI"].image]

gWarriorBattleAttack_image_list = [sprite_collection["warrior_1"].image, sprite_collection["warrior_2"].image,
                                sprite_collection["warrior_3"].image, sprite_collection["warrior_4"].image,
                                sprite_collection["warrior_5"].image,sprite_collection["warrior_6"].image,
                                sprite_collection["warrior_7"].image]

gWarriorBattleSkill_image_list = [sprite_collection["warrior_1_BS"].image, sprite_collection["warrior_2_BS"].image,
                                sprite_collection["warrior_3_BS"].image, sprite_collection["warrior_4_BS"].image,
                                sprite_collection["warrior_5_BS"].image,sprite_collection["warrior_6_BS"].image,
                                sprite_collection["warrior_7_BS"].image,sprite_collection["warrior_8_BS"].image]

gWarriorBattleHurt_image_list = [sprite_collection["warrior_1_BH"].image, sprite_collection["warrior_2_BH"].image,
                                sprite_collection["warrior_3_BH"].image]

gWarriorBattleDead_image_list = [sprite_collection["warrior_1_BD"].image, sprite_collection["warrior_2_BD"].image,
                                sprite_collection["warrior_3_BD"].image, sprite_collection["warrior_4_BD"].image,
                                sprite_collection["warrior_5_BD"].image,sprite_collection["warrior_6_BD"].image,
                                sprite_collection["warrior_7_BD"].image]

gWarriorBattleSkill2_image_list = [sprite_collection["warrior_1_BS2"].image, sprite_collection["warrior_2_BS2"].image,
                                sprite_collection["warrior_3_BS2"].image, sprite_collection["warrior_4_BS2"].image,
                                sprite_collection["warrior_5_BS2"].image,sprite_collection["warrior_6_BS2"].image,
                                sprite_collection["warrior_7_BS2"].image]

gWarriorBattleDeadIdle_image_list = [sprite_collection["warrior_7_BD"].image, sprite_collection["warrior_7_BD"].image]

gWarriorBattle_image_list = [gWarriorBattleIdle_image_list, gWarriorBattleAttack_image_list, gWarriorBattleHurt_image_list,
                             gWarriorBattleDead_image_list, gWarriorBattleDeadIdle_image_list,gWarriorBattleSkill_image_list, 
                             gWarriorBattleSkill2_image_list]

#wizard battle sprite
gWizardBattleIdle_image_list = [sprite_collection["wizard_1_BI"].image, sprite_collection["wizard_2_BI"].image,
                    sprite_collection["wizard_3_BI"].image, sprite_collection["wizard_4_BI"].image,
                    sprite_collection["wizard_5_BI"].image, sprite_collection["wizard_6_BI"].image,
                    sprite_collection["wizard_7_BI"].image, sprite_collection["wizard_8_BI"].image]

gWizardBattleAttack_image_list = [sprite_collection["wizard_1_BA"].image, sprite_collection["wizard_2_BA"].image,
                    sprite_collection["wizard_3_BA"].image, sprite_collection["wizard_4_BA"].image,
                    sprite_collection["wizard_5_BA"].image, sprite_collection["wizard_6_BA"].image,
                    sprite_collection["wizard_7_BA"].image, sprite_collection["wizard_8_BA"].image]

gWizardBattleSkill_image_list = [sprite_collection["wizard_1_BS"].image, sprite_collection["wizard_2_BS"].image,
                    sprite_collection["wizard_3_BS"].image, sprite_collection["wizard_4_BS"].image,
                    sprite_collection["wizard_5_BS"].image, sprite_collection["wizard_6_BS"].image,
                    sprite_collection["wizard_7_BS"].image, sprite_collection["wizard_8_BS"].image]

gWizardBattleHurt_image_list = [sprite_collection["wizard_1_BH"].image, sprite_collection["wizard_2_BH"].image,
                    sprite_collection["wizard_3_BH"].image]

gWizardBattleDead_image_list = [sprite_collection["wizard_1_BD"].image, sprite_collection["wizard_2_BD"].image,
                    sprite_collection["wizard_3_BD"].image, sprite_collection["wizard_4_BD"].image,
                    sprite_collection["wizard_5_BD"].image, sprite_collection["wizard_6_BD"].image,
                    sprite_collection["wizard_7_BD"].image]

gWizardBattleDeadIdle_image_list = [sprite_collection["wizard_7_BD"].image, sprite_collection["wizard_7_BD"].image]

gWizardBattleSkill2_image_list = [sprite_collection["wizard_1_BD"].image, sprite_collection["wizard_2_BD"].image,
                                  sprite_collection["wizard_1_BD"].image, sprite_collection["wizard_2_BD"].image,
                                  sprite_collection["wizard_1_BD"].image, sprite_collection["wizard_2_BD"].image]

gWizardBattle_image_list = [gWizardBattleIdle_image_list, gWizardBattleAttack_image_list, gWizardBattleHurt_image_list,
                            gWizardBattleDead_image_list,gWizardBattleDeadIdle_image_list, gWizardBattleSkill_image_list,
                            gWizardBattleSkill2_image_list]

#rogue battle sprite
gRogueBattleIdle_image_list = [sprite_collection["rogue_1_BI"].image, sprite_collection["rogue_2_BI"].image,
                    sprite_collection["rogue_3_BI"].image, sprite_collection["rogue_4_BI"].image]

gRogueBattleAttack_image_list = [sprite_collection["rogue_1_BA"].image, sprite_collection["rogue_2_BA"].image,
                    sprite_collection["rogue_3_BA"].image, sprite_collection["rogue_4_BA"].image,
                    sprite_collection["rogue_5_BA"].image, sprite_collection["rogue_6_BA"].image,
                    sprite_collection["rogue_7_BA"].image, sprite_collection["rogue_8_BA"].image,
                    sprite_collection["rogue_9_BA"].image, sprite_collection["rogue_10_BA"].image]

gRogueBattleDead_image_list = [sprite_collection["rogue_1_BD"].image, sprite_collection["rogue_2_BD"].image,
                    sprite_collection["rogue_3_BD"].image, sprite_collection["rogue_4_BD"].image,
                    sprite_collection["rogue_5_BD"].image, sprite_collection["rogue_6_BD"].image,
                    sprite_collection["rogue_7_BD"].image]

gRogueBattleSkill_image_list = [sprite_collection["rogue_1_BS"].image, sprite_collection["rogue_2_BS"].image,
                    sprite_collection["rogue_3_BS"].image, sprite_collection["rogue_4_BS"].image,
                    sprite_collection["rogue_5_BS"].image, sprite_collection["rogue_6_BS"].image,
                    sprite_collection["rogue_7_BS"].image, sprite_collection["rogue_8_BS"].image,
                    sprite_collection["rogue_9_BS"].image]
gRogueBattleHurt_image_list = [sprite_collection["rogue_1_Hurt"].image, sprite_collection["rogue_2_Hurt"].image,
                    sprite_collection["rogue_3_Hurt"].image, sprite_collection["rogue_4_Hurt"].image,
                    sprite_collection["rogue_5_Hurt"].image]

gRogueBattleSkill2_image_list = [sprite_collection["rogue_1_BS2"].image, sprite_collection["rogue_2_BS2"].image,
                    sprite_collection["rogue_3_BS2"].image, sprite_collection["rogue_4_BS2"].image,
                    sprite_collection["rogue_5_BS2"].image, sprite_collection["rogue_6_BS2"].image,
                    sprite_collection["rogue_7_BS2"].image, sprite_collection["rogue_8_BS2"].image,
                    sprite_collection["rogue_9_BS2"].image, sprite_collection["rogue_10_BS2"].image]

gRogueBattle_image_list = [gRogueBattleIdle_image_list, gRogueBattleAttack_image_list, gRogueBattleHurt_image_list, gRogueBattleDead_image_list,
                           gRogueBattleDead_image_list, gRogueBattleSkill_image_list, gRogueBattleSkill2_image_list]
# end of rogue battle sprite

#knight1
gKnightBattleAttack_image_list = [sprite_collection["knight_1_BA"].image, sprite_collection["knight_2_BA"].image, 
                                  sprite_collection["knight_3_BA"].image, sprite_collection["knight_4_BA"].image,
                                  sprite_collection["knight_5_BA"].image]
gKnightBattleHurt_image_list = [sprite_collection["knight_1_Hurt"].image, sprite_collection["knight_2_Hurt"].image]
gKnightBattleIdle_image_list = [sprite_collection["knight_1_Idle"].image, sprite_collection["knight_2_Idle"].image]
gKnightBattleDead_image_list = [sprite_collection["knight_1_dead"].image, sprite_collection["knight_2_dead"].image,
                                sprite_collection["knight_3_dead"].image, sprite_collection["knight_4_dead"].image,
                                sprite_collection["knight_5_dead"].image, sprite_collection["knight_6_dead"].image]
gKnightBattleDeadIdle_image_list = [sprite_collection["knight_1_deadidle"].image,sprite_collection["knight_2_deadidle"].image]

gKnightBattle_image_list = [gKnightBattleIdle_image_list, gKnightBattleAttack_image_list, gKnightBattleHurt_image_list, 
                            gKnightBattleDead_image_list, gKnightBattleDeadIdle_image_list]
# end of knight1 battle sprite

#card
gCard_image_list=[sprite_collection["AS"].image, sprite_collection["2S"].image,
                    sprite_collection["3S"].image, sprite_collection["4S"].image,
                    sprite_collection["5S"].image, sprite_collection["6S"].image,
                    sprite_collection["7S"].image, sprite_collection["8S"].image,
                    sprite_collection["9S"].image, sprite_collection["10S"].image,
                    sprite_collection["JS"].image, sprite_collection["QS"].image,
                    sprite_collection["KS"].image,
                    sprite_collection["AC"].image, sprite_collection["2C"].image,
                    sprite_collection["3C"].image, sprite_collection["4C"].image,
                    sprite_collection["5C"].image, sprite_collection["6C"].image,
                    sprite_collection["7C"].image, sprite_collection["8C"].image,
                    sprite_collection["9C"].image, sprite_collection["10C"].image,
                    sprite_collection["JC"].image, sprite_collection["QC"].image,
                    sprite_collection["KC"].image,
                    sprite_collection["AH"].image, sprite_collection["2H"].image,
                    sprite_collection["3H"].image, sprite_collection["4H"].image,
                    sprite_collection["5H"].image, sprite_collection["6H"].image,
                    sprite_collection["7H"].image, sprite_collection["8H"].image,
                    sprite_collection["9H"].image, sprite_collection["10H"].image,
                    sprite_collection["JH"].image, sprite_collection["QH"].image,
                    sprite_collection["KH"].image,
                    sprite_collection["AD"].image, sprite_collection["2D"].image,
                    sprite_collection["3D"].image, sprite_collection["4D"].image,
                    sprite_collection["5D"].image, sprite_collection["6D"].image,
                    sprite_collection["7D"].image, sprite_collection["8D"].image,
                    sprite_collection["9D"].image, sprite_collection["10D"].image,
                    sprite_collection["JD"].image, sprite_collection["QD"].image,
                    sprite_collection["KD"].image,
                    ]
gCardBack_image_list=[sprite_collection["cardBack"].image]
#card end

#flame
flame_image_list=[sprite_collection["flame_1"].image, sprite_collection["flame_2"].image,
                    sprite_collection["flame_3"].image, sprite_collection["flame_4"].image,
                    sprite_collection["flame_5"].image, sprite_collection["flame_6"].image,
                    sprite_collection["flame_7"].image,sprite_collection["flame_8"].image,
                    sprite_collection["flame_9"].image,]
#water
gWaterSplash_image_list = [sprite_collection["waterstart_1"].image, sprite_collection["waterstart_2"].image,
                    sprite_collection["waterstart_3"].image, sprite_collection["waterstart_4"].image,
                    sprite_collection["waterstart_5"].image, sprite_collection["waterstart_6"].image,
                    sprite_collection["waterstart_7"].image, sprite_collection["waterstart_8"].image,
                    sprite_collection["waterstart_9"].image, sprite_collection["waterstart_10"].image,
                    sprite_collection["waterstart_11"].image, sprite_collection["watersplash_1"].image,
                    sprite_collection["watersplash_2"].image, sprite_collection["watersplash_3"].image,
                    sprite_collection["watersplash_4"].image, sprite_collection["watersplash_5"].image,
                    sprite_collection["watersplash_6"].image, sprite_collection["watersplash_7"].image,
                    sprite_collection["watersplash_8"].image]
#Demon hunter sprite
gDhunter_image_list = [sprite_collection["dhunter_1_BI"].image, sprite_collection["dhunter_2_BI"].image,
                    sprite_collection["dhunter_3_BI"].image, sprite_collection["dhunter_4_BI"].image]



#NightBorne sprite Every stage Jack
gNightBorneBattleIdle_image_list = [sprite_collection["nightborne_1_BI"].image, sprite_collection["nightborne_2_BI"].image,
                    sprite_collection["nightborne_3_BI"].image, sprite_collection["nightborne_4_BI"].image,
                    sprite_collection["nightborne_5_BI"].image, sprite_collection["nightborne_6_BI"].image,
                    sprite_collection["nightborne_7_BI"].image, sprite_collection["nightborne_8_BI"].image,
                    sprite_collection["nightborne_9_BI"].image]

gNightBorneBattleAttack_image_list = [sprite_collection["nightborne_1_BA"].image, sprite_collection["nightborne_2_BA"].image,
                    sprite_collection["nightborne_3_BA"].image, sprite_collection["nightborne_4_BA"].image,
                    sprite_collection["nightborne_5_BA"].image, sprite_collection["nightborne_6_BA"].image,
                    sprite_collection["nightborne_7_BA"].image, sprite_collection["nightborne_8_BA"].image,
                    sprite_collection["nightborne_9_BA"].image, sprite_collection["nightborne_10_BA"].image,
                    sprite_collection["nightborne_11_BA"].image, sprite_collection["nightborne_12_BA"].image]

gNightBorneBattleHurt_image_list = [sprite_collection["nightborne_1_BH"].image, sprite_collection["nightborne_2_BH"].image,
                    sprite_collection["nightborne_3_BH"].image, sprite_collection["nightborne_4_BH"].image,
                    sprite_collection["nightborne_5_BH"].image]

gNightBorneBattleDead_image_list = [sprite_collection["nightborne_1_BD"].image, sprite_collection["nightborne_2_BD"].image,
                    sprite_collection["nightborne_3_BD"].image, sprite_collection["nightborne_4_BD"].image,
                    sprite_collection["nightborne_5_BD"].image, sprite_collection["nightborne_6_BD"].image,
                    sprite_collection["nightborne_7_BD"].image, sprite_collection["nightborne_8_BD"].image,
                    sprite_collection["nightborne_9_BD"].image, sprite_collection["nightborne_10_BD"].image,
                    sprite_collection["nightborne_11_BD"].image, sprite_collection["nightborne_12_BD"].image,
                    sprite_collection["nightborne_13_BD"].image, sprite_collection["nightborne_14_BD"].image,
                    sprite_collection["nightborne_15_BD"].image, sprite_collection["nightborne_16_BD"].image,
                    sprite_collection["nightborne_17_BD"].image, sprite_collection["nightborne_18_BD"].image,
                    sprite_collection["nightborne_19_BD"].image, sprite_collection["nightborne_20_BD"].image,
                    sprite_collection["nightborne_21_BD"].image, sprite_collection["nightborne_22_BD"].image,
                    sprite_collection["nightborne_23_BD"].image, sprite_collection["nightborne_24_BD"].image]

gNightBorneBattleSkill_image_list = [sprite_collection["nightborne_1_BS"].image, sprite_collection["nightborne_2_BS"].image,
                    sprite_collection["nightborne_3_BS"].image, sprite_collection["nightborne_4_BS"].image,
                    sprite_collection["nightborne_5_BS"].image, sprite_collection["nightborne_6_BS"].image,
                    sprite_collection["nightborne_1_BS"].image, sprite_collection["nightborne_2_BS"].image,
                    sprite_collection["nightborne_3_BS"].image, sprite_collection["nightborne_4_BS"].image,
                    sprite_collection["nightborne_5_BS"].image, sprite_collection["nightborne_6_BS"].image]

gNightBorneBattleDeadIdle_image_list = [sprite_collection["nightborne_24_BD"].image, sprite_collection["nightborne_24_BD"].image]

gNightBorneBattle_image_list = [gNightBorneBattleIdle_image_list, gNightBorneBattleAttack_image_list, gNightBorneBattleHurt_image_list,
                              gNightBorneBattleDead_image_list, gNightBorneBattleDeadIdle_image_list, gNightBorneBattleSkill_image_list]



#Medieval King
gMedKingBattleIdle_image_list = [sprite_collection["medking_1_BI"].image, sprite_collection["medking_2_BI"].image,
                   sprite_collection["medking_3_BI"].image, sprite_collection["medking_4_BI"].image,
                    sprite_collection["medking_5_BI"].image, sprite_collection["medking_6_BI"].image,
                    sprite_collection["medking_7_BI"].image, sprite_collection["medking_8_BI"].image]

gMedKingBattleAttack_image_list = [sprite_collection["medking_1_BA"].image, sprite_collection["medking_2_BA"].image,
                    sprite_collection["medking_3_BA"].image, sprite_collection["medking_4_BA"].image]

gMedKingBattleSkill_image_list = [sprite_collection["medking_1_BS"].image, sprite_collection["medking_2_BS"].image,
                    sprite_collection["medking_3_BS"].image, sprite_collection["medking_4_BS"].image]

gMedKingBattleHurt_image_list = [sprite_collection["medking_1_BH"].image, sprite_collection["medking_2_BH"].image,
                    sprite_collection["medking_3_BH"].image]

gMedKingBattleDead_image_list = [sprite_collection["medking_1_BD"].image, sprite_collection["medking_2_BD"].image,
                    sprite_collection["medking_3_BD"].image, sprite_collection["medking_4_BD"].image,
                    sprite_collection["medking_5_BD"].image, sprite_collection["medking_6_BD"].image]

gMedKingBattleDeadIdle_image_list = [sprite_collection["medking_6_BD"].image, sprite_collection["medking_6_BD"].image]

gMedKingBattleSkill2_image_list = [sprite_collection["medking_1_BS2"].image, sprite_collection["medking_2_BS2"].image,
                    sprite_collection["medking_3_BS2"].image, sprite_collection["medking_4_BS2"].image]

gMedKingBattle_image_list = [gMedKingBattleIdle_image_list, gMedKingBattleAttack_image_list, gMedKingBattleHurt_image_list,
                             gMedKingBattleDead_image_list, gMedKingBattleDeadIdle_image_list, gMedKingBattleSkill_image_list, 
                             gMedKingBattleSkill2_image_list]

#Huntress Stage1 mob
gHuntressBattleIdle_image_list = [sprite_collection["huntress_1_BI"].image, sprite_collection["huntress_2_BI"].image,
                    sprite_collection["huntress_3_BI"].image, sprite_collection["huntress_4_BI"].image,
                    sprite_collection["huntress_5_BI"].image, sprite_collection["huntress_6_BI"].image,
                    sprite_collection["huntress_7_BI"].image, sprite_collection["huntress_8_BI"].image]

gHuntressBattleAttack_image_list = [sprite_collection["huntress_1_BA"].image, sprite_collection["huntress_2_BA"].image,
                    sprite_collection["huntress_3_BA"].image, sprite_collection["huntress_4_BA"].image,
                    sprite_collection["huntress_5_BA"].image]

gHuntressBattleSkill_image_list = [sprite_collection["huntress_1_BS"].image, sprite_collection["huntress_2_BS"].image,
                    sprite_collection["huntress_3_BS"].image, sprite_collection["huntress_4_BS"].image,
                    sprite_collection["huntress_5_BS"].image, sprite_collection["huntress_6_BS"].image,
                    sprite_collection["huntress_7_BS"].image, sprite_collection["huntress_7_BS"].image,
                    sprite_collection["huntress_1_BI"].image]

gHuntressBattleHurt_image_list = [sprite_collection["huntress_1_BH"].image, sprite_collection["huntress_2_BH"].image,
                    sprite_collection["huntress_3_BH"].image]

gHuntressBattleDead_image_list = [sprite_collection["huntress_1_BD"].image, sprite_collection["huntress_2_BD"].image,
                    sprite_collection["huntress_3_BD"].image, sprite_collection["huntress_4_BD"].image,
                    sprite_collection["huntress_5_BD"].image, sprite_collection["huntress_6_BD"].image,
                    sprite_collection["huntress_7_BD"].image, sprite_collection["huntress_8_BD"].image]

gHuntressBattleDeadIdle_image_list = [sprite_collection["huntress_8_BD"].image, sprite_collection["huntress_8_BD"].image]

gHuntressBattle_image_list = [gHuntressBattleIdle_image_list, gHuntressBattleAttack_image_list, gHuntressBattleHurt_image_list,
                             gHuntressBattleDead_image_list, gHuntressBattleSkill_image_list]

#Heroknight sprite stage4 mob
gHeroknightBattleIdle_image_list = [sprite_collection["heroknight_1_BI"].image, sprite_collection["heroknight_2_BI"].image,
                    sprite_collection["heroknight_3_BI"].image, sprite_collection["heroknight_4_BI"].image,
                    sprite_collection["heroknight_5_BI"].image, sprite_collection["heroknight_6_BI"].image,
                    sprite_collection["heroknight_7_BI"].image, sprite_collection["heroknight_8_BI"].image,
                    sprite_collection["heroknight_9_BI"].image, sprite_collection["heroknight_10_BI"].image,
                    sprite_collection["heroknight_11_BI"].image]

gHeroknightBattleAttack_image_list = [sprite_collection["heroknight_1_BA"].image, sprite_collection["heroknight_2_BA"].image,
                    sprite_collection["heroknight_3_BA"].image, sprite_collection["heroknight_4_BA"].image,
                    sprite_collection["heroknight_5_BA"].image, sprite_collection["heroknight_6_BA"].image,
                    sprite_collection["heroknight_7_BA"].image]

gHeroknightBattleDead_image_list = [sprite_collection["heroknight_1_BD"].image, sprite_collection["heroknight_2_BD"].image,
                    sprite_collection["heroknight_3_BD"].image, sprite_collection["heroknight_4_BD"].image,
                    sprite_collection["heroknight_5_BD"].image, sprite_collection["heroknight_6_BD"].image,
                    sprite_collection["heroknight_7_BD"].image, sprite_collection["heroknight_8_BD"].image,
                    sprite_collection["heroknight_9_BD"].image, sprite_collection["heroknight_10_BD"].image,
                    sprite_collection["heroknight_11_BD"].image]

gHeroknightBattleDeadIdle_image_list = [sprite_collection["heroknight_11_BD"].image, sprite_collection["heroknight_11_BD"].image]

gHeroknightBattleSkill_image_list = [sprite_collection["heroknight_1_BS"].image, sprite_collection["heroknight_2_BS"].image,
                    sprite_collection["heroknight_3_BS"].image, sprite_collection["heroknight_4_BS"].image,
                    sprite_collection["heroknight_5_BS"].image, sprite_collection["heroknight_6_BS"].image,
                    sprite_collection["heroknight_7_BS"].image]

gHeroknightBattleHurt_image_list = [sprite_collection["heroknight_1_BH"].image, sprite_collection["heroknight_2_BH"].image,
                    sprite_collection["heroknight_3_BH"].image, sprite_collection["heroknight_4_BH"].image]

gHeroknightBattle_image_list = [gHeroknightBattleIdle_image_list, gHeroknightBattleAttack_image_list, gHeroknightBattleHurt_image_list,
                              gHeroknightBattleDead_image_list, gHeroknightBattleSkill_image_list]

#Undead Executioner sprite stage2 mob
gUndeadBattleIdle_image_list = [sprite_collection["undead_1_BI"].image, sprite_collection["undead_2_BI"].image,
                    sprite_collection["undead_3_BI"].image, sprite_collection["undead_4_BI"].image,
                    sprite_collection["undead_5_BI"].image, sprite_collection["undead_6_BI"].image,
                    sprite_collection["undead_7_BI"].image, sprite_collection["undead_8_BI"].image]

gUndeadBattleAttack_image_list = [sprite_collection["undead_1_BA"].image, sprite_collection["undead_2_BA"].image,
                    sprite_collection["undead_3_BA"].image, sprite_collection["undead_4_BA"].image,
                    sprite_collection["undead_5_BA"].image, sprite_collection["undead_6_BA"].image,
                    sprite_collection["undead_7_BA"].image, sprite_collection["undead_8_BA"].image,
                    sprite_collection["undead_9_BA"].image, sprite_collection["undead_10_BA"].image,
                    sprite_collection["undead_11_BA"].image, sprite_collection["undead_12_BA"].image,
                    sprite_collection["undead_13_BA"].image]

gUndeadBattleDead_image_list = [sprite_collection["undead_1_BD"].image, sprite_collection["undead_2_BD"].image,
                    sprite_collection["undead_3_BD"].image, sprite_collection["undead_4_BD"].image,
                    sprite_collection["undead_5_BD"].image, sprite_collection["undead_6_BD"].image,
                    sprite_collection["undead_7_BD"].image, sprite_collection["undead_8_BD"].image,
                    sprite_collection["undead_9_BD"].image, sprite_collection["undead_10_BD"].image,
                    sprite_collection["undead_11_BD"].image, sprite_collection["undead_12_BD"].image,
                    sprite_collection["undead_13_BD"].image, sprite_collection["undead_14_BD"].image,
                    sprite_collection["undead_15_BD"].image, sprite_collection["undead_16_BD"].image,
                    sprite_collection["undead_17_BD"].image, sprite_collection["undead_18_BD"].image,
                    sprite_collection["undead_19_BD"].image]

gUndeadBattleDeadIdle_image_list = [sprite_collection["undead_19_BD"].image, sprite_collection["undead_19_BD"].image]

gUndeadBattleSkill_image_list = [sprite_collection["undead_1_BS"].image, sprite_collection["undead_2_BS"].image,
                    sprite_collection["undead_3_BS"].image, sprite_collection["undead_4_BS"].image,
                    sprite_collection["undead_5_BS"].image, sprite_collection["undead_6_BS"].image,
                    sprite_collection["undead_7_BS"].image, sprite_collection["undead_8_BS"].image,
                    sprite_collection["undead_9_BS"].image, sprite_collection["undead_10_BS"].image,
                    sprite_collection["undead_11_BS"].image, sprite_collection["undead_12_BS"].image]

gUndeadBattleHurt_image_list = [sprite_collection["undead_1_BH"].image, sprite_collection["undead_2_BH"].image,
                    sprite_collection["undead_5_BH"].image, sprite_collection["undead_3_BH"].image,
                    sprite_collection["undead_4_BH"].image]

gUndeadBattle_image_list = [gUndeadBattleIdle_image_list, gUndeadBattleAttack_image_list, gUndeadBattleHurt_image_list,
                              gUndeadBattleDead_image_list, gUndeadBattleSkill_image_list]

#Cthulu sprite Secret boss
gCthuluBattleIdle_image_list = [sprite_collection["cthulu_1_BI"].image, sprite_collection["cthulu_2_BI"].image,
                    sprite_collection["cthulu_3_BI"].image, sprite_collection["cthulu_4_BI"].image,
                    sprite_collection["cthulu_5_BI"].image, sprite_collection["cthulu_6_BI"].image,
                    sprite_collection["cthulu_7_BI"].image, sprite_collection["cthulu_8_BI"].image,
                    sprite_collection["cthulu_9_BI"].image, sprite_collection["cthulu_10_BI"].image,
                    sprite_collection["cthulu_11_BI"].image, sprite_collection["cthulu_12_BI"].image,
                    sprite_collection["cthulu_13_BI"].image, sprite_collection["cthulu_14_BI"].image,
                    sprite_collection["cthulu_15_BI"].image]

gCthuluBattleAttack_image_list = [sprite_collection["cthulu_1_BA"].image, sprite_collection["cthulu_2_BA"].image,
                    sprite_collection["cthulu_3_BA"].image, sprite_collection["cthulu_4_BA"].image,
                    sprite_collection["cthulu_5_BA"].image, sprite_collection["cthulu_6_BA"].image,
                    sprite_collection["cthulu_7_BA"].image]

gCthuluBattleDead_image_list = [sprite_collection["cthulu_1_BD"].image, sprite_collection["cthulu_2_BD"].image,
                    sprite_collection["cthulu_3_BD"].image, sprite_collection["cthulu_4_BD"].image,
                    sprite_collection["cthulu_5_BD"].image, sprite_collection["cthulu_6_BD"].image,
                    sprite_collection["cthulu_7_BD"].image, sprite_collection["cthulu_8_BD"].image,
                    sprite_collection["cthulu_9_BD"].image, sprite_collection["cthulu_10_BD"].image,
                    sprite_collection["cthulu_11_BD"].image]

gCthuluBattleDeadIdle_image_list = [sprite_collection["cthulu_11_BD"].image, sprite_collection["cthulu_11_BD"].image]

gCthuluBattleSkill_image_list = [sprite_collection["cthulu_1_BS"].image, sprite_collection["cthulu_2_BS"].image,
                    sprite_collection["cthulu_3_BS"].image, sprite_collection["cthulu_4_BS"].image,
                    sprite_collection["cthulu_5_BS"].image, sprite_collection["cthulu_6_BS"].image,
                    sprite_collection["cthulu_7_BS"].image, sprite_collection["cthulu_8_BS"].image,
                    sprite_collection["cthulu_9_BS"].image]

gCthuluBattleSkill2_image_list = [sprite_collection["cthulu_1_BS2"].image, sprite_collection["cthulu_2_BS2"].image,
                    sprite_collection["cthulu_3_BS2"].image, sprite_collection["cthulu_4_BS2"].image,
                    sprite_collection["cthulu_5_BS2"].image, sprite_collection["cthulu_6_BS2"].image]

gCthuluBattleHurt_image_list = [sprite_collection["cthulu_1_BH"].image, sprite_collection["cthulu_2_BH"].image,
                    sprite_collection["cthulu_3_BH"].image, sprite_collection["cthulu_4_BH"].image,
                    sprite_collection["cthulu_5_BH"].image]

gCthuluBattle_image_list = [gCthuluBattleIdle_image_list, gCthuluBattleAttack_image_list, gCthuluBattleHurt_image_list,
                            gCthuluBattleDead_image_list, gCthuluBattleDeadIdle_image_list, gCthuluBattleSkill_image_list, gCthuluBattleSkill2_image_list]

#Witch sprite
gWitchBattleIdle_image_list = [sprite_collection["witch_1_BI"].image, sprite_collection["witch_1_BI"].image,
                    sprite_collection["witch_3_BI"].image, sprite_collection["witch_4_BI"].image,
                    sprite_collection["witch_5_BI"].image, sprite_collection["witch_6_BI"].image]

gWitchBattleAttack_image_list = [sprite_collection["witch_1_BA"].image, sprite_collection["witch_1_BA"].image,
                    sprite_collection["witch_3_BA"].image, sprite_collection["witch_4_BA"].image,
                    sprite_collection["witch_5_BA"].image, sprite_collection["witch_6_BA"].image,
                    sprite_collection["witch_7_BA"].image, sprite_collection["witch_8_BA"].image,
                    sprite_collection["witch_9_BA"].image]

gWitchBattleDead_image_list = [sprite_collection["witch_1_BD"].image, sprite_collection["witch_2_BD"].image,
                    sprite_collection["witch_3_BD"].image, sprite_collection["witch_4_BD"].image,
                    sprite_collection["witch_5_BD"].image, sprite_collection["witch_6_BD"].image,
                    sprite_collection["witch_7_BD"].image, sprite_collection["witch_8_BD"].image,
                    sprite_collection["witch_9_BD"].image, sprite_collection["witch_10_BD"].image,
                    sprite_collection["witch_11_BD"].image, sprite_collection["witch_12_BD"].image]

gWitchBattleDeadIdle_image_list = [sprite_collection["witch_12_BD"].image, sprite_collection["witch_12_BD"].image]

gWitchBattleSkill_image_list = [sprite_collection["witch_1_BS"].image, sprite_collection["witch_1_BS"].image,
                    sprite_collection["witch_3_BS"].image, sprite_collection["witch_4_BS"].image,
                    sprite_collection["witch_5_BS"].image]

gWitchBattleHurt_image_list = [sprite_collection["witch_1_BH"].image, sprite_collection["witch_1_BH"].image,
                    sprite_collection["witch_3_BH"].image]

gWitchBattleSkill2_image_list = [sprite_collection["witch_1_BS"].image, sprite_collection["witch_1_BS"].image,
                    sprite_collection["witch_3_BS"].image, sprite_collection["witch_4_BS"].image,
                    sprite_collection["witch_5_BS"].image,sprite_collection["witch_1_BA"].image, sprite_collection["witch_1_BA"].image,
                    sprite_collection["witch_3_BA"].image, sprite_collection["witch_4_BA"].image,
                    sprite_collection["witch_5_BA"].image, sprite_collection["witch_6_BA"].image,
                    sprite_collection["witch_7_BA"].image, sprite_collection["witch_8_BA"].image,
                    sprite_collection["witch_9_BA"].image]

gWitchBattle_image_list = [gWitchBattleIdle_image_list, gWitchBattleAttack_image_list, gWitchBattleHurt_image_list,
                            gWitchBattleDead_image_list, gWitchBattleDeadIdle_image_list, gWitchBattleSkill_image_list, gWitchBattleSkill2_image_list]


#GroundMonk Queen of Club sprite
gGroundMonkBattleIdle_image_list = [sprite_collection["groundmonk_1_BI"].image, sprite_collection["groundmonk_2_BI"].image,
                    sprite_collection["groundmonk_3_BI"].image, sprite_collection["groundmonk_4_BI"].image,
                    sprite_collection["groundmonk_5_BI"].image, sprite_collection["groundmonk_6_BI"].image]

gGroundMonkBattleAttack_image_list = [sprite_collection["groundmonk_1_BA"].image, sprite_collection["groundmonk_2_BA"].image,
                    sprite_collection["groundmonk_3_BA"].image, sprite_collection["groundmonk_4_BA"].image,
                    sprite_collection["groundmonk_5_BA"].image, sprite_collection["groundmonk_6_BA"].image]

gGroundMonkBattleDead_image_list = [sprite_collection["groundmonk_1_BD"].image, sprite_collection["groundmonk_2_BD"].image,
                    sprite_collection["groundmonk_3_BD"].image, sprite_collection["groundmonk_4_BD"].image,
                    sprite_collection["groundmonk_5_BD"].image, sprite_collection["groundmonk_6_BD"].image,
                    sprite_collection["groundmonk_7_BD"].image, sprite_collection["groundmonk_8_BD"].image,
                    sprite_collection["groundmonk_9_BD"].image, sprite_collection["groundmonk_10_BD"].image,
                    sprite_collection["groundmonk_11_BD"].image, sprite_collection["groundmonk_12_BD"].image,
                    sprite_collection["groundmonk_13_BD"].image, sprite_collection["groundmonk_14_BD"].image,
                    sprite_collection["groundmonk_15_BD"].image, sprite_collection["groundmonk_16_BD"].image,
                    sprite_collection["groundmonk_17_BD"].image, sprite_collection["groundmonk_18_BD"].image]

gGroundMonkBattleDeadIdle_image_list = [sprite_collection["groundmonk_18_BD"].image, sprite_collection["groundmonk_18_BD"].image]

gGroundMonkBattleSkill_image_list = [sprite_collection["groundmonk_1_BS"].image, sprite_collection["groundmonk_2_BS"].image,
                    sprite_collection["groundmonk_3_BS"].image, sprite_collection["groundmonk_4_BS"].image,
                    sprite_collection["groundmonk_5_BS"].image, sprite_collection["groundmonk_6_BS"].image,
                    sprite_collection["groundmonk_7_BS"].image, sprite_collection["groundmonk_8_BS"].image,
                    sprite_collection["groundmonk_9_BS"].image, sprite_collection["groundmonk_10_BS"].image,
                    sprite_collection["groundmonk_11_BS"].image, sprite_collection["groundmonk_12_BS"].image,
                    sprite_collection["groundmonk_13_BS"].image, sprite_collection["groundmonk_14_BS"].image,
                    sprite_collection["groundmonk_15_BS"].image, sprite_collection["groundmonk_16_BS"].image,
                    sprite_collection["groundmonk_17_BS"].image, sprite_collection["groundmonk_18_BS"].image,
                    sprite_collection["groundmonk_19_BS"].image,sprite_collection["groundmonk_20_BS"].image,
                    sprite_collection["groundmonk_21_BS"].image,sprite_collection["groundmonk_22_BS"].image,
                    sprite_collection["groundmonk_23_BS"].image]

gGroundMonkBattleHurt_image_list = [sprite_collection["groundmonk_1_BH"].image, sprite_collection["groundmonk_2_BH"].image,
                    sprite_collection["groundmonk_3_BH"].image, sprite_collection["groundmonk_4_BH"].image,
                    sprite_collection["groundmonk_5_BH"].image, sprite_collection["groundmonk_6_BH"].image]

gGroundMonkBattleSkill2_image_list = [sprite_collection["groundmonk_1_BS"].image, sprite_collection["groundmonk_2_BS2"].image,
                    sprite_collection["groundmonk_3_BS2"].image, sprite_collection["groundmonk_4_BS2"].image,
                    sprite_collection["groundmonk_5_BS2"].image, sprite_collection["groundmonk_6_BS2"].image,
                    sprite_collection["groundmonk_7_BS2"].image, sprite_collection["groundmonk_8_BS2"].image,
                    sprite_collection["groundmonk_9_BS2"].image, sprite_collection["groundmonk_10_BS2"].image,
                    sprite_collection["groundmonk_11_BS2"].image, sprite_collection["groundmonk_12_BS2"].image,
                    sprite_collection["groundmonk_13_BS2"].image, sprite_collection["groundmonk_14_BS2"].image,
                    sprite_collection["groundmonk_15_BS2"].image, sprite_collection["groundmonk_16_BS2"].image,
                    sprite_collection["groundmonk_17_BS2"].image, sprite_collection["groundmonk_18_BS2"].image,
                    sprite_collection["groundmonk_19_BS2"].image, sprite_collection["groundmonk_20_BS2"].image,
                    sprite_collection["groundmonk_21_BS2"].image, sprite_collection["groundmonk_22_BS2"].image,
                    sprite_collection["groundmonk_23_BS2"].image, sprite_collection["groundmonk_24_BS2"].image,
                    sprite_collection["groundmonk_25_BS2"].image]

gGroundMonkBattle_image_list = [gGroundMonkBattleIdle_image_list, gGroundMonkBattleAttack_image_list, gGroundMonkBattleHurt_image_list,
                            gGroundMonkBattleDead_image_list, gGroundMonkBattleDeadIdle_image_list, gGroundMonkBattleSkill_image_list, 
                            gGroundMonkBattleSkill2_image_list]

#Bladekeeper Queen of Diamond sprite
gBladekeeperBattleIdle_image_list = [sprite_collection["bladekeeper_1_BI"].image, sprite_collection["bladekeeper_2_BI"].image,
                    sprite_collection["bladekeeper_3_BI"].image, sprite_collection["bladekeeper_4_BI"].image,
                    sprite_collection["bladekeeper_5_BI"].image, sprite_collection["bladekeeper_6_BI"].image,
                    sprite_collection["bladekeeper_7_BI"].image, sprite_collection["bladekeeper_8_BI"].image]

gBladekeeperBattleAttack_image_list = [sprite_collection["bladekeeper_1_BA"].image, sprite_collection["bladekeeper_2_BA"].image,
                    sprite_collection["bladekeeper_3_BA"].image, sprite_collection["bladekeeper_4_BA"].image,
                    sprite_collection["bladekeeper_5_BA"].image, sprite_collection["bladekeeper_6_BA"].image,
                    sprite_collection["bladekeeper_7_BA"].image, sprite_collection["bladekeeper_8_BA"].image]

gBladekeeperBattleDead_image_list = [sprite_collection["bladekeeper_1_BD"].image, sprite_collection["bladekeeper_2_BD"].image,
                    sprite_collection["bladekeeper_3_BD"].image, sprite_collection["bladekeeper_4_BD"].image,
                    sprite_collection["bladekeeper_5_BD"].image, sprite_collection["bladekeeper_6_BD"].image,
                    sprite_collection["bladekeeper_7_BD"].image, sprite_collection["bladekeeper_8_BD"].image,
                    sprite_collection["bladekeeper_9_BD"].image, sprite_collection["bladekeeper_10_BD"].image,
                    sprite_collection["bladekeeper_11_BD"].image, sprite_collection["bladekeeper_12_BD"].image]

gBladekeeperBattleDeadIdle_image_list = [sprite_collection["bladekeeper_12_BD"].image, sprite_collection["bladekeeper_12_BD"].image]

gBladekeeperBattleSkill_image_list = [sprite_collection["bladekeeper_1_BS"].image, sprite_collection["bladekeeper_2_BS"].image,
                    sprite_collection["bladekeeper_3_BS"].image, sprite_collection["bladekeeper_4_BS"].image,
                    sprite_collection["bladekeeper_5_BS"].image, sprite_collection["bladekeeper_6_BS"].image,
                    sprite_collection["bladekeeper_7_BS"].image, sprite_collection["bladekeeper_8_BS"].image]

gBladekeeperBattleSkill2_image_list = [sprite_collection["bladekeeper_1_BS2"].image, sprite_collection["bladekeeper_2_BS2"].image,
                    sprite_collection["bladekeeper_3_BS2"].image, sprite_collection["bladekeeper_4_BS2"].image,
                    sprite_collection["bladekeeper_5_BS2"].image, sprite_collection["bladekeeper_6_BS2"].image,
                    sprite_collection["bladekeeper_7_BS2"].image, sprite_collection["bladekeeper_8_BS2"].image,
                    sprite_collection["bladekeeper_9_BS2"].image, sprite_collection["bladekeeper_10_BS2"].image,
                    sprite_collection["bladekeeper_11_BS2"].image]

gBladekeeperBattleHurt_image_list = [sprite_collection["bladekeeper_1_BH"].image, sprite_collection["bladekeeper_3_BH"].image,
                    sprite_collection["bladekeeper_3_BH"].image, sprite_collection["bladekeeper_4_BH"].image,
                    sprite_collection["bladekeeper_5_BH"].image, sprite_collection["bladekeeper_6_BH"].image]

gBladekeeperBattle_image_list = [gBladekeeperBattleIdle_image_list, gBladekeeperBattleAttack_image_list, gBladekeeperBattleHurt_image_list,
                              gBladekeeperBattleDead_image_list, gBladekeeperBattleDeadIdle_image_list, gBladekeeperBattleSkill_image_list, 
                              gBladekeeperBattleSkill2_image_list]

#Spearwoman Queen of Heart sprite
gSpearwomanBattleIdle_image_list = [sprite_collection["spearwoman_1_BI"].image, sprite_collection["spearwoman_2_BI"].image,
                    sprite_collection["spearwoman_3_BI"].image, sprite_collection["spearwoman_4_BI"].image,
                    sprite_collection["spearwoman_5_BI"].image, sprite_collection["spearwoman_6_BI"].image,
                    sprite_collection["spearwoman_7_BI"].image, sprite_collection["spearwoman_8_BI"].image]

gSpearwomanBattleAttack_image_list = [sprite_collection["spearwoman_1_BA"].image, sprite_collection["spearwoman_1_BA"].image,
                    sprite_collection["spearwoman_1_BA"].image, sprite_collection["spearwoman_1_BA"].image,
                    sprite_collection["spearwoman_1_BA"].image, sprite_collection["spearwoman_1_BA"].image]

gSpearwomanBattleDead_image_list = [sprite_collection["spearwoman_1_BD"].image, sprite_collection["spearwoman_2_BD"].image,
                    sprite_collection["spearwoman_3_BD"].image, sprite_collection["spearwoman_4_BD"].image,
                    sprite_collection["spearwoman_5_BD"].image, sprite_collection["spearwoman_6_BD"].image,
                    sprite_collection["spearwoman_7_BD"].image, sprite_collection["spearwoman_8_BD"].image,
                    sprite_collection["spearwoman_9_BD"].image]

gSpearwomanBattleDeadIdle_image_list = [sprite_collection["spearwoman_9_BD"].image, sprite_collection["spearwoman_9_BD"].image]

gSpearwomanBattleSkill_image_list = [sprite_collection["spearwoman_1_BS"].image, sprite_collection["spearwoman_1_BS"].image,
                    sprite_collection["spearwoman_3_BS"].image, sprite_collection["spearwoman_4_BS"].image,
                    sprite_collection["spearwoman_5_BS"].image, sprite_collection["spearwoman_6_BS"].image,
                    sprite_collection["spearwoman_7_BS"].image, sprite_collection["spearwoman_8_BS"].image,
                    sprite_collection["spearwoman_9_BS"].image, sprite_collection["spearwoman_10_BS"].image,
                    sprite_collection["spearwoman_11_BS"].image, sprite_collection["spearwoman_12_BS"].image,
                    sprite_collection["spearwoman_13_BS"].image, sprite_collection["spearwoman_14_BS"].image]

gSpearwomanBattleSkill2_image_list = [sprite_collection["spearwoman_1_BS2"].image, sprite_collection["spearwoman_2_BS2"].image,
                    sprite_collection["spearwoman_3_BS2"].image, sprite_collection["spearwoman_4_BS2"].image,
                    sprite_collection["spearwoman_5_BS2"].image, sprite_collection["spearwoman_6_BS2"].image,
                    sprite_collection["spearwoman_7_BS2"].image, sprite_collection["spearwoman_8_BS2"].image,
                    sprite_collection["spearwoman_9_BS2"].image, sprite_collection["spearwoman_10_BS2"].image,
                    sprite_collection["spearwoman_11_BS2"].image, sprite_collection["spearwoman_12_BS2"].image,
                    sprite_collection["spearwoman_13_BS2"].image, sprite_collection["spearwoman_14_BS2"].image,
                    sprite_collection["spearwoman_15_BS2"].image, sprite_collection["spearwoman_16_BS2"].image,
                    sprite_collection["spearwoman_17_BS2"].image, sprite_collection["spearwoman_18_BS2"].image,
                    sprite_collection["spearwoman_19_BS2"].image, sprite_collection["spearwoman_20_BS2"].image,
                    sprite_collection["spearwoman_21_BS2"].image, sprite_collection["spearwoman_22_BS2"].image]

gSpearwomanBattleHurt_image_list = [sprite_collection["spearwoman_1_BH"].image, sprite_collection["spearwoman_2_BH"].image,
                    sprite_collection["spearwoman_3_BH"].image, sprite_collection["spearwoman_4_BH"].image]

gSpearwomanBattle_image_list = [gSpearwomanBattleIdle_image_list, gSpearwomanBattleAttack_image_list, gSpearwomanBattleHurt_image_list,
                              gSpearwomanBattleDead_image_list, gSpearwomanBattleDeadIdle_image_list,
                              gSpearwomanBattleSkill_image_list, gSpearwomanBattleSkill2_image_list]

#Water Priestess Queen of Spade sprite
gWaterPriestessBattleIdle_image_list = [sprite_collection["priestess_1_BI"].image, sprite_collection["priestess_2_BI"].image,
                    sprite_collection["priestess_3_BI"].image, sprite_collection["priestess_4_BI"].image,
                    sprite_collection["priestess_5_BI"].image, sprite_collection["priestess_6_BI"].image,
                    sprite_collection["priestess_7_BI"].image, sprite_collection["priestess_8_BI"].image]

gWaterPriestessBattleAttack_image_list = [sprite_collection["priestess_1_BA"].image, sprite_collection["priestess_2_BA"].image,
                    sprite_collection["priestess_3_BA"].image, sprite_collection["priestess_4_BA"].image,
                    sprite_collection["priestess_5_BA"].image, sprite_collection["priestess_6_BA"].image,
                    sprite_collection["priestess_7_BA"].image, sprite_collection["priestess_8_BA"].image]

gWaterPriestessBattleDead_image_list = [sprite_collection["priestess_1_BD"].image, sprite_collection["priestess_2_BD"].image,
                    sprite_collection["priestess_3_BD"].image, sprite_collection["priestess_4_BD"].image,
                    sprite_collection["priestess_5_BD"].image, sprite_collection["priestess_6_BD"].image,
                    sprite_collection["priestess_7_BD"].image, sprite_collection["priestess_8_BD"].image,
                    sprite_collection["priestess_9_BD"].image, sprite_collection["priestess_10_BD"].image,
                    sprite_collection["priestess_11_BD"].image, sprite_collection["priestess_12_BD"].image,
                    sprite_collection["priestess_13_BD"].image, sprite_collection["priestess_14_BD"].image,
                    sprite_collection["priestess_15_BD"].image, sprite_collection["priestess_16_BD"].image]

gWaterPriestessBattleDeadIdle_image_list = [sprite_collection["priestess_16_BD"].image, sprite_collection["priestess_16_BD"].image]

gWaterPriestessBattleSkill_image_list = [sprite_collection["priestess_1_BS"].image, sprite_collection["priestess_2_BS"].image,
                    sprite_collection["priestess_3_BS"].image, sprite_collection["priestess_4_BS"].image,
                    sprite_collection["priestess_5_BS"].image, sprite_collection["priestess_6_BS"].image,
                    sprite_collection["priestess_7_BS"].image, sprite_collection["priestess_8_BS"].image,
                    sprite_collection["priestess_9_BS"].image, sprite_collection["priestess_10_BS"].image,
                    sprite_collection["priestess_11_BS"].image, sprite_collection["priestess_12_BS"].image,
                    sprite_collection["priestess_13_BS"].image, sprite_collection["priestess_14_BS"].image,
                    sprite_collection["priestess_15_BS"].image, sprite_collection["priestess_16_BS"].image,
                    sprite_collection["priestess_17_BS"].image, sprite_collection["priestess_18_BS"].image,
                    sprite_collection["priestess_19_BS"].image, sprite_collection["priestess_20_BS"].image,
                    sprite_collection["priestess_21_BS"].image, sprite_collection["priestess_22_BS"].image,
                    sprite_collection["priestess_23_BS"].image, sprite_collection["priestess_24_BS"].image,
                    sprite_collection["priestess_25_BS"].image, sprite_collection["priestess_26_BS"].image,
                    sprite_collection["priestess_27_BS"].image]

gWaterPriestessBattleSkill2_image_list = [sprite_collection["priestess_1_BS2"].image, sprite_collection["priestess_2_BS2"].image,
                    sprite_collection["priestess_3_BS2"].image, sprite_collection["priestess_4_BS2"].image,
                    sprite_collection["priestess_5_BS2"].image, sprite_collection["priestess_6_BS2"].image,
                    sprite_collection["priestess_7_BS2"].image, sprite_collection["priestess_8_BS2"].image,
                    sprite_collection["priestess_9_BS2"].image, sprite_collection["priestess_10_BS2"].image,
                    sprite_collection["priestess_11_BS2"].image, sprite_collection["priestess_12_BS2"].image]

gWaterPriestessBattleHurt_image_list = [sprite_collection["priestess_1_BH"].image, sprite_collection["priestess_2_BH"].image,
                    sprite_collection["priestess_3_BH"].image, sprite_collection["priestess_4_BH"].image,
                    sprite_collection["priestess_5_BH"].image, sprite_collection["priestess_6_BH"].image]

gWaterPriestessBattle_image_list = [gWaterPriestessBattleIdle_image_list, gWaterPriestessBattleAttack_image_list, gWaterPriestessBattleHurt_image_list,
                              gWaterPriestessBattleDead_image_list, gWaterPriestessBattleDeadIdle_image_list, gWaterPriestessBattleSkill_image_list, 
                              gWaterPriestessBattleSkill2_image_list]

#Ranger King of Club sprite
gRangerBattleIdle_image_list = [sprite_collection["ranger_1_BI"].image, sprite_collection["ranger_2_BI"].image,
                    sprite_collection["ranger_3_BI"].image, sprite_collection["ranger_4_BI"].image,
                    sprite_collection["ranger_5_BI"].image, sprite_collection["ranger_6_BI"].image,
                    sprite_collection["ranger_7_BI"].image, sprite_collection["ranger_8_BI"].image,
                    sprite_collection["ranger_9_BI"].image, sprite_collection["ranger_10_BI"].image,
                    sprite_collection["ranger_11_BI"].image, sprite_collection["ranger_12_BI"].image]

gRangerBattleAttack_image_list = [sprite_collection["ranger_1_BA"].image, sprite_collection["ranger_2_BA"].image,
                    sprite_collection["ranger_3_BA"].image, sprite_collection["ranger_4_BA"].image,
                    sprite_collection["ranger_5_BA"].image, sprite_collection["ranger_6_BA"].image,
                    sprite_collection["ranger_7_BA"].image, sprite_collection["ranger_8_BA"].image,
                    sprite_collection["ranger_9_BA"].image, sprite_collection["ranger_10_BA"].image,
                    sprite_collection["ranger_11_BA"].image, sprite_collection["ranger_12_BA"].image,
                    sprite_collection["ranger_13_BA"].image, sprite_collection["ranger_14_BA"].image,
                    sprite_collection["ranger_15_BA"].image]

gRangerBattleDead_image_list = [sprite_collection["ranger_1_BD"].image, sprite_collection["ranger_2_BD"].image,
                    sprite_collection["ranger_3_BD"].image, sprite_collection["ranger_4_BD"].image,
                    sprite_collection["ranger_5_BD"].image, sprite_collection["ranger_6_BD"].image,
                    sprite_collection["ranger_7_BD"].image, sprite_collection["ranger_8_BD"].image,
                    sprite_collection["ranger_9_BD"].image, sprite_collection["ranger_10_BD"].image,
                    sprite_collection["ranger_11_BD"].image, sprite_collection["ranger_12_BD"].image,
                    sprite_collection["ranger_13_BD"].image, sprite_collection["ranger_14_BD"].image,
                    sprite_collection["ranger_15_BD"].image, sprite_collection["ranger_16_BD"].image,
                    sprite_collection["ranger_17_BD"].image, sprite_collection["ranger_18_BD"].image,
                    sprite_collection["ranger_19_BD"].image]

gRangerBattleDeadIdle_image_list = [sprite_collection["ranger_19_BD"].image, sprite_collection["ranger_19_BD"].image]

gRangerBattleSkill_image_list = [sprite_collection["ranger_1_BS"].image, sprite_collection["ranger_2_BS"].image,
                    sprite_collection["ranger_3_BS"].image, sprite_collection["ranger_4_BS"].image,
                    sprite_collection["ranger_5_BS"].image, sprite_collection["ranger_6_BS"].image,
                    sprite_collection["ranger_7_BS"].image, sprite_collection["ranger_8_BS"].image,
                    sprite_collection["ranger_9_BS"].image, sprite_collection["ranger_10_BS"].image,
                    sprite_collection["ranger_11_BS"].image, sprite_collection["ranger_12_BS"].image,
                    sprite_collection["ranger_13_BS"].image, sprite_collection["ranger_14_BS"].image,
                    sprite_collection["ranger_15_BS"].image, sprite_collection["ranger_16_BS"].image,
                    sprite_collection["ranger_17_BS"].image]

gRangerBattleHurt_image_list = [sprite_collection["ranger_1_BH"].image, sprite_collection["ranger_2_BH"].image,
                    sprite_collection["ranger_3_BH"].image, sprite_collection["ranger_4_BH"].image,
                    sprite_collection["ranger_5_BH"].image, sprite_collection["ranger_6_BH"].image]

gRangerBattleSkill2_image_list = [sprite_collection["ranger_1_BS2"].image, sprite_collection["ranger_2_BS2"].image,
                    sprite_collection["ranger_3_BS2"].image, sprite_collection["ranger_4_BS2"].image,
                    sprite_collection["ranger_5_BS2"].image, sprite_collection["ranger_6_BS2"].image,
                    sprite_collection["ranger_7_BS2"].image, sprite_collection["ranger_8_BS2"].image,
                    sprite_collection["ranger_9_BS2"].image, sprite_collection["ranger_10_BS2"].image]

gRangerBattle_image_list = [gRangerBattleIdle_image_list, gRangerBattleAttack_image_list, gRangerBattleHurt_image_list,
                            gRangerBattleDead_image_list, gRangerBattleDeadIdle_image_list, gRangerBattleSkill_image_list, 
                            gRangerBattleSkill2_image_list]

#Hashashin King of Diamond sprite
gHashashinBattleIdle_image_list = [sprite_collection["hashashin_1_BI"].image, sprite_collection["hashashin_2_BI"].image,
                    sprite_collection["hashashin_3_BI"].image, sprite_collection["hashashin_4_BI"].image,
                    sprite_collection["hashashin_5_BI"].image, sprite_collection["hashashin_6_BI"].image,
                    sprite_collection["hashashin_7_BI"].image, sprite_collection["hashashin_8_BI"].image]

gHashashinBattleAttack_image_list = [sprite_collection["hashashin_1_BA"].image, sprite_collection["hashashin_2_BA"].image,
                    sprite_collection["hashashin_3_BA"].image, sprite_collection["hashashin_4_BA"].image,
                    sprite_collection["hashashin_5_BA"].image, sprite_collection["hashashin_6_BA"].image,
                    sprite_collection["hashashin_7_BA"].image, sprite_collection["hashashin_8_BA"].image]

gHashashinBattleDead_image_list = [sprite_collection["hashashin_1_BD"].image, sprite_collection["hashashin_2_BD"].image,
                    sprite_collection["hashashin_3_BD"].image, sprite_collection["hashashin_4_BD"].image,
                    sprite_collection["hashashin_5_BD"].image, sprite_collection["hashashin_6_BD"].image,
                    sprite_collection["hashashin_7_BD"].image, sprite_collection["hashashin_8_BD"].image,
                    sprite_collection["hashashin_9_BD"].image, sprite_collection["hashashin_10_BD"].image,
                    sprite_collection["hashashin_11_BD"].image, sprite_collection["hashashin_12_BD"].image,
                    sprite_collection["hashashin_13_BD"].image, sprite_collection["hashashin_14_BD"].image,
                    sprite_collection["hashashin_15_BD"].image, sprite_collection["hashashin_16_BD"].image,
                    sprite_collection["hashashin_17_BD"].image, sprite_collection["hashashin_18_BD"].image,
                    sprite_collection["hashashin_19_BD"].image]

gHashashinBattleDeadIdle_image_list = [sprite_collection["hashashin_19_BD"].image, sprite_collection["hashashin_19_BD"].image]

gHashashinBattleSkill_image_list = [sprite_collection["hashashin_1_BS"].image, sprite_collection["hashashin_2_BS"].image,
                    sprite_collection["hashashin_3_BS"].image, sprite_collection["hashashin_4_BS"].image,
                    sprite_collection["hashashin_5_BS"].image, sprite_collection["hashashin_6_BS"].image,
                    sprite_collection["hashashin_7_BS"].image]

gHashashinBattleSkill2_image_list = [sprite_collection["hashashin_1_BS2"].image, sprite_collection["hashashin_2_BS2"].image,
                    sprite_collection["hashashin_3_BS2"].image, sprite_collection["hashashin_4_BS2"].image,
                    sprite_collection["hashashin_5_BS2"].image, sprite_collection["hashashin_6_BS2"].image,
                    sprite_collection["hashashin_7_BS2"].image, sprite_collection["hashashin_8_BS2"].image,
                    sprite_collection["hashashin_9_BS2"].image, sprite_collection["hashashin_10_BS2"].image,
                    sprite_collection["hashashin_11_BS2"].image, sprite_collection["hashashin_12_BS2"].image,
                    sprite_collection["hashashin_13_BS2"].image, sprite_collection["hashashin_14_BS2"].image,
                    sprite_collection["hashashin_15_BS2"].image, sprite_collection["hashashin_16_BS2"].image,
                    sprite_collection["hashashin_17_BS2"].image, sprite_collection["hashashin_18_BS2"].image,
                    sprite_collection["hashashin_19_BS2"].image, sprite_collection["hashashin_20_BS2"].image,
                    sprite_collection["hashashin_21_BS2"].image, sprite_collection["hashashin_22_BS2"].image,
                    sprite_collection["hashashin_23_BS2"].image, sprite_collection["hashashin_24_BS2"].image,
                    sprite_collection["hashashin_25_BS2"].image, sprite_collection["hashashin_26_BS2"].image]

gHashashinBattleHurt_image_list = [sprite_collection["hashashin_1_BH"].image, sprite_collection["hashashin_2_BH"].image,
                    sprite_collection["hashashin_3_BH"].image, sprite_collection["hashashin_4_BH"].image,
                    sprite_collection["hashashin_5_BH"].image, sprite_collection["hashashin_6_BH"].image]

gHashashinBattle_image_list = [gHashashinBattleIdle_image_list, gHashashinBattleAttack_image_list, gHashashinBattleHurt_image_list,
                            gHashashinBattleDead_image_list, gHashashinBattleDeadIdle_image_list, gHashashinBattleSkill_image_list,
                            gHashashinBattleSkill2_image_list]

#FireKnight King of Heart sprite
gFireKnightBattleIdle_image_list = [sprite_collection["fireknight_1_BI"].image, sprite_collection["fireknight_2_BI"].image,
                    sprite_collection["fireknight_3_BI"].image, sprite_collection["fireknight_4_BI"].image,
                    sprite_collection["fireknight_5_BI"].image, sprite_collection["fireknight_6_BI"].image,
                    sprite_collection["fireknight_7_BI"].image, sprite_collection["fireknight_8_BI"].image]

gFireKnightBattleAttack_image_list = [sprite_collection["fireknight_1_BA"].image, sprite_collection["fireknight_2_BA"].image,
                    sprite_collection["fireknight_3_BA"].image, sprite_collection["fireknight_4_BA"].image,
                    sprite_collection["fireknight_5_BA"].image, sprite_collection["fireknight_6_BA"].image,
                    sprite_collection["fireknight_7_BA"].image, sprite_collection["fireknight_8_BA"].image,
                    sprite_collection["fireknight_9_BA"].image, sprite_collection["fireknight_10_BA"].image,
                    sprite_collection["fireknight_11_BA"].image]

gFireKnightBattleDead_image_list = [sprite_collection["fireknight_1_BD"].image, sprite_collection["fireknight_2_BD"].image,
                    sprite_collection["fireknight_3_BD"].image, sprite_collection["fireknight_4_BD"].image,
                    sprite_collection["fireknight_5_BD"].image, sprite_collection["fireknight_6_BD"].image,
                    sprite_collection["fireknight_7_BD"].image, sprite_collection["fireknight_8_BD"].image,
                    sprite_collection["fireknight_9_BD"].image, sprite_collection["fireknight_10_BD"].image,
                    sprite_collection["fireknight_11_BD"].image, sprite_collection["fireknight_12_BD"].image,
                    sprite_collection["fireknight_13_BD"].image]

gFireKnightBattleDeadIdle_image_list = [sprite_collection["fireknight_13_BD"].image, sprite_collection["fireknight_13_BD"].image]

gFireKnightBattleSkill_image_list = [sprite_collection["fireknight_1_BS"].image, sprite_collection["fireknight_2_BS"].image,
                    sprite_collection["fireknight_3_BS"].image, sprite_collection["fireknight_4_BS"].image,
                    sprite_collection["fireknight_5_BS"].image, sprite_collection["fireknight_6_BS"].image,
                    sprite_collection["fireknight_7_BS"].image, sprite_collection["fireknight_8_BS"].image,
                    sprite_collection["fireknight_9_BS"].image, sprite_collection["fireknight_10_BS"].image,
                    sprite_collection["fireknight_11_BS"].image, sprite_collection["fireknight_12_BS"].image,
                    sprite_collection["fireknight_13_BS"].image, sprite_collection["fireknight_14_BS"].image,
                    sprite_collection["fireknight_15_BS"].image, sprite_collection["fireknight_16_BS"].image,
                    sprite_collection["fireknight_17_BS"].image, sprite_collection["fireknight_18_BS"].image,
                    sprite_collection["fireknight_19_BS"].image,sprite_collection["fireknight_20_BS"].image,
                    sprite_collection["fireknight_21_BS"].image,sprite_collection["fireknight_22_BS"].image,
                    sprite_collection["fireknight_23_BS"].image,sprite_collection["fireknight_24_BS"].image,
                    sprite_collection["fireknight_25_BS"].image,sprite_collection["fireknight_26_BS"].image,
                    sprite_collection["fireknight_27_BS"].image,sprite_collection["fireknight_28_BS"].image]

gFireKnightBattleSkill2_image_list = [sprite_collection["fireknight_1_BS2"].image, sprite_collection["fireknight_2_BS2"].image,
                    sprite_collection["fireknight_3_BS2"].image, sprite_collection["fireknight_4_BS2"].image,
                    sprite_collection["fireknight_5_BS2"].image, sprite_collection["fireknight_6_BS2"].image,
                    sprite_collection["fireknight_7_BS2"].image, sprite_collection["fireknight_8_BS2"].image,
                    sprite_collection["fireknight_9_BS2"].image, sprite_collection["fireknight_10_BS2"].image,
                    sprite_collection["fireknight_11_BS2"].image, sprite_collection["fireknight_12_BS2"].image,
                    sprite_collection["fireknight_13_BS2"].image, sprite_collection["fireknight_14_BS2"].image,
                    sprite_collection["fireknight_15_BS2"].image, sprite_collection["fireknight_16_BS2"].image,
                    sprite_collection["fireknight_17_BS2"].image, sprite_collection["fireknight_18_BS2"].image]

gFireKnightBattleHurt_image_list = [sprite_collection["fireknight_1_BH"].image, sprite_collection["fireknight_2_BH"].image,
                    sprite_collection["fireknight_3_BH"].image, sprite_collection["fireknight_4_BH"].image,
                    sprite_collection["fireknight_5_BH"].image, sprite_collection["fireknight_6_BH"].image]

gFireKnightBattle_image_list = [gFireKnightBattleIdle_image_list, gFireKnightBattleAttack_image_list, gFireKnightBattleHurt_image_list,
                              gFireKnightBattleDead_image_list, gFireKnightBattleDeadIdle_image_list, 
                              gFireKnightBattleSkill_image_list, gFireKnightBattleSkill2_image_list]

#Skeleton sprite
gSkeletonBattleIdle_image_list = [sprite_collection["skeleton_1_BI"].image, sprite_collection["skeleton_2_BI"].image,
                    sprite_collection["skeleton_3_BI"].image, sprite_collection["skeleton_4_BI"].image]

gSkeletonBattleAttack_image_list = [sprite_collection["skeleton_1_BA"].image, sprite_collection["skeleton_2_BA"].image,
                    sprite_collection["skeleton_3_BA"].image, sprite_collection["skeleton_4_BA"].image,
                    sprite_collection["skeleton_5_BA"].image, sprite_collection["skeleton_6_BA"].image,
                    sprite_collection["skeleton_7_BA"].image, sprite_collection["skeleton_8_BA"].image]

gSkeletonBattleHurt_image_list = [sprite_collection["skeleton_1_BH"].image, sprite_collection["skeleton_2_BH"].image,
                    sprite_collection["skeleton_3_BH"].image, sprite_collection["skeleton_4_BH"].image]

gSkeletonBattleDead_image_list = [sprite_collection["skeleton_1_BD"].image, sprite_collection["skeleton_2_BD"].image,
                    sprite_collection["skeleton_3_BD"].image, sprite_collection["skeleton_4_BD"].image,
                    sprite_collection["skeleton_4_BD"].image,]

gSkeletonBattleDeadIdle_image_list = [sprite_collection["skeleton_4_BD"].image, sprite_collection["skeleton_4_BD"].image]

gSkeletonBattleSkill_image_list = [sprite_collection["skeleton_1_BS"].image, sprite_collection["skeleton_2_BS"].image,
                    sprite_collection["skeleton_3_BS"].image, sprite_collection["skeleton_4_BS"].image]

gSkeletonBattle_image_list = [gSkeletonBattleIdle_image_list, gSkeletonBattleAttack_image_list, gSkeletonBattleHurt_image_list,
                              gSkeletonBattleDead_image_list, gSkeletonBattleDeadIdle_image_list, gSkeletonBattleSkill_image_list]



#items list
#pistol
gLwPistol_image_list = [sprite_collection["pistol_1"].image, sprite_collection["pistol_2"].image,
                    sprite_collection["pistol_3"].image, sprite_collection["pistol_4"].image,
                    sprite_collection["pistol_5"].image, sprite_collection["pistol_6"].image,
                    sprite_collection["pistol_7"].image, sprite_collection["pistol_8"].image,
                    sprite_collection["pistol_9"].image, sprite_collection["pistol_10"].image,
                    sprite_collection["pistol_11"].image, sprite_collection["pistol_12"].image]
#gravity
gItemGravity_image_list = [sprite_collection["gravity_1"].image, sprite_collection["gravity_2"].image,
                    sprite_collection["gravity_3"].image, sprite_collection["gravity_4"].image,
                    sprite_collection["gravity_5"].image, sprite_collection["gravity_6"].image,
                    sprite_collection["gravity_7"].image, sprite_collection["gravity_8"].image,
                    sprite_collection["gravity_9"].image, sprite_collection["gravity_10"].image,
                    sprite_collection["gravity_11"].image, sprite_collection["gravity_12"].image,
                    sprite_collection["gravity_13"].image, sprite_collection["gravity_14"].image,
                    sprite_collection["gravity_15"].image, sprite_collection["gravity_16"].image,
                    sprite_collection["gravity_17"].image, sprite_collection["gravity_18"].image,
                    sprite_collection["gravity_19"].image, sprite_collection["gravity_20"].image]
#Holy
gItemHoly_image_list = [sprite_collection["holy_1"].image, sprite_collection["holy_2"].image,
                    sprite_collection["holy_3"].image, sprite_collection["holy_4"].image,
                    sprite_collection["holy_5"].image, sprite_collection["holy_6"].image,
                    sprite_collection["holy_7"].image, sprite_collection["holy_8"].image,
                    sprite_collection["holy_9"].image, sprite_collection["holy_10"].image,
                    sprite_collection["holy_11"].image, sprite_collection["holy_12"].image,
                    sprite_collection["holy_13"].image, sprite_collection["holy_14"].image,
                    sprite_collection["holy_15"].image, sprite_collection["holy_16"].image]
#Dark
gItemDark_image_list = [sprite_collection["dark_1"].image, sprite_collection["dark_2"].image,
                    sprite_collection["dark_3"].image, sprite_collection["dark_4"].image,
                    sprite_collection["dark_5"].image, sprite_collection["dark_6"].image,
                    sprite_collection["dark_7"].image, sprite_collection["dark_8"].image,
                    sprite_collection["dark_9"].image, sprite_collection["dark_10"].image,
                    sprite_collection["dark_11"].image, sprite_collection["dark_12"].image,
                    sprite_collection["dark_13"].image, sprite_collection["dark_14"].image,
                    sprite_collection["dark_15"].image, sprite_collection["dark_16"].image]
#Ice
gItemIce_image_list = [sprite_collection["ice_1"].image, sprite_collection["ice_2"].image,
                    sprite_collection["ice_3"].image, sprite_collection["ice_4"].image,
                    sprite_collection["ice_5"].image, sprite_collection["ice_6"].image,
                    sprite_collection["ice_7"].image, sprite_collection["ice_8"].image,
                    sprite_collection["ice_9"].image, sprite_collection["ice_10"].image]
#Thunder
gItemThunder_image_list = [sprite_collection["thunder_1"].image, sprite_collection["thunder_2"].image,
                    sprite_collection["thunder_3"].image, sprite_collection["thunder_4"].image,
                    sprite_collection["thunder_5"].image, sprite_collection["thunder_6"].image,
                    sprite_collection["thunder_7"].image, sprite_collection["thunder_8"].image,
                    sprite_collection["thunder_9"].image, sprite_collection["thunder_10"].image,
                    sprite_collection["thunder_11"].image, sprite_collection["thunder_12"].image,
                    sprite_collection["thunder_13"].image, sprite_collection["thunder_14"].image,
                    sprite_collection["thunder_15"].image, sprite_collection["thunder_16"].image]
#Water
gItemWater_image_list = [sprite_collection["water_5"].image, sprite_collection["water_6"].image,
                    sprite_collection["water_7"].image, sprite_collection["water_8"].image,
                    sprite_collection["water_9"].image, sprite_collection["water_10"].image,
                    sprite_collection["water_11"].image, sprite_collection["water_12"].image,
                    sprite_collection["water_13"].image, sprite_collection["water_14"].image,
                    sprite_collection["water_15"].image, sprite_collection["water_16"].image,
                    sprite_collection["water_17"].image, sprite_collection["water_18"].image,
                    sprite_collection["water_19"].image, sprite_collection["water_20"].image,
                    sprite_collection["water_21"].image]
#Joker
gItemJoker_image_list = [sprite_collection["joker_1"].image, sprite_collection["joker_2"].image,
                    sprite_collection["joker_3"].image, sprite_collection["joker_4"].image,
                    sprite_collection["joker_5"].image, sprite_collection["joker_6"].image,
                    sprite_collection["joker_7"].image, sprite_collection["joker_8"].image,
                    sprite_collection["joker_9"].image, sprite_collection["joker_10"].image,
                    sprite_collection["joker_11"].image, sprite_collection["joker_12"].image]
#Sword
gItemSword_image_list = [sprite_collection["sword_1"].image, sprite_collection["sword_2"].image,
                    sprite_collection["sword_3"].image, sprite_collection["sword_4"].image]
#Scorpion
gItemScorpion_image_list = [sprite_collection["Scorpion_1"].image, sprite_collection["Scorpion_2"].image,
                    sprite_collection["Scorpion_3"].image, sprite_collection["Scorpion_4"].image]
#Worm
gItemWorm_image_list = [sprite_collection["Worm_1"].image, sprite_collection["Worm_2"].image,
                    sprite_collection["Worm_3"].image, sprite_collection["Worm_4"].image,
                    sprite_collection["Worm_5"].image, sprite_collection["Worm_6"].image,
                    sprite_collection["Worm_7"].image, sprite_collection["Worm_8"].image]
#Spider
gItemSpider_image_list = [sprite_collection["Spider_1"].image, sprite_collection["Spider_2"].image,
                    sprite_collection["Spider_3"].image, sprite_collection["Spider_4"].image,
                    sprite_collection["Spider_5"].image, sprite_collection["Spider_6"].image,
                    sprite_collection["Spider_7"].image, sprite_collection["Spider_8"].image]

gSounds = {
    'music': pygame.mixer.Sound('sounds/music.wav'),
    #extra
    'Retro_Single_v6': pygame.mixer.Sound('sounds/Retro_Single_v6.wav'),
    'late-hours': pygame.mixer.Sound('sounds/late-hours.wav'),
    'campfire_fireplace': pygame.mixer.Sound('sounds/campfire_fireplace.wav'),
    'no-select': pygame.mixer.Sound('sounds/no-select.wav'),
    'select': pygame.mixer.Sound('sounds/select.wav'),
    'confirm': pygame.mixer.Sound('sounds/confirm.wav'),
    'wall_hit': pygame.mixer.Sound('sounds/wall_hit.wav'),
    'burning_card': pygame.mixer.Sound('sounds/fire-magic-6947.wav'),
    'burning_continue': pygame.mixer.Sound('sounds/fire-winds-swoosh.wav'),
    'water_droplets': pygame.mixer.Sound('sounds/droplets-in-a-cave.wav'),
    'weird-mysterious': pygame.mixer.Sound('sounds/weird-mysterious-motif.wav'),
    'door-creaking': pygame.mixer.Sound('sounds/door-creaking.wav'),
    'mystery_unfold': pygame.mixer.Sound('sounds/mystery_unfold.wav'),
    'epic-orchestra': pygame.mixer.Sound('sounds/epic-orchestra.wav'),
    'sad-violin': pygame.mixer.Sound('sounds/sad-violin.wav'),
    'battle1': pygame.mixer.Sound('sounds/battle_music/chasing-victory.mp3'),
    'battle2': pygame.mixer.Sound('sounds/battle_music/epic-motivational.mp3'),
    'battle3': pygame.mixer.Sound('sounds/battle_music/medieval-fantasy.mp3'),
    'battle4': pygame.mixer.Sound('sounds/battle_music/war-is-coming.mp3'),
    'battle5': pygame.mixer.Sound('sounds/battle_music/where-the-brave-may-live-forever-viking.mp3')
}

gFonts = {
    'small': pygame.font.Font('fonts/font.ttf', 24),
    'medium': pygame.font.Font('fonts/font.ttf', 48),
    'large': pygame.font.Font('fonts/font.ttf', 96),
    'zelda_small': pygame.font.Font('fonts/zelda.otf', 96),
    'zelda': pygame.font.Font('fonts/zelda.otf', 192),
    'gothic_medium': pygame.font.Font('fonts/GothicPixels.ttf', 48),
    'gothic_large': pygame.font.Font('fonts/GothicPixels.ttf', 96),

}


from src.states.game.StartState import StartState
from src.states.game.CharacterSelectState import CharacterSelectState
from src.states.game.RollDiceState import RollDiceState
from src.StateMachine import StateMachine
from src.states.game.CardState import CardState
from src.states.game.BattleState import BattleState
from src.states.game.HealingState import HealingState
from src.states.game.LootingState import LootingState
from src.states.game.MeetingState import MeetingState
from src.states.game.EndingCutState import EndingCutState
from src.states.game.GameEndingState import GameEndingState