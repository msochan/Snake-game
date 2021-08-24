from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"SCORE: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self, food):
        if food.shape() == "turtle":
            self.score += 3
        else:
            self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", False, align="center", font=("Arial", 15, "normal"))

    def print_game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)