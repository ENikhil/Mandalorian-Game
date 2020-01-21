from element import Element
import sys
from smh import ascii

class Magnet(Element):
    def __init__(self, x, y, str=ascii[5]):
        Element.__init__(self, x, y, str=ascii[5])
        self.setname("magnet")
        self.printc()