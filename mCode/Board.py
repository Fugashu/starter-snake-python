class Board:

    def __init__(self):
        self.occupiedBlocks = []
        self.field = []  # True/False values. True if tile is free.
        self.wallCoordinates = []
        self.initField = []
        self.foodBlocks =[]
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
        self.field = [[True for x in range(self.boardHeight)] for y in range(self.boardWidth)]
        self.foodBlocks = [[False for x in range(self.boardHeight)] for y in range(self.boardWidth)]

    def updateBlocks(self, food, aliveSnakes):

        self.occupiedBlocks = []
        self.field = [[True for x in range(self.boardHeight)] for y in range(self.boardWidth)]
        self.foodBlocks = [[False for x in range(self.boardHeight)] for y in range(self.boardWidth)]
       # print("in update blocks: self.field:")
       # print(self.field)

        for index in range(len(aliveSnakes)):
            self.occupiedBlocks.append(aliveSnakes[index]["body"])
        for index in range(len(self.occupiedBlocks)):
            for element in self.occupiedBlocks[index]:
                occ_x = element["x"]
                occ_y = element["y"]
                print("Occupied field: x: {}  y: {}".format(element["x"], element["y"]))
                self.field[occ_y][occ_x] = False
        # Loop through food array
        for index in range(len(food)):
            self.foodBlocks[food[index]["y"]][food[index]["x"]] = True

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

    def isFoodBlock(self, yCoordinate, xCoordinate):
        """
        :return: true if the block has food
        """
        if xCoordinate >= self.boardWidth or xCoordinate < 0:
            return False
        if yCoordinate >= self.boardHeight or yCoordinate < 0:
            return False
        if self.field[yCoordinate][xCoordinate]:
            return True
        else:
            return False
