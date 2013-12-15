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

    #This is applied to attacking
    def get_increased_damage(self, damage):
        return damage * self.increase_damage_percentage + self.increase_damage

    #This is applied to attacking skills
    def get_increased_skill_damage(self, damage):
        return damage * self.increase_damage_percentage

    #This is applied to defense skills, healing skills
    def get_increased_skill_effect(self, damage):
        return damage * self.increase_skill_effect_percentage

    def get_decreased_damage(self, damage):
        return damage * self.decrease_damage_percentage

    def get_decreased_skill_damage(self, damage):
        return damage * self.decrease_skill_damage_percentage


