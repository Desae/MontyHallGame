from random import shuffle, randint


class MontyHallGame:
    '''
        Game that simulates the Monty Hall Problem
        Author: Aseda Addai-Deseh
    '''
    def __init__(self):
        self.gifts = ["car", "goat", "goat"]  # creating gifts list
        self.giftsCopy = []

    # initializing game
    def initializeGame(self):
        shuffle(self.gifts)  # shuffling gifts
        print("Gifts", self.gifts)
        self.giftsCopy = self.gifts.copy()  # copying list into giftCopy for later computations

    # asking for user imput
    def askUserInput(self):
        doorNum = abs(int(input("Select a door from 1-3: ")))  # ask user to select a door
        if doorNum < 4:
            doorIndex = doorNum - 1  # calculating index of door/gift from door number chosen
            selectedDoor = self.gifts[doorIndex]  # content of selected door
            return doorNum, selectedDoor
        else:
            self.askUserInput()

    # getting host's door choice
    def getHostChoice(self, selectedDoorNum):
        doorIndex = selectedDoorNum - 1
        selectedDoorContent = self.gifts[doorIndex]

        if selectedDoorContent == "goat":
            self.giftsCopy[doorIndex] = "air"
            moderatorDoor = self.giftsCopy.index("goat")  # moderator chooses door with other goat
            moderatorDoor += 1
            print("Moderator opens door", moderatorDoor)  # 1 is added to the index to get the door number
            return moderatorDoor
        else:
            self.giftsCopy[doorIndex] = "air"  # replacing selected gift with air in the copied list
            if randint(1, 3) == 1:
                moderatorDoor = self.giftsCopy.index("goat")
            else:
                moderatorDoor = len(self.giftsCopy) - 1 - self.giftsCopy[::-1].index("goat")
                moderatorDoor += 1
                print("Moderator opens door", moderatorDoor)  # 1 is added to the index to get the door number
                return moderatorDoor, selectedDoorContent

    # asking user for option to maintain/switch door
    def askUserOption(self):
        userOption = str(input("maintain (m) or switch (s) ?"))  # getting the newOption of the player
        return userOption

    def gameOutcome(self, selectedDoorContent, userOption):
        if selectedDoorContent == "goat":
            if userOption == 'm':
                print("Sorry you lost!")  # if user maintains door, he loses
            elif userOption == 's':
                print("Great you won!")  # if user switches door, he wins
        elif selectedDoorContent == "car":
            if userOption == 'm':
                print("Great you won!")  # if user maintains door, he wins
            elif userOption == 's':
                print("Sorry you lost!")  # if user switches door, he loses


def main():
    # creating instance of game
    game = MontyHallGame()

    # initializing game
    game.initializeGame()

    # getting door number and its contents from user
    selectedDoorNum, selectedDoorContent = game.askUserInput()

    # getting host's door choice
    game.getHostChoice(selectedDoorNum)

    # getting user option after host's choice
    userOption = game.askUserOption()

    # getting the outcome of the game
    game.gameOutcome(selectedDoorContent, userOption)


if __name__ == '__main__':
    main()
