''' Drawing Rectangles
Created Feb 27 2017
Homework 04
@author: Ivanna Rodriguez (imr6)
'''
#Gain access to the turtle and name it Juan
import turtle
window = turtle.Screen()
juan = turtle.Turtle()
 
#prompt for rectangle one information
x1=int(input('Enter x-coordinate for left corner of first rectangle: '))
y1=int(input('Enter y-coordinate for left corner of first rectangle: '))
w1=int(input('Enter first rectangle width: '))
h1=int(input('Enter first rectangle height: '))
 
#draw first rectangle
juan.up()
juan.goto(x1, y1)
juan.down()
juan.forward(w1)
juan.right(90)
juan.forward(h1)
juan.right(90)
juan.forward(w1)
juan.right(90)
juan.forward(h1)
juan.right(90)

#prompt for rectangle two information
x2=int(input('Enter x-coordinate for left corner of second rectangle: '))
y2=int(input('Enter y-coordinate for left corner of second rectangle: '))
w2=int(input('Enter second rectangle width: '))
h2=int(input('Enter second rectangle height: '))
 
#draw second rectangle
juan.up()
juan.goto(x2, y2)
juan.down()
juan.forward(w2)
juan.right(90)
juan.forward(h2)
juan.right(90)
juan.forward(w2)
juan.right(90)
juan.forward(h2)
juan.right(90)

#condition for rectangle overlap:
#Idea of finding rectangle center and hypotenuse contributed by Judy Kwon @dk43
r1=(x1+w1)/2
r2=(x2+w2)/2
dist=juan.distance(r1, r2)

if r1+r2<=dist:
    juan.write("The rectangles are disjoint ", move=False, align= "right", font = ("Arial", "20", "normal"))
else:
    juan.write("The rectangles overlap ", move=False, align= "right", font = ("Arial", "20", "normal"))
 
 
#exit window with one click
window.exitonclick()