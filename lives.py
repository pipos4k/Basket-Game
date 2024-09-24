import turtle


class Lives(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 4
        self.goto(180, 250)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.write(f"Lives: {self.lives}", font=("Calibri", 18, "normal"))

    def lose_life(self):
        self.lives -= 1
        self.update_lives()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center",
                   font=("Calibri", 40, "bold"))
