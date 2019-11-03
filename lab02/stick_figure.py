''' Drawing a Stickman
Created Feb 09 2017
Lab 02
@author: Ivanna Rodriguez (imr6) and Valeria Martinez (vam6)
'''

# Gain access to the collection of code named "turtle".
import turtle
window = turtle.Screen()
larry = turtle.Turtle()

# Gain access to math 
import math

#Created a constant with value 50
UNIT = 50

# Draw Stickman's head
larry.circle(UNIT)
larry.right(90)
larry.forward(UNIT*2)

# Draw Stickman's body
larry.right(45)
larry.forward(UNIT*1.1442)
larry.penup()
larry.backward(UNIT*1.1442)
larry.left(90)
larry.pendown()
larry.forward(UNIT*1.1442)
larry.up()
larry.goto(0,-UNIT)
larry.left(45)
larry.forward(UNIT)
larry.left(180)
larry.pendown()
larry.forward(UNIT*2)



window.exitonclick()