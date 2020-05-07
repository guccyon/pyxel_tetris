import numpy as np
from enum import Enum
from constants import RotateDirection

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

class Rotator:
    def __init__(self, matrix, rotation):
        self.matrix = matrix
        self.rotation = rotation

    def rotate(self):
        if self.rotation == Rotation.RIGHT:
            return [list(i) for i in np.transpose(list(reversed(self.matrix)))]
        elif self.rotation == Rotation.DOWN:
            return [list(i) for i in reversed([reversed(i) for i in self.matrix])]
        elif self.rotation == Rotation.LEFT:
            return list(reversed([i for i in np.transpose(self.matrix)]))
        else:
            return self.matrix
