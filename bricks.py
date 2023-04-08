from turtle import *
import random
from turtle import Turtle


COLOR_LIST = ['#FA9884', '#FEFF86','#BFDB38',
              'light cyan', 'light sky blue',
              'violet','sandy brown', 'purple',
              'medium sea green']

weights = [1, 2, 3, 4]

class Brick(Turtle):

        def __init__(self, x_cor, y_cor):
            super().__init__()
            self.penup()
            self.shape('square')
            self.shapesize(stretch_wid=1.5, stretch_len=3)
            self.color(random.choice(COLOR_LIST))
            self.goto(x=x_cor, y=y_cor)
            self.quantity = random.choice(weights)

            # Defining borders of the brick
            self.left_wall = self.xcor() - 30
            self.right_wall = self.xcor() + 30
            self.upper_wall = self.ycor() + 15
            self.bottom_wall = self.ycor() - 15

class Bricks:
        def __init__(self):
            self.y_start = 0
            self.y_end = 240
            self.bricks = []
            self.create_all_lanes()

        def create_lane(self, y_cor):
            for i in range(-500, 500, 63):
                brick = Brick(i, y_cor)
                self.bricks.append(brick)

        def create_all_lanes(self):
            for i in range(self.y_start, self.y_end, 32):
                self.create_lane(i)





