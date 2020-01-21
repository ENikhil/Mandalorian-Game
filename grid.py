import numpy as np
from terminal import getTerminalSize
from coin import Coin
from firebeam import Beam
from boost import Boost
import random
from smh import ascii

class Grid():
    def __init__(self, rowlen, columnlen):
        self._rowlen=rowlen
        self._columnlen=columnlen
        self._objectlist = []
        self._coinlist = []
        self._beamlist = []
        self._bulletlist = []
        self._icelist = []
        self._matrix=[[" " for i in range(self._rowlen)] for i in range(self._columnlen)]
        for i in range(self._columnlen):
            for j in range(self._rowlen):
                if i==0 or i==2 or i==self._columnlen-1 or j==0 or j==self._rowlen-1:
                    self._matrix[i][j] = '*'
                else:
                    pass

    def print_Grid(self):
        for i in range(self._columnlen):
            for j in range(self._rowlen):
                print (self._matrix[i][j], end = "")

    def getlist(self):
        return self._objectlist
    
    def getmatrix(self):
        return self._matrix
    
    def generate(self):
        num = random.randrange(0, 4, 1)
        if num == 0:
            y = random.randrange(4, self._columnlen-3, 1)
            paisa = Coin(self._rowlen-5, y, ascii[1])
            self._objectlist.append(paisa)
        elif num == 1:
            y = random.randrange(4, self._columnlen-3, 1)
            vroom = Boost(self._rowlen-6, y, ascii[2])
            self._objectlist.append(vroom)
        elif num == 2:
            shape = random.randrange(0, 3, 1)
            if shape == 0:
                y = random.randrange(4, self._columnlen-3, 1)
                fire = Beam(self._rowlen-19, y, ascii[3], 0)
            elif shape == 1:
                y = random.randrange(4, self._columnlen-11, 1)    
                fire = Beam(self._rowlen-3, y, ascii[4], 1)
            elif shape == 2:
                y = random.randrange(4, self._columnlen-11, 2)
                fire = Beam(self._rowlen-19, y, "o", 2)
            self._objectlist.append(fire)
                
a = getTerminalSize()
grid = Grid(a[0], a[1])