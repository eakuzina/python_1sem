from turtle import *

speed(10)
back(500)
forward(1000)
back(900)
shape('circle')

s=h=450
for j in range(13):
    s=h=int(2*s/3)
    c=xcor()
    for i in range(s+1):
        goto(i+c,4*h*(i/s-(i/s)**2))

mainloop()