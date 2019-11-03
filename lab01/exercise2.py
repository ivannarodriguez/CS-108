''' This program will draw a star
Created Feb 2 2017
Lab 01
@author: Ivanna Rodriguez (imr6)
'''

# Gain access to the collection of code named "turtle".
import turtle

# Give the name "window" to the screen where the turtle will appear.
window = turtle.Screen()

# Create a turtle and name it bob.
bob = turtle.Turtle()

# Create a STar
bob.forward(250)
bob.right(144) 
bob.forward(250)
bob.right(144)
bob.forward(250)
bob.right(144)
bob.forward(250)
bob.right(144)
bob.forward(250)

# Keep the window open until it is clicked.
window.exitonclick()