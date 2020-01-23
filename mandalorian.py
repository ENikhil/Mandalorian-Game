from element import Element
from inp import kb
from grid import grid
from bullet import Bullet
import sys
import time as t

class Mandalorian(Element):
    def __init__(self, x, y, str):
        Element.__init__(self, x, y, str)
        self._downvelocity = 1
        self._hvelocity = 0
        self._vvelocity = 0
        self._gravity = 1
        self._lives = 3
        self._bullet = "="
        self._timebullet = 0
        self._shield = 0
        self._boost = 0
        self.setname("mando")
        self._time = 0
        self._magnettime = 0
        self._shieldtime = 0
        self._creationtime = t.time()
        self.printc()
    
    def shield(self):
        return self._shield
    
    def toggleshield(self):
        if self._shield == 0:
            self._shield = 1
        elif self._shield == 1:
            self._shield = 0
        self._shieldtime = t.time()
    
    def shieldtime(self):
        return self._shieldtime
    
    def gravity(self):
        return self._gravity
    
    def lives(self):
        return self._lives
    
    def dec_lives(self):
        self._lives-=1
        
    def inc_lives(self):
        self._score-=10
        self._lives+=1
    
    def acceltime(self):
        return self._time
    
    def setacceltime(self, time):
        self._time = time
    
    def accelerate(self):
        self._downvelocity+=self._gravity

    def shieldtoggle(self):
        self._shield = 1 - self._shield
    
    def dvelocity(self):
        return self._downvelocity
    
    def reset_downvelocity(self):
        self._downvelocity=1
    
    def createBullet(self):
        if t.time()-self._timebullet>1 and (grid.boss() == 0 or (grid.boss() == 1 and 10<=self.y()<len(grid.matrix())-9)):
            goli = Bullet(self.x()+self.length(), self.y()+1)
            grid.appendlist(goli)
            self._timebullet=t.time()
    
    def checkmagnet(self, matrix):
        a = 0
        b = 0
        for o in grid.getlist():
            if o.name() == "magnet":
                if o.y()>self._y:
                    a = -1
                elif o.y() < self._y:
                    a = 1
                if o.x()>self._x:
                    b = 1
                elif o.x()<self._x:
                    b = -1
        if a > 0:
            self.update_loc(matrix, 'd', 1)
        elif a < 0:
            self.update_loc(matrix, 'u', 1)
        if b > 0:
            self.update_loc(matrix, 'r', 1)
        elif b < 0:
            self.update_loc(matrix, 'l', 2)
        
    
    def move(self, matrix, num):
        if(kb.kbhit()):
            key = kb.getch()
            if key == 'a':
                self.update_loc(matrix, 'l', 2*grid.boost())
            elif key == 'd':
                self.update_loc(matrix, 'r', 2*grid.boost())
            elif key == 'w':
                if self._downvelocity > 5:
                    self.update_loc(matrix, 'u', 1)
                else:
                    self.update_loc(matrix, 'u', 2)
                self._time = t.time()
                self.reset_downvelocity()
            #elif key == 's':
            #    self.update_loc(matrix, 'd', 1)
            elif key == 'e':
                self.createBullet()
            elif key == ' ':
                if self._shield == 0 and (self._shieldtime == 0 or t.time()-self._shieldtime>60):
                    self._shield = 1
                    self._shieldtime = t.time()
            elif key == 'l':
                if grid.score()>=30:
                    self._lives+=1
                    grid.addlife()
            elif key == 'q':
                quit()
        for o in grid.getlist():
            if o.name() == "coin":
                if o.scope()==1 and (0<=o.x()-self.x()<=4 or 0<=self.x()-o.x()<=2) and (0<=o.y()-self.y()<=2 or 0<=self.y()-o.y()<=0):
                    o.remove()
                    del o
                    self.printc()
                    grid.addscore(1)
            elif o.name() == "boost":
                if o.scope()==1 and (0<=o.x()-self.x()<=4 or 0<=self.x()-o.x()<=3) and (0<=o.y()-self.y()<=2 or 0<=self.y()-o.y()<=3):
                    o.remove()
                    del o
                    #if grid.boost() == 1:
                    grid.toggleboost()
                    
            elif o.name() == "beam" and self._shield == 0:
                if o.scope()==1 and o.type() == 0 and (0<=o.x()-self.x()<=4 or 0<=self.x()-o.x()<=16) and (0<=o.y()-self.y()<=2 or 0<=self.y()-o.y()<=0):
                    o.remove()
                    del o
                    self.printc()
                    self._lives-=1
                    #print("gg")
                elif o.scope()==1 and o.type() == 1 and 0<=o.x()-self.x()<=4 and (0<=o.y()-self.y()<=2 or 0<=self.y()-o.y()<=7):
                    o.remove()
                    del o
                    self.printc()
                    self._lives-=1
                    #print("gg")
                elif o.scope()==1 and o.type() == 2:
                    flag = 0
                    for i in range(9):
                        if 0<=o.x()+2*i-self.x()<=4 and -2<=self.y()-o.y()-i<=2:
                            flag = 1
                            break
                    if flag:
                        o.remove()
                        del o
                        self.printc()
                        self._lives-=1
                        #print("gg")
            elif o.scope()==1 and o.name() == "ball" and self._shield == 0:
                if 0<=o.x()-self.x()<=4 and 0<=o.y()-self.y()<=2:
                    o.remove()
                    del o
                    self.printc()
                    self._lives-=1