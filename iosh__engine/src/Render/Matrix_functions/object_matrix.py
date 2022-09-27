from src.Render.Matrix_functions.matrix import MatrixFunctions


class Object:
    @staticmethod
    def translate_object(self, pos):
        self.vertices = self.vertices @ MatrixFunctions.translate(pos)

    @staticmethod
    def scale_object(self, scale_to):
        self.vertices = self.vertices @ MatrixFunctions.scale(scale_to)

    @staticmethod
    def rotate_x_object(self, angle):
        self.vertices = self.vertices @ MatrixFunctions.rotate_x(angle)

    @staticmethod
    def rotate_y_object(self, angle):
        self.vertices = self.vertices @ MatrixFunctions.rotate_y(angle)

    @staticmethod
    def rotate_z_object(self, angle):
        self.vertices = self.vertices @ MatrixFunctions.rotate_z(angle)
