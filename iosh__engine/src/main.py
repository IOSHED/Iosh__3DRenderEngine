import threading

from src.Render.render import Render
from src.Window.window import Window
from src.Interfase.control_panel import WindowControlPanel

if __name__ == '__main__':
    # app = Render()
    control_panel = threading.Thread(target=WindowControlPanel).start()
    # Window().window(app)
