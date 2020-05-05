from enum import Enum
import pyxel
from rotator import Rotator
from constants import MinoType, Rotation, MoveDirection, RotateDirection

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def apply(self, direction):
        return Vec2(
            self.x + direction.value[0],
            self.y + direction.value[1]
        )

class Block(Enum):
    Blank = 0
    GREEN = 1
    RED = 2
    BLUE = 3
    ORANGE = 4
    YELLOW = 5
    PURPLE = 6
    L_BLUE = 7

    def draw_block(self, x, y):
        if self == self.__class__.Blank:
            pyxel.rect(x, y, 8, 8, pyxel.COLOR_BLACK)
        else:
            pyxel.blt(x, y, 0, self.value * 8, 0, 8, 8)


class Mino:
    def __init__(self, mino_type, position = Vec2(4, -1), rotation = Rotation.UP):
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

    
    def draw(self, offset_x, offset_y):
        for i, row in enumerate(self.rotated_blocks()):
            for j, column in enumerate(row):
                if column == 0: continue

                actual_x = (self.position.x + offset_x + j) * 8
                actual_y = (self.position.y + offset_y + i) * 8
                block = Block(column)
                block.draw_block(actual_x, actual_y)
    
    def __update_size(self):
        blocks = self.rotated_blocks()
        self.height = len(blocks)
        self.width = len(blocks[0])



if __name__ == "__main__":
    pos = Vec2(5, 5)
    down = pos.apply(MoveDirection.DOWN)
    assert down.x == 5
    assert down.y == 6
    left = pos.apply(MoveDirection.LEFT)
    assert left.x == 4
    assert left.y == 5
    right = pos.apply(MoveDirection.RIGHT)
    assert right.x == 6
    assert right.y == 5
