from character import Character
import getch as inp

class Mandalorian(Character)
    def __init__(self, x, y, str):
        Character.__init__(self, x, y, str)
        self.body = self.char.split("\n")
        self.height = len(self.body)
        self.length = len(self.body[0])
        
    def update_loc(self, matrix, ch):
        for i in range(self.height):
            for j in range(self.length):
                matrix[self.y+i][self.x+j] = " "
        if ch == 'l' and self.x > 1:
            for i in range(self.height):
                for j in range(self.length):
                    matrix[self.y-1+i][self.x+j] = self.body[i][j]
        if ch == 'r' and self.x < len(matrix[0])-1:
            for i in range(self.height):
                for j in range(self.length):
                    matrix[self.y+1+i][self.x+j] = self.body[i][j]
        
    def movement(self, matrix):
        def alarmhandler(signum, frame):
            raise AlarmException

        def USER_INP(timeout=0.1):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                char = getChar()()
                signal.alarm(0)
                return char
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''
        
        key = USER_INP()
        
        if key == 'a':
            self.update_loc(matrix, 'l')
        elif key == 'd'
            self.update_loc(matrix, 'r')
        elif key == 'w'
            self.boost()