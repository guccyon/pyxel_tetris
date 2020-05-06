import pyxel
import random
from queue import SimpleQueue
from constants import MinoType
from mino import Mino


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
            offset.x * 8, offset.y * 8,
            4 * 8, 4 * 8,
            pyxel.COLOR_BLACK)


        # self.draw_comming_mino(self.list[0].value)
        
        # self.list[0].draw(
        #     offset_x.add(1).actual(),
        #     offset_y.add(1).actual(),
        #     small = True
        # )
    
    # def draw_comming_mino(self, blocks):
    #     for i, row in enumerate(blocks):
    #         for j, column in enumerate(row):
    #             if column == 0: continue

    #             actual_x = (self.position.x + offset_x + j) * 8
    #             actual_y = (self.position.y + offset_y + i) * 8
    #             block = Block(column)
    #             block.draw_block(actual_x, actual_y, small)

        
