import os
from grid import grid
#from terminal import getTerminalSize
from smh import ascii
from mandalorian import Mandalorian
#print(ascii[0])

os.system('clear')    
#print_str(100, 70, mandalorian)
#print_str(100, 69, mandalorian)

#termsize=getTerminalSize()
#a = Grid(termsize[0], termsize[1])
#a.create_Grid()
#a.matrix[1][2]=mandalorian
#grid.print_Grid()
#print(ascii[0].split('\n'))
grid.print_Grid()
mando = Mandalorian(5, 30, ascii[0])
mando.printmando(grid.matrix)

#print(ascii[0])
