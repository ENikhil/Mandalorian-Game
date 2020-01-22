from terminal import getTerminalSize
from coin import Coin
from firebeam import Beam
from boost import Boost
from magnet import Magnet
import random
from smh import ascii
import time as t

class Grid():
    def __init__(self, rowlen, columnlen):
        self._rowlen=rowlen
        self._columnlen=columnlen
        self._objectlist = []
        self._attacklist = []
        self._boost = 1
        self._coingen = 3
        self._beamgen = 3
        self._magnetgen = 45
        self._lastcoin = 0
        self._lastbeam = 0
        self._lastboost = 0
        self._lastmagnet = 0
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
    
    def appendlist(self, a):
        self._objectlist.append(a)
    
    def matrix(self):
        return self._matrix
    
    def boost(self):
        return self._boost
    
    def toggleboost(self):
        if self._boost == 1:
            self._boost = 3
        elif self._boost ==3:
            self._boost = 1
    
    def generate(self, num):
        if num == 0 and t.time()-self._lastcoin>self._coingen/self._boost:
            y = random.randrange(4, self._columnlen-3, 1)
            paisa = Coin(self._rowlen-5, y, ascii[1])
            self._objectlist.append(paisa)
            self._lastcoin=t.time()
        elif num == 5:
            y = random.randrange(4, self._columnlen-5, 1)
            chep = Magnet(self._rowlen-9, y, ascii[5])
            self._objectlist.append(chep)
            self._lastmagnet=t.time()
        elif num == 2 and t.time()-self._lastbeam>self._beamgen/self._boost:
            shape = random.randrange(0, 3, 1)
            if shape == 0:
                y = random.randrange(4, self._columnlen-3, 5)
                fire = Beam(self._rowlen-19, y, ascii[3], 0)
            elif shape == 1:
                y = random.randrange(4, self._columnlen-11, 5)    
                fire = Beam(self._rowlen-4, y, "o", 1)
            elif shape == 2:
                y = random.randrange(4, self._columnlen-11, 5)
                fire = Beam(self._rowlen-19, y, "o", 2)
            self._objectlist.append(fire)
            self._lastbeam=t.time()
        elif num == 4 and t.time()-self._lastboost>30:
            y = random.randrange(4, self._columnlen-3, 1)
            vroom = Boost(self._rowlen-6, y, ascii[2])
            self._objectlist.append(vroom)
            self._lastboost=t.time()
        
a = getTerminalSize()
grid = Grid(a[0], a[1])