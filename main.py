from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        """ Выполнить атаку и вернуть количество наносимого урона. """
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")
        print("Монстр побежден!")
        return 50

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")
        print("Монстр побежден!")
        return 30

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self, monster):
        """ Атаковать монстра, используя текущее оружие. """
        damage = self.weapon.attack()
        monster.health -= damage
        if monster.is_defeated():
            print("Монстр побежден!")

class Monster:
    def __init__(self):
        self.health = 100

    def is_defeated(self):
        return self.health <= 0

def battle_demo():
    fighter = Fighter(Sword())
    monster = Monster()

    print("Боец выбирает меч.")
    fighter.fight(monster)

    if not monster.is_defeated():
        fighter.change_weapon(Bow())
        print("\nБоец выбирает лук.")
        fighter.fight(monster)


battle_demo()


