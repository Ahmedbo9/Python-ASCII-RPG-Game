import os

run = True
menu = True
play = False
rules = False
game = True
HP = 50
ATK = 5


def clear():
    os.system('clear')


def draw():
    print("_______________________________________________________")


def save():
    stats = [
        playerName,
        str(HP),
        str(ATK)
    ]

    file = open("save.txt", "w")
    for stat in stats:
        file.write(stat + "\n")
    file.close()


while run:
    while menu:
        clear()
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
            f = open("save.txt", "r")
            load_save = f.readlines()
            playerName = load_save[0][:-1]
            HP = load_save[1][:-1]
            ATK = load_save[2][:-1]
            f.close()
            clear()
            print("Save is Loaded , welcome back " + playerName)
            print(playerName, HP, ATK)
            input("> ")
            menu = False
            play = True

        elif playerChoice == "3":
            rules = True
        elif playerChoice == "4":
            quit()

    while play:
        clear()
        draw()
        print("Type '0' to save and exit the game")
        draw()
        save()
        print("IN PLAY " + playerName)
        destination = input("# ")
        if destination == "0":
            play = False
            menu = True
            save()
