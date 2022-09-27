import math
import numpy as np


class MatrixFunctions:
    @staticmethod
    def translate(pos):
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [pos[0], pos[1], pos[2], 1]
        ])

    @staticmethod
    def rotate_x(a):
        return np.array([
            [1, 0, 0, 0],
            [0, math.cos(a), math.sin(a), 0],
            [0, -math.sin(a), math.cos(a), 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def rotate_y(a):
        return np.array([
            [math.cos(a), 0, -math.sin(a), 0],
            [0, 1, 0, 0],
            [math.sin(a), 0, math.cos(a), 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def rotate_z(a):
        return np.array([
            [math.cos(a), math.sin(a), 0, 0],
            [-math.sin(a), math.cos(a), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def scale(n):
        return np.array([
            [n, 0, 0, 0],
            [0, n, 0, 0],
            [0, 0, n, 0],
            [0, 0, 0, 1]
        ])
