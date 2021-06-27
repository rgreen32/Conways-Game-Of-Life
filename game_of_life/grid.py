from game_of_life.models import Cell
from typing import List
from tkinter import Canvas, Tk

class Grid:
    NUMBER_OF_CELLS_Y_AXIS = 10
    CELL_SIDE_LENGTH = 1
    def __init__(self, window: Tk, canvas: Canvas):
        self.window = window
        self.canvas = canvas
        self.window_height = window.winfo_height()
        self.window_width = window.winfo_width()
        self.pixel_ratio: int = self.window_height/self.NUMBER_OF_CELLS_Y_AXIS
        self.cell_side_length = self.CELL_SIDE_LENGTH * self.pixel_ratio
        number_of_cells = self.window_width 
        self.cells: List[List[Cell]] = self._create_cells()


    def _create_cells(self) -> Cell:
        cell_rows = []
        for position_x in range(0, self.window_width, int(self.cell_side_length)):
            cell_columns = []
            for position_y in range(0, self.window_height, int(self.cell_side_length)):               
                cell_canvas_id = self.canvas.create_rectangle(position_x, position_y, (position_x + self.cell_side_length), (position_y + self.cell_side_length), outline='green')
                cell = Cell(position_x, position_y, cell_canvas_id)
                cell_columns.append(cell)
            cell_rows.append(cell_columns)
        return cell_rows

    def start_sim_loop(self):
        self.window.update()
        self.cells[3][5].is_alive = True
        while True:
            for cell_column in self.cells:
                for cell in cell_column:
                        if cell.is_alive:
                            self.canvas.itemconfigure(cell.canvas_id, fill="green")
                        else:
                            self.canvas.itemconfigure(cell.canvas_id, fill=None)
            self.window.update()
            break
           