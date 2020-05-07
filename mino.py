import pyxel
import constants as C
from constants import MoveDirection
from rotator import Rotator, Rotation
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
        if self.__is_collision(field, self.blocks, next_pos):
            return False
        else:
            return True
    
    def can_rotate(self, field, direction):
        next_rotation = self.rotation.apply(direction)
        rotated = Rotator(self.mino_type.value, next_rotation).rotate()
        if self.__is_collision(field, Blocks(rotated), self.position):
            return False
        else:
            return True
    
    def is_initial_position(self):
        return self.position.y == Mino.INITIAL
        
    def draw(self, offset):
        offset = Point(self.position.x + offset.x, self.position.y + offset.y)
        self.blocks.draw(offset)
    
    def __update_ceched_blocks(self):
        rotated = Rotator(self.mino_type.value, self.rotation).rotate()
        self.blocks = Blocks(rotated)

    def __is_collision(self, field, blocks, position):
        for pos, _ in blocks.flatten(position):
            if pos.x < 0: return True                     # left edge
            if C.FIELD_WIDTH <= pos.x: return True        # right edge
            if C.FIELD_HEIGHT <= pos.y: return True       # bottom edge
            if field.is_stored(pos.x, pos.y): return True # stored blocks
        return False


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
