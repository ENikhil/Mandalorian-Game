from element import Element
from smh import ascii

class Boost(Element):
    def __init__(self, x, y, str=ascii[2]):
        Element.__init__(self, x, y, str=ascii[2])
        self.setname("boost")
        self.printc()