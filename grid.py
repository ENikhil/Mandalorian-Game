import numpy as np
from terminal import getTerminalSize

class Grid():
    def __init__(self, rowlen, columnlen):
        self.rowlen=rowlen
        self.columnlen=columnlen
        self.matrix=[[" " for i in range(self.rowlen)] for i in range(self.columnlen)]
        for i in range(self.columnlen):
            for j in range(self.rowlen):
                if i==0 or i==self.columnlen-1 or j==0 or j==self.rowlen-1:
                    self.matrix[i][j] = '*'
                else:
                    pass

    def print_Grid(self):
        for i in range(self.columnlen):
            for j in range(self.rowlen):
                print (self.matrix[i][j], end = "")
                
a = getTerminalSize()
grid = Grid(a[0], a[1])