# coding=utf-8

from src.const import *

class Ai:
    def __init__(self):
        self.type = AI_NORMAL
        self._priority_1 = ACT_ATTACK
        self._priority_2 = ACT_SKILL_1
        self._priority_3 = ACT_SKILL_2
        self._priority_4 = ACT_DEFENSE
        self._priorities = [self._priority_1, self._priority_2, self._priority_3, self._priority_4]
        self.defense_ratio = 0

    def get_priority_name(self):
        message = ""
        for i in range(len(self._priorities)):
            if message != "":
                message += ">"
            if self._priorities[i] == ACT_ATTACK:
                message += u"攻撃"
            elif self._priorities[i] == ACT_SKILL_1:
                message += u"スキル１"
            elif self._priorities[i] == ACT_SKILL_2:
                message += u"スキル２"
            elif self._priorities[i] == ACT_DEFENSE:
                message += u"ディフェンス"
        return message

    def set_priorities_each(self, priority_1, priority_2, priority_3, priority_4):
        self._priority_1 = priority_1
        self._priority_2 = priority_2
        self._priority_3 = priority_3
        self._priority_4 = priority_4
        self._priorities = [priority_1, priority_2, priority_3, priority_4]

    def set_priorities(self, priorities):
        self.set_priorities_each(priorities[0], priorities[1], priorities[2], priorities[3])

    def choose_action(self, actions, skill_1, skill_2, defense_ratio):
        action = None
        if self.type == AI_BALANCE:
            action = self._choose_balance_action(actions)
        elif self.type == AI_SPEED:
            pass
        elif self.type == AI_TECHNICAL:
            pass
        elif self.type == AI_DEFENSE:
            pass
        elif self.type == AI_SAVING:
            action = self._choose_saving_action(actions, defense_ratio)
        elif self.type == AI_DAMAGE:
            pass
        elif self.type == AI_LETHAL:
            pass

        if action:
            return action

        return self._choose_normal_action(actions, skill_1, skill_2, defense_ratio)

    def _choose_normal_action(self, actions, skill_1, skill_2, defense_ratio):
        #Desides the action by priority
        for priority in self._priorities:
            if priority == ACT_ATTACK:
                attack_condition = 2
                if self.type == AI_DAMAGE:
                    attack_condition = 4
                if self.type == AI_LETHAL:
                    attack_condition = 5

                if actions[ICON_INDEX[ACT_ATTACK]] >= attack_condition:
                        action = Action()
                        action.act = ACT_ATTACK
                        action.icon = ICON_INDEX[ACT_ATTACK]
                        action.quantity = actions[ICON_INDEX[ACT_ATTACK]]
                        return action

            if priority == ACT_SKILL_1:
                if (skill_1
                    and actions[ICON_INDEX[ACT_SKILL_1]] >= skill_1.cost
                    and skill_1.wait == 0):
                        action = Action()
                        action.act = ACT_SKILL_1
                        action.icon = ICON_INDEX[ACT_SKILL_1]
                        action.quantity = skill_1.cost
                        return action

            if priority == ACT_SKILL_2:
                if (skill_2
                    and actions[ICON_INDEX[ACT_SKILL_2]] >= skill_2.cost
                    and skill_2.wait == 0):
                        action = Action()
                        action.act = ACT_SKILL_2
                        action.icon = ICON_INDEX[ACT_SKILL_2]
                        action.quantity = skill_2.cost
                        return action

            if priority == ACT_DEFENSE:
                if (actions[ICON_INDEX[ACT_DEFENSE]] >= 1
                    and defense_ratio <= self.defense_ratio):
                        action = Action()
                        action.act = ACT_DEFENSE
                        action.icon = ICON_INDEX[ACT_DEFENSE]
                        action.quantity = actions[ICON_INDEX[ACT_DEFENSE]]
                        return action

        #Attack with one attack icon
        if actions[ICON_INDEX[ACT_ATTACK]] > 0:
            action = Action()
            action.act = ACT_ATTACK
            action.icon = ACT_ATTACK
            action.quantity = actions[ICON_INDEX[ACT_ATTACK]]
            return action

        #Discard icon(s)
        for priority in reversed(self._priorities):
            if self.type == AI_DAMAGE or self.type == AI_LETHAL:
                action = Action()
                action.type = TYPE_DISCARD
                action.act = ACT_DISCARD_SKILL_DEFENSE
                action.icon = ICON_INDEX[ACT_DISCARD_SKILL_DEFENSE]
                action.quantity = actions[ICON_SKILL] + actions[ICON_DEFENSE]
                return action

            if priority == ACT_SKILL_1:
                action = Action()
                action.type = TYPE_DISCARD
                action.act = ACT_SKILL_1
                action.icon = ICON_INDEX[ACT_SKILL_1]
                action.quantity = 3 if actions[ICON_INDEX[ACT_SKILL_1]] > 3 else actions[ICON_INDEX[ACT_SKILL_1]]
                return action

            if priority == ACT_SKILL_2:
                action = Action()
                action.type = TYPE_DISCARD
                action.act = ACT_SKILL_2
                action.icon = ICON_INDEX[ACT_SKILL_2]
                action.quantity = 3 if actions[ICON_INDEX[ACT_SKILL_2]] > 3 else actions[ICON_INDEX[ACT_SKILL_2]]
                return action

            if priority == ACT_DEFENSE:
                action = Action()
                action.type = TYPE_DISCARD
                action.act = ACT_DEFENSE
                action.icon = ICON_INDEX[ACT_DEFENSE]
                action.quantity = 3 if actions[ICON_INDEX[ACT_DEFENSE]] > 3 else actions[ICON_INDEX[ACT_DEFENSE]]
                return action

    @staticmethod
    def _choose_balance_action(actions):
        attack = actions[ICON_INDEX[ACT_ATTACK]]

        if attack >= 2:
            action = Action()
            action.act = ACT_ATTACK
            action.icon = ICON_INDEX[ACT_ATTACK]
            action.quantity = 2
            return action
        return None

    def _choose_saving_action(self, actions, defense_ratio):
        defense = actions[ICON_INDEX[ACT_DEFENSE]]

        if defense >= 1:
            if actions[ICON_INDEX[ACT_DEFENSE]] >= 1 \
                and defense_ratio <= self.defense_ratio:
                action = Action()
                action.act = ACT_DEFENSE
                action.icon = ICON_INDEX[ACT_DEFENSE]
                action.quantity = 1
                return action
        return None


class Action:
    def __init__(self):
        self.type = TYPE_USE
        self.act = ACT_ATTACK
        self.icon = ICON_ATTACK
        self.quantity = 0
