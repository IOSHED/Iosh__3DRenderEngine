import numpy as np
import pygame as pg
from Render.Object.object_engine import ObjectEngine
from settings import RESOURCES_OBJECTS, PRIMITIVE_COLOR_R, PRIMITIVE_COLOR_B, PRIMITIVE_COLOR_G


class Ball(ObjectEngine):
    def __init__(self, render, faces=np.array([]),
                 vertices=np.array([]), obj=0):
        super().__init__(render, vertices, faces, obj)

        self.vertices = vertices
        self.update_position(RESOURCES_OBJECTS[obj][1])
        self.faces = faces

        self.color_faces = [(pg.Color(PRIMITIVE_COLOR_R, PRIMITIVE_COLOR_G, PRIMITIVE_COLOR_B), face) for face in
                            self.faces]

        self.drawing_vertices = False
        self.label = ''
