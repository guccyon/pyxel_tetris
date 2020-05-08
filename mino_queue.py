import pyxel
import random
from queue import SimpleQueue
from constants import MinoType
from mino import Mino
from block import Block
from coordinate import Px

class MinoQueue:
    def __init__(self):
        self.list = []
        self.prepare_next_round()

    def get_next(self):
        mino = Mino(self.list.pop(0))
        if len(self.list) < 5:
            self.prepare_next_round()
        return mino
    
    def prepare_next_round(self):
        types = list(MinoType)
        random.shuffle(types)
        for i in types:
            self.list.append(i)
    
    def draw(self, offset):
        pyxel.rect(
            offset.actual().x, offset.actual().y,
            Px(4).actual(), Px(4).actual(),
            pyxel.COLOR_BLACK)
            
        pyxel.text(
            offset.add(1, 0).actual().x, offset.actual().y,
            "Next",
            pyxel.COLOR_WHITE
        )
        self.__draw_comming_block(offset.add(0, 1), self.list[0].value)
    
    def __draw_comming_block(self, offset, matrix):       
        actual_offset = offset.actual().add(
            (32 - len(matrix[0]) * 6) / 2,
            (24 - len(matrix) * 6) / 2)
        for y, row in enumerate(matrix):
            for x, column in enumerate(row):
                if column == 0: continue
                
                Block(column).draw_block(
                    actual_offset.x + (x * 6),
                    actual_offset.y + (y * 6),
                    True)

