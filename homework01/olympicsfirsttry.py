''' Drawing the Olympics Logo
Created Feb 04 2017
Homework 01
@author: Ivanna Rodriguez (imr6)
'''

# Gain access to the collection of code named "turtle".
import turtle

# Give the name "window" to the screen where the turtle will appear.
window = turtle.Screen()

# Create a turtle and name it juan.
juan = turtle.Turtle()

#position turtle at top right
juan.penup()
juan.left(180)
juan.forward(350)
juan.right(90)
juan.forward(150)

#create blue circle
juan.color("blue")
juan.down()
juan.width(10)
juan.circle(80)

#create yellow circle
juan.up()
juan.color("yellow")
juan.down()
juan.left(90)
juan.width(10)
juan.circle(80)

#create black circle
juan.up()
juan.color("black")
juan.width(10)
juan.back(30)
juan.down()
juan.left(90)
juan.width(10)
juan.circle(80)

#create black circle
juan.up()
juan.color("green")
juan.width(10)
juan.left(90)
juan.forward(150)
juan.right(180)
juan.down()
juan.circle(80)

#create black circle
juan.up()
juan.color("red")
juan.width(10)
juan.back(30)
juan.down()
juan.left(90)
juan.width(10)
juan.circle(80)

# Keep the window open until it is clicked.
window.exitonclick()