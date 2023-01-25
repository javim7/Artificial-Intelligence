class Celda():
    def __init__(self, x,y, color):
        self.posicion = [y,x]
        self.padre = None
        self.vecinoArriba = None
        self.vecinoAbajo = None
        self.vecinoIzquierda = None
        self.vecinoDerecha = None
        self.color = color

    def identificador(self):
        return [self.color,self.position[0],self.position[1]]
    
    def movimiento(self):
        return [self.VecinoIzquierda,self.VecinoArriba,self.VecinoAbajo,self.VecinoDerecha]
    
    def color(self):
        return self.color
