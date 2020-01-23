import sys
import colorama as c

class Element:
    def __init__(self, x, y, str):
        self._x=x
        self._y=y
        self._char=str
        self._body = self._char.split("\n")
        self._height = len(self._body)
        self._length = len(self._body[0])
        self._scope = 1
        self._name = "element"

    def x(self):
        return self._x
    
    def y(self):
        return self._y
    
    def setx(self, x):
        self._x = x
    
    def sety(self, y):
        self._y = y
    
    def body(self):
        return self._body

    def setbody(self, arr):
        self._body = arr
        
    def height(self):
        return self._height
    
    def length(self):
        return self._length
    
    def setheight(self, y):
        self._height = y
        
    def setlength(self, x):
        self._length = x
    
    def setparam(self, arr):
        self._body = arr
        self._height = len(arr)
        self._length = len(arr[0])
        #print(self._height)
        #print(self._height)
    
    def scope(self):
        return self._scope
    
    def change_scope(self):
        self._scope = 1 - self._scope

    def name(self):
        return self._name
    
    def setname(self, a):
        self._name = a

    def erase(self, ch='x', num=1):
        a = 0
        b = 0
        if ch == 'x':   
            pass
        elif ch == 'r':
            b = -num
        elif ch == 'l':
            b = num
        elif ch == 'd':
            a = -num
        elif ch == 'u':
            a = num
        for i in range(self._height):
            sys.stdout.write("\x1b[%d;%df%s" % (self._y+i+a, self._x+b, " "*self._length))
            sys.stdout.flush()
    
    def printc(self, ch='x', num=1):
        if(ch=='x'):
            pass
        else:
            self.erase(ch, num)
        a = c.Fore.WHITE + c.Style.BRIGHT
        name = self._name
        if name == "mando":
            a = c.Style.RESET_ALL + c.Fore.RED + c.Style.DIM
        elif name == "bullet":
            a = c.Style.RESET_ALL + c.Fore.MAGENTA
        elif name == "dragon":
            a = c.Style.RESET_ALL + c.Fore.GREEN + c.Style.DIM
        elif name == "coin":
            a = c.Style.RESET_ALL + c.Fore.YELLOW
        elif name == "ball":
            a = c.Style.RESET_ALL + c.Fore.BLUE
        elif name == "beam":
            a = c.Style.RESET_ALL + c.Fore.CYAN
        elif name == "magnet":
            a = c.Style.RESET_ALL + c.Fore.WHITE
        elif name == "boost":
            a = c.Style.RESET_ALL + c.Fore.GREEN
        for i in range(self._height):
            sys.stdout.write("\x1b[%d;%df%s" % (self._y+i, self._x, a + self._body[i]))
            sys.stdout.flush()
    
    def update_loc(self, matrix, ch, num=1):
        if ch == 'l' and self._x > 1+num:
            self._x-=num
            self.printc('l', num)
        elif ch == 'r' and self._x < (len(matrix[0])- self._length - 1 - num):
            self._x+=num
            self.printc('r', num)
        elif ch == 'u':
            if self._y >= 4+num:
                self._y-=num
                self.printc('u', num)
            elif self._y == 3+num:
                self._y-=num-1
                self.printc('u', num-1)
        elif ch == 'd':
            if self._y < (len(matrix) - self._height - 1 - num):
                self._y+=num
                self.printc('d', num)
            else:
                num = len(matrix) - self._height - 2 - self._y
                self._y = len(matrix)-2-self._height
                self.printc('d', num)
        else:
            pass
        
    def remove(self):
        self.erase()
        self.change_scope()
    
    def move(self, matrix, num=1):
        if self.scope()==1 and self.x()>1+num:
            self.update_loc(matrix, 'l', num)
        else:
            self.remove()