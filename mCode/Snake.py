import mCode.Board

class Snake:
    def __init__(self):
        self.length = None
        self.headPos = None
        self.fitness = -1

    def initialize(self, length, headPos):
        self.length = length
        self.headPos = headPos
        self.fitness = -1

    def __str__(self):
        return "My length: {}\nMy head pos: {}".format(self.length, self.headPos)

    def updateHeadPos(self, hP):
        self.headPos = hP #first coordinate is y, second is x

    def checkSurroundings(self, gameBoard):
        print("checktest")
        moveArr = []

        if gameBoard.isFree(self.headPos[0]-1, self.headPos[1]):
            print ("appending up")
            moveArr.append('up')# up side
        if gameBoard.isFree(self.headPos[0]+1, self.headPos[1]):
            print("appending down")
            moveArr.append('down')# down side
        if gameBoard.isFree(self.headPos[0], self.headPos[1]-1):
            print("appending left")
            moveArr.append('left')# left side
        if gameBoard.isFree(self.headPos[0], self.headPos[1]+1):
            print("appending right")
            moveArr.append('right')# right side

        return moveArr


