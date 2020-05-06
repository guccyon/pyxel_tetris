import pyxel
import constants as C
from rotator import Rotator
from constants import Rotation, MoveDirection
from coordinate import Point
from block import Blocks, Block

class Mino:
    INITIAL = -1

    def __init__(self, mino_type, position = Point(4, INITIAL), rotation = Rotation.UP):
        self.rotation = rotation
        self.mino_type = mino_type
        self.position = position
        self.__update_ceched_blocks()

    def move(self, direction):
        self.position = self.position.apply(direction)
            
    def rotate(self, direction):
        self.rotation = self.rotation.apply(direction)
        self.__update_ceched_blocks()
    
    def can_move(self, field, direction):
        next_pos = self.position.apply(direction)
        if next_pos.x < 0: return False
        if C.FIELD_WIDTH < next_pos.x + self.blocks.width: return False
        if C.FIELD_HEIGHT < next_pos.y + self.blocks.height: return False
        for pos, _ in self.blocks.flatten(next_pos):
            if field[pos.y][pos.x] != Block.Blank: return False

        return True
    
    def can_rotate(self, field, direction):
        next_rotation = self.rotation.apply(direction)
        rotated = Rotator(self.mino_type.value, next_rotation).rotate()
        for pos, _ in Blocks(rotated).flatten(self.position):
            if pos.x < 0: return False                          # left edge
            if C.FIELD_WIDTH < pos.x: return False              # right edge
            if C.FIELD_HEIGHT < pos.y: return False             # bottom edge
            if field[pos.y][pos.x] != Block.Blank: return False # stored blocks

        return True
    
    def draw(self, offset):
        offset = Point(self.position.x + offset.x, self.position.y + offset.y)
        self.blocks.draw(offset)
    
    def __update_ceched_blocks(self):
        rotated = Rotator(self.mino_type.value, self.rotation).rotate()
        self.blocks = Blocks(rotated)



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
