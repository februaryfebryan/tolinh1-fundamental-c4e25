from turtle import *

d = 0.5
speed(0)
for i in range(20):
    forward(d)
    left(90)
    d *=2 # d +=1, d -= 5, d *= 2, d /=2


mainloop()