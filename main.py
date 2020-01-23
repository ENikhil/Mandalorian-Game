import os
import sys
from grid import grid
from smh import ascii
from mandalorian import Mandalorian
from dragon import Dragon
import time as t
import random

def stats(u, w, x, y, z, num):
    a = str(u)
    b = str(w)
    c = str(x)
    if num==1:
        lmao = "    TIME REMAINING= " + c
    elif num==2:
        lmao = "    BOSS LIVES = " + c
    if y == 1:
        sh = "ACTIVATED"
    elif y == 0:
        if t.time()-z<60:
            sh = "RECHARGING"
        else:
            sh = "READY"
    info = "LIVES = " + a + "    SCORE = " + b + "    SHIELD = " + sh + lmao + "                       "
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
magnet_time = boost_time = creation_time
mando.setacceltime(t.time())
boss_time = 10
stats(mando.lives(), grid.score(), boss_time-t.time()+creation_time, mando.shield(), mando.shieldtime(), 1)
con = 0

while(1):
    if mando.lives() == 0:
        con = 1
        break
    if mando.shield() == 1 and t.time()-mando.shieldtime()>10:
        mando.toggleshield()
    if grid.boost() != 1:
        grid.toggleboost()
    stats(mando.lives(), grid.score(), boss_time-t.time()+creation_time, mando.shield(), mando.shieldtime(), 1)
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
    if t.time()-magnet_time>35:
        grid.generate(5)
        magnet_time = t.time()
    elif t.time()-boost_time>20:
        grid.generate(4)
        boost_time = t.time()
    num = random.randrange(0, 4, 1)
    grid.generate(num)  #    last_gen_time = t.time()
    if t.time()-creation_time>=boss_time:
        break

if con == 1:
    os.system('clear')
    sys.stdout.write("\x1b[%d;%df%s" % (1, 1, "YOU LOST THE GAME!!"))
    sys.stdout.flush()
    quit()

grid.changeboss()
dragon = Dragon(170, 20, ascii[6])
grid.appendlist(dragon)
dragon.setdragontime(t.time())

stats(mando.lives(), grid.score(), dragon.lives(), mando.shield(), mando.shieldtime(), 2)

while(1):    
    if mando.lives() == 0:
        con = 1
        break
    if dragon.lives() == 0:
        con = 2
        break
    stats(mando.lives(), grid.score(), dragon.lives(), mando.shield(), mando.shieldtime(), 2)
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

if con == 1:
    os.system('clear')
    sys.stdout.write("\x1b[%d;%df%s" % (1, 1, "YOU LOST THE GAME!!"))
    sys.stdout.flush()
elif con == 2:
    os.system('clear')
    sys.stdout.write("\x1b[%d;%df%s" % (1, 1, "YOU BEAT THE GAME!!"))
    sys.stdout.flush()
    yoda = ascii[7].split('\n')
    sys.stdout.write("\x1b[%d;%df%s" % (2, 8, yoda[0]))
    sys.stdout.flush()    
    sys.stdout.write("\x1b[%d;%df%s" % (3, 8, yoda[1]))
    sys.stdout.flush()