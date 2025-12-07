import turtle

L=turtle.left
R=turtle.right
U=turtle.penup
D=turtle.pendown
F=turtle.forward
SIZE=50
DIAG = SIZE * 2**0.5
a0=[F, SIZE, R, 90, F, 2*SIZE, R, 90, F, SIZE, R, 90, F, 2*SIZE]
a1=[U, R, 90, F, SIZE, L, 135, D, F, DIAG, R, 135, F, 2*SIZE]
a2=[F, SIZE, R, 90, F, SIZE, R, 45, F, DIAG, L, 135, F, SIZE]
a3=[F, SIZE, R, 135, F, DIAG, L, 135, F, SIZE, R, 135, F, DIAG]
a4=[R, 90, F, SIZE, L, 90, F, SIZE, L, 90, F, SIZE, L, 180, F, 2*SIZE]
a5=[F, SIZE, L, 180, F, SIZE, L, 90, F, SIZE, L, 90, F, SIZE, R, 90, F, SIZE, R, 90, F, SIZE]
a6=[U, F, SIZE, D, R, 135, F, DIAG, L, 45, F, SIZE, L, 90, F, SIZE, L, 90, F, SIZE, L, 90, F, SIZE]
a7=[F, SIZE, R, 135, F, DIAG, L, 45, F, SIZE]
a8=[F, SIZE, R, 90, F, SIZE, R, 90, F, SIZE, R, 90, F, SIZE, R, 180, F, 2*SIZE, L, 90, F, SIZE, L, 90, F, SIZE]
a9=[F, SIZE, R, 90, F, SIZE, R, 45, F, DIAG, R, 180, F, DIAG, L, 135, F, SIZE, R, 90, F, SIZE]

def do(seq):
    i = 0
    while i < len(seq):
        if seq[i] == U or seq[i] == D:
            seq[i]()
            i += 1
        else:
            seq[i](seq[i+1])
            i += 2 

x = -200    
for i in '1234567890':
    turtle.penup()
    turtle.goto(x, 0)
    turtle.setheading(0)
    turtle.pendown()
    if i == '0': do(a0)
    if i == '1': do(a1)
    if i == '2': do(a2)
    if i == '3': do(a3)
    if i == '4': do(a4)
    if i == '5': do(a5)
    if i == '6': do(a6)
    if i == '7': do(a7)
    if i == '8': do(a8)
    if i == '9': do(a9)
    x += 60
