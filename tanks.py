import random

def rules():
    print("In this game you must guess the position of 10 tanks on a 8x8 grid \nWhen playing you will be prompted to enter a value for the column and then prompted for a value for the row. You must NOT enter both in one input \nA - means the space is open, a X means you missed & a T means you found a tank \nYou have 30 turns\n")
    input("Press enter when ready to continue\n")


def getInput():
    correct = False
    while correct == False:
        position1 = input("\nEnter the first position (Top Row): ")
        if position1.isdigit() == False:
            print("Must be a digit. Try again")
        elif (int(position1) < 0) or (int(position1) > 7):
            print("Number must be between 0 and 7. Try again")
        else:
            correct = True
    correct = False
    while correct == False:
        position2 = input("Enter the second position (Left Column): ")
        if position2.isdigit() == False:
            print("Must be a digit. Try again")
        elif (int(position2) < 0) or (int(position2) > 7):
            print("Number must be between 0 and 7. Try again")
        else:
            correct = True
    userChoice = position2 + position1
    return userChoice

def getPositions():
    tankPositions = []
    tankPositions_set = set()
    while len(tankPositions_set) < 10:
        random1 = random.randint(0, 7)
        random2 = random.randint(0, 7)
        tankPositions_set.add(str(random1) + str(random2))
    tankPositions = list(tankPositions_set)
    return tankPositions

def theGame(tankPositions):
    tanksGrid = [[" ", "0", "1", "2", "3", "4", "5", "6", "7"], ["0", "-", "-", "-", "-", "-", "-", "-", "-"], ["1", "-", "-", "-", "-", "-", "-", "-", "-"], ["2", "-", "-", "-", "-", "-", "-", "-", "-"], ["3", "-", "-", "-", "-", "-", "-", "-", "-"], ["4", "-", "-", "-", "-", "-", "-", "-", "-"], ["5", "-", "-", "-", "-", "-", "-", "-", "-"], ["6", "-", "-", "-", "-", "-", "-", "-", "-"], ["7", "-", "-", "-", "-", "-", "-", "-", "-"]]
    index = 1
    tanks = 10
    while (tanks != 0) and (index <= 30):
        for item in range(index, 31):
            if tanks == 0:
                break
            for row in tanksGrid:
                print(" ".join(row))
            print("\nIt is turn", str(index) + "/30")
            userChoice = getInput()
            found = False
            if tanksGrid[int(userChoice[0]) + 1][int(userChoice[1]) + 1] != "-":
                print("\n\033[1mYou have already guessed" + " (" + userChoice[0] + "," + userChoice[1] + "). Try again\n\033[0m")
            else:
                found = False
                for item in tankPositions:
                    if userChoice == item:
                        tanks -= 1
                        print("\n\033[1mHIT\033[0m\n" + str(tanks), "\033[1mTANKS REMAINING\033[0m\n")
                        tanksGrid[int(userChoice[0]) + 1][int(userChoice[1]) + 1] = "T"
                        found = True
                        index += 1
                if found == False:
                    print("\n\033[1mMISS\033[0m\n" + str(tanks), "\033[1mTANKS REMAINING\033[0m\n")
                    tanksGrid[int(userChoice[0]) + 1][int(userChoice[1]) + 1] = "X"
                    index += 1
            print("\n" + "-" * 30 + "\n")
    return tanks, index

def output(tanks, index, wins, gamesPlayed):
    gamesPlayed += 1
    if tanks == 0:
        print("You won!\nYou won in", str(index), "turns")
        wins += 1
        print(f"You have won {wins} out of {gamesPlayed} games played")
    else:
        print("You lost!\nYou where", str(tanks), "tanks away from winning")
        print(f"You have won {wins} out of {gamesPlayed} games played")
    return wins, gamesPlayed

def main():
    wins = 0
    gamesPlayed = 0
    running = True
    while running == True:
        while True:
            print("Welcome to tanks")
            choice = input("Do you need to see the rules (y/n)?\n")
            try:
                choice.upper()
            except:
                print("Not a valid option, try again\n")
            else:
                choice = choice.upper()
                if choice == "Y":
                    rules()
                    break
                elif choice == "N":
                    break
                else:
                    print("Not a valid option, try again\n")
        tankPositions = getPositions()
        tanks, index = theGame(tankPositions)
        wins, gamesPlayed = output(tanks, index, wins, gamesPlayed)
        while True:
            choice = input("Do you want to continue playing (y/n)?\n")
            try:
                choice.upper()
            except:
                print("Not a valid option, try again\n")
            else:
                choice = choice.upper()
                if choice == "Y":
                    break
                elif choice == "N":
                    print("Thanks for playing")
                    running = False
                    break
                else:
                    print("Not a valid option, try again\n")

main()
