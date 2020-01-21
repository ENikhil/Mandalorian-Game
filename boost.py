from element import Element
from smh import ascii

class Boost(Element):
    def __init__(self, x, y, str=ascii[2]):
        Element.__init__(self, x, y, str=ascii[2])
        self.setname("boost")
        self.printc()

    def move(self, matrix, num=1):
        if self.scope()==1 and self.x()>2:
            self.update_loc(matrix, 'l', num)
        else:
            self.erase()
            self.change_scope()