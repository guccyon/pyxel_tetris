import pyxel
from enum import Enum
import constants as C

class Score:
    def __init__(self):
        self.score = 0
        self.line_count = 0
    
    def count_removed(self, removed_lines):
        self.line_count += len(removed_lines)

        if len(removed_lines) == 1:
            self.score += 100
        elif len(removed_lines) == 2:
            self.score += 300
        elif len(removed_lines) == 3:
            self.score += 800
        elif len(removed_lines) == 4:
            self.score += 1500

    def draw(self, offset):
        pyxel.text(
            offset.actual().x,
            offset.actual().y,
            "Lines: " + str(self.line_count),
            pyxel.COLOR_WHITE
        )
        pyxel.text(
            offset.actual().x,
            offset.actual().y + 8,
            "Score:" + str(self.score),
            pyxel.COLOR_WHITE
        )
