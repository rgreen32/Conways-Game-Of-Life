from tkinter import Tk, Canvas
from game_of_life.grid import Grid
import time


class GameBoard():

    def __init__(self, window_height: int = 600, window_width: int = 600):
        self.window_height = window_height
        self.window_width = window_width
        self.window: Tk = self._create_window(window_height, window_width)
        self.window.update() #open window

        self.canvas: Canvas = self._create_canvas()
        self.grid = Grid(self.window, self.canvas)
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

    def _meters_to_pixels_position_x(self, position_x):
        position_x_in_pixels = None
        if position_x > 0:
            position_x_in_pixels = (self.window_width/2.0) + (self.pixel_ratio * position_x)
        elif position_x < 0:
            position_x_in_pixels = (self.window_width/2.0) + (self.pixel_ratio * position_x)
        else:
            position_x_in_pixels = (self.window_width/2.0)
        
        return position_x_in_pixels

    def _meters_to_pixels_position_y(self, position_y):
        position_y_in_pixels = None
        if position_y > 0:
            position_y_in_pixels = (self.window_height/2.0) - (self.pixel_ratio * position_y)
        elif position_y < 0.0:
            position_y_in_pixels = (self.window_height/2.0) - (self.pixel_ratio * position_y)
        else:
            position_y_in_pixels = (self.window_height/2.0)
        
        return position_y_in_pixels

game_board = GameBoard()
# game_board.canvas.create_rectangle(0, 0, 30, 30, fill="blue")
# game_board.window.update()
time.sleep(2)

