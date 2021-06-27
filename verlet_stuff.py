import tkinter
import time
from datetime import datetime

class Simulation():
    def __init__(self):
        self.window = self.create_window()
        self.canvas = self.create_canvas()
        self.pixels_to_meters_ratio = self.window_height/100

    def create_window(self):
        window = tkinter.Tk()
        self.window_width = 600
        self.window_height = 600
        window.geometry(f'{self.window_width}x{self.window_height}')
        window.title("Tkinter Animation Demo")
        return window

    def create_canvas(self):
        canvas = tkinter.Canvas(self.window)
        canvas.configure(bg="black")
        canvas.pack(fill="both", expand=True)
        return canvas

    def start_animation_loop(self):
        position_x = 0
        position_y = 0
        old_position_y = position_y
        old_position_x = position_x - 1
        position_x_pixels = self.meters_to_pixels_position_x(position_x)
        position_y_pixels = self.meters_to_pixels_position_y(position_y)
        ball_radius = 3.33
        ball = self.canvas.create_oval(
            self.meters_to_pixels_position_x(-ball_radius),
            self.meters_to_pixels_position_y(ball_radius), 
            self.meters_to_pixels_position_x(ball_radius), 
            self.meters_to_pixels_position_y(-ball_radius), 
            fill="blue",
            state=tkinter.HIDDEN
            )
        dt = 0.01
        self.canvas.moveto(ball, x=self.meters_to_pixels_position_x(position_x), y=self.meters_to_pixels_position_y(position_y))
        self.canvas.itemconfig(ball, state=tkinter.NORMAL) #make visible


        start = datetime.now()
        while True:
            dt = (start - datetime.now()).total_seconds()
            start = datetime.now()
            old_position_x, position_x = self.apply_verlet_integration(old_position_x, position_x, dt, 0)
            old_position_y, position_y = self.apply_verlet_integration(old_position_y, position_y, dt, 0)
            self.canvas.moveto(ball, x=self.meters_to_pixels_position_x(position_x), y=self.meters_to_pixels_position_y(position_y))
            
            if position_y < -43:
                vy = position_y - old_position_y
                position_y = -43
                old_position_y = -43 + (vy * 1.0)
            elif position_y > 50:
                vy = position_y - old_position_y
                position_y = 50
                old_position_y = 50 + (vy * 1.0)

            if position_x > 43:
                vx = position_x - old_position_x
                position_x = 43
                old_position_x = 43 + (vx * 1.0)
            elif position_x < -50:
                vx = position_x - old_position_x
                position_x = -50
                old_position_x = -50 + (vx * 1.0)

            
            self.window.update()


    def apply_verlet_integration(self, old_position, position, dt, acceleration):
        new_position = position * 2 - old_position + (acceleration * dt * dt)
        old_position, position = position, new_position
        return old_position, position


    def meters_to_pixels_position_x(self, position_x):
        position_x_in_pixels = None
        if position_x > 0:
            position_x_in_pixels = (self.window_width/2.0) + (self.pixels_to_meters_ratio * position_x)
        elif position_x < 0:
            position_x_in_pixels = (self.window_width/2.0) + (self.pixels_to_meters_ratio * position_x)
        else:
            position_x_in_pixels = (self.window_width/2.0)
        
        return position_x_in_pixels

    def meters_to_pixels_position_y(self, position_y):
        position_y_in_pixels = None
        if position_y > 0:
            position_y_in_pixels = (self.window_height/2.0) - (self.pixels_to_meters_ratio * position_y)
        elif position_y < 0.0:
            position_y_in_pixels = (self.window_height/2.0) - (self.pixels_to_meters_ratio * position_y)
        else:
            position_y_in_pixels = (self.window_height/2.0)
        
        return position_y_in_pixels


simulation = Simulation()
# time.sleep(3)
simulation.start_animation_loop() 

