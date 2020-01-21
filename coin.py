from element import Element
from smh import ascii

class Coin(Element):
    def __init__(self, x, y, str=ascii[1]):
        Element.__init__(self, x, y, str=ascii[1])
        self.setname("coin")
        self.printc()

    def move(self, matrix, num=1):
        if self.scope()==1 and self.x()>2:
            self.update_loc(matrix, 'l', num)
        else:
            self.erase()
            self.change_scope()