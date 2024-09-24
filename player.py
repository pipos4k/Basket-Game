import turtle
import time

STARTING_MOVEMENT = 25


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        time.sleep(0.01)
        self.shape("square")
        self.shapesize(0.4, 3.9, 32)
        self.color("orange")
        self.penup()
        self.goto(x=0, y=-270)

    def move_right(self):
        self.forward(STARTING_MOVEMENT)

    def move_left(self):
        self.backward(STARTING_MOVEMENT)
