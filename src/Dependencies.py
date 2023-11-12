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

gWizardBattle_image_list = [gWizardBattleIdle_image_list, gWizardBattleAttack_image_list, gWizardBattleHurt_image_list,
                            gWizardBattleDead_image_list, gWizardBattleSkill_image_list,gWizardBattleDeadIdle_image_list]

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
                              gSkeletonBattleDead_image_list, gSkeletonBattleSkill_image_list]


#NightBorne sprite
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
                              gNightBorneBattleDead_image_list, gNightBorneBattleSkill_image_list]

#necSkeleton sprite
gNecroSkeletonBattleIdle_image_list = [sprite_collection["necskeleton_1_BI"].image, sprite_collection["necskeleton_2_BI"].image,
                    sprite_collection["necskeleton_3_BI"].image, sprite_collection["necskeleton_4_BI"].image]

gNecroSkeletonBattleAttack_image_list = [sprite_collection["necskeleton_1_BA"].image, sprite_collection["necskeleton_2_BA"].image,
                    sprite_collection["necskeleton_3_BA"].image, sprite_collection["necskeleton_4_BA"].image,
                    sprite_collection["necskeleton_5_BA"].image, sprite_collection["necskeleton_6_BA"].image,
                    sprite_collection["necskeleton_7_BA"].image, sprite_collection["necskeleton_8_BA"].image,
                    sprite_collection["necskeleton_9_BA"].image, sprite_collection["necskeleton_10_BA"].image,
                    sprite_collection["necskeleton_11_BA"].image, sprite_collection["necskeleton_12_BA"].image,
                    sprite_collection["necskeleton_13_BA"].image]

gNecroSkeletonBattleHurt_image_list = [sprite_collection["necskeleton_1_BH"].image, sprite_collection["necskeleton_1_BH"].image,
                    sprite_collection["necskeleton_1_BH"].image]

gNecroSkeletonBattleDead_image_list = [sprite_collection["necskeleton_1_BD"].image, sprite_collection["necskeleton_2_BD"].image,
                    sprite_collection["necskeleton_3_BD"].image, sprite_collection["necskeleton_4_BD"].image,
                    sprite_collection["necskeleton_5_BD"].image, sprite_collection["necskeleton_6_BD"].image,
                    sprite_collection["necskeleton_7_BD"].image, sprite_collection["necskeleton_8_BD"].image,
                    sprite_collection["necskeleton_9_BD"].image, sprite_collection["necskeleton_10_BD"].image,
                    sprite_collection["necskeleton_11_BD"].image, sprite_collection["necskeleton_12_BD"].image,
                    sprite_collection["necskeleton_13_BD"].image]

gNecroSkeletonBattleDeadIdle_image_list = [sprite_collection["necskeleton_13_BD"].image, sprite_collection["necskeleton_13_BD"].image]

gNecroSkeletonBattle_image_list = [gNecroSkeletonBattleIdle_image_list, gNecroSkeletonBattleAttack_image_list, gNecroSkeletonBattleHurt_image_list,
                              gNecroSkeletonBattleDead_image_list, gNecroSkeletonBattleAttack_image_list]

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

gMedKingBattle_image_list = [gMedKingBattleIdle_image_list, gMedKingBattleAttack_image_list, gMedKingBattleHurt_image_list,
                             gMedKingBattleDead_image_list, gMedKingBattleSkill_image_list]

#Huntress
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
    'sad-violin': pygame.mixer.Sound('sounds/sad-violin.wav')
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