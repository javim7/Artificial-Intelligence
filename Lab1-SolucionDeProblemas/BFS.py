from framework import *

class BFS(Framework):
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
    
    def bfs(self):
        fronteras = self.fronteras
        visitados = self.visitados
       
        x = 0
        while x <5:
            if len(fronteras):

                visitados.append(fronteras.pop(0))
                print(visitados)
                estado = visitados[-1]
                print(estado)

                if self.goal_test(estado):
                    return visitados
                acciones = self.actions(estado)
                for a in acciones:
                    copyvisitados = visitados.copy()
                    copyvisitados.append(a)
                    fronteras.append(copyvisitados)
                print(fronteras) 
            else:
                return False

            
