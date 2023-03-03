from turtle import  Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.restart_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart_position(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

