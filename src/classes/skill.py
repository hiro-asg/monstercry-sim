class Skill:
    def __init__(self):
        self.name = ""
        self.level = 0
        self.cost = 0

        self.duration = 1
        self.cool_time = 0
        self.used = 0
        self.active = 0 #set duration and then decrement 1 by 1 turn
        self.wait   = 0 #set cool_time and then decrement 1 by 1 turn. The skill can be used again when wait is 0

        self.damage = 0
        self.defense = 0
        self.heal = 0
        self.attack_up = 0

    def ready(self):
        self.active = 0
        self.wait = 0
        self.used = 0

    def use(self):
        self.active = self.duration
        self.wait   = self.cool_time
        self.used += 1

    def get_skill_damage(self):
        if self.damage == 0:
            return 0

        if self.active > 0:
            return self.damage

        return 0

    def get_skill_defense(self):
        if self.defense == 0:
            return 0

        if self.active > 0:
            adjust = 0.5 if self.used >= 6 else 1.1 - self.used * 0.1
            return self.defense * adjust

        return 0

    def get_skill_heal(self):
        if self.heal == 0:
            return 0

        if self.active > 0:
            adjust = 0.5 if self.used >= 6 else 1.1 - self.used * 0.1
            return self.heal * adjust

        return 0

    def get_skill_attack_up(self):
        if self.attack_up == 0:
            return 0

        if self.active > 0:
            return self.attack_up

        return 0

    def turn_end(self):
        self.active = 0 if self.active - 1 <= 0 else self.active - 1
        self.wait   = 0 if self.wait - 1 <= 0 else self.wait - 1