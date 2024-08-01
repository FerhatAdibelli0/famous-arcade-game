from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_increase(self):
        self.l_score += 1

    def r_increase(self):
        self.r_score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=("Courier", 80, "normal"))

    def reset(self):
        self.l_score = 0
        self.r_score = 0
