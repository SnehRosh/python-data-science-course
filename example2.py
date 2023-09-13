from turtle import * 
#make square
speed('fastest')
penup()
goto(-200,-200)#changing the position of the turtle
pendown()
for i in range(30):
 fd(10)
 lt(90)
 fd(10)
 rt(90)


hideturtle() #Hide the turtle sign
mainloop() #keeps the window open