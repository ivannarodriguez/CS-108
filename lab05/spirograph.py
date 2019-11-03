'''Spirograh drawing
3/2/17
Lab 05
@author: Annalane Miller (asm9) and Ivanna Rodriguez (imr6)'''
 
import turtle
window = turtle.Screen()
bob = turtle.Turtle()
window.setup(500,500)
 
import math
 
#get user's input
answer=input('Do you want to draw a spirograph? (Y/n): ')
#while the user's input is not Y or n, prompt again
while answer!='Y' and answer!='n' and answer!='':
        answer=(input("Please enter either 'Y' or 'n': "))
#while the user inputs Y, promp for info and draw the spirograph
while answer=='Y' or answer=='':
    mov_rad=float(input('Enter moving radius: '))
    fix_rad=float(input('Enter fixed radius: '))
    pen_offset=float(input('Enter pen offset: '))
    color=input('Enter color: ')
    rad_sum=fix_rad+mov_rad
    #setup
    time=0.0
    x=(rad_sum)*math.cos(time)+pen_offset*math.cos((rad_sum*time)/mov_rad)
    y=(rad_sum)*math.sin(time)+pen_offset*math.sin((rad_sum*time)/mov_rad)
    bob.up()
    bob.goto(x, y)
    bob.down()
    bob.color(color)
    while time<100:
        time+=0.1
        x=(rad_sum)*math.cos(time)+pen_offset*math.cos((rad_sum*time)/mov_rad)
        y=(rad_sum)*math.sin(time)+pen_offset*math.sin((rad_sum*time)/mov_rad)
        bob.goto(x, y)
        time+=0.1
    #ask user if they want to draw another one
    answer=input("Do you want to draw another Spirograph? (Y/n)")
    #prompt if they enter invalid input
    while answer!='Y' and answer!='n' and answer!='':
        answer=(input("Please enter either 'Y' or 'n': "))
    #exit the loop if they answer no
    if answer=='n':
        break
   
#close screen      
window.exitonclick() 