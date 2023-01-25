from PIL import Image
from framework import *

class DFS(Framework):
    def __init__(self, matriz, inicial, finales, caminables):
        super().__init__(matriz, inicial, finales, caminables)
        self.final = None

    def actions(self, estado):
        i, j = estado
        
        movimientosPosibles = []
        
        if ((i,j+1) in self.caminables) or ((i,j+1) in self.finales):
            movimientosPosibles.append((i,j+1))
        if ((i,j-1) in self.caminables) or ((i,j-1) in self.finales):
            movimientosPosibles.append((i,j-1))
        if ((i+1,j) in self.caminables) or ((i+1,j) in self.finales):
            movimientosPosibles.append((i+1,j))
        if ((i-1,j) in self.caminables) or ((i-1,j) in self.finales):
            movimientosPosibles.append((i-1,j))
        
        return movimientosPosibles

    def result(self, estado, accion):
        return super().result(estado, accion)

    def goal_test(self, estado):
        return estado in self.finales

    def stepCost(self, estado, accion, estado2):
        return super().stepCost(estado, accion, estado2)

    def path_cost(self, matriz):
        return super().path_cost(matriz)
    
    def dfs(self):
        pass
