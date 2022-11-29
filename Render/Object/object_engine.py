import numpy as np
import pygame as pg
from numba import njit
from Render.Matrix_functions.object_matrix import Object
from settings import SPEED_TRANSLATE_X, SPEED_TRANSLATE_Z, SPEED_TRANSLATE_Y, SPEED_TRANSLATE_OBJECT, \
    VERTICES_COLOR_R, VERTICES_COLOR_B, VERTICES_COLOR_G, FACES_COLOR_R, FACES_COLOR_B, FACES_COLOR_G, \
    FONT_INSCRIPTIONS, MOVING_OBJECT, DRAWING_VERTICALS, THICKNESS_POLYGONS, THICKNESS_VERTICES, DRAWING_AXES, \
    RESOURCES_OBJECTS


class ObjectEngine:
    def __init__(self, render, vertices, faces, obj):
        self.render = render

        self.vertices = np.array([np.array(v) for v in vertices])
        self.update_position(RESOURCES_OBJECTS[obj][1])

        self.faces = np.array([np.array(face) for face in faces], dtype=object)

        Object.translate_object(self, [SPEED_TRANSLATE_X, SPEED_TRANSLATE_Y, SPEED_TRANSLATE_Z])

        self.font = pg.font.SysFont('Arial', FONT_INSCRIPTIONS, bold=True)
        self.color_faces = [(pg.Color(FACES_COLOR_R, FACES_COLOR_G, FACES_COLOR_B), face) for face in self.faces]

        self.movement_flag, self.drawing_vertices, self.drawing_axes = MOVING_OBJECT, DRAWING_VERTICALS, DRAWING_AXES

        self.label = ''

    @staticmethod
    @njit(fastmath=True)
    def concatenate_matrix(obj, width, height):
        return np.any((obj == width) | (obj == height))

    def draw_projection(self):
        self.screen_projection()
        self.movement()

    def movement(self):
        if self.movement_flag:
            Object.rotate_y_object(self, -(pg.time.get_ticks() % SPEED_TRANSLATE_OBJECT))

    def screen_projection(self):
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1, 1)      # нормализация вершин
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.render.projection.screen_matrix
        vertices = vertices[:, :2]

        self.draw_polygons(vertices)
        self.draw_vertices(vertices)

    def draw_vertices(self, vertices):
        if self.drawing_vertices:
            for vertex in vertices:
                if not ObjectEngine.concatenate_matrix(vertex, self.render.middle_width, self.render.middle_height):
                    pg.draw.circle(self.render.screen, pg.Color(VERTICES_COLOR_R,
                                                                VERTICES_COLOR_G,
                                                                VERTICES_COLOR_B), vertex, THICKNESS_VERTICES)

    def draw_polygons(self, vertices):
        for index, color_face in enumerate(self.color_faces):
            color, face = color_face
            polygon = vertices[face]
            if not ObjectEngine.concatenate_matrix(polygon, self.render.window.middle_width,
                                                   self.render.window.middle_height):
                pg.draw.polygon(self.render.window.screen, color, polygon, THICKNESS_POLYGONS)
                if self.label:
                    text = self.font.render(self.label[index], True, pg.Color(VERTICES_COLOR_R,
                                                                              VERTICES_COLOR_G,
                                                                              VERTICES_COLOR_B))
                    self.render.window.screen.blit(text, polygon[-1])

    def update_position(self, position):
        for mass in range(0, np.shape(self.vertices)[0]):
            for i in range(0, 3):
                self.vertices[mass][i] += position[i]
