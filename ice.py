from grid import Grid

class Ball(Element):
    def __init__(self, x, y, str='@'):
        Element.__init__(self, x, y, str='@')
        self.setname("ball")
        self.printc()
    
    def remove(self):
        self.erase()
        self.change_scope()
    
    def move(self, matrix, num=1):
        if self.scope()==1 and self.x()>1+num:
            self.update_loc(matrix, 'l', 3)
        else:
            self.remove()