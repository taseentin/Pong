import time
from turtle import Screen
from paddle import Paddle
from ball import Ball


# from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_paddle()
        l_paddle.score += 1
        ball.x_move+=2
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_paddle()
    if ball.xcor() < -390:
        ball.game_over(side="Right side", streak=l_paddle.score)
        game_is_on = False
    if ball.xcor() > 390:
        ball.game_over(side="Left side", streak=l_paddle.score)
        game_is_on = False

    # Keyboard bindings
screen.exitonclick()

# Main game loop
