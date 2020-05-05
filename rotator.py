import numpy as np
from enums import Rotation, MinoType

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
            return [list(i) for i in np.transpose(self.matrix)]
        else:
            return self.matrix

if __name__ == "__main__":
    for i in Rotator(MinoType.Z_MINO.value, Rotation.UP).rotate(): print(i)
    for i in Rotator(MinoType.Z_MINO.value, Rotation.RIGHT).rotate(): print(i)
    for i in Rotator(MinoType.Z_MINO.value, Rotation.DOWN).rotate(): print(i)
    for i in Rotator(MinoType.Z_MINO.value, Rotation.LEFT).rotate(): print(i)
    for i in Rotator(MinoType.I_MINO.value, Rotation.UP).rotate(): print(i)
    for i in Rotator(MinoType.I_MINO.value, Rotation.RIGHT).rotate(): print(i)
    for i in Rotator(MinoType.I_MINO.value, Rotation.DOWN).rotate(): print(i)
    for i in Rotator(MinoType.I_MINO.value, Rotation.LEFT).rotate(): print(i)
    for i in Rotator(MinoType.T_MINO.value, Rotation.UP).rotate(): print(i)
    for i in Rotator(MinoType.T_MINO.value, Rotation.RIGHT).rotate(): print(i)
    for i in Rotator(MinoType.T_MINO.value, Rotation.DOWN).rotate(): print(i)
    for i in Rotator(MinoType.T_MINO.value, Rotation.LEFT).rotate(): print(i)