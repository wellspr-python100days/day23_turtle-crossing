from turtle import Turtle

class Info(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.speed('fastest')

    def start(self):
        self.write("Press 'space' key to start game.", align='center', font=('Arial', 18, 'normal'))