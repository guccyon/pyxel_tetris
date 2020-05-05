import pyxel
from mino_queue import MinoQueue
from field import Field
from frame import Frame
from mino import Mino
from enums import MoveDirection, RotateDirection
from enum import Enum

SCREEN_WIDTH = 80 + 16
SCREEN_HEIGHT = 160 + 16

class App:
    ####################
    ## Initialization
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps = 30)
        pyxel.load('assets/images.pyxres')
        self.field = Field()
        self.frame = Frame(self.field)
        self.queue = MinoQueue()
        self.current_mino = self.queue.get_next()
        self.__reset_counter()
        pyxel.run(self.update, self.draw)


    ####################
    ## Input
    def handle_event(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        ## Moving
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.move(MoveDirection.LEFT)
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.move(MoveDirection.RIGHT)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.move(MoveDirection.DOWN)

        ## Rotating
        if pyxel.btnp(pyxel.KEY_Z):
            self.rotate(RotateDirection.LEFT)
        if pyxel.btnp(pyxel.KEY_X) or pyxel.btn(pyxel.KEY_SPACE):
            self.rotate(RotateDirection.RIGHT)

    ####################
    ## Game Logic
    def update(self):
        if self.field.remove_complete_lines():
            return
                
        if self.field.is_game_over(self.current_mino):
            return

        self.handle_event()

        self.advance_counter -= 1
        if self.advance_counter <= 0:
            self.advance()

    def move(self, direction):
        next_mino = self.current_mino.clone_applied_with(move_direction=direction)
        if self.field.is_collision(next_mino):
            self.current_mino.move(direction)
    
    def rotate(self, direction):
        next_mino = self.current_mino.clone_applied_with(rotate_direction=direction)
        if self.field.is_collision(next_mino):
            self.current_mino.rotate(direction)
    
    def advance(self):
        if self.field.can_move(self.current_mino, MoveDirection.DOWN):
            self.current_mino.move(MoveDirection.DOWN)
        else:
            self.field.store(self.current_mino)
            self.current_mino = self.queue.get_next()
        self.__reset_counter()

    def __reset_counter(self):
        self.advance_counter = 30

    ####################
    ## Output
    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        self.frame.draw(self.current_mino)

App()
