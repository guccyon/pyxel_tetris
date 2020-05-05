import pyxel
from mino import Block

class Frame:
    def __init__(self, field):
        self.field = field
        self.__drawable_line = self.field.height + 2
    
    def draw(self, current_mino):
        self.__draw_background()

        self.field.draw(1, 1, self.__drawable_line)

        if self.__drawable_line > 2:
            self.__output_mino()        
            current_mino.draw(1, 1)

        if self.field.is_game_over(current_mino):
            self.__drawable_line -= 1

    def __draw_background(self):
        for y in range(self.field.height + 2):
            for x in range(self.field.width + 2):
                pyxel.blt(x * 8, y * 8, 0, 0, 8, 8, 8)  

    def __output_mino(self):
        for x in range(3, 9):
            Block.Blank.draw_block(x * 8, 0)
