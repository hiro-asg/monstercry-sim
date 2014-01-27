#!/usr/bin/env python
#!-*- coding:utf-8 -*-

AI_NORMAL = "normal"
AI_BALANCE = "balance"
AI_SPEED = "speed"
AI_TECHNICAL = "technical"
AI_DEFENSE = "defense"
AI_SAVING = "saving"
AI_DAMAGE = "damage"
AI_LETHAL = "lethal"

AI_NAME = {AI_NORMAL: u"ノーマル", AI_BALANCE: u"バランス", AI_SPEED: u"スピード", AI_TECHNICAL: u"テクニカル",
           AI_DEFENSE: u"ディフェンス", AI_SAVING: u"セーヴィング", AI_DAMAGE: u"ダメージ", AI_LETHAL: u"一撃必殺"}

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

ICON_INDEX = {ACT_DISCARD_SKILL_DEFENSE: ICON_DISCARD_SKILL_DEFENSE, ACT_ATTACK: ICON_ATTACK, ACT_SKILL_1: ICON_SKILL,
              ACT_SKILL_2: ICON_SKILL, ACT_DEFENSE: ICON_DEFENSE}

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
        , "fire_bomb": {"name": u"火炎爆弾", "cost": 4, "duration": 1, "cool_time": 3, "level": 10, "damage": 13250,
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
        "imelda": {"name": u"幻影剣舞", "level": 10,
                   "increase_life": 6250, "increase_attack": 0, "increase_defense": 0, "increase_bonus": 0,
                   "increase_life_percentage": 1, "increase_attack_percentage": 1, "increase_defense_percentage": 1,
                   "increase_bonus_percentage": 1,
                   "increase_damage": 0, "increase_damage_percentage": 1.13, "increase_skill_damage_percentage": 1.13,
                   "increase_skill_effect_percentage": 1,
                   "decrease_damage_percentage": 1, "decrease_skill_damage_percentage": 1,
                   "special_skill": False}

        , "crystal": {"name": u"夜明に輝く剣", "level": 10,
                      "increase_life": 0, "increase_attack": 0, "increase_defense": 0, "increase_bonus": 100,
                      "increase_life_percentage": 1, "increase_attack_percentage": 1.24,
                      "increase_defense_percentage": 1, "increase_bonus_percentage": 1,
                      "increase_damage": 0, "increase_damage_percentage": 1, "increase_skill_damage_percentage": 1,
                      "increase_skill_effect_percentage": 1,
                      "decrease_damage_percentage": 1, "decrease_skill_damage_percentage": 1,
                      "special_skill": False}

        , "melawen": {"name": u"高潔な翼", "level": 10,
                      "increase_life": 0, "increase_attack": 0, "increase_defense": 1250, "increase_bonus": 0,
                      "increase_life_percentage": 1, "increase_attack_percentage": 1,
                      "increase_defense_percentage": 1, "increase_bonus_percentage": 1,
                      "increase_damage": 0, "increase_damage_percentage": 1, "increase_skill_damage_percentage": 1,
                      "increase_skill_effect_percentage": 1,
                      "decrease_damage_percentage": 0.76, "decrease_skill_damage_percentage": 1,
                      "special_skill": False}

        , "blesilda": {"name": u"霊魂の呼びかけ", "level": 10,
                       "increase_life": 0, "increase_attack": 1250, "increase_defense": 0, "increase_bonus": 0,
                       "increase_life_percentage": 1, "increase_attack_percentage": 1,
                       "increase_defense_percentage": 1, "increase_bonus_percentage": 1,
                       "increase_damage": 0, "increase_damage_percentage": 1, "increase_skill_damage_percentage": 1,
                       "increase_skill_effect_percentage": 1,
                       "decrease_damage_percentage": 0.85, "decrease_skill_damage_percentage": 1,
                       "special_skill": False}

        , "sialar": {"name": u"華麗なる炎の剣舞", "level": 10,
                       "increase_life": 3750, "increase_attack": 1750, "increase_defense": 0, "increase_bonus": 0,
                       "increase_life_percentage": 1, "increase_attack_percentage": 1,
                       "increase_defense_percentage": 1, "increase_bonus_percentage": 1,
                       "increase_damage": 0, "increase_damage_percentage": 1, "increase_skill_damage_percentage": 1,
                       "increase_skill_effect_percentage": 1,
                       "decrease_damage_percentage": 1, "decrease_skill_damage_percentage": 1,
                       "special_skill": False}

        , "princess_barbala": {"name": u"バーバラの邪悪な魔法", "level": 10,
                       "increase_life": 0, "increase_attack": 0, "increase_defense": 0, "increase_bonus": 500,
                       "increase_life_percentage": 1, "increase_attack_percentage": 1,
                       "increase_defense_percentage": 1, "increase_bonus_percentage": 1,
                       "increase_damage": 0, "increase_damage_percentage": 1, "increase_skill_damage_percentage": 1,
                       "increase_skill_effect_percentage": 1,
                       "decrease_damage_percentage": 1, "decrease_skill_damage_percentage": 1,
                       "special_skill": False}

        , "inferna": {"name": u"ソンズオブダークネス", "level": 10,
                       "increase_life": 0, "increase_attack": 0, "increase_defense": 0, "increase_bonus": 0,
                       "increase_life_percentage": 1, "increase_attack_percentage": 1,
                       "increase_defense_percentage": 1, "increase_bonus_percentage": 1,
                       "increase_damage": 0, "increase_damage_percentage": 1, "increase_skill_damage_percentage": 1,
                       "increase_skill_effect_percentage": 1,
                       "decrease_damage_percentage": 1, "decrease_skill_damage_percentage": 1,
                       "special_skill": True}

        , "fiora": {"name": u"砂漠のレンジャー", "level": 10,
                      "increase_life": 0, "increase_attack": 0, "increase_defense": 0, "increase_bonus": 0,
                      "increase_life_percentage": 1, "increase_attack_percentage": 1,
                      "increase_defense_percentage": 1, "increase_bonus_percentage": 1,
                      "increase_damage": 0, "increase_damage_percentage": 1, "increase_skill_damage_percentage": 1,
                      "increase_skill_effect_percentage": 1,
                      "decrease_damage_percentage": 1, "decrease_skill_damage_percentage": 1,
                      "special_skill": True}

        , "chabana": {"name": u"全能なる月光", "level": 10,
                      "increase_life": 0, "increase_attack": 0, "increase_defense": 0, "increase_bonus": 100,
                      "increase_life_percentage": 1, "increase_attack_percentage": 1,
                      "increase_defense_percentage": 1, "increase_bonus_percentage": 1,
                      "increase_damage": 0, "increase_damage_percentage": 1.208, "increase_skill_damage_percentage": 1.208,
                      "increase_skill_effect_percentage": 1,
                      "decrease_damage_percentage": 1, "decrease_skill_damage_percentage": 1,
                      "special_skill": False}

        , "grengal": {"name": u"伝説の翠緑槍", "level": 10,
                      "increase_life": 0, "increase_attack": 0, "increase_defense": 0, "increase_bonus": 250,
                      "increase_life_percentage": 1, "increase_attack_percentage": 1,
                      "increase_defense_percentage": 1, "increase_bonus_percentage": 1,
                      "increase_damage": 1250, "increase_damage_percentage": 1, "increase_skill_damage_percentage": 1,
                      "increase_skill_effect_percentage": 1,
                      "decrease_damage_percentage": 1, "decrease_skill_damage_percentage": 1,
                      "special_skill": False}

        , "patricia": {"name": u"血染めの剣", "level": 10,
                   "increase_life": 0, "increase_attack": 0, "increase_defense": 0, "increase_bonus": 0,
                   "increase_life_percentage": 1, "increase_attack_percentage": 1, "increase_defense_percentage": 1,
                   "increase_bonus_percentage": 1,
                   "increase_damage": 0, "increase_damage_percentage": 1.26, "increase_skill_damage_percentage": 1.26,
                   "increase_skill_effect_percentage": 1,
                   "decrease_damage_percentage": 1, "decrease_skill_damage_percentage": 1,
                   "special_skill": False}
    }

    CREATURE = {
        "imelda": {"name": u"イメルダ", "rank": "epic", "life": 3600, "attack": 810, "defense": 1075, "bonus": 112}
        , "crystal": {"name": u"クリスタル", "rank": "epic", "life": 5100, "attack": 510, "defense": 1075, "bonus": 112}
        , "melawen": {"name": u"メラウェン", "rank": "epic", "life": 3600, "attack": 510, "defense": 1825, "bonus": 112}
        , "blesilda": {"name": u"ブリシルダ", "rank": "epic", "life": 5100, "attack": 510, "defense": 1075, "bonus": 112}
        , "sialar": {"name": u"シアラー", "rank": "epic", "life": 3600, "attack": 810, "defense": 1075, "bonus": 112}
        , "princess_barbala": {"name": u"皇女バーバラ", "rank": "epic", "life": 3600, "attack": 510, "defense": 1825, "bonus": 112}
        , "inferna": {"name": u"インフェルナ", "rank": "epic", "life": 3600, "attack": 810, "defense": 1075, "bonus": 112}
        , "fiora": {"name": u"フィオラ", "rank": "epic", "life": 5100, "attack": 510, "defense": 1075, "bonus": 112}
        , "chabana": {"name": u"チャバナ", "rank": "epic", "life": 3600, "attack": 510, "defense": 1075, "bonus": 172}
        , "grengal": {"name": u"グレンガル", "rank": "epic", "life": 3600, "attack": 510, "defense": 1075, "bonus": 172}
        , "patricia": {"name": u"パトリシア", "rank": "epic", "life": 3600, "attack": 810, "defense": 1075, "bonus": 112}
    }

    MODEL_ATTACK = {
        "status": [
            {"life": 340, "attack": 155, "defense": 0, "bonus": 0}
            , {"life": 320, "attack": 175, "defense": 0, "bonus": 0}
            , {"life": 300, "attack": 195, "defense": 0, "bonus": 0}
            , {"life": 280, "attack": 215, "defense": 0, "bonus": 0}
        ]
        ,
        "equipment": [
            {"life": 9300, "attack": 3120, "defense": 0, "bonus": 372}
            , {"life": 9300, "attack": 3120, "defense": 4650, "bonus": 0}
        ]
        ,
        "ai": [AI_TECHNICAL]
        ,
        "priorities": [ACT_SKILL_1, ACT_SKILL_2, ACT_ATTACK, ACT_DEFENSE]
        ,
        "skills": [
            ["boomerang", "knife_throwing"]
            , ["boomerang", "lightning_bolt"]
            , ["depth_charge", "knife_throwing"]
            , ["depth_charge", "lightning_bolt"]
            , ["cure_large", "patience"]
            , ["impregnable_defense", "lightning_bolt"]
            , ["regeneration_large", "lightning_bolt"]
        ]
    }

    MODEL_BONUS = {
        "status": [
            {"life": 300, "attack": 0, "defense": 0, "bonus": 195}
            , {"life": 280, "attack": 0, "defense": 0, "bonus": 215}
            , {"life": 260, "attack": 0, "defense": 0, "bonus": 235}
            , {"life": 200, "attack": 0, "defense": 40, "bonus": 255}
            , {"life": 180, "attack": 0, "defense": 60, "bonus": 255}
            , {"life": 180, "attack": 0, "defense": 40, "bonus": 275}
        ]
        ,
        "equipment": [
            {"life": 9300, "attack": 0, "defense": 4650, "bonus": 624}
        ]
        ,
        "ai": [AI_DAMAGE]
        ,
        "priorities": [ACT_ATTACK, ACT_SKILL_1, ACT_SKILL_2, ACT_DEFENSE]
        ,
        "skills": [
            ["boomerang", "knife_throwing"]
            , ["boomerang", "lightning_bolt"]
            , ["depth_charge", "knife_throwing"]
            , ["depth_charge", "lightning_bolt"]
            , ["cure_large", "knife_throwing"]
            , ["cure_medium", "knife_throwing"]
        ]
    }

    MODEL_BONUS_TEC = {
        "status": [
            {"life": 420, "attack": 0, "defense": 0, "bonus": 75}
            , {"life": 360, "attack": 0, "defense": 60, "bonus": 75}
            , {"life": 380, "attack": 0, "defense": 40, "bonus": 75}
            , {"life": 390, "attack": 0, "defense": 0, "bonus": 105}
            , {"life": 340, "attack": 0, "defense": 0, "bonus": 155}
        ]
        ,
        "equipment": [
            {"life": 9300, "attack": 0, "defense": 4650, "bonus": 624}
        ]
        ,
        "ai": [AI_TECHNICAL]
        ,
        "priorities": [ACT_SKILL_1, ACT_SKILL_2, ACT_DEFENSE, ACT_ATTACK]
        ,
        "skills": [
            ["boomerang", "knife_throwing"]
            , ["boomerang", "lightning_bolt"]
            , ["depth_charge", "knife_throwing"]
            , ["cure_large", "knife_throwing"]
            , ["regeneration_medium", "knife_throwing"]
            , ["regeneration_medium", "acid_poison"]
        ]
    }

    MODEL_DEFENSE = {
        "status": [
            {"life": 300, "attack": 0, "defense": 75, "bonus": 120}
            , {"life": 260, "attack": 0, "defense": 115, "bonus": 120}
            , {"life": 200, "attack": 0, "defense": 175, "bonus": 125}
            , {"life": 150, "attack": 0, "defense": 225, "bonus": 120}
            , {"life": 160, "attack": 0, "defense": 115, "bonus": 220}
            , {"life": 300, "attack": 120, "defense": 75, "bonus": 0}
            , {"life": 260, "attack": 120, "defense": 115, "bonus": 0}
            , {"life": 200, "attack": 120, "defense": 175, "bonus": 0}
            , {"life": 150, "attack": 120, "defense": 225, "bonus": 0}
            , {"life": 160, "attack": 220, "defense": 115, "bonus": 0}
        ]
        ,
        "equipment": [
              {"life": 9300, "attack": 1860, "defense": 7800, "bonus": 0}
             , {"life": 9300, "attack": 0, "defense": 7800, "bonus": 372}
        ]
        ,
        "ai": [AI_SAVING, AI_DEFENSE]
        ,
        "priorities": [ACT_DEFENSE, ACT_SKILL_1, ACT_SKILL_2, ACT_ATTACK]
        ,
        "skills": [
            ["regeneration_medium", "acid_poison"]
            , ["choke_wave", "cure_medium"]
            , ["choke_wave", "regeneration_medium"]
            , ["choke_wave", "regeneration_small"]
            , ["regeneration_large", "choke_wave"]
            , ["regeneration_large", "fighting_spirit"]
        ]
    }

    MODEL_BALANCE = {
        "status": [
            {"life": 405, "attack": 100, "defense": 0, "bonus": 0}
            , {"life": 380, "attack": 125, "defense": 0, "bonus": 0}
            , {"life": 340, "attack": 155, "defense": 0, "bonus": 0}
            , {"life": 320, "attack": 175, "defense": 0, "bonus": 0}
            , {"life": 320, "attack": 100, "defense": 75, "bonus": 0}
            , {"life": 300, "attack": 195, "defense": 0, "bonus": 0}
        ]
        ,
        "equipment": [
            {"life": 9300, "attack": 0, "defense": 4650, "bonus": 372}
        ]
        ,
        "ai": [AI_BALANCE]
        ,
        "priorities": [ACT_ATTACK, ACT_SKILL_1, ACT_DEFENSE, ACT_SKILL_2]
        ,
        "skills": [
            ["regeneration_medium", "lightning_bolt"]
            , ["cure_large", "lightning_bolt"]
            , ["fighting_spirit", "patience"]
            , ["regeneration_large", "fighting_spirit"]
        ]
    }

    MODEL_SPEED = {
        "status": [
            {"life": 340, "attack": 155, "defense": 0, "bonus": 0}
            , {"life": 320, "attack": 175, "defense": 0, "bonus": 0}
            , {"life": 320, "attack": 100, "defense": 75, "bonus": 0}
            , {"life": 300, "attack": 195, "defense": 0, "bonus": 0}
            , {"life": 280, "attack": 215, "defense": 0, "bonus": 0}
        ]
        ,
        "equipment": [
            {"life": 9300, "attack": 3120, "defense": 0, "bonus": 372}
            , {"life": 9300, "attack": 3120, "defense": 4650, "bonus": 0}
        ]
        ,
        "ai": [AI_SPEED]
        ,
        "priorities": [ACT_ATTACK, ACT_SKILL_1, ACT_DEFENSE, ACT_SKILL_2]
        ,
        "skills": [
            ["regeneration_medium", "lightning_bolt"]
            , ["cure_large", "lightning_bolt"]
            , ["fighting_spirit", "patience"]
            , ["regeneration_large", "fighting_spirit"]
        ]
    }

    MODEL_KOZO_A = {
        "status": [
            {"life": 405, "attack": 0, "defense": 0, "bonus": 90}
        ]
        ,
        "equipment": [
            {"life": 9150, "attack": 0, "defense": 4613, "bonus": 609}
        ]
        ,
        "ai": [AI_TECHNICAL]
        ,
        "priorities": [ACT_SKILL_1, ACT_SKILL_2, ACT_DEFENSE, ACT_ATTACK]
        ,
        "skills": [
            ["beast_attack", "knife_throwing"]
        ]
    }

    MODEL_KOZO_B = {
        "status": [
            {"life": 340, "attack": 155, "defense": 0, "bonus": 0}
        ]
        ,
        "equipment": [
            {"life": 12650, "attack": 2375, "defense": 0, "bonus": 372}
        ]
        ,
        "ai": [AI_TECHNICAL]
        ,
        "priorities": [ACT_SKILL_1, ACT_SKILL_2, ACT_ATTACK, ACT_DEFENSE]
        ,
        "skills": [
            ["beast_attack", "knife_throwing"]
        ]
    }

    MODEL_NITEN_BAR = {
        "status": [
            {"life": 340, "attack": 0, "defense": 80, "bonus": 75}
        ]
        ,
        "equipment": [
            {"life": 9300, "attack": 0, "defense": 4650, "bonus": 624}
        ]
        ,
        "ai": [AI_TECHNICAL]
        ,
        "priorities": [ACT_SKILL_1, ACT_SKILL_2, ACT_DEFENSE, ACT_ATTACK]
        ,
        "skills": [
            ["regeneration_medium", "knife_throwing"]
        ]
    }

    MODEL_NITEN_CHABANA = {
        "status": [
            {"life": 350, "attack": 0, "defense": 80, "bonus": 65}
        ]
        ,
        "equipment": [
            {"life": 9300, "attack": 0, "defense": 4650, "bonus": 624}
        ]
        ,
        "ai": [AI_TECHNICAL]
        ,
        "priorities": [ACT_SKILL_1, ACT_SKILL_2, ACT_DEFENSE, ACT_ATTACK]
        ,
        "skills": [
            ["beast_attack", "knife_throwing"]
        ]
    }

    MODEL_INFERNA = {
        "status": [
            {"life": 330, "attack": 165, "defense": 0, "bonus": 0}
        ]
        ,
        "equipment": [
            {"life": 13600, "attack": 2700, "defense": 4650, "bonus": 0}
        ]
        ,
        "ai": [AI_BALANCE]
        ,
        "priorities": [ACT_ATTACK, ACT_SKILL_1, ACT_SKILL_2, ACT_DEFENSE]
        ,
        "skills": [
            ["regeneration_large", "fighting_spirit"]
        ]
    }

    MODEL_FIORA = {
        "status": [
            {"life": 330, "attack": 165, "defense": 0, "bonus": 0}
        ]
        ,
        "equipment": [
            {"life": 15600, "attack": 1860, "defense": 4650, "bonus": 0}
        ]
        ,
        "ai": [AI_BALANCE]
        ,
        "priorities": [ACT_ATTACK, ACT_SKILL_1, ACT_SKILL_2, ACT_DEFENSE]
        ,
        "skills": [
            ["regeneration_large", "fighting_spirit"]
        ]
    }

    MODEL_TEST = {
        "status": [
            {"life": 285, "attack": 210, "defense": 0, "bonus": 0}
        ]
        ,
        "equipment": [
            {"life": 15600, "attack": 1860, "defense": 4650, "bonus": 0}
        ]
        ,
        "ai": [AI_TECHNICAL]
        ,
        "priorities": [ACT_SKILL_1, ACT_SKILL_2, ACT_ATTACK, ACT_DEFENSE]
        ,
        "skills": [
            ["boomerang", "acid_poison"]
            , ["depth_charge", "acid_poison"]
            , ["beast_attack", "acid_poison"]
            , ["choke_wave", "acid_poison"]
        ]
    }

    MODEL_TEST2 = {
        "status": [
            {"life": 220, "attack": 155, "defense": 80, "bonus": 0}
            , {"life": 220, "attack": 0, "defense": 80, "bonus": 155}
            , {"life": 250, "attack": 205, "defense": 0, "bonus": 0}
        ]
        ,
        "equipment": [
            {"life": 9300, "attack": 3120, "defense": 4650, "bonus": 0}
            , {"life": 9300, "attack": 0, "defense": 4650, "bonus": 624}
            , {"life": 9300, "attack": 3120, "defense": 0, "bonus": 372}
        ]
        ,
        "ai": [AI_TECHNICAL]
        ,
        "priorities": [ACT_SKILL_1, ACT_SKILL_2, ACT_ATTACK, ACT_DEFENSE]
        ,
        "skills": [
            ["boomerang", "acid_poison"]
            ,["fire_bomb", "tussock_moth"]
            ,["fire_bomb", "acid_poison"]
            ,["depth_charge", "knife_throwing"]
            ,["depth_charge", "acid_poison"]
            ,["beast_attack", "knife_throwing"]
        ]
    }
