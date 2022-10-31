import numpy as np
import pygame as pg

from Render.Object.object_engine import ObjectEngine
from settings import SLEEVE_AXES_LENGTH, POSITION_AXIS_Z, POSITION_AXIS_Y, POSITION_AXIS_X, RESOURCES_OBJECTS


class Axes(ObjectEngine):
    def __init__(self, render, faces=np.array([(0, 1), (0, 2), (0, 3)]), vertices=np.array([
                                            (POSITION_AXIS_X, POSITION_AXIS_Y, POSITION_AXIS_Z, 1),
                                            (SLEEVE_AXES_LENGTH + POSITION_AXIS_X, POSITION_AXIS_Y, POSITION_AXIS_Z, 1),
                                            (POSITION_AXIS_X, SLEEVE_AXES_LENGTH + POSITION_AXIS_Y, POSITION_AXIS_Z, 1),
                                            (POSITION_AXIS_X, POSITION_AXIS_Y, SLEEVE_AXES_LENGTH, 1)]), obj=0):
        super().__init__(render, vertices, faces, obj)

        self.vertices = vertices
        self.update_position(RESOURCES_OBJECTS[obj][1])
        self.faces = faces

        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]

        self.drawing_vertices = False
        self.label = 'XYZ'
