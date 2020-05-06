from enum import Enum
import pyxel
from rotator import Rotator
from constants import MinoType, Rotation, MoveDirection, RotateDirection
from coordinate import Point

class Block(Enum):
    Blank = 0
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
        else:
            pyxel.blt(point.x * 8, point.y * 8, 0, self.value * 8, 0, 8, 8)

class Blocks:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def draw(self, offset, small = False):
        for i, row in enumerate(self.matrix):
            for j, column in enumerate(row):
                if column == 0: continue
                
                Block(column).draw_block(Point(offset.x + j, offset.y + i))

class Mino:
    def __init__(self, mino_type, position = Point(4, -1), rotation = Rotation.UP):
        self.rotation = rotation
        self.mino_type = mino_type
        self.position = position
        self.__update_size()

    def move(self, direction):
        self.position = self.position.apply(direction)
            
    def rotate(self, direction):
        self.rotation = self.rotation.apply(direction)
        
    def rotated_blocks(self):
        return Rotator(self.mino_type.value, self.rotation).rotate()
    
    def clone_applied_with(self, move_direction = None, rotate_direction = None):
        position = self.position.apply(move_direction) if move_direction else self.position
        rotation = self.rotation.apply(rotate_direction) if rotate_direction else self.rotation
        return Mino(self.mino_type, position, rotation)

    
    def draw(self, offset):
        for i, row in enumerate(self.rotated_blocks()):
            for j, column in enumerate(row):
                if column == 0: continue

                point = Point(self.position.x + offset.x + j, self.position.y + offset.y + i)
                Block(column).draw_block(point)
    
    def __update_size(self):
        blocks = self.rotated_blocks()
        self.height = len(blocks)
        self.width = len(blocks[0])



if __name__ == "__main__":
    pos = Point(5, 5)
    down = pos.apply(MoveDirection.DOWN)
    assert down.x == 5
    assert down.y == 6
    left = pos.apply(MoveDirection.LEFT)
    assert left.x == 4
    assert left.y == 5
    right = pos.apply(MoveDirection.RIGHT)
    assert right.x == 6
    assert right.y == 5
