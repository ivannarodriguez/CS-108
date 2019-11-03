''' This program will calculate the user's change 
Created Feb 11 2017
Homework 02
@author: Ivanna Rodriguez (imr6)
'''
#ask user for the cost of transaction and amount paid
cost=int(input('Please enter the amount charged for transaction: '))
amount_paid=int(input('Please enter the amount you paid: '))

#calculate the change the user should receive
change=amount_paid-cost

#calculate how many of each bill the user should receive
twenty=change//20
tens=(change%20)//10
fives=(change%20)%10//5
ones=(change%20)%10%5

#print change and bill amounts in dollars
print('Your change is','$'+str(change)+':', twenty, '$20 bills', tens, '$10 bills', fives, '$5 bills', ones, '$1 bills')









