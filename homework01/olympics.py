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

#draw blue circle
juan.color("blue")
juan.down()
juan.width(15)
juan.circle(80)
juan.up()

#draw yellow circle
juan.color("yellow")
juan.width(15)
juan.right(90)
juan.forward(10)
juan.right(180)
juan.down()
juan.circle(80)
juan.up()

#draw black circle
juan.color("black")
juan.width(15)
juan.right(180)
juan.forward(95)
juan.left(90)
juan.forward(80)
juan.left(90)
juan.down()
juan.circle(80)
juan.up()

#draw green circle
juan.color("lawn green")
juan.width(15)
juan.right(180)
juan.forward(175)
juan.right(90)
juan.forward(160)
juan.left(180)
juan.down()
juan.circle(80)
juan.up()

#draw green circle
juan.color("red")
juan.width(15)
juan.right(90)
juan.forward(15)
juan.down()
juan.circle(80)



# Keep the window open until it is clicked.
window.exitonclick()