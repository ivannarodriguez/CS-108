'''
Temperature Class
Created on Apr 25, 2017

@author: Ivanna Rodriguez (imr6)
'''

class Temperature:
    '''This class stores information about the temperature'''    
    def __init__(self, fahrenheit=0.0):#constructor
        if fahrenheit<-459.67:
            raise AttributeError("Temperature can't be less than the absolute zero")#raise exception when fahrenheit is greater than absolute zero
        else:
            self._fahrenheit = float(fahrenheit)
    #accessors
    def getDegrees(self):
        return self._fahrenheit
    
    def getCelsius(self):
        self._celsius = (float(self._fahrenheit) - 32) * 5 / 9
        return self._celsius
    
    def set_temp(self, newTemp):
        if newTemp<-459.67:
            raise AttributeError("Temperature can't be less than the absolute zero")#raise exception when fahrenheit is greater than absolute zero
        else:
            self._fahrenheit = float(newTemp)
            return newTemp

#tests
if __name__ == '__main__':
    #test getDegrees
    temp=Temperature()
    print("This should equal 0.0=", temp.getDegrees())
    #test default getCelcius
    temp=Temperature()
    if temp.getCelsius()==-17.77777777777778:
        print('Test one passed')
    #other tests
    temp=Temperature(80)
    if temp.getCelsius()==26.666666666666667:
        print('Test two passed')
    temp=Temperature(32)
    if temp.getCelsius()==0:
        print('Test three passed')
    temp=Temperature(-38)
    if temp.getCelsius()==-38.888888888888889:
        print('Test four passed')
    #absolute zero
    try:
        temp=Temperature(-500)
    except AttributeError:
        print("Temperature can't be less than the absolute zero")
    