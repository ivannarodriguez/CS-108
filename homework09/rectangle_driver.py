''' Modules and Files 
Created April 11, 2016
Homework 09
@author: Ivanna Rodriguez (imr6))
'''
import turtle
from solution_rectangle import Rectangle

#create a list for rectangle specifications
specs=[]
with open('rectangles.txt', 'r') as rec_file:#open file and read it
    for line in rec_file:#split each line in the file 
        splits=line.split()
        rec1=Rectangle(int(splits[0]),int(splits[1]),int(splits[2]),int(splits[3]),splits[4])#index attributes 
        specs.append(rec1)#append rectangle specifications to specs list
    for rectangle in specs:#index each rectangle in specs and call render function to draw the rectangles
        rectangle.render(turtle)
        
