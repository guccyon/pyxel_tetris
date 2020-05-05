import pyxel
from game import Game, GameState
from enums import MoveDirection, RotateDirection

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
        self.start_game()
        pyxel.run(self.update, self.draw)

    ####################
    ## Input
    def handle_event(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        if self.game.state == GameState.GAME_OVER:
            self.handle_event_game_over()
        else:
            self.handle_event_playing()
    
    def handle_event_game_over(self):
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD_1_X):
            self.start_game()
    
    def handle_event_playing(self):
        ## Moving
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.game.move(MoveDirection.LEFT)
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.game.move(MoveDirection.RIGHT)
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD_1_DOWN):
            self.game.move(MoveDirection.DOWN)
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD_1_UP):
            self.game.drop()

        ## Rotating
        if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.GAMEPAD_1_A):
            self.game.rotate(RotateDirection.LEFT)
        if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.GAMEPAD_1_X):
            self.game.rotate(RotateDirection.RIGHT)

    ####################
    ## Game Logic
    def update(self):
        self.game.update()

        self.handle_event()
    
    def start_game(self):
        self.game = Game()      

    ####################
    ## Output
    def draw(self):
        # pyxel.cls(pyxel.COLOR_BLACK)
        self.game.draw()

App()
