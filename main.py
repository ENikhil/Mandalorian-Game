import os
from grid import Grid
from terminal import getTerminalSize

mandalorian="( ͡° ͜ʖ ͡°)=ε/̵͇̿̿/'̿̿ ̿"
#print(mandalorian)

os.system('clear')    
#print_str(100, 70, mandalorian)
#print_str(100, 69, mandalorian)

termsize=getTerminalSize()
a = Grid(termsize[0], termsize[1])
a.create_Grid()
a.print_Grid()