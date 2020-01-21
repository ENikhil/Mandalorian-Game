import os
from grid import grid
from smh import ascii
from mandalorian import Mandalorian
import time as t

os.system('clear')
grid.print_Grid()
mando = Mandalorian(5, 30, ascii[0])

while(1):
    grid.generate()
    for o in grid.getlist():
        if o.scope() == 0:
            del o
        else:
            o.move(grid._matrix)
    mando.movement(grid._matrix)