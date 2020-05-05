import pyxel
from mino import Block, Mino
from constants import MoveDirection
from rotator import Rotator
    
FIELD_WIDTH = 10
FIELD_HEIGHT = 20

def slice_rect(field, x, y, width, height):
    result = []
    for row_num in range(y, y + height):
        row = field[row_num][x:(x + width)]
        result.append(row)
    return result

class Field:
    def __init__(self):
        self.field = []
        for _ in range(FIELD_HEIGHT):
            self.field.append([0] * FIELD_WIDTH)
        self.width = len(self.field[0])
        self.height = len(self.field)
    
    def store(self, mino):
        for i, row in enumerate(mino.rotated_blocks()):
            field_line_num = i + mino.position.y
            for j, col in enumerate(row):
                if col == 0: continue    
                field_col_num = j + mino.position.x
                self.field[field_line_num][field_col_num] = col
    
    def remove_complete_lines(self):
        complete_line_indexes = [   
            i
            for i, line in enumerate(self.field)
            if all( col != 0 for col in line )
        ]
        for i in complete_line_indexes:
            del self.field[i]
            self.field.insert(0, [0] * FIELD_WIDTH)
        
        return len(complete_line_indexes) > 0

    def can_move(self, mino, direction):
        mino = mino.clone_applied_with(move_direction=direction)
        return self.is_collision(mino)
    
    def is_collision(self, mino):
        if self.__is_collision_with_edge(mino):
            return False

        if self.__is_collision_with_placed_blocks(mino):
            return False

        return True
    
    def is_game_over(self, mino):
        if mino.position.y == -1:
            clone = mino.clone_applied_with(move_direction=MoveDirection.DOWN)
            return self.__is_collision_with_placed_blocks(clone)
        else:
            return False

    def __is_collision_with_edge(self, mino):
        # left edge
        if mino.position.x < 0: return True
        # right edge
        if FIELD_WIDTH < mino.position.x + mino.width: return True
        # bottom edge
        if FIELD_HEIGHT < mino.position.y + mino.height: return True

        return False

    def __is_collision_with_placed_blocks(self, mino):
        rect = slice_rect(self.field, mino.position.x, mino.position.y, mino.width, mino.height)
        for i, row in enumerate(mino.rotated_blocks()):
            if any( x * y != 0 for x,y in zip(row, rect[i]) ):
                return True

        return False

    def draw(self, offset_x, offset_y, drawable_line):
        for i, line in enumerate(self.field):
            if i < drawable_line:
                self.__draw_line(i, line, offset_x, offset_y)
                
    def __draw_line(self, line_num, line, offset_x, offset_y):
        for col_num, col in enumerate(line):
            Block(col).draw_block(
                (col_num + offset_x) * 8,
                (line_num + offset_y) * 8
            )
