import os
from grid import Grid
from terminal import getTerminalSize
from smh import ascii

#print(ascii[0])

os.system('clear')    
#print_str(100, 70, mandalorian)
#print_str(100, 69, mandalorian)

termsize=getTerminalSize()
a = Grid(termsize[0], termsize[1])
a.create_Grid()
#a.matrix[1][2]=mandalorian
a.print_Grid()

 