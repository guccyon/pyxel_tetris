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
        self.current_mino = self.queue.get_next()
        self.state = GameState.PLAYING
        self.__reset_counter()

    def update(self):
        if self.field.remove_complete_lines():
            return
                
        if self.field.is_game_over(self.current_mino):
            self.state = GameState.GAME_OVER
            return

        self.advance_counter -= self.reduce_count
        if self.advance_counter <= 0:
            self.__advance()
        

    def draw(self):
        self.layout.draw(self.current_mino)

    def move(self, direction):
        if self.current_mino.can_move(self.field.field, direction):
            self.current_mino.move(direction)
    
    def rotate(self, direction):
        if self.current_mino.can_rotate(self.field.field, direction):
            self.current_mino.rotate(direction)
    
    def drop(self):
        while self.current_mino.can_move(self.field.field, MoveDirection.DOWN):
            self.current_mino.move(MoveDirection.DOWN)
    
    def __advance(self):
        if self.current_mino.can_move(self.field.field, MoveDirection.DOWN):
            self.current_mino.move(MoveDirection.DOWN)
            self.__reset_counter()
        else:
            self.field.store(self.current_mino)
            self.current_mino = self.queue.get_next()
            self.advance_counter += 1

    def __reset_counter(self):
        self.advance_counter = C.ADVANCE_COUNTER
        self.reduce_count = C.REDUCE_COUNT
