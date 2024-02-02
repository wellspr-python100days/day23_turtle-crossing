from turtle import Turtle
import random

TOP = 270
BOTTOM = -270
SEP = 30
TRACKS = int((TOP - BOTTOM) / SEP)

X_START = 350
X_END = 450

STEP = 10
STEP_INCREMENT = 1

colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'black', 'gray']

class Car(Turtle):
    
    def __init__(self):
        super().__init__(shape='square')
        self.speed('fastest')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.goto(random.randint(-300, X_END), TOP)
        self.color(random.choice(colors))
        self.setheading(180)
        self.step = STEP

    def move(self):
        self.forward(self.step)

    def accelerate(self):
        self.step += STEP_INCREMENT

    def set_step(self, step):
        self.step = step

    def assign_random_position(self):
        self.goto(random.randint(X_START, X_END), self.ycor())
        self.color(random.choice(colors))


class Traffic:

    def __init__(self):
        self.cars = []
        self.create()
    
    def create(self):
        for i in range(TRACKS+1):
            new_car = Car()
            new_car.goto(new_car.xcor(), new_car.ycor() - i * SEP)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.move()

            if car.xcor() < -360:
                self.recycle(car)

    def recycle(self, car: Turtle):
        car.assign_random_position()

    def accelerate(self):
        for car in self.cars:
            car.accelerate()


class Decorator(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.speed('fastest')
        
    def draw(self):
        self.penup()
        self.goto(-300, 282)
        self.pendown()
        self.goto(300, 282)

        self.penup()
        self.goto(-300, -282)
        self.pendown()
        self.goto(300, -282)
