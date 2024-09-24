import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(-250, 250)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Calibri", 18, "normal"))

    def level_up(self):
        self.score += 1
        self.update_score()
