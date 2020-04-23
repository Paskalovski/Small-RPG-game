from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import item


# Black Magic
fire = Spell("Fire", 10, 100, "black magic")
thunder = Spell("Thunder", 10, 100, "black magic")
blizzard = Spell("Blizzard", 10, 100, "black magic")
meteor = Spell("Meteor", 20, 200, "black magic")
quake = Spell("Quake", 14, 140, "black magic")

# White Magic
cure = Spell("Cure", 12, 120, "white magic")
cura = Spell("Cura", 18, 200, "white magic")

# Items
potion = item("Potion", "potion", "Heals 50 HP", 50)
hipotion = item("Hi Potion", "potion", "Heals 100 HP", 100)
superpotion = item("Super Potion", "potion","Heals 500 HP", 500)
elixer = item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = item("Grenade", "attack", "Deals 500 damage", 500)

# Characters
player_magic = [thunder,blizzard,meteor,quake,cure,cura]
player_items = [{"item":potion,"quantity":15},{"item":hipotion,"quantity":5},
                {"item":superpotion,"quantity":5},{"item":elixer,"quantity":5},
                {"item":hielixer,"quantity":2},{"item":grenade,"quantity":5}]

player1 = Person("Valos:",3560,65,60,34,player_magic,player_items)
player2 = Person("Rick: ",4160,65,60,34,player_magic,player_items)
player3 = Person("Morty:",3100,65,60,34,player_magic,player_items)

players = [player1, player2, player3]
enemy_magic = []
enemy_items = []
enemy = Person("Voldemor",10000,65, 1500, 50,enemy_magic,enemy_items)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATACKS!" + bcolors.ENDC)

while running:
    print( "================")

    for player in players:
        player.get_stats()

    for player in players:

        player.chose_action()
        choice = input("Chose action: ")
        index = int(choice) - 1


        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print(bcolors.OKBLUE + "Your attack dealt", dmg,"damage" + bcolors.ENDC)


        elif index == 1:
            player.chose_magic()
            magic_choice = int(input("Choose magic: ")) -1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "Not enough MP" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white magic":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "Your", spell.name, "spell heals up", str(magic_dmg), "HP", bcolors.ENDC )
            elif spell.type == "black magic":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "Your", spell.name, "spell dealt", magic_dmg, "damage", bcolors.ENDC)


        elif index == 2:
            player.chose_item()
            item_choice = int(input("Chose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "The", item.name, "heals up", item.prop, "HP", bcolors.ENDC)
            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "The", item.name, "fully restores players HP/MP", bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.OKGREEN + "The", item.name, "dealt", item.prop, "damage", bcolors.ENDC)


    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(bcolors.FAIL + "Enemy attack dealt", enemy_dmg,"damage!" + bcolors.ENDC)

    print("-----------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "YOU WIN!!!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "YOU LOSE!" + bcolors.ENDC)
        running = False
