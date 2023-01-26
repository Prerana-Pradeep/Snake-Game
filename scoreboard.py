from turtle import Turtle

FONT_S = 15
FONT = 'Arial'
FONT_T = "normal"
ALIGN = 'center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.get_highscore())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        self.goto(0, 275)
        self.write(f"Score = {self.score}, High Score = {self.high_score}", align=ALIGN, font=(FONT, FONT_S, FONT_T))

    def ate_food(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.update_score()
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALIGN, font=(FONT, FONT_S, FONT_T))
        self.clear()
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.new_highscore()
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.update_score()

    def get_highscore(self):
        with open("highscore.txt") as file:
            return file.read()

    def new_highscore(self):
        with open("highscore.txt", mode='w') as file:
            file.write(str(self.score))
