from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Black")
        self.goto(-240, 260)
        self.level = 0
        self.write(f"Level: {self.level}", align="center", font=("Verdana", 15, "normal"))

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("Verdana", 15, "normal"))

    def lost(self):
        self.home()
        self.write("You Lost", align="center", font=("Algerian", 30, "normal"))
