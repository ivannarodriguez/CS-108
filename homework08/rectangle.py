''' Create a Class Representing Rectangle Objects
4 April 2017
Homework 08
@author: Ivanna Rodriguez (imr6)
'''

#access turtle
import sys
import turtle

#create rectangle class:
class rectangle:
    '''a class that represents rectangles
    '''
    #constructor
    def __init__(self, x=0, y=0, width=50, height=50, color='black'):#create constructor
        if height>=0 and width>=0:
            self._x=x
            self._y=y
            self._w=width
            self._h=height
            self._color=color
        else:
            print('invalid rectangle: neither height nor width can be negative', file=sys.stderr)
            sys.exit(-1) 
    
    #__str__ method for printing
    def __str__(self):
        '''This method prints rectangle's internal state'''
        return 'position='+'('+str(self._x)+','+str(self._y)+')'+" width="+str(self._w)+" height="+str(self._h)+' color='+str(self._color)
    
    #accessors
    def get_area(self):
        '''returns the area of the rectangle'''
        return self._w*self._h
    
    def get_perimeter(self):
        '''returns the perimeter of the rectangle'''
        return 2*self._w+2*self._h
    
    def get_width(self):
        '''returns rectangle's width'''
        return self._w
    
    def get_height(self):
        '''returns rectangle's height'''
        return self._h
    
    def get_x(self):
        '''returns rectangle's x-coordinate'''
        return self._x
    
    def get_y(self):
        '''returns rectangle's y-coordinate'''
        return self._y
    
    #mutators
    def modify_width(self, integer):
        '''Enter an integer that will
        modify the width of the rectangle'''
        self._w=self._w+integer
        return self._w
          
    
    def modify_height(self, integer):
        '''Enter an integer that will 
        modify the height of the rectangle'''
        self._h=self._h+integer
        return self._h
    
    def overlaps(self, other):
        '''determines whether two rectangle objects overlap
        and returns True of False accordingly'''
        r2_left_r1=(other.get_x()+other.get_width())<self.get_x()
        r2_right_r1=(self.get_x()+self.get_width())<other.get_x()
        r2_above_r1=self.get_y()<(other.get_y()-other.get_height())
        r2_below_r1=other.get_y()<(self.get_y()-self.get_height())
        
        if r2_above_r1 or r2_below_r1 or r2_left_r1 or r2_right_r1:
            return False
        else:
            return True       

    # render method
    def render(self, turtle):
        '''receives a turtle object from its calling program
        and uses that object to draw itself on the canvas'''
        turtle.color(self._color)
        turtle.up()
        turtle.goto(self._x, self._y)
        turtle.down()
        turtle.forward(self._w)
        turtle.right(90)
        turtle.forward(self._h)
        turtle.right(90)
        turtle.forward(self._w)
        turtle.right(90)
        turtle.forward(self._h)
        turtle.right(90)
        

#main code
window = turtle.Screen()
turtle = turtle.Turtle()

#Test one: default rectangle, overlap
rec1=rectangle()
rec1.render(turtle)
rec2=rectangle(10,10,100,100,'green')
rec2.render(turtle)
print('rec1(black) overlaps rec2(green):',rec1.overlaps(rec2))

#Test two: disjoint
rec3=rectangle(100,100,50,250, 'pink')
rec3.render(turtle)
rec4=rectangle(-100,-100,100,200, 'purple')
rec4.render(turtle)
print('rec3(pink) overlaps rec4(purple):', rec3.overlaps(rec4))

#Test three: the __str__ method
print("rec3(pink) internal state:",rec3)
print('rec4(purple) internal state before mutators:', rec4)

#Test four: the mutator methods
rec4.modify_height(50)
rec4.modify_width(15)
print('rec4(purple) internal state after mutators:', rec4)

#Test five: invalid rectangle
rec_invalid=rectangle(200,200,-100,-150,'gold')
print(rec_invalid)

#exit window with one click
window.exitonclick()

