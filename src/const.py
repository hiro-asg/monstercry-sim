#!/usr/bin/env python
#!-*- coding:utf-8 -*-
from src.classes.passive_skill import PassiveSkill

AI_NORMAL = "normal"
AI_BALANCE = "balance"
AI_SPEED = "speed"
AI_TECHNICAL = "technical"
AI_DEFENSE = "defense"
AI_SAVING = "saving"
AI_DAMAGE = "damage"
AI_LETHAL = "lethal"

TYPE_USE = 0
TYPE_DISCARD = 1

ACT_DISCARD_SKILL_DEFENSE = -1
ACT_ATTACK = 0
ACT_SKILL_1 = 1
ACT_SKILL_2 = 2
ACT_DEFENSE = 3

ICON_DISCARD_SKILL_DEFENSE = -1
ICON_ATTACK = 0
ICON_SKILL = 1
ICON_DEFENSE = 2

PROBABILITY_ATTACK = 0.50
PROBABILITY_SKILL = 0.30
PROBABILITY_DEFENSE = 0.20
PROBABILITIES = {ICON_ATTACK: PROBABILITY_ATTACK, ICON_SKILL: PROBABILITY_SKILL, ICON_DEFENSE: PROBABILITY_DEFENSE}

ICON_INDEX = {ACT_DISCARD_SKILL_DEFENSE: ICON_DISCARD_SKILL_DEFENSE, ACT_ATTACK: ICON_ATTACK, ACT_SKILL_1: ICON_SKILL, ACT_SKILL_2: ICON_SKILL, ACT_DEFENSE: ICON_DEFENSE}

ROLE_1 = "PLAYER 1"
ROLE_2 = "PLAYER 2"


