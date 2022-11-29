import numpy as np
import pygame as pg
from Render.Object.object_engine import ObjectEngine
from settings import RESOURCES_OBJECTS, PRIMITIVE_COLOR_R, PRIMITIVE_COLOR_G, PRIMITIVE_COLOR_B


class Pyramid(ObjectEngine):
    def __init__(self, render, faces=np.array([(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 3, 2)]),
                 vertices=np.array([(0, 0, 0, 1), (20, 0, 0, 1), (10, 0, 20, 1), (10, 20, 10, 1)]), obj=0):
        super().__init__(render, vertices, faces, obj)

        self.vertices = vertices
        self.update_position(RESOURCES_OBJECTS[obj][1])
        self.faces = faces

        self.color_faces = [(pg.Color(PRIMITIVE_COLOR_R, PRIMITIVE_COLOR_G, PRIMITIVE_COLOR_B), face) for face in
                            self.faces]

        self.drawing_vertices = False
        self.label = ''
