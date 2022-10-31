import math
import numpy as np


class Projection:
    def __init__(self, render):
        self.projection_matrix = np.array([
            [2 / (math.tan(render.camera.fov_height / 2) - (-math.tan(render.camera.fov_height / 2))), 0, 0, 0],
            [0, 2 / (math.tan(render.camera.fov_width / 2) - (-math.tan(render.camera.fov_width / 2))), 0, 0],
            [0, 0, (render.camera.far_plane + render.camera.near_plane) /
             (render.camera.far_plane - render.camera.near_plane), 1],
            [0, 0, -2 * render.camera.near_plane * render.camera.far_plane /
             (render.camera.far_plane - render.camera.near_plane), 0]
        ])

        self.screen_matrix = np.array([
            [render.window.middle_width, 0, 0, 0],
            [0, -render.window.middle_height, 0, 0],
            [0, 0, 1, 0],
            [render.window.middle_width, render.window.middle_height, 0, 1]
        ])
