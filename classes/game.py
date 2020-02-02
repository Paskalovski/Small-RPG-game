import random
from .magic import Spell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk -10
        self.atkh = atk +10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    # def generate_spell_damage(self, i):
    #     mgl = self.magic[i]["dmg"] - 5
    #     mgh = self.magic[i]["dmg"] + 5
    #     return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def chose_action(self):
        i = 1
        print(bcolors.OKBLUE+bcolors.BOLD + self.name + bcolors.ENDC)
        print("Actions")
        for item in self.actions:
            print("  " + str(i) + ":" + item + "")
            i += 1

    def chose_magic(self):
        i = 1
        print(bcolors.OKBLUE + "\n Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("  " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1


    def chose_item(self):
        i = 1
        print(bcolors.OKGREEN + "\n ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("  " +str(i) + ":", item["item"].name, "-", item["item"].description, "(x" +str(item["quantity"]) + ")")
            i += 1

    def get_stats(self):
        print(self.name + "     " + str(self.hp) + "/" + str(self.maxhp) +" HP     " + str(self.mp) + "/" + str(self.maxmp) +" MP")

