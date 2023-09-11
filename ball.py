from turtle import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_paddle(self):
        self.x_move *= -1
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def game_over(self, side, streak):
        print(f"Game over!!!!!!!!! {side} wins")
        self.color("white")
        self.goto(0, 0)
        self.write(arg=f"Game over!!!!!!!!! {side} wins \n Score: {streak}", align="center",
                   font=("Arial", 18, "normal"), move=False)
