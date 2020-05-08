import pyxel
from game import Game
from constants import GameState, MoveDirection, RotateDirection
import constants as C
from block import Block
from coordinate import Point

class App:
    ####################
    ## Initialization
    def __init__(self):
        pyxel.init(C.SCREEN_WIDTH, C.SCREEN_HEIGHT, fps = C.FPS)
        pyxel.load('assets/tetris.pyxres')
        self.start_game()
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    ####################
    ## Input
    def handle_event(self):
        if self.games[0].state == GameState.GAME_OVER:
            self.handle_event_game_over()
        else:
            self.handle_event_playing_for_1()
            if len(self.games) == 2:
                self.handle_event_playing_for_2()

    def handle_event_game_over(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.start_game()
    
    def handle_event_playing_for_1(self):
        ## Moving
        if pyxel.btnp(pyxel.KEY_W) or pyxel.btnp(pyxel.GAMEPAD_1_UP):
            self.games[0].drop()
        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.GAMEPAD_1_LEFT):
            self.games[0].move(MoveDirection.LEFT)
        if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.GAMEPAD_1_DOWN):
            self.games[0].move(MoveDirection.DOWN)
        if pyxel.btnp(pyxel.KEY_D) or pyxel.btnp(pyxel.GAMEPAD_1_RIGHT):
            self.games[0].move(MoveDirection.RIGHT)
        ## Holding
        if pyxel.btnp(pyxel.KEY_C) or pyxel.btnp(pyxel.GAMEPAD_1_RIGHT_SHOULDER):
            self.games[0].hold()        
        ## Rotating
        if pyxel.btnp(pyxel.KEY_V) or pyxel.btnp(pyxel.GAMEPAD_1_A):
            self.games[0].rotate(RotateDirection.LEFT)
        if pyxel.btnp(pyxel.KEY_B) or pyxel.btnp(pyxel.GAMEPAD_1_X):
            self.games[0].rotate(RotateDirection.RIGHT)
    
    def handle_event_playing_for_2(self):
        ## Moving
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD_2_UP):
            self.games[1].drop()
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD_2_LEFT):
            self.games[1].move(MoveDirection.LEFT)
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD_2_DOWN):
            self.games[1].move(MoveDirection.DOWN)
        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD_2_RIGHT):
            self.games[1].move(MoveDirection.RIGHT)
        ## Holding
        if pyxel.btnp(pyxel.KEY_M) or pyxel.btnp(pyxel.GAMEPAD_2_RIGHT_SHOULDER):
            self.games[1].hold()
        ## Rotating
        if pyxel.btnp(pyxel.KEY_COMMA) or pyxel.btnp(pyxel.GAMEPAD_2_A):
            self.games[1].rotate(RotateDirection.LEFT)
        if pyxel.btnp(pyxel.KEY_PERIOD) or pyxel.btnp(pyxel.GAMEPAD_2_X):
            self.games[1].rotate(RotateDirection.RIGHT)        


    ####################
    ## Game Logic
    def update(self):
        for g in self.games: g.update()

        self.handle_event()
    
    def start_game(self):
        self.games = [Game(0)]

    ####################
    ## Output
    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        self.__draw_background()
        for g in self.games: g.draw()

    def __draw_background(self):
        for y in range(C.FIELD_HEIGHT + 2):
            for x in range(C.SCREEN_WIDTH):
                Block.BRICK.draw(Point(x, y))        

App()
