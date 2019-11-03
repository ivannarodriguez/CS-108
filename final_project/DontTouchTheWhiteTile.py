'''Final Project
Don't Touch The White Tile
@author: Ivanna Rodriguez (imr6)
May 2017 
'''

from tkinter import *
from tkinter.font import ITALIC
from random import randint


CANVAS_WIDTH = 240
CANVAS_HEIGHT = 500
RECT_WIDTH = 60
RECT_HEIGHT =125
NUM_CELLS_WIDE = int(CANVAS_WIDTH / RECT_WIDTH)
NUM_CELLS_HIGH=5
YSPEED = 5

class Cell:
    '''stores information of cells on the grid'''
    def __init__(self, canvas, x, y):# from VTN2's grid example 
        self._canv = canvas
        self._x = x
        self._y = y
        self._color='white'
        self._size = RECT_WIDTH 
        self._ulx = x * RECT_WIDTH          # upper-left x
        self._lrx = self._ulx + RECT_WIDTH  # lower-right x
        self._uly = y * RECT_HEIGHT          # upper-left y
        self._lry = self._uly + RECT_HEIGHT  # lower-right y
        self._tag = "cell" + str(x) + str(y)

    def render(self):
        '''draws cell on grid'''
        self._canv.create_rectangle(self._ulx, self._uly, self._lrx, self._lry,
                                    outline='black', fill=self._color, tag=self._tag)
        
    def get_uly(self):
        return self._uly
    
    def get_color(self):
        return self._color
    
    # ADDED BY VTN2
    def move(self):
        '''moves cells down the screen'''
        self._uly += YSPEED
        self._lry += YSPEED
    
    def set_color(self, color):
        self._color= color
        
    def __contains__(self, xy):
        '''Return True if the given x,y tuple is in the rectangle, False
        otherwise.'''
        x, y = xy
        return self._ulx < x < self._lrx and self._uly < y < self._lry
        

class GUI:
    '''Develops a Graphical User Interface for the Game to be played'''
    def __init__(self, root):
        self._root = root
        root.geometry('240x580')     #set window size
        root.configure(background='yellow')
        self._score=0
        self._move=True
        self._canv = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self._canv.pack()
        #status message
        self._label= Label(root, text="Don't Touch the White Tile!",
                           font=('Arial', 14, ITALIC), bg='yellow')
        self._label.pack()
        #instructions label
        self._label2= Label(root, text="Click on the black tiles.\nIf you click on a white one,\nit's game over!",
                           font=('Arial', 10, ITALIC), bg='yellow')
        self._label2.pack()

        # A 2-d grid of locations--from Prof Norman
        self._grid = []
        for row in range(NUM_CELLS_HIGH):
            rowlist = []
            for col in range(NUM_CELLS_WIDE):
                rowlist.append(Cell(self._canv, col, row))
            self._grid.append(rowlist)
        
        # place one black tile per row at random on the canvas
        row_index = 0
        for row in self._grid:
            rand_col_index = randint(0,3)
            self.black_cell = self._grid[row_index][rand_col_index].set_color('black')
            if row_index==2:
                self.black_index=int(rand_col_index)
            row_index += 1
            
        # ADDED BY VTN2
        self._canv.after(20, self.renderAll)#move tiles      
        
    # ADDED BY VTN2
    def renderAll(self):
        '''moves all cells down the screen'''
        self._canv.delete(ALL) 
        #imr6
        for row in range(NUM_CELLS_WIDE):
            yval=self._grid[row][0].get_uly()
            if yval >= CANVAS_HEIGHT:
                self._grid.remove(self._grid[row])
                self.addRow()#####
            #VTN2
            for col in range(NUM_CELLS_WIDE):
                cell = self._grid[row][col]
                self._move==True
                if self._move==True:
                    cell.move()                
                cell.render()
        self._canv.after(20, self.renderAll)
        #score label
        self._scoreLabel = self._canv.create_text(115, 50, text=str(self._score), font=('Arial',60), fill='red')
        self._canv.tag_raise(self._scoreLabel) 
        self._canv.bind("<Button-1>", self.processMouseEvent)
    
    def addRow(self):
        '''adds a row to the top of grid'''
        rowlist = []
        for col in range(NUM_CELLS_HIGH):
            rowlist.append(Cell(self._canv, col, 0))
        self._grid.insert(0, rowlist)
        #black tile placed at random
        self.rand_col_index = randint(0,3)
        self._grid[0][self.rand_col_index].set_color('black')
    
    def processMouseEvent(self, event):
        '''enables user to click on tiles'''
        x, y = event.x, event.y
        for col in range(NUM_CELLS_WIDE):
            if (x, y) in self._grid[2][col]:
                if self._grid[2][col].get_color() == 'black':
                    self._grid[2][col].set_color('gray')
                    if self._grid[2][col].get_color()=='gray':
                        #update score
                        self._score+=1
                elif self._grid[2][col].get_color()=='white':
                    self._grid[2][col].set_color('red')
                    self._move=False
                    self._label.config(text= "Game Over!")
                    self._label2.pack_forget()
                    

root = Tk()
root.title("Don't Touch The White Tile!")
GUI(root)
root.mainloop()

