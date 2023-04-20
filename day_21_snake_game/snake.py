from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def move_snake(self, d=20):
        for s_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[s_num - 1].xcor()
            new_y = self.snake_body[s_num - 1].ycor()
            self.snake_body[s_num].goto(new_x, new_y)

        self.snake_body[0].forward(d)

    def create_snake(self):
        for s in range(3):
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(x=0 - 20 * s, y=0)
            self.snake_body.append(new_square)

    def add_seg(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.snake_body.append(new_square)

    def extend(self):
        self.add_seg(self.snake_body[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move_snake(1)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move_snake(1)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move_snake(1)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move_snake(1)

    def reset_snake(self):
        for s in self.snake_body:
            s.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

