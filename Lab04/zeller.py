''' Zeller's Congruence
Created Feb 23 2017
Lab 04
@author: Ivanna Rodriguez (imr6) and Valeria Martinez (vam6)
'''

#prompt user for year, day of month, and month
year=int(input('Please enter the year: '))
q_day=int(input('Please enter day of the month: '))
m_month=int(input('Please enter the month: '))

#get values
J_year=year//100
k_year=year%100

#create restrictions for formula
if m_month==1:
    m_month=13
    k_year=k_year-1
elif m_month==2:
    m_month=14
    k_year=k_year-1

#calculate h
h=((q_day)+(((m_month+1)*26)//10)+(k_year)+(k_year//4)+(J_year//4)+(5*J_year))%7

#Create List for days of the week 
days_week=['Saturday', 'Sunday', 'Monday', 'Tuesday','Wednesday','Thursday', 'Friday']

#print days of the week based on h
print(days_week[h])




