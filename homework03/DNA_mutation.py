''' Mutating a DNA Sequence
Created Feb 18 2017
Homework 03
@author: Ivanna Rodriguez (imr6)
'''

#ask user for a String and pattern
string=input('Please enter a sequence of characters: ' )
pattern=input('Please enter a pattern in the string: ')

#locate pattern and its reverse
length=int(len(pattern))
index_pattern = int(string.find(pattern))
index_reverse = int(string.find(pattern[::-1]))

#locate string between pattern
middle_startindex=int(length+index_pattern)
middle_endindex=index_reverse
middle_length=len(string[middle_startindex:middle_endindex])

#make middle index and length into a string and reverse the string
middle_text=string[middle_startindex:middle_endindex]
reversed_middle=middle_text[::-1]

#split list into three parts, with reversed middle in between pattern and reversed pattern
first_part=string[0:middle_startindex]
second_part=reversed_middle
third_part=string[middle_endindex:len(string)]

#print concatenated string
print(first_part+second_part+third_part)
































