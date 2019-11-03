''' Validation 
16 March 2017
lab 07
@author: Ivanna Rodriguez (imr6) and Annalane Miller (asm9)
'''
#validation info for SSN
def isValidSSN(SSN):
    '''(str)-> bool
    Return True if (str) is proper format'''
    return len(SSN)==11 and SSN[3]=='-' and SSN[6]=='-' and SSN[0:3].isdigit()and SSN[4:6].isdigit() and SSN[7:].isdigit()        


#validation info for password
def isValidPassword(password):
    '''(str)-> v=bool
    Return Truei f (str) is proper format'''
    if len(password)>=8 and password.isalnum():
        countdigits=0
        for ch in password:
            if ch.isdigit():
                countdigits+=1
        if countdigits>=2:
            return True
    else:
        return False


#Validation info for Credit Card
def isValidPrefix(cc):
    return cc.startswith('37') or cc.startswith('4') or cc.startswith('5') or cc.startswith('6')

def sum_of_odds(cc):
    reverse=cc[::-1]
    total=[]
    for idx in range(len(reverse)):
        if idx%2==1:
            total.append(int(cc[idx]))
    return sum(total)

def sum_of_double_evens(cc):
    reverse=cc[::-1]
    evenlist=[]
    doubledevens=[]
    finallist= []
    for idx in range(len(reverse)):
        if idx%2==0:
            evenlist.append(int(cc[idx]))
    for idx in evenlist:
        doubleidx= idx+idx
        doubledevens.append(doubleidx)
    for idx in doubledevens:
        
        if idx>=10:
            idx=idx-9
            finallist.append(idx)
        else:
            finallist.append(idx)   
             
    return sum(finallist)  

def isValidCC(cc):
    return isValidPrefix(cc)==True and 13<=len(cc)<=16 and cc.isdigit() and (sum_of_odds(cc)+ sum_of_double_evens(cc))%10==0
         

#Print Menu
def printMenu():
    '''Print the text menu.'''
    print('\nPlease select from the following list of options (type the appropriate character):')
    print('A. Social Security Number')
    print('B. Password')
    print("C. Credit Card")
    # Add menu options here for three new string tests.
    print('Q. Quit')
    
# Run the text-menu interface until the user wants to quit.
while True:
    printMenu()
    choice = input('Choice: ').upper()
    if choice == 'A':
        SSN=input('Enter an SSN: ')
        if isValidSSN(SSN):
            print('SSN is valid')
        else:
            print('SSN is not valid')
    elif choice == 'B':
        Password=input('Enter Password: ')  
        if isValidPassword(Password):
            print('Password is valid')
        else:
            print('Password is invalid')
    elif choice =="C":
        cc=input("Enter a credit card number: ")
        if isValidCC(cc):
            print("Credit Card is Valid")
        else:
            print("Credit Card is Invalid")
    elif choice == 'Q':
        break
    else:
        print('I\'m sorry, {0} is not a valid option.'.format(choice))
    
print('\nGood-bye!')