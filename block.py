import pyxel
from enum import Enum
from coordinate import Point

class Block(Enum):
    Blank = -1
    GREEN = 1
    RED = 2
    BLUE = 3
    ORANGE = 4
    YELLOW = 5
    PURPLE = 6
    L_BLUE = 7

    def draw_block(self, point, small = False):
        if self == self.__class__.Blank:
            pyxel.rect(point.x * 8, point.y * 8, 8, 8, pyxel.COLOR_BLACK)
        elif small:
            pyxel.blt(point.x * 8, point.y * 8, 0, self.value * 6, 8, 6, 6)
            # pyxel.blt(point.x * 8, point.y * 8, 0, self.value * 8, 0, 8, 8)
        else:
            pyxel.blt(point.x * 8, point.y * 8, 0, self.value * 8, 0, 8, 8)

class Blocks:
    def __init__(self, matrix):
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)

    def flatten(self, offset):
        result = []
        for y, row in enumerate(self.matrix):
            for x, col in enumerate(row):
                if col == 0: continue
                result.append( (offset.add(x, y), col) )
        return result
    
    def draw(self, offset):
        for i, row in enumerate(self.matrix):
            for j, column in enumerate(row):
                if column == 0: continue

                point = Point(offset.x + j, offset.y + i)
                Block(column).draw_block(point)
