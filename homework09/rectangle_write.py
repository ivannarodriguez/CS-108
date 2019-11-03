''' Modules and Files 
Created April 12, 2016
Homework 09
@author: Ivanna Rodriguez (imr6))
'''

with open('rectangles.txt', 'w') as rec_text:#open the rectangles.txt file in writing mode
    newspecs="0 0 200 100 salmon\n100 100 120 130 chartreuse\n200 150 300 350 cyan\n"#create string with new specifications for three rectangles 
    rec_text.write(newspecs)#overwrite old specifications with the new ones created above