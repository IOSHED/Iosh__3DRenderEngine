import math
import numpy as np
from Render.Matrix_functions.camera_matrix import CameraMatrix
from Render.Camera.control_camera import ControlCamera
from Render.Matrix_functions.matrix import MatrixFunctions


class Camera:
    def __init__(self, render, position):
        self.render = render
        self.control = ControlCamera(self)

        self.position = np.array([*position, 1.0])

        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])
        self.left = np.array([0, 1, 0, 1])

        self.fov_height = math.pi / 3
        self.fov_width = self.fov_height * (render.window.height / render.window.width)

        self.near_plane = 1
        self.far_plane = 100

    def camera_matrix(self):
        return CameraMatrix.translate_matrix(self) @ CameraMatrix.rotate_matrix(self)

    def camera_yaw(self, angle):
        rotate = MatrixFunctions.rotate_y(angle)
        self.forward = self.forward @ rotate
        self.left = self.left @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    def camera_pitch(self, angle):
        rotate = MatrixFunctions.rotate_x(angle)
        self.forward = self.forward @ rotate
        self.left = self.left @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    def control_camera(self):
        self.control.control_camera()
