from enum import Enum
from field import Field
from layout import Layout
from mino_queue import MinoQueue
from constants import GameState, MoveDirection
import constants as C

class Game:
    def __init__(self):
        self.field = Field()
        self.queue = MinoQueue()
        self.layout = Layout(self.field, self.queue)
        self.mino = self.queue.get_next()
        self.state = GameState.PLAYING
        self.__reset_counter()

    def update(self):
        if self.field.remove_complete_lines():
            return
                
        if self.__is_game_over():
            self.state = GameState.GAME_OVER
            self.layout.reduce_drawable_line()
            return

        self.advance_counter -= self.reduce_count
        if self.advance_counter <= 0:
            self.__advance()
        

    def draw(self):
        self.layout.draw(self.mino)

    def move(self, direction):
        if self.mino.can_move(self.field, direction):
            self.mino.move(direction)
    
    def rotate(self, direction):
        if self.mino.can_rotate(self.field, direction):
            self.mino.rotate(direction)
    
    def drop(self):
        while self.mino.can_move(self.field, MoveDirection.DOWN):
            self.mino.move(MoveDirection.DOWN)
   
    def __is_game_over(self):
        if not self.mino.is_initial_position(): return False
        if self.mino.can_move(self.field, C.MoveDirection.DOWN): return False

        return True

    def __advance(self):
        if self.mino.can_move(self.field, MoveDirection.DOWN):
            self.mino.move(MoveDirection.DOWN)
            self.__reset_counter()
        else:
            self.field.store(self.mino.blocks, self.mino.position)
            self.mino = self.queue.get_next()
            self.advance_counter += 1

    def __reset_counter(self):
        self.advance_counter = C.ADVANCE_COUNTER
        self.reduce_count = C.REDUCE_COUNT
