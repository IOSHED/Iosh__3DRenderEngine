import numpy as np
import pygame as pg
from Render.Object.object_engine import ObjectEngine
from settings import RESOURCES_OBJECTS, PRIMITIVE_COLOR_R, PRIMITIVE_COLOR_G, PRIMITIVE_COLOR_B


class Cube(ObjectEngine):
    def __init__(self, render, faces=np.array([(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (2, 3, 7, 6), (1, 2, 6, 5),
                                               (0, 3, 7, 4)]), vertices=np.array([(0, 0, 0, 1), (0, 20, 0, 1),
                                                                                  (20, 20, 0, 1), (20, 0, 0, 1),
                                                                                  (0, 0, 20, 1), (0, 20, 20, 1),
                                                                                  (20, 20, 20, 1), (20, 0, 20, 1)]),
                 obj=0):
        super().__init__(render, vertices, faces, obj)

        self.vertices = vertices
        self.update_position(RESOURCES_OBJECTS[obj][1])
        self.faces = faces

        self.colors = pg.Color(PRIMITIVE_COLOR_R, PRIMITIVE_COLOR_G, PRIMITIVE_COLOR_B)
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]

        self.drawing_vertices = False
        self.label = ''
