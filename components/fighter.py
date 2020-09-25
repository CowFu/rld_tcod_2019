class Fighter:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner})

        return results

    def attack(self, target):
        damage = self.power - target.fighter.defense

        if damage > 0:
            target.fighter.take_damage(damage)
            print('%s attacks %s for %d hitpoints.' %
                  (self.owner.name.capitalize(), target.name, damage))
        else:
            print('%s attacks %s for no damage.' %
                  (self.owner.name.capitalize(), target.name))
