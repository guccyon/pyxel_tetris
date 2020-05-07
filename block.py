import pyxel
from enum import Enum
from coordinate import Point

class Block(Enum):
    BLANK = -1
    BRICK = 0
    GREEN = 1
    RED = 2
    BLUE = 3
    ORANGE = 4
    YELLOW = 5
    PURPLE = 6
    L_BLUE = 7

    def draw_block(self, x, y, small = False):
        if self == self.__class__.BLANK:
            pyxel.rect(x, y, 8, 8, pyxel.COLOR_BLACK)
        elif small:
            pyxel.blt(x, y, 0, self.value * 6, 8, 6, 6)
        else:
            pyxel.blt(x, y, 0, self.value * 8, 0, 8, 8)
    
    def draw(self, point, small = False):
        actual = point.actual()
        self.draw_block(actual.x, actual.y, small)

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
        for y, row in enumerate(self.matrix):
            for x, column in enumerate(row):
                if column == 0: continue
                
                Block(column).draw(offset.add(x, y))
