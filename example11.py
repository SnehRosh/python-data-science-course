from turtle import *

for i in range(6):
    fd(150)
    rt(60)
else:
   # home() (for returing to initial position)
   penup()
   goto(75, -140)
   pendown()
   write("Hexagon", align = 'center')
hideturtle()
mainloop()