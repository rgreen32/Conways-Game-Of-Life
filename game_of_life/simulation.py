from tkinter import Tk, Canvas
from game_of_life.grid import Grid
import time



class Simulation():

    def __init__(self, window_height: int = 600, window_width: int = 600):
        self.window_height = window_height
        self.window_width = window_width
        self.window: Tk = self._create_window(window_height, window_width)
        self.window.update() #open window

        self.canvas: Canvas = self._create_canvas()
        self.grid = Grid(self.window, self.canvas)

        print("made it here..")
        
        
    def start(self):
        self.grid.start_sim_loop()

    def _create_window(self, width, height) -> Tk:
        window = Tk()
        window.geometry(f'{self.window_width}x{self.window_height}')
        window.title("Tkinter Animation Demo")
        return window

    def _create_canvas(self) -> Canvas:
        canvas = Canvas(self.window)
        canvas.configure(bg="black")
        canvas.pack(fill="both", expand=True)
        return canvas

