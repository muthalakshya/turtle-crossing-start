from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.level_up()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",font=FONT,align="Center")

    def level_up(self):
        self.clear()
        self.goto(-280,260)
        self.write(f"Level : {self.level}", align="left", font=FONT)
        self.level += 1

