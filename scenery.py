from element import Element
from smh import ascii

class AT(Element):
    def __init__(self, x, y, str = ascii[8]):
        Element.__init__(self, x, y, str = ascii[8])
        self.setname("at")
        self.setlength(18)
        self.printc

class Ship(Element):
    def __init__(self, x, y, str = ascii[9]):
        Element.__init__(self, x, y, str = ascii[9])
        self.setname("ship")
        self.setlength(27)
        self.printc