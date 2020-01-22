import os
from grid import grid
from smh import ascii
from mandalorian import Mandalorian
import time as t
import random

os.system('clear')
grid.print_Grid()
mando = Mandalorian(5, 30, ascii[0])
#grid.appendlist(mando)
last_gen_time = 0
last_mov_time = 0
gen_time = 2
mov_time = 0.1

mando.setacceltime(t.time())

while(1):
    #if mando.lives() == 0:
    #    quit()
    mando.move(grid.matrix(), grid.boost())
    if t.time() - last_mov_time > mov_time:
        for o in grid.getlist():
            if o.scope() == 0:
                grid.getlist().remove(o)
                del o
            else:
                o.move(grid.matrix(), grid.boost())
        last_mov_time = t.time()
    if t.time()-mando.acceltime() > mov_time:
        mando.update_loc(grid.matrix(), 'd', mando.dvelocity())
        mando.accelerate()
    #if t.time() - last_gen_time > gen_time:
    num = random.randrange(0, 4, 1)
    grid.generate(num)
    #    last_gen_time = t.time()