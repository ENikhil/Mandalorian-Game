from element import Element
from smh import ascii

class Coin(Element):
    def __init__(self, x, y, str=ascii[1]):
        Element.__init__(self, x, y, str=ascii[1])
        self.setname("coin")
        self.printc()