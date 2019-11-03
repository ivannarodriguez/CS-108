''' Wind Chill
Created Feb 23 2017
Lab 04
@author: Ivanna Rodriguez (imr6) and Valeria Martinez (vam6)
'''

#prompt user for temperature and wind speed
temp_a= float(input('Please enter temperature in degrees Fahrenheit: '))
wind_v= float(input('Please enter wind speed in miles per hour: '))

#Calculate wind chill
wind_chill=35.74+(0.6215*temp_a)-(35.75*(wind_v**0.16))+((0.4275*temp_a)*(wind_v**0.16))

#Restrict wind speed and temperature in order to get wind chill
if wind_v<2 or -58>temp_a>41:
    print('Program will not work')
else:
    print(wind_chill)
if wind_chill<-40:
    print('Stay Home...')
elif -40<=wind_chill<-10:
    print('4 layers')
elif -10<= wind_chill<20:
    print('3 layers')
elif 20 <= wind_chill < 40:
    print('2 layers')
elif wind_chill >= 40:
    print('1 layer')
    
    