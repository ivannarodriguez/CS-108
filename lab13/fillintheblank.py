'''
Models a short answer problem
Created Fall 2014

@author: imr6, vam6
'''

from problem import *

#exercise 13.3
class FillInTheBlank(Problem):
    def __init__(self, q, a):
        ''' Construct a Fill in the black question with question and answer texts '''
        Problem.__init__(self, q)
        self.text = q
        self.answer = a
    def ask_question(self):
        ''' Return the question text '''
        return super().get_text() + '\nFill in the blank.'
    
    def check_answer(self, a):
        ''' Return True if a is the correct answer; False otherwise '''
        return self.answer == a
    
    def get_answer(self):
        ''' Return the answer text '''
        return self.answer