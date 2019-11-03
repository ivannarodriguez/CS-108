''' Creating a Function that Draws a Stickman
14 March 2017
Homework 06
@author: Ivanna Rodriguez (imr6)
'''

# Gain access to "turtle".
import turtle
window = turtle.Screen()
perro = turtle.Turtle()

def stickfigure(turtle, x, y, UNIT):
    '''This function draws a stick figure. 
    x and y are coordinates, the UNIT is 
    a length'''
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    # Draw Stickman's head
    turtle.circle(UNIT)
    # Draw Stickman's body
    turtle.right(90)
    turtle.forward(UNIT*2)
    # Draw Stickman's legs
    turtle.right(45)
    turtle.forward(UNIT*1.1442)
    turtle.penup()
    turtle.backward(UNIT*1.1442)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(UNIT*1.1442)
    turtle.penup()
    # Draw Stickman's arms
    turtle.left(135)
    turtle.goto(x,y)
    turtle.right(180)
    turtle.forward(UNIT)
    turtle.left(90)
    turtle.forward(UNIT)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(UNIT*2)


stickfigure(perro, -500, 100, 50)


#close screen      
window.exitonclick() 