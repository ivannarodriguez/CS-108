'''Finding Prefixes
03/31/17
Homework 07
@author: Ivanna Rodriguez (imr6)'''

string1=input('Enter string one: ')
string2=input('Enter string two: ')
shortest_string_lenght=min(len(string1), len(string2))

#code idea taken from Adam D'Angelo in //www.quora.com/hWhat-is-the-easiest-way-to-find-the-longest-common-prefix-or-suffix-of-two-sequences-in-Python
def find_longest_prefix(string1, string2):
    common_letter_index = 0
    while common_letter_index < shortest_string_lenght:
        if string1[common_letter_index] != string2[common_letter_index]:
            break
        common_letter_index += 1
    return string1[:common_letter_index]

#call find_longest_perfix function and print result
print(find_longest_prefix(string1, string2))


#create test Function for different cases
def test_find_longest_prefix():
    result=find_longest_prefix('unhappy', 'uncommon')
    if result=='un':
        print('Test one Passes')
    else:
        print('Test one Fails')
    
    result=find_longest_prefix('precaution', 'presto')
    if result=='pre':
        print('Test two Passes')
    else:
        print('Test two Fails')
        
    result=find_longest_prefix('cat', 'caterpillar')
    if result=='cat':
        print('Test three Passes')
    else:
        print('Test three Fails')
        
    result=find_longest_prefix('nothing', 'carrot')
    if result=='':
        print('Test four Passes')
    else:
        print('Test four Fails')

#call the test function        
test_find_longest_prefix()