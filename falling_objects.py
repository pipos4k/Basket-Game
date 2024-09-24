import random
import turtle

STARTING_MOVE_DISTANCE = 2
LEVELING_MOVEMENT = 0.4


class Object:
    def __init__(self):
        self.all_objects = []
        self.object_speed = STARTING_MOVE_DISTANCE

    def add_object(self):
        fall_object = turtle.Turtle("turtle")
        fall_object.setheading(270)
        fall_object.penup()
        fall_object.color("green")
        fall_object.setx(random.randint(-220, 220))
        fall_object.sety(290)
        self.all_objects.append(fall_object)

    def move_object(self):
        for i in self.all_objects:
            i.forward(self.object_speed)

    def remove_object(self, x):
        self.all_objects.remove(x)

    def level_up(self):
        self.object_speed += LEVELING_MOVEMENT
