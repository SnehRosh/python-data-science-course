from turtle import *
speed = ('slowest')
dis=[50, 50, 50, 50, 50, 60, 60, 25, 60, 150, 50, 30, 50, 90, 76, 200, 80, 100, 90]
ngl=[90, 60, 60, 60, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 240, 300, 310, 200]
for d, a in zip(dis, ngl):
    fd(d)
    if a < 0:
      rt(abs(a))
    else:
      lt(a)

#hideturtle()
mainloop()