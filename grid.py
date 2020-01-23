from terminal import getTerminalSize
from coin import Coin
from firebeam import Beam
from boost import Boost
from magnet import Magnet
from scenery import AT, Ship
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
        self._timeboost = 0
        self._lastmagnet = 0
        self._score = 0
        self._boss = 0
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
            self._timeboost=t.time()
        elif t.time()-self._timeboost>5 and self._boost==3:
            self._boost = 1
    
    def timeboost(self):
        return self._timeboost
    
    def changetimeboost(self, a):
        self._timeboost = a
    
    def score(self):
        return self._score
    
    def addscore(self, a):
        self._score+=a
    
    def addlife(self):
        self._score-=50
    
    def boss(self):
        return self._boss
    
    def changeboss(self):
        self._boss=1-self._boss
    
    def generate(self, num):
        if num == 0 and t.time()-self._lastcoin>self._coingen/self._boost:
            y = random.randrange(4, self._columnlen-3, 1)
            paisa = Coin(self._rowlen-5, y, ascii[1])
            self._objectlist.append(paisa)
            self._lastcoin=t.time()
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
        elif num == 4:
            y = random.randrange(4, self._columnlen-3, 1)
            vroom = Boost(self._rowlen-6, y, ascii[2])
            self._objectlist.append(vroom)
            self._timeboost=t.time()
        elif num == 5:
            y = random.randrange(4, self._columnlen-5, 1)
            chep = Magnet(self._rowlen-9, y, ascii[5])
            self._objectlist.append(chep)
            self._lastmagnet=t.time()
        elif num == 6:
            y = 42
            bandook = AT(self._rowlen-19, y, ascii[8])
            self._objectlist.append(bandook)
        elif num == 7:
            y = 7
            gaadi = Ship(self._rowlen-27, y, ascii[9])
            self._objectlist.append(gaadi)

a = getTerminalSize()
grid = Grid(a[0], a[1])