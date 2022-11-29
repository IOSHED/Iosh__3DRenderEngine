import pygame as pg

from settings import SPEED_MOVING_CAMERA, SPEED_ROTATION_CAMERA, MAUS_CONTROL, MAUS_NOT, AREA_OF_TRANQUILITY_CAMERA


class ControlCamera:
    def __init__(self, camera):
        self.camera = camera

        self.moving_speed = SPEED_MOVING_CAMERA
        self.rotation_speed = SPEED_ROTATION_CAMERA

        self.maus_control = MAUS_CONTROL
        self.maus_not = MAUS_NOT

    def control_camera(self):
        key = pg.key.get_pressed()

        if key[pg.K_a]:
            self.camera.position -= self.camera.right * self.moving_speed
        elif key[pg.K_d]:
            self.camera.position += self.camera.right * self.moving_speed
        elif key[pg.K_w]:
            self.camera.position += self.camera.forward * self.moving_speed
        elif key[pg.K_s]:
            self.camera.position -= self.camera.forward * self.moving_speed
        elif key[pg.K_q]:
            self.camera.position += self.camera.up * self.moving_speed
        elif key[pg.K_e]:
            self.camera.position -= self.camera.up * self.moving_speed

        if not self.maus_control:
            if key[pg.K_LEFT]:
                self.camera.camera_yaw(-self.rotation_speed)
            elif key[pg.K_RIGHT]:
                self.camera.camera_yaw(self.rotation_speed)
            elif key[pg.K_UP]:
                self.camera.camera_pitch(-self.rotation_speed)
            elif key[pg.K_DOWN]:
                self.camera.camera_pitch(self.rotation_speed)
        else:
            if self.maus_not:
                pg.mouse.set_visible(False)

            position = pg.mouse.get_pos()

            if position[1] < self.camera.render.window.middle_height - AREA_OF_TRANQUILITY_CAMERA:
                self.camera.camera_pitch(-self.rotation_speed)

            elif position[0] > self.camera.render.window.middle_width + AREA_OF_TRANQUILITY_CAMERA:
                self.camera.camera_yaw(self.rotation_speed)

            elif position[0] < self.camera.render.window.middle_width - AREA_OF_TRANQUILITY_CAMERA:
                self.camera.camera_yaw(-self.rotation_speed)

            elif position[1] > self.camera.render.window.middle_height + AREA_OF_TRANQUILITY_CAMERA:
                self.camera.camera_pitch(self.rotation_speed)
