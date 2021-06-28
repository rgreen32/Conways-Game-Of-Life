from game_of_life.models import Cell
from game_of_life.rules_engine import RulesEngine
from typing import List, Tuple
from tkinter import Canvas, Tk
from extension.target.release import grid

class Grid:
    NUMBER_OF_CELLS_Y_AXIS = 30
    CELL_SIDE_LENGTH = 1
    def __init__(self, window: Tk, canvas: Canvas):
        self.window = window
        self.canvas = canvas
        self.window_height = window.winfo_height()
        self.window_width = window.winfo_width()
        self.pixel_ratio: int = self.window_height/self.NUMBER_OF_CELLS_Y_AXIS
        self.cell_side_length = self.CELL_SIDE_LENGTH * self.pixel_ratio
        number_of_cells = self.window_width 
        self.cells: List[List[Tuple]] = self._create_cells()

        rust_grid = grid.Grid(self.grid.cells)
        # self.rules_engine = RulesEngine(self.cells)

        # self.cells[4][3].is_alive = True
        # self.cells[4][4].is_alive = True
        # self.cells[4][5].is_alive = True ## Glider
        # self.cells[3][5].is_alive = True
        # self.cells[2][4].is_alive = True
        # self._render_cells()


    def start_sim_loop(self): 
        while True: # the operations made by these methods need to be optimized
            self._reset_cells() # sets every cell's was_alive property to its is_alive property 
            self._sim_step() # sets every cell's is_alive property based on its neighborings cells' was_alive properties
            self._render_cells() # updates window

    
    def _sim_step(self): # determines is_alive from was_alive
        for cell_column in self.cells:
            for cell in cell_column:
                    cell_is_alive = self.rules_engine.cell_is_alive(cell)
                    cell.is_alive = cell_is_alive

                        
    def _create_cells(self) -> Cell:
        cell_rows = []
        for row_index, rect_x in enumerate(range(0, self.window_width, int(self.cell_side_length))):
            cell_columns = []
            for column_index, rect_y in enumerate(range(0, self.window_height, int(self.cell_side_length))):               
                cell_canvas_id = self.canvas.create_rectangle(rect_x, rect_y, (rect_x + self.cell_side_length), (rect_y + self.cell_side_length), outline='green')
                cell = (row_index, column_index, rect_x, rect_y, cell_canvas_id, False, False)
                cell_columns.append(cell)
            cell_rows.append(cell_columns)
        return cell_rows

    def _render_cells(self):
        for cell_column in self.cells:
            for cell in cell_column:
                if cell.is_alive:
                    self.canvas.itemconfigure(cell.canvas_id, fill="green")
                else:
                    self.canvas.itemconfigure(cell.canvas_id, fill="black")
        self.window.update()
    
    def _reset_cells(self):
        for cell_column in self.cells:
            for cell in cell_column:
                cell.was_alive = cell.is_alive
                cell.is_alive = None

