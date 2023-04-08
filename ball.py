from turtle import *
from tkinter import *

class Ball(Turtle):
    X_POS = 0
    Y_POS = -180
    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.goto(self.X_POS, self.Y_POS)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # bounce from paddle
    def bounce(self, bounce_x, bounce_y):
        if bounce_y:
            self.y_move *= -1

        if bounce_x:
            self.x_move *= -1
    def first_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def game_over(self,pts):
        self.penup()
        self.hideturtle()
        self.goto(-20, -50)
        self.color('red')
        self.write("Game Over!"
                   f"Points: {pts}", font=('Ariel', 70, "bold"), align='center')









