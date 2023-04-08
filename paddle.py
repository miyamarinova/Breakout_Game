from turtle import *

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(1, 4)
        self.hideturtle()
        self.goto(x=0, y=-200)
        self.pendown()
        self.showturtle()


    def move_left(self):
        self.penup()
        self.setx(self.xcor() - MOVE_DISTANCE)


    def move_right(self):
        self.penup()
        self.setx(self.xcor() + MOVE_DISTANCE)


    def reset(self):
        self.setposition(0, -280)

