import pyxel
import random
from queue import SimpleQueue
from constants import MinoType
from mino import Mino
from block import Block


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
            6 * 6, 4 * 6,
            pyxel.COLOR_BLACK)

        self.__draw_comming_block(
            offset.add(1, 0.7),
            self.list[0].value)
    
    def __draw_comming_block(self, offset, matrix):
        actual_offset = offset.actual()
        for y, row in enumerate(matrix):
            for x, column in enumerate(row):
                if column == 0: continue
                
                Block(column).draw_block(
                    actual_offset.x + (x * 6),
                    actual_offset.y + (y * 6),
                    True)

