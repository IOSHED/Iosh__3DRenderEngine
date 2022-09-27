import numpy as np


class CameraMatrix:
    @staticmethod
    def translate_matrix(self):
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-self.position[0], -self.position[1], -self.position[2], 1]
        ])

    @staticmethod
    def rotate_matrix(self):
        return np.array([
            [self.right[0], self.up[0], self.forward[0], 0],
            [self.right[1], self.up[1], self.forward[1], 0],
            [self.right[2], self.up[2], self.forward[2], 0],
            [0, 0, 0, 1]
        ])
