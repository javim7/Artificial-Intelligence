class Celda():
    def __init__(self, pos, color):
        self.color = color
        self.pos = pos
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __str__(self):
        if self.color == 0:
            return str('Color: N' + ' Pos: ' + str(self.pos))
        if self.color == 1:
            return str('Color: B' + ' Pos: ' + str(self.pos))
        if self.color == 2:
            return str('Color: R' + ' Pos: ' + str(self.pos))
        if self.color == 3:
            return str('Color: V' + ' Pos: ' + str(self.pos))