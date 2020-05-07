import pyxel
import constants as C
from block import Block
from coordinate import Point

class Field:
    def __init__(self):
        self.__matrix = []
        for _ in range(C.FIELD_HEIGHT):
            self.__matrix.append([Block.BLANK] * C.FIELD_WIDTH)
    
    def store(self, blocks, position):
        for pos, value in blocks.flatten(position):
            self.__matrix[pos.y][pos.x] = Block(value)
    
    def remove_complete_lines(self):
        complete_line_indexes = [   
            i
            for i, line in enumerate(self.__matrix)
            if all( col != Block.BLANK for col in line )
        ]
        for i in complete_line_indexes:
            del self.__matrix[i]
            self.__matrix.insert(0, [Block.BLANK] * C.FIELD_WIDTH)
        
        return len(complete_line_indexes) > 0
    
    def is_stored(self, x, y):
        return self.__matrix[y][x] != Block.BLANK
        
    def draw(self, offset, drawable_line):
        for i, line in enumerate(self.__matrix):
            if drawable_line <= i: return 

            for j, block in enumerate(line):
                point = Point(offset.x + j, offset.y + i)             
                block.draw(point)
