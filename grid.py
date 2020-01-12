import numpy as np

class Grid:
    def __init__(self, rows, columns):
        self.rows=rows
        self.columns=columns
        self.matrix=[]
    def create_Grid(self):
        self.matrix = np.repeat(" ", self.rows*self.columns).reshape(self.rows, self.columns)
    def print_Grid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print (self.matrix[i][j], end="")