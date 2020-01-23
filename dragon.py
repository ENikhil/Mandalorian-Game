from element import Element
from ice import Ball
from grid import grid
import sys
from smh import ascii
import time as t

class Dragon(Element):
    def __init__(self, x, y, str):
        Element.__init__(self, x, y, ascii[6])
        self._lives = 20
        self.setname("dragon")
        self._time = t.time()
        self.setlength(len(self._body[2]))
        self.printc()
        self._dragontime = t.time()

    def dragontime(self):
        return self._dragontime
    
    def setdragontime(self, lmao):
        self._dragontime = lmao
    
    def lives(self):
        return self._lives    
    
    def dec_lives(self):
        self._lives-=1
    
    def createBall(self):
        if t.time()-self._time>0.66:
            baraf = Ball(self.x()-1, self.y()+7)
            grid.appendlist(baraf)
            self._time=t.time()
    
    def update_loc(self, matrix, num):
        if num>0:
            #down
            if self.y() < (len(matrix) - self.height() - 1 - num):
                self.sety(self.y()+num)
                self.printc('d', num)
            else:
                num = len(matrix) - self.height() - 2 - self.y()
                self.sety(len(matrix)-2-self.height())
                self.printc('d', num)
        elif num<0:
            #up
            num = 0 - num
            if self.y() >= 4+num:
                self.sety(self.y()-num)
                self.printc('u', num)
            elif self.y() == 3+num:
                self.sety(self.y()-num+1)
                self.printc('u', num-1)      
        self._dragontime = t.time()

    def dead(self):
        sys.stdout.write("\x1b[%d;%df%s" % (self.y()+5, self.x()+3, "xx"))
        sys.stdout.flush()