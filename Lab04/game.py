''' Rock, Paper, Scissors
Created Feb 23 2017
Lab 04
@author: Ivanna Rodriguez (imr6) and Valeria Martinez (vam6)
'''
#import random
from random import randint

#prompt user for choice
user_choice=int(input('Choose 0 for Rock, 1 for Paper, or 2 for scissors: '))

#generate random number
computer_choice=randint(0,2)
print('Computer chose:'+' '+str(computer_choice))

#create algorithm for game and print results
if user_choice==0:
    if computer_choice==1:
        print('Computer Wins!')
    elif computer_choice==2:
        print('You win!')
    elif computer_choice==0:
        print("It's a draw!") 
if user_choice==1:
    if computer_choice==1:
        print("It's a draw!")
    elif computer_choice==2:
        print('Computer Wins!')
    elif computer_choice==0:
        print("You Win!") 
if user_choice==2:
    if computer_choice==2:
        print("It's a draw!")
    elif computer_choice==0:
        print('Computer Wins!')
    elif computer_choice==1:
        print("You Win!") 
        
       


    
    
    
  


