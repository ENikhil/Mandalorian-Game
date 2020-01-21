from element import Element
import inp
from grid import grid
import sys

class Mandalorian(Element):
    def __init__(self, x, y, str):
        Element.__init__(self, x, y, str)
        self._downvelocity = 1
        self._hvelocity = 0
        self._gravity = 1
        self._lives = 3
        self._bullet = "="
        self._boost = 0
        self.printc()
    
    def gravity(self):
        return self._gravity
    
    def lives(self):
        return self._lives
    
    def dec_lives(self):
        self._lives-=1
        
    def inc_lives(self):
        self._lives+=1
    
    def accelerate(self):
        self._velocity+=self._gravity
    
    def reset_downvelocity(self):
        self._velocity=1
    
    def movement(self, matrix):
        kb = inp.KBHit()
        if(kb.kbhit()):
            key = kb.getch()
            if key == 'a':
                self.update_loc(matrix, 'l')
            elif key == 'd':
                self.update_loc(matrix, 'r')
            elif key == 'w':
                if self._downvelocity > 5:
                    self.reset_downvelocity()
                    self.update_loc(matrix, 'u')
                else:
                    self.reset_downvelocity()
                    self.update_loc(matrix, 'u', 2)
            elif key == 's':
                self.update_loc(matrix, 'd')
            elif key == 'q':
                quit()