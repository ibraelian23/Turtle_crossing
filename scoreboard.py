from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-220, y=250)
        self.write(arg=f"Level: {self.level}", align="center",font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center",font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.clear()
        self.write(arg=f"Game Over", align="center", font=FONT)

