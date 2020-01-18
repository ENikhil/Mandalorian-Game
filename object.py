import numpy as np

class Object:
    def __init__(self, x, y, str):
        self.x=x
        self.y=y
        self.obj=str
    
    def x_get(self):
        return self.x
    
    def y_get(self):
        return self.y