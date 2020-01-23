from grid import Grid
from element import Element

class Ball(Element):
    def __init__(self, x, y, str=u"\u2744"):
        Element.__init__(self, x, y, str=u"\u2744")
        self.setname("ball")
        self.printc()
    
    def remove(self):
        self.erase()
        self.change_scope()
    
    def move(self, matrix, num=1):
        if self.scope()==1 and self.x()>3+num:
            self.update_loc(matrix, 'l', 3)
        else:
            self.remove()