class Const:
    def __init__(self):
        pass

    SKILL = {
        #Healing skills
        "cure_medium": {"name": u"回復(中)", "cost": 2, "duration": 1, "cool_time": 3, "level": 10, "damage": 0,
                        "defense": 0, "heal": 6250, "attack_up": 0}
        , "cure_large": {"name": u"回復(大)", "cost": 3, "duration": 1, "cool_time": 3, "level": 10, "damage": 0,
                         "defense": 0, "heal": 10000, "attack_up": 0}

        #Regeneration skills
        , "regeneration_small": {"name": u"再生(小)", "cost": 2, "duration": 3, "cool_time": 4, "level": 10, "damage": 0,
                                 "defense": 0, "heal": 2500, "attack_up": 0}
        , "regeneration_medium": {"name": u"再生(中)", "cost": 3, "duration": 3, "cool_time": 4, "level": 10, "damage": 0,
                                  "defense": 0, "heal": 3750, "attack_up": 0}
        , "regeneration_large": {"name": u"再生(大)", "cost": 4, "duration": 3, "cool_time": 4, "level": 10, "damage": 0,
                                 "defense": 0, "heal": 6000, "attack_up": 0}

        #DOT skills
        , "tussock_moth": {"name": u"毒蛾", "cost": 2, "duration": 5, "cool_time": 5, "level": 10, "damage": 1500,
                           "defense": 0, "heal": 0, "attack_up": 0}
        , "acid_poison": {"name": u"酸性毒", "cost": 2, "duration": 3, "cool_time": 4, "level": 10, "damage": 2500,
                          "defense": 0, "heal": 0, "attack_up": 0}
        , "beast_attack": {"name": u"野獣の追撃", "cost": 3, "duration": 3, "cool_time": 4, "level": 10, "damage": 3750,
                           "defense": 0, "heal": 0, "attack_up": 0}
        , "choke_wave": {"name": u"窒息の波動", "cost": 3, "duration": 5, "cool_time": 5, "level": 10, "damage": 2750,
                         "defense": 0, "heal": 0, "attack_up": 0}
        , "stigma_of_death": {"name": u"死神の烙印", "cost": 4, "duration": 3, "cool_time": 4, "level": 10, "damage": 5000,
                              "defense": 0, "heal": 0, "attack_up": 0}

        #Attack skills
        , "knife_throwing": {"name": u"短剣投擲", "cost": 2, "duration": 1, "cool_time": 3, "level": 10, "damage": 6250,
                             "defense": 0, "heal": 0, "attack_up": 0}
        , "lightning_bolt": {"name": u"光の矢", "cost": 2, "duration": 1, "cool_time": 6, "level": 10, "damage": 7000,
                             "defense": 0, "heal": 0, "attack_up": 0}
        , "boomerang": {"name": u"ブーメラン", "cost": 3, "duration": 1, "cool_time": 3, "level": 10, "damage": 9250,
                        "defense": 0, "heal": 0, "attack_up": 0}
        , "depth_charge": {"name": u"爆雷", "cost": 3, "duration": 1, "cool_time": 6, "level": 10, "damage": 10000,
                           "defense": 0, "heal": 0, "attack_up": 0}

        #Defence skills
        ,
        "patience": {"name": u"忍耐", "cost": 2, "duration": 1, "cool_time": 3, "level": 10, "damage": 0, "defense": 7500,
                     "heal": 0, "attack_up": 0}
        , "guts": {"name": u"根性", "cost": 3, "duration": 1, "cool_time": 3, "level": 10, "damage": 0, "defense": 10000,
                   "heal": 0, "attack_up": 0}
        , "impregnable_defense": {"name": u"鉄壁", "cost": 4, "duration": 1, "cool_time": 3, "level": 10, "damage": 0,
                                  "defense": 15000, "heal": 0, "attack_up": 0}

        #Attack boost skills
        , "fighting_spirit": {"name": u"闘争心", "cost": 3, "duration": 5, "cool_time": 5, "level": 10, "damage": 0,
                              "defense": 0, "heal": 0, "attack_up": 5000}
        , "rage": {"name": u"激怒", "cost": 3, "duration": 3, "cool_time": 3, "level": 10, "damage": 0, "defense": 0,
                   "heal": 0, "attack_up": 7500}
    }

    PASSIVE_SKILL = {
        "imelda": {"name": u"幻影剣舞", "level": 10, "increase_life": 6250, "increase_attack": 0, "increase_defense": 0,
                   "increase_bonus": 0,
                   "increase_life_percentage": 1, "increase_attack_percentage": 1, "increase_defense_percentage": 1,
                   "increase_bonus_percentage": 1,
                   "increase_damage": 0, "increase_damage_percentage": 1.13, "increase_skill_damage_percentage": 1.13,
                   "increase_skill_effect_percentage": 1,
                   "decrease_damage_percentage": 1, "decrease_skill_damage_percentage": 1,
                   "special_skill": False}

        , "crystal": {"name": u"夜明に輝く剣", "level": 10, "increase_life": 0, "increase_attack": 0, "increase_defense": 0,
                      "increase_bonus": 100,
                      "increase_life_percentage": 1, "increase_attack_percentage": 1.24,
                      "increase_defense_percentage": 1, "increase_bonus_percentage": 1,
                      "increase_damage": 1, "increase_damage_percentage": 1, "increase_skill_damage_percentage": 1,
                      "increase_skill_effect_percentage": 1,
                      "decrease_damage_percentage": 1, "decrease_skill_damage_percentage": 1,
                      "special_skill": False}
    }

    CREATURE = {
        "imelda": {"name": u"イメルダ", "rank": "epic", "life": 3600, "attack": 810, "defense": 1075, "bonus": 112}
        , "crystal": {"name": u"クリスタル", "rank": "epic", "life": 5100, "attack": 510, "defense": 1075, "bonus": 112}
    }


def get_special_skill(self, creature_id):
    if creature_id == "inferna":
        #FIXME
        return PassiveSkill()
    elif creature_id == "lucifer":
        #FIXME
        return PassiveSkill()
    else:
        raise Exception("The special skill is not found. id : " + creature_id)
