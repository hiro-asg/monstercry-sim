from src.const import ICON_ATTACK


class PassiveSkill:
    def __init__(self):
        self.name = ""
        self.increase_life    = 0
        self.increase_attack  = 0
        self.increase_defense = 0
        self.increase_bonus   = 0

        self.increase_life_percentage = 1
        self.increase_attack_percentage = 1
        self.increase_defense_percentage = 1
        self.increase_bonus_percentage = 1

        self.increase_damage = 0
        self.increase_damage_percentage = 1
        self.increase_skill_damage_percentage = 1
        self.increase_skill_effect_percentage = 1

        self.decrease_damage_percentage = 1
        self.decrease_skill_damage_percentage = 1

    def ready(self):
        pass

    #This is applied to attacking
    def get_increased_damage(self, damage):
        return damage * self.increase_damage_percentage + self.increase_damage

    #This is applied to attacking skills
    def get_increased_skill_damage(self, damage):
        return damage * self.increase_skill_damage_percentage

    #This is applied to defense skills, healing skills
    def get_increased_skill_effect(self, damage):
        return damage * self.increase_skill_effect_percentage

    def get_decreased_damage(self, damage):
        return damage * self.decrease_damage_percentage

    def get_decreased_skill_damage(self, damage):
        return damage * self.decrease_skill_damage_percentage

    def before_skill_action(self, creature, icon_type):
        pass

    def after_skill_action(self, creature, icon_type):
        pass


class InfernaSkill(PassiveSkill):
    def __init__(self):
        PassiveSkill.__init__(self)
        self._attacked = False

    def ready(self):
        self._attacked = False
        self.increase_damage_percentage = 1

    def get_increased_damage(self, damage):
        if self._attacked:
            self.increase_damage_percentage += 0.5
        return damage * self.increase_damage_percentage + self.increase_damage

    def after_skill_action(self, creature, icon_type):
        if icon_type == ICON_ATTACK:
            self._attacked = True
        else:
            self._attacked = False


class FioraSkill(PassiveSkill):
    def __init__(self):
        PassiveSkill.__init__(self)

    def ready(self):
        self.increase_damage_percentage = 1

    def before_skill_action(self, creature, icon_type):
        if icon_type == ICON_ATTACK and float(creature.current_life) / creature.life <= 0.6:
            self.increase_damage_percentage += 0.6