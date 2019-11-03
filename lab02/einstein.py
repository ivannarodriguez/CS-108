''' This program will create Einstein's puzzle
Created Feb 9 2017
Lab 02
@author: Ivanna Rodriguez (imr6) and Valeria Martinez (vam6)
'''

#ask user for three digit number
number=int(input('Please enter a three digit number where the first and last digits differ by at least 2: ' ))

#reverse digit order
digit1=(number//100)%100
digit2=(number//10)%10
digit3=number%10
rev_number=digit3*100+digit2*10+digit1

#subtract user input with its reverse
difference=abs(number-rev_number)
number=difference

#reverse the result obtained from the difference
digit1=(number//100)%100
digit2=(number//10)%10
digit3=number%10
rev_diff=digit3*100+digit2*10+digit1

#print the number obtained above plus the original number
print(difference+rev_diff)






