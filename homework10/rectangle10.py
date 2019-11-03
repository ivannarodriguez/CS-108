'''rectangle.py for CS108, Homework 8.
Author: Keith VanderLinden and Victor Norman
Date: 7 April 2017
Modified by: Ivanna Rodriguez @imr6
'''

import turtle
import sys

class Rectangle:
    
    def __init__(self, x=0, y=0, width=50, height=50, color='black'):
        self._color = color
        self._x = x
        self._y = y
        if width > 0 and height > 0:
            self._width = width
            self._height = height
        else:
            raise ValueError('Width and height must be positive.')#raise exception if rectangle values are not positive
            
    def __str__(self):
        return '(' + str(self._x) + ',' + str(self._y) + '), ' + str(self._width) + \
               ', ' + str(self._height) + ', ' + str(self._color)
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_color(self):
        return self._color
    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def get_area(self):
        return self._width * self._height
    
    def get_perimeter(self):
        return 2 * (self._width + self._height)
    
    def modify_width(self, delta=0.0):
        '''Modify the height of the rectangle by the given delta.
        Ensure that the width is still a positive number.'''
        new_width = self._width + delta
        if new_width > 0:
            self._width = new_width
        else:
            print('invalid width...')
            sys.exit(-1)
    
    def modify_height(self, delta=0.0):
        '''Modify the height of the rectangle by the given delta.
        Ensure that the height is still a positive number.'''
        new_height = self._height + delta
        if new_height > 0:
            self._height = new_height
        else:
            print('invalid height...')
            sys.exit(-1)
    
    def overlaps(self, rectangle2):
        '''
        Return True if this rectangle overlaps with the given rectangle2;
        False otherwise.
        '''
        r1_left_of_r2 = self._x + self._width < rectangle2.get_x() 
        r2_left_of_r1 = rectangle2.get_x() + rectangle2.get_width() < self._x
        r1_above_r2 = self._y - self._height > rectangle2.get_y()
        r2_above_r1 = rectangle2.get_y() - rectangle2.get_height() > self._y
        return not (r1_left_of_r2 or r2_left_of_r1 or r1_above_r2 or r2_above_r1)
        
    def render(self, turtle):
        '''Draw the rectangle using the given turtle.'''
        turtle.penup()
        turtle.seth(0)
        turtle.color(self._color)
        turtle.goto(self._x, self._y)
        turtle.pendown()
        turtle.forward(self._width)
        turtle.right(90)
        turtle.forward(self._height)
        turtle.right(90)
        turtle.forward(self._width)
        turtle.right(90)
        turtle.forward(self._height)


#Testing  
if __name__ == '__main__':
    window = turtle.Screen()
    pen = turtle.Turtle()
#draw two rectangles and determine if they overlap
    r1 = Rectangle()#default rectangle
    r1.render(pen)
    print(r1) 
    r2 = Rectangle(10, 10, 50, 50, 'red')
    r2.render(pen)
    print(r1.overlaps(r2))
#try valid rectangle and print its properties
    try:
        r6=Rectangle(100,100,500,400, 'violet')
        print(r6)
    except ValueError as ve:
        print(ve)
#try invalid rectangles to raise exceptions
    try:
        r3= Rectangle(0,0,-100,-250, 'blue')
        print(r3)
    except ValueError as ve:
        print(ve)
    try:
        r4= Rectangle(0,0,-100,300, 'blue')
        print(r4)
    except ValueError as ve:
        print(ve)
    try:
        r5= Rectangle(0,0,300,-250, 'blue')
        print(r5)
    except ValueError as ve:
        print(ve)
        
    pen.hideturtle()
    window.exitonclick()
   