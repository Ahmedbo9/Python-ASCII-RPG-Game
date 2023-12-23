import os
import random

run = True
menu = True
play = False
rules = False
game = True
key = False
fight = False
immune = True
HP = 50
HPMAX = HP
ATK = 5
potion = 1
elixir = 0
gold = 0
x = 0
y = 0

#  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
gameMap = [["plains", "plains", "plains", "plains", "forest", "mountain", "cave"],  # y = 0
           ["forest", "forest", "forest", "forest", "forest", "hills", "mountain"],  # y = 1
           ["forest", "fields", "bridge", "plains", "hills", "forest", "hills"],  # y = 2
           ["plains", "shop", "town", "mayor", "plains", "hills", "mountain"],  # y = 3
           ["plains", "fields", "fields", "plains", "hills", "mountain", "mountain"]]  # y = 4

x_len = len(gameMap[0]) - 1
y_len = len(gameMap) - 1

biom = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "mayor": {
        "t": "MAYOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True,
    }
}

e_list = ["Goblin", "Orc", "Slime"]

mobs = {
    "Goblin": {
        "hp": 15,
        "at": 3,
        "gold": 8
    },
    "Orc": {
        "hp": 35,
        "at": 5,
        "gold": 18
    },
    "Slime": {
        "hp": 30,
        "at": 2,
        "gold": 12
    },
    "Dragon": {
        "hp": 100,
        "at": 8,
        "gold": 100
    }
}


def print_player_info():
    draw()
    print("LOCATION: " + biom[gameMap[y][x]]["t"])
    draw()
    print("NAME: " + playerName)
    print(playerName + ' health : ' + show_health_bar(HP, HPMAX))
    print("ATK: " + str(ATK))
    print("POTIONS: " + str(potion))
    print("ELIXIRS: " + str(elixir))
    print("GOLD: " + str(gold))
    print("COORD:", x, y)
    draw()


def clear():
    os.system('clear')


def draw():
    print("_______________________________________________________")


