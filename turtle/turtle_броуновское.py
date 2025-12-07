from turtle import *
from random import randint

shape('turtle')
color("red")
width(2)
speed(10)

for i in range(100):
    left(randint(0,359))
    forward(randint(1,50))

mainloop()