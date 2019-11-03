'''
Model a single particle
Created Fall 2014
Updated Summer, 2015

@author: smn4
@author: kvlinden
modified by : vam6, imr6
'''

class Particle:
    '''
    Particle models a single particle that may be rendered to a canvas
    '''

    def __init__(self, x = 50, y = 50, velX = 10, velY = 15, radius = 15, color = '#663977'):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._velX = velX
        self._velY = velY
        self._radius = radius
        self._color = color
        
    def render(self,canvas): #Instance method render 
        canvas.create_oval(self._x - self._radius,self._y - self._radius,self._x + self._radius,self._y + self._radius,fill = self._color)
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_radius(self):
        return self._radius
    
    def move(self,canvas): #Instance method move 
        self._x+=self._velX
        self._y+=self._velY 
        # Create boolean to cause the particle to bounce at the edges of the screen 
        if self._x + self._radius > canvas.winfo_reqwidth() or self._x - self._radius < 0:
            self._velX= -self._velX
        elif self._y + self._radius > canvas.winfo_reqwidth() or self._y- self._radius < 0:
            self._velY=-self._velY
            
            