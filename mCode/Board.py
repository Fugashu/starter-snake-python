class Board:

    def __init__(self, bH, bW, bS, food, aliveSnakes):
        self.boardSize = bS
        self.boardHeight = bH
        self.boardWidth = bW

        self.aliveSnakes = aliveSnakes
        self.wallCoordinates = []
        self.occupiedBlocks = []
        self.foodBlocks = food
        self.field = []  # True/False values. True if tile is free.

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
        for index in range(len(aliveSnakes)):
            self.occupiedBlocks.append(self.aliveSnakes[index]["body"])
        for index in range(len(self.occupiedBlocks)):
            for element in self.occupiedBlocks[index]:
                occ_x = element["x"]
                occ_y = element["y"]
                print("Occupied field: x: {}  y: {}".format(element["x"], element["y"]))
                self.field[occ_y][occ_x] = False

    #   Override string function to output Board values.
    def __str__(self):
        return "Board size: {}\nBoard Width: {}\nBoardHeight: {}\nBoard Matrix: {}\nOccupiedBlocks: {}" \
               "\nWall Coordinates:{}"\
            .format(self.boardSize, self.boardWidth, self.boardHeight, self.field, self.occupiedBlocks, self
                    .wallCoordinates)

    def isFree(self, xCoordinate, yCoordinate):
        """
        :return: true if the block is free
        TODO: somehow still throws exception.
        """
        if xCoordinate >= self.boardWidth or xCoordinate < 0:
            return False
        if yCoordinate >= self.boardHeight or yCoordinate < 0:
            return False

        if self.field[xCoordinate][yCoordinate]:
            return True
        else:
            return False


