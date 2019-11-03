'''
Models a short answer problem
Created Fall 2014

@author: imr6, vam6
'''
from problem import *

#exercise 13.3
class TrueFalse(Problem):
    ''' Model a short-answer question '''
    
    def __init__(self, q, a):
        ''' Construct a short-answer question with question and answer texts '''
        if isinstance(a, bool):
            Problem.__init__(self, q)
            self.answer = a
        else:
            raise ValueError('Enter True or False')
              
    def ask_question(self):
        ''' Return the question text '''
        return super().get_text() + '\nIs this statement true or false?'
    
    def check_answer(self, a):
        ''' Return True if a is the correct answer; False otherwise '''
        return str(self.answer) == a
    
    def get_answer(self):
        ''' Return the answer text '''
        return str(self.answer)
