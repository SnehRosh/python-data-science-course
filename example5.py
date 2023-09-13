from turtle import *
speed=('slowest')
data=[23, 25, 27, 29 , 31, 33, 35, 37, 39, 41, 43]
for val in data:
    fd(val)
    lt(360/5)

hideturtle()
mainloop()