import pyxel
from mino_queue import MinoQueue
from field import Field
from frame import Frame
from mino import Mino
from enums import MoveDirection, RotateDirection
from enum import Enum

SCREEN_WIDTH = 80 + 16
SCREEN_HEIGHT = 160 + 16

# REDUCE_COUNT / ADVANCE_COUNTER = times to move per frame
REDUCE_COUNT = 1
ADVANCE_COUNTER = 15
FPS = 30

class App:
    ####################
    ## Initialization
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps = FPS)
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
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.move(MoveDirection.LEFT)
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.move(MoveDirection.RIGHT)
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD_1_DOWN):
            self.move(MoveDirection.DOWN)
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD_1_UP):
            self.drop()

        ## Rotating
        if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.GAMEPAD_1_A):
            self.rotate(RotateDirection.LEFT)
        if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.GAMEPAD_1_X):
            self.rotate(RotateDirection.RIGHT)

    ####################
    ## Game Logic
    def update(self):
        if self.field.remove_complete_lines():
            return
                
        if self.field.is_game_over(self.current_mino):
            return

        self.handle_event()

        self.advance_counter -= self.reduce_count
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
        self.advance_counter = ADVANCE_COUNTER
        self.reduce_count = REDUCE_COUNT

    ####################
    ## Output
    def draw(self):
        # pyxel.cls(pyxel.COLOR_BLACK)
        self.frame.draw(self.current_mino)

App()
