# ---- Player, Character, Class

class Character:
    def __init__(self, name, character_class,):
        self.name = name
        self.character_class = character_class
        print(type(character_class))
        self.character_class.setupCharactor(self)
        self.level = 100
        self.health = 100
        self.attack_power = 10
        self.defense = 10

    def setHealth(self, )

    def attack(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} ist verstorben")


class PlayerCharacter(Character):
    def __init__(self, name, character_class, player):
        super().__init__(self, name, character_class)
        self.player = player
        self.inventory = []

class NpcCharacter(Character):
    def __init__(self, name, character_class):
        super().__init__(name, character_class)
        self.droplist = []


class CharacterClass:
    def __init__(self, className):
        self.className = className

    def setupCharacter(self, Charactor):
        print("Abstract class no function")

        
class WarriorClass(CharacterClass):
    def __init__(self,):
        super().__init__("Warrior")

    def setupCharacter(self, Charactor):
        print(type(Charactor))
        charactor.health


class MageClass(CharacterClass):
    def __init__(self,):
        super().__init__("Mage")


c1 = Character("Horst", "Warrior")
p1 = PlayerCharacter("Hansli", "Magier", "Player1")
    
print(p1.attack_power)

print(c1.health)