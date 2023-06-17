class Wizard:
    def __init__(self, name, health, mana, magic_power):
        self.name = name
        self.health = health
        self.mana = mana
        self.magic_power = magic_power

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            return self.magic_power
        else:
            return 0


class Fighter:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self):
        return self.strength


class Monster:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self):
        return self.strength


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Game:
    def __init__(self):
        self.player = None
        self.monster = None
        self.weapon = None
        self.experience = 0

    def choose_player(self):
        player_type = input("Choose your player type (Wizard or Fighter): ")
        if player_type.lower() == "wizard":
            name = input("Enter your wizard name: ")
            health = 100
            mana = 50
            magic_power = 20
            self.player = Wizard(name, health, mana, magic_power)
        elif player_type.lower() == "fighter":
            name = input("Enter your fighter name: ")
            health = 150
            strength = 30
            defense = 10
            self.player = Fighter(name, health, strength, defense)
        else:
            print("Invalid player type")

    def choose_monster(self):
        self.monster = Monster("Goblin", 50, 10, 5)

    def choose_weapon(self):
        weapon_type = input("Choose your weapon (Sword or Wand): ")
        if weapon_type.lower() == "sword":
            self.weapon = Weapon("Sword", 15)
        elif weapon_type.lower() == "wand":
            self.weapon = Weapon("Wand", 10)
        else:
            print("Invalid weapon type")

    def fight(self):
        while self.player.health > 0 and self.monster.health > 0:
            player_damage = self.player.attack() + self.weapon.damage
            monster_damage = self.monster.attack()
            self.monster.health -= player_damage
            self.player.health -= monster_damage
            if self.player.health <= 0:
                print("You lost the game")
                return
            elif self.monster.health <= 0:
                print("You won the game!")
                self.experience += 50
                return

    def play(self):
        self.choose_player()
        self.choose_monster()
        self.choose_weapon()
        self.fight()

