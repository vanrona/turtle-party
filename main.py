#Turtle Party Project
# Natalya VR
#27/08/24
import turtle
turtle.color("red")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360/num)
    
polygon(4,100)
back(125)
polygon(3,50)
