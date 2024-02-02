from turtle import Turtle

START = -300
FINISH = 290

class CrossingTurtle(Turtle):

    def __init__(self):
        super().__init__(shape='turtle')
        self.penup()
        self.goto(0, START)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def has_crossed(self):
        return self.ycor() > FINISH
    
    def restart(self):
        self.goto(0, START)