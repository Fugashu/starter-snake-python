class Snake:
    def __init__(self, length, headPos):
        self.length = length
        self.headPos = headPos
        self.fitness = -1

    def __str__(self):
        return "My length: {}\nMy head pos: {}".format(self.length, self.headPos)
