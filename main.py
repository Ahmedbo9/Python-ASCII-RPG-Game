
run = True
menu = True
play = False
rules = False
game = True
HP = 50
ATK = 5


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
        print("Welcome to my game , please choose an option from 1 to 4")
        print("1 | NEW GAME")
        print("2 | LOAD SAVED GAME")
        print("3 |  RULES")
        print("4 |  QUIT GAME")
        if rules:
            print("rules")
            rules = False
            playerChoice = ""
            input("> ")
        else:
            playerChoice = input("# ")
        if playerChoice == "1":
            playerName = input("Enter your name padawan: ")
            menu = False
            play = True
        elif playerChoice == "2":
            pass
        elif playerChoice == "3":
            rules = True
        elif playerChoice == "4":
            quit()

    while play:
        save()
        print("Welcome  padawan " + playerName)
        destination = input("# ")
        if destination == "0":
            play = False
            menu = True
            save()
