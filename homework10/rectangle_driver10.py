''' Rectangle Driver with Exception
Created April 18, 2017
Homework 10
@author: Ivanna Rodriguez (imr6))
'''
import turtle
from rectangle10 import Rectangle

#create a list for rectangle specifications
specs=[]
userfile=input('Enter filename.txt: ')#ask user for filename 
try:#except a FileNotFoundError if filename is invalid (e.g. an int) or if it is not in the directory
    with open(userfile, 'r') as rec_file:#open file and read it
        for line in rec_file:#split each line in the file 
            splits=line.split()
            try:#except a ValueError if the width and height of rectangles in rectangles10.txt are negative
                rec1=Rectangle(int(splits[0]),int(splits[1]),int(splits[2]),int(splits[3]),splits[4])#index attributes 
                specs.append(rec1)#append rectangle specifications to specs list
            except ValueError as VE:
                print(VE)
except FileNotFoundError as FNE:
    print(FNE)
#draw rectangles in list        
for rectangle in specs:#index each rectangle in specs and call render function to draw the rectangles
    rectangle.render(turtle)