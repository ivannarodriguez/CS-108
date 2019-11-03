'''
GUI controller for a particle simulation
Created Fall 2014
Updated Summer, 2015

@author: smn4
@author: kvlinden
modified by: vam6, imr6
'''

from tkinter import *
from random import randint
from particle import *
from helpers import *
import random 

class ParticleSimulation:
    ''' Creates particle simulator '''
    
    def __init__(self, window):
        ''' Construct the particle simulator GUI '''
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self.width = 400
        self.height= self.width
        self.canvas = Canvas(self.window, bg='black',
                        width=self.width, height=self.height)
        add_button = Button(window, text="Add particle",command=self.add_particle)
        add_button.pack()
        self.p_list=[] # replace self.p1 with an empty list 
        self.canvas.pack()
        self.terminated = False
        self.render()
        self.canvas.bind('<Button-1>', self.check_remove_particle)
        
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()
    
    def render(self):
        if self.terminated== False: # if the program is not terminated 
            self.canvas.delete(ALL)
            for particle in self.p_list:
                particle.move(self.canvas)
                particle.render(self.canvas)
#         if self.terminated== False: # if the program is not terminated 
#             self.canvas.delete(ALL)
#             self.p1.move(self.canvas)
#             self.p1.render(self.canvas)
        self.canvas.after(50,self.render)
 
            
    def add_particle(self):
        p1= Particle(x=randint(0,self.width),y=randint(0,self.height),velX=randint(-25,25),velY=randint(-25,25),radius=randint(10,25),color=get_random_color())
        self.p_list.append(p1)
    
    def check_remove_particle(self, event):
        copy = self.p_list[:]
        for p in copy:
            if distance(event.x, event.y, p.get_x(), p.get_y())<p.get_radius():
                self.p_list.remove(p)
 

if __name__ == '__main__':
    root = Tk()
    root.title('Particle Simulation')    
    app = ParticleSimulation(root)
    root.mainloop()
    

