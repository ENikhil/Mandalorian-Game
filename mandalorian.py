from character import Character
import getch as inp
from grid import grid
import sys

class Mandalorian(Character):
    def __init__(self, x, y, str):
        Character.__init__(self, x, y, str)
        self.body = self.char.split("\n")
        self.height = len(self.body)
        self.length = len(self.body[0])
        #print(self.height, self.length)
    
    def printmando(self, matrix):
        for i in range(self.height):
            sys.stdout.write("\x1b[%d;%df%s" % (self.y+i, self.x, self.body[i]))
            sys.stdout.flush()
    
    def erasemando(self, matrix):
        for i in range(self.height):
            sys.stdout.write("\x1b[%d;%df%s" % (self.y+i, self.x, ' '*self.length))
            sys.stdout.flush()
        
    def update_loc(self, matrix, ch):
        if ch == 'l' and self.x > 1:
            self.x-=1
            erasemando(matrix)
            printmando(matrix)
        elif ch == 'r' and self.x < len(matrix[0])-1:
            self.x+=1
            erasemando(matrix)
            printmando(matrix)
        elif ch == 'u' and self.y > 1:
            self.y-=1
            erasemando(matrix)
            printmando(matrix)
            
    #def movement(self, matrix):

    #    def USER_INP(timeout=0.1):
            
        
    #    key = USER_INP()
        
    #    if key == 'a':
    #        self.update_loc(matrix, 'l')
    #    elif key == 'd':
    #        self.update_loc(matrix, 'r')
    #    elif key == 'w':
    #        self.update_loc(matrix, 'u')