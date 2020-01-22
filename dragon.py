from element import Element
import sys
from smh import ascii

class Dragon(Element):
    def __init__(self, x, y, str):
        Element.__init__(self, x, y, str)
        self._lives = 10
        self._type = "dragon"
        