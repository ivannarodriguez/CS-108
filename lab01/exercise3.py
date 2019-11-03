''' This Program will draw the letters CS
Created Feb 2 2017
Lab 01
@author: Ivanna Rodriguez (imr6)
'''
# Gain access to the collection of code named "turtle".
import turtle
# Give the name "window" to the screen where the turtle will appear.
window = turtle.Screen()

# Create a turtle and name it will.
will = turtle.Turtle()

# Create letter C.
will.back(100)
will.left(90)
will.forward(180)
will.right(90)
will.forward(100)

# Move to Create space between the two letters.
will.penup()
will.forward(150)

# Create letter S
will.pendown()
will.back(100)
will.right(90)
will.forward(90)
will.left(90)
will.forward(100)
will.right(90)
will.forward(100)
will.right(90)
will.forward(100)


# Keep the window open until it is clicked.
window.exitonclick()