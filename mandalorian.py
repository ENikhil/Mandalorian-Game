from character import Character

class Mandalorian(Character)
    def __init__(self, x, y, str):
        Character.__init__(self, x, y, str)
        
    def movement(self):
        