'''Bouncing turtle
March 07
Homework 05
@author: Ivanna Rodriguez (imr6)'''

import turtle
window = turtle.Screen()
bob = turtle.Turtle()
window.setup(500,500)

import random

bob.shape('circle')
#define turtle velocity
vel=3
#generate random starting angle for turtle
randomangle=random.randint(1,360)
bob.setheading(randomangle)

#make turtle move and bounce off walls
bob.goto(0, 0)
bob.penup() 
while True:    
    if not -225<bob.xcor()<225:#if turtle's xcoor is not in between the screen boundaries, then change heading
        bob.setheading(180-bob.heading())
    bob.forward(vel)
    if not -225<bob.ycor()<225:#if turtle's ycoor is not in between the screen boundaries, then vhange heading
        bob.setheading(360-bob.heading())
    bob.forward(vel)
    
        
#close screen      
window.exitonclick() 