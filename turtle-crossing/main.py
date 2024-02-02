from turtle import Screen
from traffic import Traffic, Decorator
from crossing_turtle import CrossingTurtle
from scoreboard import ScoreBoard

import time

s = Screen()
s.setup(width=700, height=700, startx=0, starty=0)
s.title('Turtle Crossing')
s.screensize(canvwidth=600, canvheight=600)
s.tracer(0)
s.listen()

def play_game():
    decorator = Decorator()
    traffic = Traffic()
    turtle = CrossingTurtle()
    level = ScoreBoard()

    s.onkey(turtle.move, "Up")

    decorator.draw()

    play = True

    while play:
        s.update()
        time.sleep(0.1)

        traffic.move()

        # Collision detection
        for car in traffic.cars:
            x_condition = abs(car.xcor()) < 20

            diff = turtle.ycor() - car.ycor()
            y_condition = (diff>0 and diff<20) or (diff<0 and diff>-25)
 
            if y_condition and x_condition:
                play = False
                level.game_over()

        # level clearing condition
        if turtle.has_crossed():
            time.sleep(1)
            turtle.restart()
            level.up()
            traffic.accelerate()

play_game()
 
s.exitonclick()
s.mainloop()