def save():
    stats = [
        playerName,
        str(HP),
        str(ATK),
        str(potion),
        str(elixir),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    file = open("save.txt", "w")
    for stat in stats:
        file.write(stat + "\n")
    file.close()


def show_health_bar(current_hp, max_hp):
    bars = 20
    remaining_health_symbol = "█"
    lost_health_symbol = "_"
    color_green = "\033[92m"
    color_yellow = "\33[33m"
    color_red = "\033[91m"
    color_default = "\033[0m"

    remaining_health_bars = round(current_hp / max_hp * bars)
    lost_health_bars = bars - remaining_health_bars

    if current_hp > 0.66 * max_hp:
        health_color = color_green
    elif current_hp > 0.33 * max_hp:
        health_color = color_yellow
    else:
        health_color = color_red

    health_bar = f"|{health_color}{remaining_health_bars * remaining_health_symbol}" \
                 f"{lost_health_bars * lost_health_symbol}{color_default}|"

    return health_bar


while run:
    while menu:
        print("Welcome to my game , please choose an option from 1 to 4")
        print("1 | NEW GAME")
        print("2 | LOAD SAVED GAME")
        print("3 | RULES")
        print("4 | QUIT GAME")
        if rules:
            print("rules")
            rules = False
            playerChoice = ""
            input("> ")
        else:
            playerChoice = input("# ")
        if playerChoice == "1":
            clear()
            playerName = input("Enter your name padawan: ")
            menu = False
            play = True
        elif playerChoice == "2":
            try:
                f = open("save.txt", "r")
                load_save = f.readlines()
                if load_save and len(load_save) == 9:
                    playerName = load_save[0][:-1]
                    HP = load_save[1][:-1]
                    ATK = int(load_save[2][:-1])
                    potion = int(load_save[3][:-1])
                    elixir = int(load_save[4][:-1])
                    gold = int(load_save[5][:-1])
                    x = int(load_save[6][:-1])
                    y = int(load_save[7][:-1])
                    key = bool(load_save[8][:-1])
                    print("Save is Loaded , welcome back " + playerName)
                    print_player_info()
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Invalid")

            except OSError:
                print("No save found")
                input("> ")

        elif playerChoice == "3":
            rules = True
        elif playerChoice == "4":
            quit()


    def heal(heal_amount):
        pass


    def battle():
        global fight, run, play, HP, ATK, potion, gold, elixir
        print(playerName + " you need to fight")
        enemy = random.choice(e_list)
        enemy_hp = mobs[enemy]["hp"]
        enemy_atk = mobs[enemy]["at"]
        enemy_gold = mobs[enemy]["gold"]
        enemy_hpmax = enemy_hp
        while fight:
            clear()
            draw()
            print("Defeat the " + enemy + "!")
            draw()
            print(enemy + ' health :' + show_health_bar(enemy_hp, enemy_hpmax))
            print(playerName + ' health :' + show_health_bar(HP, HPMAX))
            print("POTIONS: " + str(potion))
            print("ELIXIR: " + str(elixir))
            draw()
            print("1 - ATTACK")
            if potion > 0:
                print("2 - USE POTION (30HP)")
            if elixir > 0:
                print("3 - USE ELIXIR (50HP)")
            draw()

            choice = input("# ")

            if choice == "1":
                enemy_hp -= ATK
                print(playerName + " dealt " + str(ATK) + " damage to the " + enemy + ".")
                print(enemy + ' health :' + show_health_bar(enemy_hp, enemy_hpmax))
                if enemy_hp > 0:
                    HP -= enemy_atk
                    print(enemy + " dealt " + str(enemy_atk) + " damage to " + playerName + ".")
                    print(playerName + ' health : ' + show_health_bar(HP, HPMAX))

                input("> ")

            elif choice == "2":
                if potion > 0:
                    potion -= 1
                    heal(30)
                    HP -= enemy_atk
                    print(enemy + " dealt " + str(enemy_atk) + " damage to " + playerName + ".")
                    print(playerName + ' health : ' + show_health_bar(HP, HPMAX))

                else:
                    print("No potions!")
                input("> ")

            elif choice == "3":
                if elixir > 0:
                    elixir -= 1
                    heal(50)
                    HP -= enemy_atk
                    print(enemy + " dealt " + str(enemy_atk) + " damage to " + playerName + ".")
                    print(playerName + ' health : ' + show_health_bar(HP, HPMAX))

                else:
                    print("No elixirs!")
                input("> ")

            if HP <= 0:
                print(enemy + " defeated " + playerName + "...")
                draw()
                fight = False
                play = False
                run = False
                print("GAME OVER")
                input("> ")

            if enemy_hp <= 0:
                print(playerName + " defeated the " + enemy + "!")
                draw()
                fight = False
                gold += enemy_gold
                print("You've found " + str(enemy_gold) + " gold!")
                if random.randint(0, 100) < 30:
                    potion += 1
                    print("You've found a potion!")
                if enemy == "Dragon":
                    draw()
                    print("Congratulations, you've finished the game!")
                    boss = False
                    play = False
                    run = False
                input("> ")
                clear()


    while play:
        clear()
        save()
        if not immune:
            if biom[gameMap[y][x]]["e"]:
                if random.random() < 0.6:
                    fight = True
                    battle()

        print_player_info()
        if y > 0:
            print("1 - NORTH")
        if x < x_len:
            print("2 - EAST")
        if y < y_len:
            print("3 - SOUTH")
        if x > 0:
            print("4 - WEST")

        print('PLAYER LOCATION', x, y)
        draw()

        print("Type '0' to save and exit the game")
        destination = input("# ")
        if destination == "0":
            play = False
            menu = True
            save()
        elif destination == "1":
            if y > 0:
                y -= 1
                immune = False
        elif destination == "2":
            if x < x_len:
                x += 1
                immune = False

        elif destination == "3":
            if y < y_len:
                y += 1
                immune = False

        elif destination == "4":
            if x > 0:
                x -= 1
                immune = False
