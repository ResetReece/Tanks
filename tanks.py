import random

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

def output(tanks, index):
    if tanks == 0:
        print("You won!\nYou won in", str(index), "turns")
    else:
        print("You lost!\nYou where", str(tanks), "tanks away from winning")

def main():
    tankPositions = getPositions()
    tanks, index = theGame(tankPositions)
    output(tanks, index)

main()
