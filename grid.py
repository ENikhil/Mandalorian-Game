import numpy as np

class Grid:
    def __init__(self, rows, columns):
        self.rows=rows
        self.columns=columns
        self.matrix=[]
    def create_Grid(self):
        self.matrix = np.repeat(" ", self.rows*self.columns).reshape(self.rows, self.columns)
        for i in range(self.rows):
            if(i==0 or i==self.rows-1):
                for j in range(self.columns):
                    self.matrix[i][j]="*"
            self.matrix[i][0]=self.matrix[i][self.columns-1]="*"
        
    def print_Grid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print (self.matrix[i][j], end="")