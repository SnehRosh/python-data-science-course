from turtle import *
penup()
goto(-100,-100)
pendown()
speed("fastest")
bgcolor("blue")
pencolor('yellow')
pensize(3)

for i in range(100, 0, -25):#reverse
 fd(i)
 lt(360/5)#for angle bent
 write(i) #displays the number of loops
 circle(i)
hideturtle()
mainloop()