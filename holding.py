import pyxel
from mino import Mino
from block import Block

class Holding:
    def __init__(self):
        self.__locked = False
        self.__mino_type = None

    def can_hold(self):
        return not self.__locked

    def hold(self, mino):
        self.__locked = True
        if self.__mino_type == None:
            self.__mino_type = mino.mino_type
            return None
        else:
            unhold_mino = Mino(self.__mino_type)
            self.__mino_type = mino.mino_type
            return unhold_mino

    def unlock(self):
        self.__locked = False
    
    def draw(self, offset):
        offset = offset.add(1, 1)

        pyxel.rect(
            offset.actual().x, offset.actual().y,
            32, 32,
            pyxel.COLOR_BLACK)
        pyxel.text(
            offset.add(1, 0).actual().x, offset.actual().y,
            "Hold",
            pyxel.COLOR_WHITE
        )
        if self.__mino_type:
            self.__draw_holding_mino(offset.add(0, 1), self.__mino_type.value)
        
    def __draw_holding_mino(self, offset, matrix):       
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
        