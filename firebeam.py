from element import Element
import sys
from smh import ascii

class Beam(Element):
    def __init__(self, x, y, str, num):
        Element.__init__(self, x, y, "o")        
        self.setname("beam")
        self._type = num
        if num == 0:
            a = ["o o o o o o o o o"]
            self.setparam(a)
            self.printc()
        elif num == 1:
            a = ["o" for i in range(9)]
            self.setparam(a)
            self.printc()
        elif num == 2:
            self.setheight(9)
            self.setlength(1)
            self.printd()
    
    def erased(self, num=1):
        a = 0
        b = num
        for i in range(9):
            sys.stdout.write("\x1b[%d;%df%s" % (self.y()+i+a, self.x()+2*i+b, " "*self.length()))
            sys.stdout.flush()

    def printd(self, ch='x', num=1):
        if ch == 'x':
            self.erased(num)
        for i in range(9):
            sys.stdout.write("\x1b[%d;%df%s" % (self.y()+i, self.x()+2*i, "o"))
            sys.stdout.flush()

    def updated(self, matrix, ch='x', num=1):
        if ch=='l' and self.x() > 1+num:
            self.setx(self.x()-num)
            self.printd('x', num)
        else:
            pass
            
    def move(self, matrix, num=1):
        if self.scope()==1 and self.x()>2:
            if self._type <= 1:
                self.update_loc(matrix, 'l', num)
            elif self._type == 2:
                self.updated(matrix, 'l', num)
        else:
            if self._type <= 1:
                self.erase()
                self.change_scope()
            elif self._type == 2:
                self.erased()
                self.change_scope()