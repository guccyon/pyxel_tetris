import pyxel
import constants as C
from mino import Block
from coordinate import Point

class Layout:
    def __init__(self, field, queue):
        self.field = field
        self.queue = queue
        self.__drawable_line = C.FIELD_HEIGHT + 2
    
    def draw(self, current_mino):
        self.__draw_background()

        self.field.draw(Point(1, 1), self.__drawable_line)
        self.queue.draw(Point(12, 1))

        if self.__drawable_line > 2:
            self.__output_mino()        
            current_mino.draw(Point(1, 1))

        if self.field.is_game_over(current_mino):
            self.__drawable_line -= 1

    def __draw_background(self):
        for y in range(C.FIELD_HEIGHT + 2):
            for x in range(C.FIELD_WIDTH + 8):
                pyxel.blt(x * 8, y * 8, 0, 0, 8, 8, 8)  

    def __output_mino(self):
        for x in range(3, 9):
            Block.Blank.draw_block(Point(x, 0))
