from turtle import *
speed("fastest")
bgcolor("blue")
pencolor('yellow')
pensize(3)

for i in range(1, 200, 5):
 fd(i)
 lt(360/10)#for angle bent
 write(i) #displays the number of loops

hideturtle()
mainloop()