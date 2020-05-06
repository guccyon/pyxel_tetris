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
            self.advance()
        

    def draw(self):
        self.layout.draw(self.current_mino)

    def move(self, direction):
        next_mino = self.current_mino.clone_applied_with(move_direction=direction)
        if self.field.is_collision(next_mino):
            self.current_mino.move(direction)
    
    def rotate(self, direction):
        next_mino = self.current_mino.clone_applied_with(rotate_direction=direction)
        if self.field.is_collision(next_mino):
            self.current_mino.rotate(direction)
    
    def drop(self):
        while self.field.can_move(self.current_mino, MoveDirection.DOWN):
            self.current_mino.move(MoveDirection.DOWN)
    
    def advance(self):
        if self.field.can_move(self.current_mino, MoveDirection.DOWN):
            self.current_mino.move(MoveDirection.DOWN)
            self.__reset_counter()
        else:
            self.field.store(self.current_mino)
            self.current_mino = self.queue.get_next()
            self.advance_counter += 1

    def __reset_counter(self):
        self.advance_counter = C.ADVANCE_COUNTER
        self.reduce_count = C.REDUCE_COUNT
