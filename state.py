class State:
    
    def __init__(self, value, executor):
        #(value_1, value_2) - value_1 - next state // value_2 - print value
        self.ways = [[[None, None], [None, None]], [[None, None], [None, None]]]
        self.value = value
        self.defineWays(executor)

    def __split(self, value):
        if value == 0:
            return 0, 0
        if value > 0:
            binary_string = str(bin(value))[2:]
            if len(binary_string) > 1:
                return int(binary_string[:-1], 2), int(binary_string[-1])
            else:
                return 0, int(binary_string)
        else:
            value = abs(value)
            if value == 1:
                return -1, 1
            if value % 2 == 0:
                binary_string = str(bin(value))[2:]
                return -int(binary_string[:-1], 2), int(binary_string[-1])
            else:
                binary_string = str(bin(value+2))[2:]
                return -int(binary_string[:-1], 2), int(binary_string[-1])

    def getWays(self):
        return self.ways

    def defineWays(self, f):
        for x in [0, 1]:
            for y in [0, 1]:
                if self.ways[x][y][0] is None:
                    self.ways[x][y][0], self.ways[x][y][1] = self.__split(f(x, y) - f(0, 0) + self.value)
