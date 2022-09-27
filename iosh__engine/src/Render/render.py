import math

from Render.Object.Objects.axes import Axes
from src.Render.Camera.camera import Camera
from src.Render.Matrix_functions.projection_matrix import Projection
from src.Render.Object.objectengine import *
from src.Window.window import Window
from src.settings import POSITION_CAMERA_X, POSITION_CAMERA_Y, POSITION_CAMERA_Z, BG_COLOR_R, BG_COLOR_G, BG_COLOR_B, \
    DRAWING_AXES, RESOURCES_OBJECTS, DRAWING_AXES_OBJECT


class Render:
    def __init__(self):
        pg.init()
        self.resources_objects = RESOURCES_OBJECTS
        self.blt_axes = DRAWING_AXES

        self.projection, self.camera = None, None

        self.objects = []

        self.window = Window()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [POSITION_CAMERA_X, POSITION_CAMERA_Y, POSITION_CAMERA_Z])
        self.projection = Projection(self)

        for _obj in range(0, len(self.resources_objects)):
            objecting = self.get_object_from_file(self.resources_objects[_obj][0], _obj)
            ObjectEngine.rotate_y_object(objecting, -math.pi / 4)

            if DRAWING_AXES_OBJECT:
                self.objects.append(Axes(self, obj=_obj))
            self.objects.append(objecting)

    def get_object_from_file(self, filename, obj):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split(' ')[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return ObjectEngine(self, vertex, faces, obj)

    def draw_object(self):
        self.window.screen.fill(pg.Color(BG_COLOR_R, BG_COLOR_G, BG_COLOR_B))

        if self.blt_axes:
            Axes(self).draw_projection()

        for obj in range(0, len(self.objects)):
            self.objects[obj].draw_projection()
