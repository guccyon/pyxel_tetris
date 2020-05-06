from enum import Enum

FIELD_WIDTH = 10
FIELD_HEIGHT = 20

# REDUCE_COUNT / ADVANCE_COUNTER = times to move per frame
REDUCE_COUNT = 1
ADVANCE_COUNTER = 20
FPS = 30

class GameState(Enum):
    PLAYING = 0
    GAME_OVER = 1

class MinoType(Enum):
    S_MINO = [
        [0, 1, 1],
        [1, 1, 0]
    ]
    Z_MINO = [
        [2, 2, 0],
        [0, 2, 2]
    ]
    J_MINO = [
        [3, 0, 0],
        [3, 3, 3]
    ]
    L_MINO =  [
        [4, 4, 4],
        [4, 0, 0]
    ]
    O_MINO = [
        [5, 5],
        [5, 5]
    ]
    T_MINO = [
        [0, 6, 0],
        [6, 6, 6]
    ]
    I_MINO = [
        [7, 7, 7, 7]
    ]

class Rotation(Enum):
    UP = 0
    RIGHT = 90
    DOWN = 180
    LEFT = 270        

    def apply(self, direction):
        return Rotation.value_of(self.value + direction.value)

    @staticmethod
    def value_of(num):
        return Rotation((num + 360) % 360)

class MoveDirection(Enum):
    LEFT  = (-1, 0)
    RIGHT = (1, 0)
    DOWN  = (0, 1)

class RotateDirection(Enum):
    LEFT = -90
    RIGHT = 90
