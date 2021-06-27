from dataclasses import dataclass

@dataclass
class Cell:
    position_x: int
    position_y: int
    rect_x: int
    rect_y: int
    canvas_id: int
    was_alive: bool = False
    is_alive: bool = None