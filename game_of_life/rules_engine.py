from typing import List
from game_of_life.models import Cell

class RulesEngine():
    
    def __init__(self, cell_map: List[List[Cell]]):
        self.cell_map = cell_map

    def cell_is_alive(self, cell: Cell) -> bool:
        live_neighbors = self._get_live_neighbors(cell)

        if cell.was_alive and (live_neighbors == 2 or live_neighbors == 3):
                return True
        elif not cell.was_alive and live_neighbors == 3:
            return True
        else:
            return False


    def _get_live_neighbors(self, cell: Cell) -> int:
        live_neighbors = 0

        cell_map_x_length = len(self.cell_map)-1
        cell_map_y_length = len(self.cell_map[0])-1
        for position_x in range(cell.position_x-1, cell.position_x+2):
            if position_x < 0 or position_x > cell_map_x_length: continue

            for position_y in range(cell.position_y-1, cell.position_y+2):
                if position_y < 0 or position_y > cell_map_y_length: continue
                elif position_x == cell.position_x and position_y == cell.position_y: continue

                neighboring_cell = self.cell_map[position_x][position_y]
                if neighboring_cell.was_alive:
                    live_neighbors += 1

        return live_neighbors

