'''
Temperature GUI
Created on Apr 25, 2017

@author: Ivanna Rodriguez (imr6)
'''

from tkinter  import *
from temperature import *

class Gui:
    def __init__(self,window):
        # Exercise 11.2
        self._window= window#create window
        self._temp=Temperature()
        #create text label and text entry for the user
        text_label = Label(window, text="Temperature (in Fahrenheit):")
        text_label.grid(row=0, column=0, sticky=E)
        self._text= DoubleVar()
        text_entry = Entry(window, width=6,textvariable=self._text)
        text_entry.grid(row=0, column=1, sticky=W)
        #create messsage for the status of the calculation
        self._status_message = Label(self._window, text="Welcome!")
        self._status_message.grid(row=4, column=0, sticky=E)
        #create "Convert to Celsius" button
        getCelsius_button = Button(window, text="Convert to Celsius", command=self.convert_to_Celsius)
        getCelsius_button.grid(row=3,column=0)
        #show result
        self._result= StringVar()
        self.result_label = Label(window, textvariable=self._result, width=20)
        self.result_label.grid(row=3, column=1, sticky=W)
    
    def convert_to_Celsius(self):
        try:
            self._temp.set_temp(self._text.get())
            result=self._temp.getCelsius()
            self._result.set(result)
            self._status_message.config(text= "Welcome!")
        except:
            self._status_message.config(text="Temperature can't be less than Absolute zero!")
            
        
if __name__ == '__main__':
    root=Tk()
    root.title('Temperature Converter')
    app= Gui(root)
    root.mainloop()
    
        