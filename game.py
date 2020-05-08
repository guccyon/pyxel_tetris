from enum import Enum
import pyxel
import constants as C
from constants import GameState, MoveDirection
from field import Field
from layout import Layout
from mino_queue import MinoQueue
from holding import Holding
from score import Score
        

class Game:
    def __init__(self):
        self.field = Field()
        self.queue = MinoQueue()
        self.score = Score()
        self.__holding = Holding()
        self.layout = Layout(self.field, self.queue, self.score, self.__holding)
        self.mino = self.queue.get_next()
        self.state = GameState.PLAYING
        self.__reset_counter()

    def update(self):
        removed_lines = self.field.remove_complete_lines()
        if len(removed_lines) > 0:
            self.score.count_removed(removed_lines)
            return
                
        if self.__is_game_over():
            pyxel.stop(0)
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
            pyxel.play(1, 3)
            self.mino.move(direction)
    
    def rotate(self, direction):
        if self.mino.can_rotate(self.field, direction):
            pyxel.play(1, 5)
            self.mino.rotate(direction)
    
    def drop(self):
        while self.mino.can_move(self.field, MoveDirection.DOWN):
            self.mino.move(MoveDirection.DOWN)
        self.__put_on()
    
    def hold(self):
        if self.__holding.can_hold():
            self.mino = self.__holding.hold(self.mino)
            if self.mino == None:
                self.mino = self.queue.get_next()

    def __is_game_over(self):
        if not self.mino.is_initial_position(): return False
        if self.mino.can_move(self.field, C.MoveDirection.DOWN): return False

        return True

    def __advance(self):
        if self.mino.can_move(self.field, MoveDirection.DOWN):
            self.mino.move(MoveDirection.DOWN)
            self.__reset_counter()
        else:
            self.__put_on()
    
    def __put_on(self):
        self.field.store(self.mino.blocks, self.mino.position)
        pyxel.play(1, 4)
        self.mino = self.queue.get_next()
        self.advance_counter += 1
        self.__holding.unlock()

    def __reset_counter(self):
        self.advance_counter = C.ADVANCE_COUNTER
        self.reduce_count = C.REDUCE_COUNT
