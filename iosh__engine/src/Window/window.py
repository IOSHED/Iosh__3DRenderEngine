import pygame as pg
from src.settings import HEIGHT_WINDOW, WIDTH_WINDOW, FPS


class Window:
    def __init__(self):
        self.res = self.width, self.height = WIDTH_WINDOW, HEIGHT_WINDOW
        self.middle_width, self.middle_height = self.width // 2, self.height // 2

        self.screen = pg.display.set_mode(self.res, pg.RESIZABLE)
        self.clock = pg.time.Clock()

        self.fps = FPS

    def window(self, render):
        while True:
            render.draw_object(), render.camera.control_camera()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]

            str_fps = pg.font.SysFont('Arial', 16, bold=True).render(str(round(self.clock.get_fps())), True,
                                                                     pg.Color(self.fps_tracer()))
            render.window.screen.blit(str_fps, (pg.display.get_surface().get_size()[0] - 17, 5))

            pg.display.set_caption('IoshEngine - scene')
            pg.display.flip()

            self.clock.tick(self.fps)

    def fps_tracer(self):
        fps = self.clock.get_fps()
        if fps > 120:
            return 173, 255, 47

        elif fps > 60:
            return 50, 205, 50

        elif fps > 45:
            return 152, 251, 152

        elif fps > 30:
            return 255, 215, 0

        elif fps > 15:
            return 205, 92, 92

        else:
            return 139, 0, 0
