import pyxel
import constants as C
from coordinate import Point, Px
from block import Block

class Layout:
    def __init__(self, field, queue, score, holding):
        self.field = field
        self.queue = queue
        self.score = score
        self.holding = holding
        self.__drawable_line = C.FIELD_HEIGHT + 2
    
    def draw(self, current_mino):
        self.__draw_background()

        self.holding.draw(Point(0, 1))
        self.field.draw(Point(6, 1), self.__drawable_line)
        self.queue.draw(Point(17, 1))
        self.score.draw(Point(0, 22))

        if self.__drawable_line > 2:
            # self.__output_mino()        
            current_mino.draw(Point(6, 1))
    
    def reduce_drawable_line(self):
        self.__drawable_line -= 1

    def __draw_background(self):
        for y in range(C.FIELD_HEIGHT + 2):
            for x in range(C.SCREEN_WIDTH):
                Block.BRICK.draw(Point(x, y))

    def __output_mino(self):
        pyxel.rect(2 * 8, 0, 8 * 8, 8, pyxel.COLOR_BLACK)
