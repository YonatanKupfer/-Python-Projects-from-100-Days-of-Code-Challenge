from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        if self.ycor() > 0:
            self.y_move = -10
        else:
            self.y_move = 10

    def hit_pad(self):
        self.move_speed *= 0.9
        if self.xcor() > 0:
            self.x_move = -10
        else:
            self.x_move = 10

    def reset_pos(self):
        self.hit_pad()
        self.goto(0, 0)
        self.move_speed = 0.1







