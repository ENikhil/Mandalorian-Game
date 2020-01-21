from element import Element
from grid import Grid

class Bullet(Element):
    def __init__(self, x, y, str='='):
        Element.__init__(self, x, y, str='=')
        self.setname("bullet")
        self.printc()
    
    def move(self, matrix):
        if self.scope()==1 and self.x()<(len(matrix[0])- self.length() - 4):
            self.update_loc('r', 3)
        else:
            self.erase('x')
            self.change_scope()