from element import Element
from grid import grid

class Bullet(Element):
    def __init__(self, x, y, str="="):
        Element.__init__(self, x, y, str="=")
        self.setname("bullet")
        self.printc()
    
    def remove(self):
        self.erase()
        self.change_scope()
    
    def move(self, matrix, num=1):
        if self.scope()==1 and self.x()<(len(matrix[0])- self.length() - 4):
            self.update_loc(matrix, 'r', 3)
        else:
            self.remove()
        for o in grid.getlist():
            if o.name() == "beam":
                if o.type() == 0 and 0<=o.x()-self.x()<=16 and o.x()==self.y():
                    o.remove()
                    self.remove()
                elif o.type() == 1 or 0<=self.x()-o.x()<=3 and 0<=o.y()-self.y()<=7:
                    o.remove()
                    self.remove()
                elif o.type() == 2:
                    flag = 0
                    for i in range(8):
                        if 0<=self.x()-o.x()-2*i<=3 and o.y()+i==self.y():
                            flag = 1
                            break
                    if flag:
                        o.remove()
                        self.remove()