from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.__score = 0
        self.__high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.load_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'SCORE: {self.__score}  HIGH SCORE: {self.__high_score}',
                   False, align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.__score > self.__high_score:
            self.__high_score = self.__score
            self.save_score()
        self.__score = 0
        self.update_scoreboard()

    def update_score(self, food):
        if food.shape() == "turtle":
            self.__score += 3
        else:
            self.__score += 1
        self.update_scoreboard()

    def load_score(self):
        with open("data.txt") as file:
            contents = int(file.read())
            self.__high_score = contents
    
    def save_score(self):
        with open("data.txt", mode='w') as file:
            file.write(str(self.__high_score))