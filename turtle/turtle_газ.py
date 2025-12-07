from random import randint
import turtle


number_of_turtles = 10
steps_of_time_number = 100000000

turtle.tracer(False)

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.shape("circle")
    unit.setheading(randint(0, 360))
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(2)
        if unit.xcor() > 200:
            unit.setheading(180-unit.heading())
        if unit.xcor() < -200:
            unit.setheading(180-unit.heading())
        if unit.ycor() > 200:
            unit.setheading(-unit.heading())
        if unit.ycor() < -200:
            unit.setheading(-unit.heading())
        for unit1 in pool:
            if unit !=unit1 and (unit.pos()[0]-unit1.pos()[0]):
                unit.setheading(randint(0, 360))
        turtle.update()
    turtle.update()
turtle.update()