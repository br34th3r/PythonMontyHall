import random

class MontyHallBot:
    doors = [False, False, False]
    wins = 0
    losses = 0
    repeats = 10000

    def __init__(self):
        self.runTest()

    def runTest(self):
        for i in range(self.repeats):
            self.assignDoors()
            self.userSelection()
            self.openAnotherDoor()
            self.switchUserPosition()
            self.winOrLose()
        print("WINS: " + str(self.wins))
        print("LOSSES: " + str(self.losses))
        print((self.wins/self.repeats)*100)

    def assignDoors(self):
        self.doors = ["Car", "Goat", "Goat"]
        random.shuffle(self.doors)

    def userSelection(self):
        self.choice = random.randrange(3)

    def openAnotherDoor(self):
        for j, contents in enumerate(self.doors):
            if(j != self.choice and contents == "Goat"):
                self.reveal = j
                break

    def switchUserPosition(self):
        for j, contents in enumerate(self.doors):
            if(j != self.choice and j != self.reveal):
                self.choice = j
                break

    def winOrLose(self):
        if(self.doors[self.choice] == "Car"):
            self.wins += 1
        else:
            self.losses += 1

bot = MontyHallBot()
