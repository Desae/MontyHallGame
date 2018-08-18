# importing important libraries
from tkinter import *
import tkinter.messagebox
import random


# defining the game class
class MontyHallGame:
    def __init__(self):
        self.window = Tk()  # initializing the gui window
        self.window.title("Monty Hall Game 1.0")  # setting the title for the window
        self.doorColor = "#242582"
        self.doorNum = 0
        self.gifts = ["car", "goat", "goat"]
        self.selectedDoor = ""
        self.carImg = PhotoImage(file="./imgs/car.gif")
        self.goatImg = PhotoImage(file="./imgs/goat.gif")
        self.btns = []

        # creating a menu bar
        menubar = Menu(self.window)  # initializing the menu bar
        self.window.config(menu=menubar)  # displaying the menu bar

        # Create a pull-down menu, and add it to the menu bar
        operationMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Options", menu=operationMenu)
        operationMenu.add_command(label="New Window", command=self.newWindow)
        operationMenu.add_command(label="Color of Doors", command=self.changeDoorColor)
        operationMenu.add_command(label="Night Mode", command=self.nightMode)
        operationMenu.add_command(label="Help", command=self.help)
        operationMenu.add_command(label="About", command=self.about)
        operationMenu.add_separator()
        operationMenu.add_command(label="Exit", command=self.exit)

        # frame for welcome message and game instructions
        frame0 = Frame(self.window)
        frame0.grid(row=1, column=1, sticky=W)  # frame is in row 1 and column 1 and sticking to the West
        self.msgCanvas = Canvas(frame0, width=800, height=200, bg="white")  # canvas is inside the frame0
        self.msgCanvas.pack()
        self.msgCanvas.create_image(90, 52, image=self.carImg)
        self.welcomeMsg = self.msgCanvas.create_text(400, 20, fill="#f64c72", font="Helvetica 15 bold",
                                                     text="Welcome to the Monty Hall Game!")
        self.msgCanvas.create_image(750, 55, image=self.goatImg)

        # button that starts game
        self.startGameBtn = Button(self.msgCanvas, fg="white", bg="blue", text="Start Game", command=self.startGame)
        self.startGameBtn.place(x=350, y=40)

        self.instructionMsg1 = self.msgCanvas.create_text(400, 155, fill="#553d67", text="")
        self.firstDoorChoice = self.msgCanvas.create_text(400, 90, fill="#553d67", text="")
        self.secondDoorChoice = self.msgCanvas.create_text(400, 120, fill="#553d67", text="")
        self.instructionMsg2 = self.msgCanvas.create_text(400, 170, fill="#553d67", text="")

        # creating frame1 inside window. This frame contains the doors
        frame1 = Frame(self.window)
        frame1.grid(row=2, column=1)  # placing frame1 in row 2 and column 1

        self.canvas = Canvas(frame1, width=800, height=400, bg="white")
        self.canvas.pack()

        self.btn1 = Button(self.canvas, bg="#242582", text="Door 1", padx=60, pady=145, state="disabled", command=lambda: self.setDoorNum(1),
                      fg="white")
        self.btn1.place(x=135, y=35)
        self.btn1.image = self.goatImg

        door1 = self.canvas.create_rectangle(130, 30, 300, 350, tags="door1", fill="blue")

        self.btn2 = Button(self.canvas, bg="#242582", text="Door 2", padx=60, pady=145, state="disabled", command=lambda: self.setDoorNum(2),
                      fg="white")
        self.btn2.place(x=355, y=35)
        door2 = self.canvas.create_rectangle(350, 30, 520, 350, tags="door2", fill="blue")

        self.btn3 = Button(self.canvas, bg="#242582", text="Door 3", padx=60, pady=145, state="disabled", command=lambda: self.setDoorNum(3),
                      fg="white")
        self.btn3.place(x=575, y=35)
        door3 = self.canvas.create_rectangle(570, 30, 740, 350, tags="door3", fill="blue")

        self.btns.append(self.btn1)
        self.btns.append(self.btn2)
        self.btns.append(self.btn3)

        self.changedDoorWinsVar = IntVar()
        self.changedDoorLossVar = IntVar()
        self.maintainedDoorWinsVar = IntVar()
        self.maintainedDoorLossVar = IntVar()

        # creating frame2 which contains stats from game since it started being played
        frame2 = Frame(self.window)
        frame2.grid(row=1, column=2)  # frame is in row 1 and column 2

        self.statsCanvas = Canvas(frame2, width=400, height=200, bg="#553d67")  # statsCanvas is in this frame
        self.statsCanvas.pack()

        self.statsCanvas.create_text(200, 30, fill="white", text="Statistics Pane")
        self.statsCanvas.create_text(100, 80, fill="white", text="Door Changed")
        self.statsCanvas.create_text(77, 100, fill="white", text="Wins: ")
        self.statsCanvas.create_text(77, 120, fill="white", text="Loss: ")

        self.statsCanvas.create_text(300, 80, fill="white", text="Door Maintained")
        self.statsCanvas.create_text(270, 100, fill="white", text="Wins: ")
        self.statsCanvas.create_text(270, 120, fill="white", text="Loss: ")

        # frame3 contains visualization of game statistics in a pie-chart
        frame3 = Frame(self.window)
        frame3.grid(row=2, column=2)  # frame3 is in row 2 and column 2

        self.statsCanvas2 = Canvas(frame3, width=400, height=400, bg="#99738c")
        self.statsCanvas2.pack()

        self.statsTitle2 = self.statsCanvas2.create_text(200, 20, fill="white", text="Data Analysis")

        self.window.mainloop()  # sets window's event loop

    # function to display statistics
    def displayStats(self):
        pass

    # function to open new window
    def newWindow(self):
        MontyHallGame()

    # function to open help menu
    def help(self):
        tkinter.messagebox.showinfo("Game Instruction", "The quick brown fox jumps over the lazy dog"
                                                        "The quick brown fox jumps over the lazy dog"
                                                        "The quick brown fox jumps over the lazy dog"
                                                        "The quick brown fox jumps over the lazy dog"
                                                        "The quick brown fox jumps over the lazy dog"
                                                        "The quick brown fox jumps over the lazy dog")

    # function to open about menu
    def about(self):
        tkinter.messagebox.showinfo("About Monty Hall", "The quick brown fox jumps over the lazy dog"
                                                        "The quick brown fox jumps over the lazy dog"
                                                        "The quick brown fox jumps over the lazy dog"
                                                        "The quick brown fox jumps over the lazy dog"
                                                        "The quick brown fox jumps over the lazy dog"
                                                        "The quick brown fox jumps over the lazy dog")

    # function to exit game
    def exit(self):
        exit = tkinter.messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if exit:
            self.window.quit()

    # function to change door color
    def changeDoorColor(self):
        pass

    # function to change display to night mode
    def nightMode(self):
        pass

    # function to detect door number clicked
    def setDoorNum(self, num):
        print("You clicked door", num)
        self.doorNum = num
        # self.setDoorColor("purple", num)
        self.msgCanvas.itemconfigure(self.firstDoorChoice,
                                     text="Your first choice: Door " + str(num))
        self.gameControl(self.doorNum)

    # function to get door number clicked
    def getDoorNum(self):
        return self.doorNum

    # setting door colors
    def setDoorColor(self, color, doornum):
        if doornum == 1:
            self.btn1["bg"] = color
        elif doornum == 2:
            self.btn2["bg"] = color
        elif doornum == 3:
            self.btn3["bg"] = color

    '''def getDoorColor(self):
        return self.doorColor'''

    def getNewOption(self, newDoorNum):
        self.msgCanvas.itemconfigure(self.secondDoorChoice,
                                     text="Your second choice: Door " + str(newDoorNum))
        if self.selectedDoor == "goat":
            if self.doorNum == newDoorNum:
                print("m")
                print("Sorry you lost!")
                self.msgCanvas.itemconfigure(self.instructionMsg2,
                                             text="Sorry you lost!")

            else:
                print("s")
                print("Great you won!")  # if user switches door, he wins
                self.msgCanvas.itemconfigure(self.instructionMsg2,
                                             text="Great you won!")

        elif self.selectedDoor == "car":
            if self.doorNum == newDoorNum:
                print("m")
                print("Great you won!")
                self.msgCanvas.itemconfigure(self.instructionMsg2,
                                             text="Great you won!")

            else:
                print("s")
                print("Sorry you lost!")  # if user switches door, he loses
                self.msgCanvas.itemconfigure(self.instructionMsg2,
                                             text="Sorry you lost!")

        self.msgCanvas.itemconfigure(self.instructionMsg1, text="")
        self.btn1["state"] = "disabled"
        self.btn2["state"] = "disabled"
        self.btn3["state"] = "disabled"
        self.startGameBtn["text"] = "Restart Game"

        i = 0
        for g in self.gifts:
            print(g)
            if g == "car":
                self.btns[i]["bg"] = "purple"
            else:
                self.btns[i]["bg"] = "white"

            self.btns[i]["text"] = "  " + g.upper()

            i += 1

    # function to start game
    def startGame(self):
        # shuffling gifts
        random.shuffle(self.gifts)
        print("Gifts", self.gifts)
        self.msgCanvas.itemconfigure(self.instructionMsg1,
                                     text="Choose a door")
        self.msgCanvas.itemconfigure(self.instructionMsg2,
                                     text="")
        self.msgCanvas.itemconfigure(self.firstDoorChoice,
                                     text="")
        self.msgCanvas.itemconfigure(self.secondDoorChoice,
                                     text="")
        self.btn1["state"] = "normal"
        self.btn1["bg"] = "#242582"
        self.btn1["text"] = "Door 1"
        self.btn1["command"] = lambda: self.setDoorNum(1)

        self.btn2["state"] = "normal"
        self.btn2["bg"] = "#242582"
        self.btn2["text"] = "Door 2"
        self.btn2["command"] = lambda: self.setDoorNum(2)

        self.btn3["state"] = "normal"
        self.btn3["bg"] = "#242582"
        self.btn3["text"] = "Door 3"
        self.btn3["command"] = lambda: self.setDoorNum(3)

        self.startGameBtn["text"] = "Restart Game"


    def gameControl(self, doorNum):
        # copying list into giftCopy for later computations
        giftsCopy = [x for x in self.gifts]
        print("Gifts", self.gifts)
        print("Copied", giftsCopy)
        print("Door number:", doorNum)
        '''# getting door number selected
        doorNum = self.getDoorNum()'''

        # checking for first door/gift selected
        # if 0 < doorNum < 4:  # making sure that door number is from 1-3
        doorIndex = self.doorNum - 1  # calculating index of door/gift from door number chosen
        self.selectedDoor = self.gifts[doorIndex]  # content of selected door
        if self.selectedDoor == "goat":  # if door selected contains goat
            print("You selected goat")
            print("Copy of gifts", giftsCopy)
            giftsCopy[doorIndex] = "air"  # replacing selected gift with air in the copied list
            print("Copy of gifts", giftsCopy)
            moderatorDoor = giftsCopy.index("goat")  # moderator chooses door with other goat
            print("Index of moderator goat selected", moderatorDoor)
            self.moderatorsChoice = moderatorDoor + 1
            print("Moderator opens door", self.moderatorsChoice)  # 1 is added to the index to get the door number

            # setting instruction text
            self.msgCanvas.itemconfigure(self.instructionMsg1, text="Moderator opens door " + str(self.moderatorsChoice))

            # disable button
            if self.moderatorsChoice == 1:
                self.btn1["state"] = "disabled"
                self.setDoorColor("white", 1)
            elif self.moderatorsChoice == 2:
                self.btn2["state"] = "disabled"
                self.setDoorColor("white", 2)
            elif self.moderatorsChoice == 3:
                self.btn3["state"] = "disabled"
                self.setDoorColor("white", 3)

        elif self.selectedDoor == "car":  # if door selected contains car
            print("You selected car")  # if door selected contains car
            print("Copy of gifts", giftsCopy)
            giftsCopy[doorIndex] = "air"  # replacing selected gift with air in the copied list
            print("Copy of gifts", giftsCopy)

            if random.randint(1, 3) == 1:  # randomly choosing the first or second occurrence of goat for moderator
                # when randint == 1 getting first occurrence of goat
                moderatorDoor = giftsCopy.index("goat")
            else:  # getting last occurrence of goat
                moderatorDoor = len(giftsCopy) - 1 - giftsCopy[::-1].index("goat")

            print("Index of moderator goat selected", moderatorDoor)
            self.moderatorsChoice = moderatorDoor + 1
            print("Moderator opens door", self.moderatorsChoice)

        # setting instruction text
        self.msgCanvas.itemconfigure(self.instructionMsg1, text="Moderator opens door " + str(self.moderatorsChoice))

        # disable button
        if self.moderatorsChoice == 1:
            #self.btn1["image"] = self.goatImg
            self.btn1["state"] = "disabled"
            self.btn1["text"] = "GOAT"
            self.setDoorColor("white", 1)
        elif self.moderatorsChoice == 2:
            #self.btn2["image"] = self.goatImg
            self.btn2["state"] = "disabled"
            self.btn2["text"] = "GOAT"
            self.setDoorColor("white", 2)
        elif self.moderatorsChoice == 3:
            #self.btn3["image"] = self.goatImg
            self.btn3["state"] = "disabled"
            self.btn3["text"] = "GOAT"
            self.setDoorColor("white", 3)

        self.msgCanvas.itemconfigure(self.instructionMsg2, text="Click on the same door to maintain your choice or on "
                                                                "the other door to switch")

        self.btn1["command"] = lambda: self.getNewOption(1)
        self.btn2["command"] = lambda: self.getNewOption(2)
        self.btn3["command"] = lambda: self.getNewOption(3)


MontyHallGame()
