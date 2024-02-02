from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.goto(0, 310)
        self.level = 1
        self.print()

    def print(self):
        self.write(f"Level {self.level}", align='center', font=("Arial", 16, "normal"))

    def update(self):
        self.clear()
        self.print()

    def up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=("Arial", 25, "bold"))


