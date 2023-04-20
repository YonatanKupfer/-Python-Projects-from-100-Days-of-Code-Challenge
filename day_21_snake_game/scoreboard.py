from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        try:
            with open("data.txt") as hs:
                saved = hs.read()
        except FileNotFoundError:
            with open("data.txt", mode="w") as hs:
                hs.write("0")
            saved = 0
        self.high_score = int(saved)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center",
                   font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as hs:
                hs.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_score()

