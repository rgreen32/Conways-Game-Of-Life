from dataclasses import dataclass

@dataclass
class Cell:
    position_x: int
    position_y: int
    canvas_id: int
    is_alive: bool = False