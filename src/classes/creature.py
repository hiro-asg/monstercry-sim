#!/usr/bin/env python
#!-*- coding:utf-8 -*-

from src.const import *


class Creature:
    def __init__(self):
        #Basic status
        self.__name = ""
        self.__passive_skill = None
        self.__skill_1 = None
        self.__skill_2 = None
        self.__ai = None

        #Base parameters
        self.__base_life = 0
        self.__base_attack = 0
        self.__base_defense = 0
        self.__base_bonus = 0

        #Status point
        self.__life_point  = 0
        self.__attack_point  = 0
        self.__defense_point  = 0
        self.__bonus_point  = 0

        #Equipments
        self.__equipment = None

        #Parameters after applied skill effects and equipments
        self.__life = 0
        self.__attack = 0
        self.__defense = 0
        self.__bonus = 0

        #
        self.__attack_up = 0

        #icon parameters
        self.action_icons = ActionIcons()

        self.action_result = None

        #number of actions
        self.attack_use  = 0
        self.defense_use = 0

        self.current_life = 0
        self.current_defense = 0
        self.current_defense_max = 0

        self._action = None

    #Getter
    @property
    def name(self):
        return self.__name

    @property
    def base_life(self):
        return self.__base_life

    @property
    def  base_attack(self):
        return self.__base_attack

    @property
    def base_defense(self):
        return self.__base_defense

    @property
    def base_bonus(self):
        return self.__base_bonus

    @property
    def life_point(self):
        return self.__life_point

    @property
    def attack_point(self):
        return self.__attack_point

    @property
    def defense_point(self):
        return self.__defense_point

    @property
    def bonus_point(self):
        return self.__bonus_point

    @property
    def equipment(self):
        return self.__equipment

    @property
    def passive_skill(self):
        return self.__passive_skill

    @property
    def skill_1(self):
        return self.__skill_1

    @property
    def skill_2(self):
        return self.__skill_2

    @property
    def ai(self):
        return self.__ai

    @property
    def life(self):
        return self.__life

    @property
    def attack(self):
        return self.__attack

    @property
    def defense(self):
        return self.__defense

    @property
    def bonus(self):
        return self.__bonus

    @property
    def action(self):
        return self._action

    #Setter
    @name.setter
    def name(self, value):
        self.__name = value

    @base_life.setter
    def base_life(self, value):
        self.__base_life = value

    @base_attack.setter
    def base_attack(self, value):
        self.__base_attack = value

    @base_defense.setter
    def base_defense(self, value):
        self.__base_defense = value

    @base_bonus.setter
    def base_bonus(self, value):
        self.__base_bonus = value

    @life_point.setter
    def life_point(self, value):
        self.__life_point = value

    @attack_point.setter
    def attack_point(self, value):
        self.__attack_point = value

    @defense_point.setter
    def defense_point(self, value):
        self.__defense_point = value

    @bonus_point.setter
    def bonus_point(self, value):
        self.__bonus_point = value

    @property
    def attack_up(self):
        return self.__attack_up

    @equipment.setter
    def equipment(self, value):
        self.__equipment = value

    @passive_skill.setter
    def passive_skill(self, value):
        self.__passive_skill = value

    @skill_1.setter
    def skill_1(self, value):
        self.__skill_1 = value

    @skill_2.setter
    def skill_2(self, value):
        self.__skill_2 = value

    @ai.setter
    def ai(self, value):
        self.__ai = value

    @life.setter
    def life(self, value):
        self.__life = value

    @attack.setter
    def attack(self, value):
        self.__attack = value

    @defense.setter
    def defense(self, value):
        self.__defense = value

    @bonus.setter
    def bonus(self, value):
        self.__bonus = value

    @attack_up.setter
    def attack_up(self, value):
        self.__attack_up = value

    #Must be called before the battle
    def ready(self):

        self.validate()

        self.attack_use = 0
        self.defense_use = 0
        self.action_icons = ActionIcons()

        if self.passive_skill:
            self.passive_skill.ready()

        if self.skill_1:
            self.skill_1.ready()

        if self.skill_2:
            self.skill_2.ready()

        self.life = self.base_life * self.passive_skill.increase_life_percentage \
                    + self.life_point * 50 + self.passive_skill.increase_life \
                    + self.equipment.life
        self.current_life = self.life
        self.attack = self.base_attack * self.passive_skill.increase_attack_percentage\
                    + self.attack_point * 10 + self.passive_skill.increase_attack\
                    + self.equipment.attack
        self.defense = self.base_defense * self.passive_skill.increase_defense_percentage\
                    + self.defense_point * 25 + self.passive_skill.increase_defense\
                    + self.equipment.defense
        self.current_defense_max = self.defense
        self.bonus = self.base_bonus * self.passive_skill.increase_bonus_percentage\
                    + self.bonus_point * 2 + self.passive_skill.increase_bonus\
                    + self.equipment.bonus

    #Set parameters on ActionResult of one turn which contains damages heal points
    #ActionResult will be used by BattleSimulation
    def act_one_turn(self):
        def get_defense_adjustment():
            if self.defense_use >= 5:
                return 0.5
            else:
                return 1 - self.defense_use * 0.1

        self._action = self.ai.choose_action(self.action_icons.get_icons_list(), self.skill_1, self.skill_2, float(self.current_defense) / self.defense)

        self.passive_skill.before_skill_action(self, self._action.icon)
        action_result = ActionResult()
        if self._action.type == TYPE_DISCARD:
            if self._action.icon == ICON_DEFENSE:
                self.action_icons.icon_defense -= self._action.quantity
            elif self._action.icon == ICON_SKILL:
                self.action_icons.icon_skill -= self._action.quantity
            elif self._action.icon == ICON_DISCARD_SKILL_DEFENSE:
                self.action_icons.icon_skill = 0
                self.action_icons.icon_defense = 0
            else:
                raise Exception("Unexpected icon :" + str(self._action.icon))
        else:
            if self._action.act == ACT_ATTACK:
                self.action_icons.icon_attack -= self._action.quantity
                action_result.attack_damage = int(self.passive_skill.get_increased_damage((self.attack + self.attack_up) * self._get_attack_rate(self._action.quantity) + self.bonus * self._get_bonus_rate(self._action.quantity)))
                self.attack_use += 1
            elif self._action.act == ACT_DEFENSE:
                self.action_icons.icon_defense -= self._action.quantity
                defense_adjust = get_defense_adjustment()
                action_result.defense = int(self.defense * defense_adjust * (0.9 + self._action.quantity / 10.0))
                self.defense_use += 1
                #Change max defense value for reuse
                defense_adjust = get_defense_adjustment()
                self.current_defense_max = int(self.defense * defense_adjust)
            elif self._action.act == ACT_SKILL_1:
                self.action_icons.icon_skill -= self._action.quantity
                if self.skill_1:
                    self.skill_1.use()
            elif self._action.act == ACT_SKILL_2:
                self.action_icons.icon_skill -= self._action.quantity
                if self.skill_2:
                    self.skill_2.use()
            else:
                raise Exception("Unexpected icon :" + str(self._action.icon))

        if self.skill_1 and self.skill_1.active > 0:
            action_result.skill_damage += int(self.passive_skill.get_increased_skill_damage(self.skill_1.get_skill_damage()))
            action_result.heal += self.skill_1.get_skill_heal()
            if self.skill_1.get_skill_defense() > 0:
                action_result.defense = self.skill_1.get_skill_defense()
            action_result.attack_up += self.skill_1.get_skill_attack_up()

        if self.skill_2 and self.skill_2.active > 0:
            action_result.skill_damage += int(self.passive_skill.get_increased_skill_damage(self.skill_2.get_skill_damage()))
            action_result.heal += self.skill_2.get_skill_heal()
            if self.skill_2.get_skill_defense() > 0:
                action_result.defense = self.skill_2.get_skill_defense()
            action_result.attack_up += self.skill_2.get_skill_attack_up()

        self.passive_skill.after_skill_action(self, self._action.icon)

        self.action_result = action_result

    def validate(self):
        if not self.equipment:
            raise CreateCreatureException("Equipment is None.")
        if not self.passive_skill:
            raise CreateCreatureException("Passive skill is None.")

    @staticmethod
    def _get_attack_rate(icon_num):
        if icon_num <= 1:
            return 0.5
        return 1

    @staticmethod
    def _get_bonus_rate(icon_num):
        if icon_num == 1:
            return 0
        return 2 ** (icon_num - 1)


class ActionResult:
    def __init__(self):
        self.attack_damage  = 0
        self.skill_damage  = 0
        self.heal    = 0
        self.defense = 0
        self.attack_up = 0


class ActionIcons:
    def __init__(self):
        self.icon_attack = 0
        self.icon_skill  = 0
        self.icon_defense = 0

    def get_icons_list(self):
        return [self.icon_attack, self.icon_skill, self.icon_defense]

    def total_icons(self):
        sum = 0
        for val in self.get_icons_list():
            sum += val
        return sum


class CreateCreatureException(Exception):
    pass