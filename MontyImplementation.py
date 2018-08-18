from random import shuffle, randint

gifts = ["car", "goat", "goat"]  # creating gifts list

shuffle(gifts)  # shuffling gifts
print("Gifts", gifts)

# copying list into giftCopy for later computations
giftsCopy = gifts.copy()

# ask user to select a door
doorNum = abs(int(input("Select a door from 1-3: ")))

# checking for first door/gift selected
if doorNum < 4:  # making sure that door number is from 1-3
    doorIndex = doorNum-1  # calculating index of door/gift from door number chosen
    selectedDoor = gifts[doorIndex]  # content of selected door
    if selectedDoor == "goat":  # if door selected contains goat
        giftsCopy[doorIndex] = "air"  # replacing selected gift with air in the copied list

        moderatorDoor = giftsCopy.index("goat")  # moderator chooses door with other goat
        print("Moderator opens door", moderatorDoor + 1)  # 1 is added to the index to get the door number

        newOption = str(input("maintain (m) or switch (s) ?"))  # getting the newOption of the player

        if newOption == 'm':
            print("Sorry you lost!")  # if user maintains door, he loses
        elif newOption == 's':
            print("Great you won!")  # if user switches door, he wins
    else:
        giftsCopy[doorIndex] = "air"  # replacing selected gift with air in the copied list

        if randint(1, 3) == 1:  # randomly choosing the first or second occurrence of goat for moderator
            # when randint == 1 getting first occurrence of goat
            moderatorDoor = giftsCopy.index("goat")
        else:  # getting last occurrence of goat
            moderatorDoor = len(giftsCopy) - 1 - giftsCopy[::-1].index("goat")

        print("Moderator opens door", moderatorDoor + 1)  # 1 is added to the index to get the door number
        newOption = str(input("maintain (m) or switch (s) ?"))  # getting the newOption of the player
        print(newOption)

        if newOption == 'm':
            print("Great you won!")  # if user maintains door, he wins
        elif newOption == 's':
            print("Sorry you lost!")  # if user switches door, he loses

else:
    print("Select from 1-3")


