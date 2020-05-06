import pyxel
import constants as C
from mino import Mino
from block import Block

class Field:
    def __init__(self):
        self.field = []
        for _ in range(C.FIELD_HEIGHT):
            self.field.append([Block.Blank] * C.FIELD_WIDTH)
    
    def store(self, mino):
        for pos, value in mino.blocks.flatten(mino.position):
            self.field[pos.y][pos.x] = Block(value)
    
    def remove_complete_lines(self):
        complete_line_indexes = [   
            i
            for i, line in enumerate(self.field)
            if all( col != Block.Blank for col in line )
        ]
        for i in complete_line_indexes:
            del self.field[i]
            self.field.insert(0, [Block.Blank] * C.FIELD_WIDTH)
        
        return len(complete_line_indexes) > 0
        
    def is_game_over(self, mino):
        if mino.position.y != Mino.INITIAL: return False
        if mino.can_move(self.field, C.MoveDirection.DOWN): return False

        return True

    def draw(self, offset, drawable_line):
        for i, line in enumerate(self.field):
            if drawable_line <= i: return 

            for j, block in enumerate(line):
                block.draw_block(offset.add(j, i))
