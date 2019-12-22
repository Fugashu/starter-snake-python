class Board:

    def __init__(self):
        self.occupiedBlocks = []
        self.field = []  # True/False values. True if tile is free.
        self.wallCoordinates = []
        self.boardSize = None
        self.boardHeight = None
        self.boardWidth = None

    #   Override string function to output Board values.
    def __str__(self):
        return "Board size: {}\nBoard Width: {}\nBoardHeight: {}\nBoard Matrix: {}\nOccupiedBlocks: {}" \
               "\nWall Coordinates:{}"\
            .format(self.boardSize, self.boardWidth, self.boardHeight, self.field, self.occupiedBlocks, self
                    .wallCoordinates)

    def initialize(self, bH, bW, bS, food, aliveSnakes):
        self.boardSize = bS
        self.boardHeight = bH
        self.boardWidth = bW

    #   Calculate wall tiles and put them into 2D array
        for i in range(self.boardWidth+2):
            self.wallCoordinates.append([-1, i-1])
            self.wallCoordinates.append([self.boardHeight, i-1])

        for i in range(self.boardHeight):
            self.wallCoordinates.append([i, -1])
            self.wallCoordinates.append([i, self.boardHeight])

    #   Calculate the occupied blocks and store them
        for rows in range(self.boardHeight):
                self.field.append([True] * self.boardWidth)
        self.updateBlocks(food, aliveSnakes)

        self.cleanup()

    def updateBlocks(self, food, aliveSnakes):
        print("in update blocks: self.field:")
        print(self.field)
        for index in range(len(aliveSnakes)):
            self.occupiedBlocks.append(aliveSnakes[index]["body"])
        for index in range(len(self.occupiedBlocks)):
            for element in self.occupiedBlocks[index]:
                occ_x = element["x"]
                occ_y = element["y"]
                print (occ_x)
                print (occ_y)

                print("Occupied field: x: {}  y: {}".format(element["x"], element["y"]))
                self.field[occ_y][occ_x] = False

    def isFree(self, yCoordinate, xCoordinate):
        """
        :return: true if the block is free
        """
        if xCoordinate >= self.boardWidth or xCoordinate < 0:
            return False
        if yCoordinate >= self.boardHeight or yCoordinate < 0:
            return False

        if self.field[yCoordinate][xCoordinate]:
            return True
        else:
            return False

    def cleanup(self):
        self.occupiedBlocks = []
        self.field = []
        #   Calculate the occupied blocks and store them
        for rows in range(self.boardHeight):
            self.field.append([True] * self.boardWidth)
