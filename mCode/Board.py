class Board:

    def __init__(self, bH, bW, bS, food, aliveSnakes, wallCoordinates):
        self.boardSize = bS
        self.boardHeight = bH
        self.boardWidth = bW
        self.food = food
        self.aliveSnakes = aliveSnakes

    def __str__(self):
        return "Board size: {}\nBoard Width: {}\nBoardHeight: {}"\
            .format(self.boardSize, self.boardWidth, self.boardHeight)

