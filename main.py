import os
import sys
from grid import grid
from smh import ascii
from mandalorian import Mandalorian
from dragon import Dragon
import time as t
import random

def stats(a, b, c, num):
    if num==1:
        lmao = "    TIME = " + str(c)
    elif num==2:
        lmao = "    BOSS LIVES = " + str(c)
    info = "LIVES = " + str(a) + "    SCORE = " + str(b) + lmao + "                   "
    sys.stdout.write("\x1b[%d;%df%s" % (2, 4, info))
    sys.stdout.flush()

os.system('clear')
grid.print_Grid()
mando = Mandalorian(5, 30, ascii[0])
creation_time = t.time()
last_gen_time = 0
last_mov_time = 0
gen_time = 2
mov_time = 0.1
magnet_time = creation_time
mando.setacceltime(t.time())
boss_time = 90
stats(mando.lives(), mando.coins(), boss_time-t.time()+creation_time, 1)

while(1):
    if mando.lives() == 0:
        quit()
    stats(mando.lives(), mando.coins(), boss_time-t.time()+creation_time, 1)
    mando.move(grid.matrix(), grid.boost())
    if t.time() - last_mov_time > mov_time/grid.boost():
        for o in grid.getlist():
            if o.scope() == 0:
                grid.getlist().remove(o)
                del o
            else:
                o.move(grid.matrix(), grid.boost())
        mando.checkmagnet(grid.matrix())
        last_mov_time = t.time()
    if t.time()-mando.acceltime() > mov_time*2.5/grid.boost():
        mando.update_loc(grid.matrix(), 'd', mando.dvelocity())
        mando.accelerate()
        mando.setacceltime(t.time())
    if t.time()-magnet_time>20:
        grid.generate(5)
        magnet_time = t.time()
    num = random.randrange(0, 4, 1)
    grid.generate(num)  #    last_gen_time = t.time()
    if t.time()-creation_time>=boss_time:
        break


dragon = Dragon(170, 20, ascii[6])
grid.appendlist(dragon)
dragon.setdragontime(t.time())

stats(mando.lives(), mando.coins(), dragon.lives(), 2)

while(1):    
    if mando.lives() == 0:
        quit()
    if dragon.lives() == 0:
        dragon.dead()
        break
    stats(mando.lives(), mando.coins(), dragon.lives(), 2)
    mando.move(grid.matrix(), grid.boost())
    if t.time()-last_mov_time>mov_time/grid.boost():
        for o in grid.getlist():
            if o.scope() == 0:
                grid.getlist().remove(o)
                del o
            elif o.name() != "dragon":
                o.move(grid.matrix(), grid.boost())
        last_mov_time = t.time()
    if t.time()-dragon.dragontime()>0.1 and mando.y()!=dragon.y()+7:
        dragon.update_loc(grid.matrix(), mando.y()-dragon.y()-7)
        dragon.createBall()
    if t.time()-mando.acceltime() > mov_time*2.5/grid.boost():
        mando.update_loc(grid.matrix(), 'd', mando.dvelocity())
        mando.accelerate()
        mando.setacceltime(t.time())