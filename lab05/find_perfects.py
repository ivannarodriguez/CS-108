'''Finding Perfect Numbers
3/2/17
@author: Annalane Miller (asm9) and Ivanna Rodriguez (imr6)'''


num_perfect = 0

for value in range(2, 10000):
#set initial values
    high= value
    low = 1
    divisors = []

#finding divisors
    while low < high:
        if value % low ==0:
            high = value// low
            divisors.append(low)
            if high != low:
                divisors.append(high)
        low += 1   
    
    
    #find if number is perfect      
    divisors.remove(value)

    total= sum(divisors)
    
#print 4 perfect numbers in range
    if total==value:
        print(value)
        num_perfect +=1
        if num_perfect > 4:
            break
        
    
   
     
