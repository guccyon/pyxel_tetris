import pyxel
import constants as C
from coordinate import Point, Px
from block import Block

class Layout:
    def __init__(self, field, queue, score, holding, player_no):
        self.field = field
        self.queue = queue
        self.score = score
        self.holding = holding
        self.__drawable_line = C.FIELD_HEIGHT + 2
        self.player_no = player_no
        self.offset = Point(15.5 * player_no, 0)
    
    def draw(self, current_mino):
        self.field.draw(self.offset.add(1, 1), self.__drawable_line)
        self.holding.draw(self.offset.add(11.5, 1))
        self.queue.draw(self.offset.add(11.5, 6))
        self.score.draw(self.offset.add(1, 22))

        if self.__drawable_line > 2:
            current_mino.draw(self.offset.add(1, 1))
    
    def reduce_drawable_line(self):
        if self.__drawable_line > 0:
            self.__drawable_line -= 1
