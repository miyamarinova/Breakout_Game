import turtle
from bricks import Bricks, Brick
from ball import Ball
from paddle import Paddle
import time


global elapsed_time
brick_pts = []


def paddle_hit():
    if ball.distance(paddle) < 50 and ball.ycor() < -170:

        if paddle.xcor() > 0:
            if ball.xcor() > paddle.xcor():
                ball.bounce(bounce_x=True, bounce_y=True)
                return
            else:
                ball.bounce(bounce_x=False,bounce_y=True)
                return
        elif paddle.xcor() < 0:
            if ball.xcor() < paddle.xcor():
                ball.bounce(bounce_x=True,bounce_y=True)
                return
            else:
                ball.bounce(bounce_x=False,bounce_y=True)
                return
        else:
            if ball.xcor() > paddle.xcor():
                ball.bounce(bounce_x=True,bounce_y=True)
                return
            elif ball.xcor() < paddle.xcor():
                ball.bounce(bounce_x=True,bounce_y=True)
                return
            else:
                ball.bounce(bounce_x=False,bounce_y=True)
                return

def wall_hit():
    global game_on
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce(bounce_x=True, bounce_y=False)
        return
    # collision with upper wall
    if ball.ycor() > 230:
        ball.bounce(bounce_x=False, bounce_y=True)
        return
        # collision with bottom wall
    if ball.ycor() < -230:
        game_on = False
        ball.game_over(len(brick_pts))

def brick_hit():

    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(1000,1000)

                brick_pts.append(brick)

                bricks.bricks.remove(brick)
            if len(bricks.bricks) == 0:
                turtle.penup()
                turtle.hideturtle()
                turtle.goto(0, 0)
                turtle.write(f'Time for win: {int(elapsed_time)}')
                # detect collision from left
                if ball.xcor() < brick.left_wall:
                    ball.bounce(bounce_x=True, bounce_y=False)
                # detect collision from right
                elif ball.xcor() > brick.right_wall:
                    ball.bounce(bounce_x=True, bounce_y=False)
                # detect collision from bottom
                elif ball.ycor() < brick.bottom_wall:
                    ball.bounce(bounce_x=False, bounce_y=True)
                # detect collision from top
                elif ball.ycor() > brick.upper_wall:
                    ball.bounce(bounce_x=False, bounce_y=True)

def count_time():
    global elapsed_time
    FONT = ('Arial', 15, 'normal')
    timer.color('white')
    timer.penup()
    timer.hideturtle()
    timer.goto(x=300, y=-240)
    timer.clear()
    elapsed_time = time.time() - start_time
    if int(elapsed_time) <= 60:
        timer.write(f'Time: {int(elapsed_time)}',align='center',font=FONT)
    else:
        timer.write(f'Time: {"%d:02dmn", time.gmtime(int(elapsed_time))}', align='left', font=FONT)


start_time = time.time()
timer = turtle.Turtle()
window = turtle.Screen()
window.tracer(0)
paddle = Paddle()
bricks = Bricks()
ball = Ball()
game_on = True
window.title("Breakout Game")
window.setup(800, 500)
window.bgcolor('black')

while game_on:
    count_time()
    window.update()
    time.sleep(0.08)
    window.listen()
    ball.move()
    window.onkeypress(paddle.move_left, "Left")
    window.onkeypress(paddle.move_right, "Right")
    brick_hit()
    wall_hit()
    paddle_hit()

window.exitonclick()

