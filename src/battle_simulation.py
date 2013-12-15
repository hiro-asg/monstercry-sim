#!/usr/bin/env python
#!-*- coding:utf-8 -*-

import random
from src.classes.ai import Ai
from src.classes.creature import Creature
from src.classes.equipment import Equipment
from src.classes.skill import Skill
from src.classes.status import Status
from src.const import *
from src.creature_action_recorder import CreatureActionRecoder


class BattleSimulation:
    def __init__(self):
        self._statistics = False
        pass

    @staticmethod
    def _create_creature(creature_id, skill_1, skill_2, status, equipment, ai):

        def set_skill(target_skill, target_skill_data):
            target_skill.name = target_skill_data["name"]
            target_skill.cost = target_skill_data["cost"]
            target_skill.duration = target_skill_data["duration"]
            target_skill.cool_time = target_skill_data["cool_time"]
            target_skill.level = target_skill_data["level"]
            target_skill.damage = target_skill_data["damage"]
            target_skill.defense = target_skill_data["defense"]
            target_skill.heal = target_skill_data["heal"]
            target_skill.attack_up = target_skill_data["attack_up"]

        creature_data = Const.CREATURE[creature_id]
        if not creature_data:
            raise Exception("Creature id is not found. id:" + creature_id)

        creature = Creature()
        creature.name = creature_data["name"]

        #Base status
        creature.base_life = creature_data["life"]
        creature.base_attack = creature_data["attack"]
        creature.base_defense = creature_data["defense"]
        creature.base_bonus = creature_data["bonus"]

        #Status parameter point
        if not status:
            status = Status()
        creature.life_point = status.life
        creature.attack_point = status.attack
        creature.defense_point = status.defense
        creature.bonus_point = status.bonus

        passive_skill_data = Const.PASSIVE_SKILL[creature_id]
        if passive_skill_data:
            if passive_skill_data["special_skill"]:
                passive_skill = Const
            else:
                passive_skill = PassiveSkill()
            passive_skill.name = passive_skill_data["name"]
            passive_skill.increase_life = passive_skill_data["increase_life"]
            passive_skill.increase_attack = passive_skill_data["increase_attack"]
            passive_skill.increase_defense = passive_skill_data["increase_defense"]
            passive_skill.increase_bonus = passive_skill_data["increase_bonus"]
            passive_skill.increase_life_percentage = passive_skill_data["increase_life_percentage"]
            passive_skill.increase_attack_percentage = passive_skill_data["increase_attack_percentage"]
            passive_skill.increase_defense_percentage = passive_skill_data["increase_defense_percentage"]
            passive_skill.increase_bonus_percentage = passive_skill_data["increase_bonus_percentage"]
            passive_skill.increase_damage = passive_skill_data["increase_damage"]
            passive_skill.increase_damage_percentage = passive_skill_data["increase_damage_percentage"]
            passive_skill.increase_skill_damage_percentage = passive_skill_data["increase_skill_damage_percentage"]
            passive_skill.increase_skill_effect_percentage = passive_skill_data["increase_skill_effect_percentage"]
            passive_skill.decrease_damage_percentage = passive_skill_data["decrease_damage_percentage"]
            passive_skill.decrease_skill_damage_percentage = passive_skill_data["decrease_skill_damage_percentage"]
        else:
            passive_skill = PassiveSkill()

        creature.passive_skill = passive_skill
        creature.equipment = equipment if equipment else Equipment()
        creature.ready()

        skill_data = Const.SKILL[skill_1]
        if skill_data:
            skill = Skill()
            set_skill(skill, skill_data)
            creature.skill_1 = skill

        skill_data = Const.SKILL[skill_2]
        if skill_data:
            skill = Skill()
            set_skill(skill, skill_data)
            creature.skill_2 = skill

        creature.ai = ai

        return creature

    def start_duel(self, handler):
        #OWNER
        status = Status()
        status.life = 280
        status.attack = 215
        status.defense = 0
        status.bonus = 0

        equipment = Equipment()
        equipment.life = 11325
        equipment.attack = 2775
        equipment.defense = 0
        equipment.bonus = 372

        ai = Ai()
        ai.type = AI_TECHNICAL
        ai.set_priorities(ACT_SKILL_2, ACT_SKILL_1, ACT_ATTACK, ACT_DEFENSE)

        owner = self._create_creature("imelda", "knife_throwing", "boomerang", status, equipment, ai)

        #OPPONENT
        status = Status()
        status.life = 200
        status.attack = 295
        status.defense = 0
        status.bonus = 0

        equipment = Equipment()
        equipment.life = 11025
        equipment.attack = 2670
        equipment.defense = 0
        equipment.bonus = 372

        ai = Ai()
        ai.type = AI_TECHNICAL
        ai.set_priorities(ACT_SKILL_2, ACT_SKILL_1, ACT_ATTACK, ACT_DEFENSE)

        opponent = self._create_creature("imelda", "knife_throwing", "boomerang", status, equipment, ai)

        handler.response.write(owner.name + "(PLAYER 1) vs " + opponent.name + "(PLAYER 2)</br></br>")

        handler.response.write(owner.name + "(PLAYER 1):</br>")
        handler.response.write(u"体力　　：" + str(int(owner.life)) + "</br>")
        handler.response.write(u"攻撃力　：" + str(int(owner.attack)) + "</br>")
        handler.response.write(u"防御力　：" + str(int(owner.defense)) + "</br>")
        handler.response.write(u"ボーナス：" + str(int(owner.bonus)) + "</br>")
        handler.response.write(u"スキル１：" + owner.skill_1.name + "</br>")
        handler.response.write(u"スキル２：" + owner.skill_2.name + "</br>")
        handler.response.write("</br>")

        handler.response.write(opponent.name + "(PLAYER 2):</br>")
        handler.response.write(u"体力　　：" + str(int(opponent.life)) + "</br>")
        handler.response.write(u"攻撃力　：" + str(int(opponent.attack)) + "</br>")
        handler.response.write(u"防御力　：" + str(int(opponent.defense)) + "</br>")
        handler.response.write(u"ボーナス：" + str(int(opponent.bonus)) + "</br>")
        handler.response.write(u"スキル１：" + opponent.skill_1.name + "</br>")
        handler.response.write(u"スキル２：" + opponent.skill_2.name + "</br>")

        handler.response.write("-------------------------------------------------</br>")

        turn = 1
        while self._fight(handler, owner, opponent, turn):
            turn += 1
            pass

    def _fight(self, handler, owner, opponent, turn):

        def get_supplied_icon_log(creature):
            ret = ""
            for i in range(creature.action_icons.icon_attack):
                ret += u"†"
            for i in range(creature.action_icons.icon_skill):
                ret += u"☆"
            for i in range(creature.action_icons.icon_defense):
                ret += u"○"
            return ret

        def write_icon_log(creature, role, supplied_icon_log):
            handler.response.write(creature.name + self._enclose(role) + " Icons: " + supplied_icon_log)

            if creature.action.icon == ICON_ATTACK:
                icon_mark = u"†"
            elif creature.action.icon == ICON_SKILL:
                icon_mark = u"☆"
            elif creature.action.icon == ICON_DEFENSE:
                icon_mark = u"○"

            str_used_icons = ""
            for i in range(creature.action.quantity):
                str_used_icons += icon_mark

            if creature.action.type == TYPE_USE:
                str_used_icons += u"を使用"
            elif creature.action.type == TYPE_DISCARD:
                str_used_icons += u"を破棄"

            handler.response.write(self._enclose(str_used_icons))
            handler.response.write("</br>")

        if turn == 1:
            owner_recorder = CreatureActionRecoder()
            opponent_recorder = CreatureActionRecoder()

        self._supply_icons(owner)
        self._supply_icons(opponent)

        if not self._statistics:
            owner_icon_log = get_supplied_icon_log(owner)
            opponent_icon_log = get_supplied_icon_log(opponent)

        owner.act_one_turn()
        opponent.act_one_turn()

        if not self._statistics:
            write_icon_log(owner, ROLE_1, owner_icon_log)
            write_icon_log(opponent, ROLE_2, opponent_icon_log)

        self._reflect_action_result(handler, owner, opponent)

        return self._turn_end(handler, owner, ROLE_1, opponent, ROLE_2)

    def _supply_icons(self, creature):
        for i in range(3):
            if creature.action_icons.total_icons() == 5:
                return
            icon = self._make_icons()
            if icon == ICON_ATTACK:
                creature.action_icons.icon_attack += 1
            elif icon == ICON_DEFENSE:
                creature.action_icons.icon_defense += 1
            elif icon == ICON_SKILL:
                creature.action_icons.icon_skill += 1
            else:
                raise Exception("Unexpected icon status.")

    @staticmethod
    def _make_icons():
        rand = random.random()
        if rand <= PROBABILITIES[ICON_ATTACK]:
            return ICON_ATTACK
        rand -= PROBABILITIES[ICON_ATTACK]
        if rand <= PROBABILITIES[ICON_SKILL]:
            return ICON_SKILL
        rand -= PROBABILITIES[ICON_SKILL]
        if rand <= PROBABILITIES[ICON_DEFENSE]:
            return ICON_DEFENSE
        return None

    def _reflect_action_result(self, handler, owner, opponent):
        def write_action_log(creature, role):
            def write_heal_log():
                if creature.skill_1.get_skill_heal() > 0 and creature.skill_1.active > 0:
                    skill_effect_remain_message = ""
                    if creature.skill_1.active > 1:
                        skill_effect_remain_message = u"（効果残り " + str(creature.skill_1.active - 1) + u" ターン）"
                    handler.response.write(
                        creature.name + self._enclose(role) + u"：[回復(" + creature.skill_1.name + ")] " + str(
                            creature.skill_1.get_skill_heal()) + u" 回復。" + skill_effect_remain_message + "</br>")

                if creature.skill_2.get_skill_heal() > 0 and creature.skill_2.active > 0:
                    skill_effect_remain_message = ""
                    if creature.skill_2.active > 1:
                        skill_effect_remain_message = u"（効果残り " + str(creature.skill_2.active - 1) + u" ターン）"
                    handler.response.write(
                        creature.name + self._enclose(role) + u"：[回復(" + creature.skill_2.name + ")] " + str(
                            creature.skill_2.get_skill_heal()) + u" 回復。" + skill_effect_remain_message + "</br>")

            def write_defense_log():
                if creature.skill_1.get_skill_defense() > 0 and creature.skill_1.active > 0:
                    handler.response.write(
                        creature.name + self._enclose(role) + u"：[スキル(" + creature.skill_1.name + ")] " + str(
                            creature.skill_1.get_skill_defense()) + u" 防御値上昇。</br>")
                elif creature.skill_2.get_skill_defense() > 0 and creature.skill_2.active > 0:
                    handler.response.write(
                        creature.name + self._enclose(role) + u"：[スキル(" + creature.skill_2.name + ")] " + str(
                            creature.skill_2.get_skill_defense()) + u" 防御値上昇。</br>")
                else:
                    handler.response.write(creature.name + self._enclose(role) + u"：[防御]" + str(
                        creature.action_result.defense) + u" 防御値上昇。</br>")

            def write_attack_log():
                damage = int(opponent.passive_skill.get_decreased_damage(creature.action_result.attack_damage))
                damage_resist_message = self._enclose(u"ダメージ減:" + str(
                    creature.action_result.attack_damage - damage)) if creature.action_result.attack_damage - damage > 0 else ""
                handler.response.write(creature.name + self._enclose(role) + u"：[攻撃]" + str(
                    creature.action_result.attack_damage) + damage_resist_message + u" ダメージ。</br>")

            def write_skill_damage_log():
                if creature.skill_1.get_skill_damage() > 0 and creature.skill_1.active > 0:
                    skill_effect_remain_message = ""
                    if creature.skill_1.active > 1:
                        skill_effect_remain_message = u"（効果残り " + str(creature.skill_1.active - 1) + u" ターン）"
                    handler.response.write(
                        creature.name + self._enclose(role) + u"：[スキル(" + creature.skill_1.name + ")] " + str(
                            creature.skill_1.get_skill_damage()) + u" ダメージ。" + skill_effect_remain_message + "</br>")

                if creature.skill_2.get_skill_damage() > 0 and creature.skill_2.active > 0:
                    skill_effect_remain_message = ""
                    if creature.skill_2.active > 1:
                        skill_effect_remain_message = u"（効果残り " + str(creature.skill_2.active - 1) + u" ターン）"
                    handler.response.write(
                        creature.name + self._enclose(role) + u"：[スキル(" + creature.skill_2.name + ")] " + str(
                            creature.skill_2.get_skill_damage()) + u" ダメージ。" + skill_effect_remain_message + "</br>")

            def write_damage_up_log():
                if creature.skill_1.get_skill_attack_up() > 0 and creature.skill_1.active > 0:
                    if creature.skill_1.active == creature.skill_1.duration:
                        handler.response.write(
                            creature.name + self._enclose(role) + u"：[スキル(" + creature.skill_1.name + ")] " + str(
                                creature.skill_1.get_skill_damage_up()) + u" 攻撃力アップ(次ターンより有効)。</br>")
                    else:
                        skill_effect_remain_message = ""
                        if creature.skill_1.active > 1:
                            skill_effect_remain_message = u"（効果残り " + str(creature.skill_1.active - 1) + u" ターン）"
                        handler.response.write(
                            creature.name + self._enclose(role) + u"：[スキル(" + creature.skill_1.name + ")] " + str(
                                creature.skill_1.get_skill_damage_up()) + u" 攻撃力アップ中。" + skill_effect_remain_message + "</br>")

                if creature.skill_2.get_skill_attack_up() > 0 and creature.skill_2.active > 0:
                    if creature.skill_2.active == creature.skill_2.duration:
                        handler.response.write(
                            creature.name + self._enclose(role) + u"：[スキル(" + creature.skill_2.name + ")] " + str(
                                creature.skill_2.get_skill_damage_up()) + u" 攻撃力アップ(次ターンより有効)。</br>")
                    else:
                        skill_effect_remain_message = ""
                        if creature.skill_2.active > 1:
                            skill_effect_remain_message = u"（効果残り " + str(creature.skill_2.active - 1) + u" ターン）"
                        handler.response.write(
                            creature.name + self._enclose(role) + u"：[スキル(" + creature.skill_2.name + ")] " + str(
                                creature.skill_2.get_skill_damage_up()) + u" 攻撃力アップ中。" + skill_effect_remain_message + "</br>")

            if creature.action_result.heal > 0:
                write_heal_log()

            if creature.action_result.defense > 0:
                write_defense_log()

            if creature.action_result.attack_damage > 0:
                write_attack_log()

            if creature.action_result.skill_damage > 0:
                write_skill_damage_log()

            if creature.action_result.attack_up > 0:
                write_damage_up_log()

        def reflect_action_defense(creature, role):
            if creature.action_result.heal > 0:
                if creature.current_life > creature.life:
                    creature.current_life = creature.life
                else:
                    creature.current_life += creature.action_result.heal

            if creature.action_result.defense > 0:
                creature.current_defense = creature.action_result.defense

        def reflect_action_offence(owner, opponent, role):
            if owner.action_result.attack_damage > 0:
                damage = int(opponent.passive_skill.get_decreased_damage(owner.action_result.attack_damage))
                defense = opponent.current_defense - damage
                if defense < 0:
                    final_damage = abs(defense)
                else:
                    final_damage = 0
                opponent.current_defense = 0 if defense < 0 else defense
                opponent.current_life -= final_damage

            if owner.action_result.skill_damage > 0:
                skill_damage = owner.passive_skill.get_decreased_skill_damage(owner.action_result.skill_damage)
                defense = opponent.current_defense - skill_damage
                if defense < 0:
                    final_skill_damage = abs(defense)
                else:
                    final_skill_damage = 0
                opponent.current_defense = 0 if defense < 0 else defense
                opponent.current_life -= final_skill_damage

            owner.attack_up = owner.action_result.attack_up

        reflect_action_defense(owner, ROLE_1)
        reflect_action_defense(opponent, ROLE_2)

        reflect_action_offence(owner, opponent, ROLE_1)
        reflect_action_offence(opponent, owner, ROLE_2)

        if not self._statistics:
            write_action_log(owner, ROLE_1)
            write_action_log(opponent, ROLE_2)

        if owner.skill_1:
            owner.skill_1.turn_end()
        if owner.skill_2:
            owner.skill_2.turn_end()

        if opponent.skill_1:
            opponent.skill_1.turn_end()
        if opponent.skill_2:
            opponent.skill_2.turn_end()

    def _turn_end(self, handler, owner, owner_role, opponent, opponent_role):
        """
            Returns:
               True: The fight continues
               False: The fight ends
        """
        handler.response.write(owner.name + self._enclose(owner_role) + u" ― 体力:" + str(int(owner.current_life)) \
                               + u" 攻撃力:" + str(int(owner.attack + owner.attack_up)) \
                               + u" 防御力:" + str(int(owner.current_defense)) \
                               + self._enclose(str(int(owner.current_defense_max))))
        handler.response.write("</br>")

        handler.response.write(
            opponent.name + self._enclose(opponent_role) + u" ― 体力:" + str(int(opponent.current_life)) \
            + u" 攻撃力:" + str(int(opponent.attack + owner.attack_up)) \
            + u" 防御力:" + str(int(opponent.current_defense)) + self._enclose(str(int(opponent.current_defense_max))))
        handler.response.write("</br>")

        if owner.current_life <= 0:
            handler.response.write("</br>")
            if opponent.current_life <= 0:
                handler.response.write("引き分け")
            else:
                handler.response.write("負け")
            return False
        elif opponent.current_life <= 0:
            handler.response.write("</br>")
            handler.response.write("勝ち")
            return False

        handler.response.write("</br>")

        return True

    @staticmethod
    def _enclose(message):
        return "(" + message + ")"

