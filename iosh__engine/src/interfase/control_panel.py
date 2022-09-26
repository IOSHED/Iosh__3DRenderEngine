import tkinter
import tkinter.ttk
from src.settings import *


class WindowControlPanel:
    def __init__(self):
        self.window = tkinter.Tk()

        self.window.geometry(f'{HEIGHT_WINDOW_INTERFACE}x{WIDTH_WINDOW_INTERFACE}')
        self.window.resizable(width=False, height=True)

        self.window.title("IoshEngine - control panel")
        self.window.config(bg="#%02x%02x%02x" % (BG_COLOR_INTERFACE_R, BG_COLOR_INTERFACE_G, BG_COLOR_INTERFACE_B))

        self.frames = []
        self.setting = self.recording_setting()

        self.string_settings()

        self.window.mainloop()

    def string_settings(self):
        for i in range(0, len(self.setting)):
            tkinter.Label(self.window, fg='#FDF5E6', text=self.setting[i][0], width=25, font=("Arial bolt", 10),
                          background="#%02x%02x%02x" % (BG_COLOR_INTERFACE_R,
                                                        BG_COLOR_INTERFACE_G,
                                                        BG_COLOR_INTERFACE_B)).grid(column=0, row=i)
            if not self.setting[i][1] == 'zero':
                entry = tkinter.Entry(self.window, bg='#24262E', fg='#FDF5E6')
                self.frames.append(entry)

                entry.insert(-1, self.setting[i][1])
                entry.grid(column=1, row=i)

    def writing_settings(self):
        for i in range(0, len(self.frames)):
            ...

    @staticmethod
    def recording_setting():
        setting = []
        with open("../src/settings.py") as s:
            for line in s:
                if not line.startswith("\n"):
                    if line.startswith("RESOURCES_OBJECTS"):
                        break
                    setting.append([str(line.split(" ")[0]), str(line.split(" ")[2]).replace("\n", "")])
                else:
                    setting.append(["", "zero"])
        return setting
